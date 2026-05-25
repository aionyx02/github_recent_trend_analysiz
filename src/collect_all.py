"""End-to-end collection orchestrator: search → languages → topics → CSVs.

Idempotent + stale-aware. Cache state lives in `data/raw/_cache_manifest.json`
and tracks per-repo `pushed_at` so a repo's /languages and /topics get
re-fetched only when GitHub reports new activity since the last fetch.

Writes `data/processed/_collection_progress.json` after each stage so you
can inspect what was finished without re-parsing all the raw files.
"""

from __future__ import annotations

import json
import logging
import time
from datetime import date, datetime, timezone
from pathlib import Path

from src import (
    cache_manifest,
    clean_data,
    collect_languages,
    collect_repos,
    collect_topics,
    config,
)
from src.github_api import GitHubClient, RateLimitExhausted

log = logging.getLogger(__name__)

SAVE_EVERY_N_REPOS = 50


def discover_repos_on_disk() -> list[dict]:
    """Parse every saved search_*.json and return the deduplicated repo list.

    Iterates oldest → newest (filenames sort by date), overwriting on
    collision so the newest file's `pushed_at` wins for staleness checks.
    """
    out: dict[int, dict] = {}
    for path in sorted(config.RAW_DIR.glob("search_*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for item in payload.get("items", []):
            out[item["id"]] = {
                "id": item["id"],
                "full_name": item["full_name"],
                "pushed_at": item.get("pushed_at"),
            }
    return list(out.values())


def collect_search_pages() -> tuple[int, int]:
    """Fetch pages 1..MAX_PAGES, skipping pages already on disk for today."""
    run_date = date.today()
    query = config.search_query(run_date)
    client = GitHubClient()
    saved = 0
    skipped = 0
    try:
        for page in range(1, config.MAX_PAGES + 1):
            path = config.RAW_DIR / f"search_{run_date.isoformat()}_page{page}.json"
            if path.exists():
                skipped += 1
                log.info("search page %d already on disk, skipping", page)
                continue
            payload = collect_repos.fetch_search_page(client, query, page)
            collect_repos.save_page(payload, run_date, page)
            saved += 1
            log.info("search page %d saved (%d items)", page, len(payload.get("items", [])))
            if len(payload.get("items", [])) < config.PAGE_SIZE:
                log.info("page %d short → end of results", page)
                break
    except RateLimitExhausted as e:
        log.error("rate-limit during search: %s", e)
    finally:
        client.close()
    return saved, skipped


def collect_per_repo(repos: list[dict], kind: str, fetch_fn, cache_path_fn,
                     manifest: dict) -> tuple[int, int, int, int]:
    """Generic per-repo collector. kind ∈ {"languages","topics"}.

    Returns (fetched, skipped, failed, stale_refetched). A "stale_refetched"
    repo is one whose cache existed but `pushed_at > fetched_at` triggered
    a re-fetch — counted toward both `fetched` and `stale_refetched`.
    """
    client = GitHubClient(accept=config.TOPICS_ACCEPT if kind == "topics" else config.API_ACCEPT)
    fetched = 0
    skipped = 0
    failed = 0
    stale_refetched = 0
    try:
        for i, repo in enumerate(repos, 1):
            path: Path = cache_path_fn(repo["id"])
            pushed_raw = repo.get("pushed_at")
            try:
                pushed_at = (cache_manifest._parse_iso(pushed_raw)
                             if pushed_raw else datetime.now(timezone.utc))
            except (TypeError, ValueError):
                pushed_at = datetime.now(timezone.utc)

            cached_was_usable = cache_manifest._is_usable(path)
            if not cache_manifest.is_stale(manifest, repo["id"], kind, pushed_at, path):
                skipped += 1
                continue
            if cached_was_usable:
                stale_refetched += 1

            try:
                data = fetch_fn(client, repo["full_name"])
                path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
                cache_manifest.mark_fetched(manifest, repo["id"], kind,
                                            datetime.now(timezone.utc))
                fetched += 1
            except RateLimitExhausted:
                raise
            except Exception as e:  # 404 from renamed repos, etc.
                log.warning("%s fetch failed for %s: %s", kind, repo["full_name"], e)
                failed += 1
            if i % SAVE_EVERY_N_REPOS == 0:
                log.info("%s progress: %d/%d (fetched=%d skipped=%d failed=%d stale=%d)",
                         kind, i, len(repos), fetched, skipped, failed, stale_refetched)
                cache_manifest.save_atomic(manifest)
    except RateLimitExhausted as e:
        log.error("rate-limit during %s: %s", kind, e)
    finally:
        cache_manifest.save_atomic(manifest)
        client.close()
    return fetched, skipped, failed, stale_refetched


def build_csvs(repos: list[dict]) -> dict[str, Path]:
    config.ensure_dirs()
    repo_ids = [r["id"] for r in repos]
    df_repos = clean_data.load_search_pages()
    df_repos = clean_data.derive_columns(df_repos)
    df_langs = clean_data.build_languages_csv(repo_ids)
    df_topics = clean_data.build_topics_csv(repo_ids)

    paths = {
        "repos": config.PROCESSED_DIR / "repos.csv",
        "repo_languages": config.PROCESSED_DIR / "repo_languages.csv",
        "repo_topics": config.PROCESSED_DIR / "repo_topics.csv",
    }
    clean_data.write_csv_atomic(df_repos, paths["repos"])
    clean_data.write_csv_atomic(df_langs, paths["repo_languages"])
    clean_data.write_csv_atomic(df_topics, paths["repo_topics"])
    return paths


def main() -> dict:
    t0 = time.monotonic()
    config.ensure_dirs()
    log.info("=== STAGE 1: search pages ===")
    s_saved, s_skipped = collect_search_pages()
    log.info("search: saved=%d skipped=%d", s_saved, s_skipped)

    repos = discover_repos_on_disk()
    log.info("=== %d unique repos on disk ===", len(repos))

    manifest = cache_manifest.load()
    today = date.today()

    # First-run-after-upgrade: stamp existing caches as fresh so we don't
    # surge ~2000 API calls re-fetching everything via the mtime fallback.
    bootstrapped = cache_manifest.bootstrap_existing(
        manifest, today, [r["id"] for r in repos])

    # Mark every repo seen today (used by prune to detect repos that have
    # rolled out of the 30-day window long enough to evict).
    for r in repos:
        cache_manifest.mark_seen(manifest, r["id"], today)
    cache_manifest.save_atomic(manifest)

    log.info("=== STAGE 2: languages ===")
    l_fetched, l_skipped, l_failed, l_stale = collect_per_repo(
        repos, "languages", collect_languages.fetch,
        collect_languages.cache_path, manifest)
    log.info("languages: fetched=%d (of which stale-refetch=%d) skipped=%d failed=%d",
             l_fetched, l_stale, l_skipped, l_failed)

    log.info("=== STAGE 3: topics ===")
    t_fetched, t_skipped, t_failed, t_stale = collect_per_repo(
        repos, "topics", collect_topics.fetch,
        collect_topics.cache_path, manifest)
    log.info("topics: fetched=%d (of which stale-refetch=%d) skipped=%d failed=%d",
             t_fetched, t_stale, t_skipped, t_failed)

    log.info("=== STAGE 4: build CSVs ===")
    paths = build_csvs(repos)

    log.info("=== STAGE 5: prune stale-cache repos ===")
    pruned = cache_manifest.prune(manifest, today)
    cache_manifest.save_atomic(manifest)

    elapsed = time.monotonic() - t0

    summary = {
        "elapsed_seconds": round(elapsed, 1),
        "repos_total": len(repos),
        "search": {"saved": s_saved, "skipped": s_skipped},
        "languages": {
            "fetched": l_fetched, "stale_refetched": l_stale,
            "skipped": l_skipped, "failed": l_failed,
        },
        "topics": {
            "fetched": t_fetched, "stale_refetched": t_stale,
            "skipped": t_skipped, "failed": t_failed,
        },
        "manifest": {
            "bootstrapped_stamps": bootstrapped,
            "pruned_repo_ids": pruned,
            "pruned_count": len(pruned),
        },
        "csvs": {k: str(v) for k, v in paths.items()},
    }
    checkpoint = config.PROCESSED_DIR / "_collection_progress.json"
    checkpoint.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    log.info("=== DONE in %.1fs ===", elapsed)
    log.info("summary written to %s", checkpoint)
    return summary


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")
    main()
