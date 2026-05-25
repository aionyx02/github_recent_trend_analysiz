"""Per-repo cache manifest for stale-aware incremental refresh.

Tracks when each repo's /languages and /topics caches were fetched, and when
the repo was last seen in a search result. Used by `collect_all.py` to decide
whether a cached file is still fresh (compared against the repo's `pushed_at`)
and to prune cache for repos that have rolled out of the 30-day window for
60+ days.

State file: `data/raw/_cache_manifest.json` (gitignored; also persisted in the
GitHub Actions cache so it survives across daily-refresh runs).

Schema:
    {
      "_manifest_version": 1,
      "repos": {
        "<repo_id>": {
          "languages_fetched_at": "<ISO 8601 UTC>",
          "topics_fetched_at":    "<ISO 8601 UTC>",
          "last_seen_at":         "<YYYY-MM-DD>"
        }
      }
    }

All timestamps are timezone-aware UTC produced via `datetime.now(timezone.utc)`
and parsed via `_parse_iso()` which normalises trailing `Z` to `+00:00`.
"""

from __future__ import annotations

import json
import logging
import os
from datetime import date, datetime, timezone
from pathlib import Path

from src import config

log = logging.getLogger(__name__)

MANIFEST_VERSION = 1
MANIFEST_PATH = config.RAW_DIR / "_cache_manifest.json"


def _empty_manifest() -> dict:
    return {"_manifest_version": MANIFEST_VERSION, "repos": {}}


def _parse_iso(s: str) -> datetime:
    """Parse ISO 8601, accepting trailing Z, always returning tz-aware UTC."""
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def _is_usable(path: Path) -> bool:
    """A cache file is usable iff it exists, is non-empty, and parses as JSON."""
    try:
        if not path.exists() or path.stat().st_size == 0:
            return False
        json.loads(path.read_text(encoding="utf-8"))
        return True
    except (OSError, json.JSONDecodeError):
        return False


def load(path: Path = MANIFEST_PATH) -> dict:
    """Read the manifest from disk; return a fresh empty one on any failure."""
    try:
        if not path.exists():
            return _empty_manifest()
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or "repos" not in data:
            log.warning("manifest at %s has unexpected shape, starting fresh", path)
            return _empty_manifest()
        return data
    except (OSError, json.JSONDecodeError) as e:
        log.warning("manifest at %s unreadable (%s), starting fresh", path, e)
        return _empty_manifest()


def save_atomic(manifest: dict, path: Path = MANIFEST_PATH) -> None:
    """Write the manifest atomically via tmp file + os.replace."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                   encoding="utf-8")
    os.replace(tmp, path)  # atomic on POSIX + Windows; Path.rename is NOT


def _entry(manifest: dict, repo_id: int | str) -> dict:
    """Return (creating if needed) the per-repo entry under manifest['repos']."""
    repos = manifest.setdefault("repos", {})
    key = str(repo_id)
    return repos.setdefault(key, {})


def mark_fetched(manifest: dict, repo_id: int | str, kind: str,
                 when: datetime) -> None:
    """Record that `kind` cache for `repo_id` was fetched at `when` (UTC)."""
    if kind not in ("languages", "topics"):
        raise ValueError(f"unknown kind: {kind!r}")
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    _entry(manifest, repo_id)[f"{kind}_fetched_at"] = when.astimezone(
        timezone.utc).isoformat()


def mark_seen(manifest: dict, repo_id: int | str, today: date) -> None:
    """Record that `repo_id` appeared in a search result on `today`."""
    _entry(manifest, repo_id)["last_seen_at"] = today.isoformat()


def is_stale(manifest: dict, repo_id: int | str, kind: str,
             pushed_at: datetime, cache_path: Path) -> bool:
    """Decide whether the cache for (repo_id, kind) should be re-fetched.

    Order of checks:
        1. Cache file missing or unusable (empty / corrupt JSON) → stale.
        2. Manifest entry missing for this (id, kind) → fall back to the
           cache file's mtime as implicit fetched_at, compare against pushed_at.
        3. Manifest entry present → compare manifest's fetched_at against pushed_at.
    """
    if not _is_usable(cache_path):
        return True

    if pushed_at.tzinfo is None:
        pushed_at = pushed_at.replace(tzinfo=timezone.utc)
    pushed_at = pushed_at.astimezone(timezone.utc)

    entry = manifest.get("repos", {}).get(str(repo_id), {})
    fetched_iso = entry.get(f"{kind}_fetched_at")

    if fetched_iso is None:
        mtime = datetime.fromtimestamp(cache_path.stat().st_mtime, tz=timezone.utc)
        return pushed_at > mtime

    return pushed_at > _parse_iso(fetched_iso)


def bootstrap_existing(manifest: dict, today: date, repo_ids: list[int]) -> int:
    """On first run after upgrade, stamp every existing cache file as fresh.

    Without this, the mtime fallback in `is_stale()` would mark thousands of
    legitimately-cached repos as stale and trigger a ~2000-call surge against
    the GitHub API. We only do this once: gated by absence of the
    `_manifest_version` sentinel (since `load()` always sets one on
    fresh-empty manifests, we detect "first creation" via empty `repos` dict
    on a manifest that was just synthesised by `load()` with no prior file).

    Returns the number of cache entries stamped (0 if not first run).
    """
    if manifest.get("repos"):
        return 0

    from src import collect_languages, collect_topics

    now_iso = datetime.now(timezone.utc).isoformat()
    today_iso = today.isoformat()
    stamped = 0
    for rid in repo_ids:
        entry = _entry(manifest, rid)
        lang_path = collect_languages.cache_path(rid)
        topic_path = collect_topics.cache_path(rid)
        if _is_usable(lang_path):
            entry["languages_fetched_at"] = now_iso
            stamped += 1
        if _is_usable(topic_path):
            entry["topics_fetched_at"] = now_iso
            stamped += 1
        entry["last_seen_at"] = today_iso
    if stamped:
        log.info("bootstrap_existing: stamped %d cache entries as fresh", stamped)
    return stamped


def prune(manifest: dict, today: date, buffer_days: int = 60,
          max_pruned: int = 200) -> list[int]:
    """Delete cache files + manifest rows for repos absent for >buffer_days.

    Refuses to prune more than `max_pruned` repos in one run (safety ceiling).
    Returns the list of evicted repo_ids (as int).
    """
    from src import collect_languages, collect_topics

    cutoff = today.toordinal() - buffer_days
    candidates: list[int] = []
    for rid_str, entry in list(manifest.get("repos", {}).items()):
        last_seen_iso = entry.get("last_seen_at")
        if not last_seen_iso:
            continue
        try:
            last_seen = date.fromisoformat(last_seen_iso)
        except ValueError:
            continue
        if last_seen.toordinal() < cutoff:
            candidates.append(int(rid_str))

    if len(candidates) > max_pruned:
        log.warning(
            "prune ceiling hit: %d candidates but max_pruned=%d — refusing to "
            "prune all. Pruning only the %d oldest. Inspect manifest if this "
            "looks wrong.",
            len(candidates), max_pruned, max_pruned,
        )
        candidates.sort(
            key=lambda rid: manifest["repos"][str(rid)].get("last_seen_at", "")
        )
        candidates = candidates[:max_pruned]

    pruned: list[int] = []
    for rid in candidates:
        for path in (collect_languages.cache_path(rid),
                     collect_topics.cache_path(rid)):
            try:
                path.unlink(missing_ok=True)
            except OSError as e:
                log.warning("could not delete %s: %s", path, e)
        manifest["repos"].pop(str(rid), None)
        pruned.append(rid)

    if pruned:
        log.info("pruned %d repo(s) absent for >%d days: %s",
                 len(pruned), buffer_days,
                 ", ".join(str(r) for r in pruned[:10])
                 + ("…" if len(pruned) > 10 else ""))
    return pruned
