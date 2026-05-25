"""Unit tests for src.cache_manifest (pure I/O against tmp_path)."""

from __future__ import annotations

import json
import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import pytest

from src import cache_manifest


# ──────────────────────── helpers ────────────────────────

def _utc(year: int, month: int, day: int, hour: int = 0) -> datetime:
    return datetime(year, month, day, hour, tzinfo=timezone.utc)


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


@pytest.fixture
def stub_caches(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """Redirect cache_path() helpers to tmp_path so prune/bootstrap touch test files only."""
    lang_dir = tmp_path / "languages"
    topic_dir = tmp_path / "topics"
    lang_dir.mkdir()
    topic_dir.mkdir()
    from src import collect_languages, collect_topics
    monkeypatch.setattr(collect_languages, "cache_path",
                        lambda rid: lang_dir / f"{rid}.json")
    monkeypatch.setattr(collect_topics, "cache_path",
                        lambda rid: topic_dir / f"{rid}.json")
    return lang_dir, topic_dir


# ──────────────────────── load / save_atomic ────────────────────────

def test_load_missing_file_returns_empty_manifest(tmp_path: Path):
    m = cache_manifest.load(tmp_path / "nope.json")
    assert m == {"_manifest_version": 1, "repos": {}}


def test_load_corrupt_file_returns_empty_manifest(tmp_path: Path):
    bad = tmp_path / "bad.json"
    bad.write_text("{ not json", encoding="utf-8")
    m = cache_manifest.load(bad)
    assert m == {"_manifest_version": 1, "repos": {}}


def test_save_atomic_roundtrip(tmp_path: Path):
    path = tmp_path / "m.json"
    m = {"_manifest_version": 1, "repos": {"42": {"last_seen_at": "2026-05-25"}}}
    cache_manifest.save_atomic(m, path)
    assert json.loads(path.read_text(encoding="utf-8")) == m
    # tmp file should not linger after a successful save
    assert not (tmp_path / "m.json.tmp").exists()


def test_save_atomic_failure_leaves_original_intact(tmp_path: Path):
    path = tmp_path / "m.json"
    original = {"_manifest_version": 1, "repos": {"1": {"last_seen_at": "2020-01-01"}}}
    cache_manifest.save_atomic(original, path)

    with patch.object(os, "replace", side_effect=OSError("disk full")):
        with pytest.raises(OSError):
            cache_manifest.save_atomic({"_manifest_version": 1, "repos": {}}, path)

    # original file unchanged because replace failed before clobbering it
    assert json.loads(path.read_text(encoding="utf-8")) == original


# ──────────────────────── is_stale truth table ────────────────────────

def test_is_stale_when_cache_file_missing(tmp_path: Path):
    m = {"_manifest_version": 1, "repos": {}}
    missing = tmp_path / "nope.json"
    assert cache_manifest.is_stale(m, 1, "languages", _utc(2026, 5, 25), missing) is True


def test_is_stale_when_cache_file_empty(tmp_path: Path):
    m = {"_manifest_version": 1, "repos": {}}
    empty = tmp_path / "empty.json"
    empty.touch()
    assert cache_manifest.is_stale(m, 1, "languages", _utc(2026, 5, 25), empty) is True


def test_is_stale_no_manifest_entry_falls_back_to_mtime(tmp_path: Path):
    cache = tmp_path / "1.json"
    _write_json(cache, {"Python": 100})
    old_mtime = (_utc(2026, 1, 1)).timestamp()
    os.utime(cache, (old_mtime, old_mtime))

    m = {"_manifest_version": 1, "repos": {}}
    # pushed_at AFTER mtime → stale
    assert cache_manifest.is_stale(m, 1, "languages", _utc(2026, 5, 1), cache) is True
    # pushed_at BEFORE mtime → fresh
    assert cache_manifest.is_stale(m, 1, "languages", _utc(2025, 12, 1), cache) is False


def test_is_stale_manifest_entry_governs_when_present(tmp_path: Path):
    cache = tmp_path / "1.json"
    _write_json(cache, {"Python": 100})
    # mtime is recent (now) so mtime fallback would say fresh
    m = {
        "_manifest_version": 1,
        "repos": {"1": {"languages_fetched_at": _utc(2026, 1, 1).isoformat()}},
    }
    # manifest says fetched in Jan; pushed in May → stale per manifest
    assert cache_manifest.is_stale(m, 1, "languages", _utc(2026, 5, 1), cache) is True


def test_is_stale_future_pushed_at_then_catchup(tmp_path: Path):
    cache = tmp_path / "1.json"
    _write_json(cache, {"Python": 100})
    m = {
        "_manifest_version": 1,
        "repos": {"1": {"languages_fetched_at": _utc(2026, 5, 25).isoformat()}},
    }
    # pushed_at in the future → still stale (re-fetch this run)
    assert cache_manifest.is_stale(m, 1, "languages", _utc(2030, 1, 1), cache) is True
    # After we re-fetch and stamp now, a future pushed_at older than fetched_at = fresh
    cache_manifest.mark_fetched(m, 1, "languages", _utc(2030, 6, 1))
    assert cache_manifest.is_stale(m, 1, "languages", _utc(2030, 1, 1), cache) is False


def test_is_stale_accepts_naive_pushed_at_as_utc(tmp_path: Path):
    cache = tmp_path / "1.json"
    _write_json(cache, {"Python": 100})
    m = {
        "_manifest_version": 1,
        "repos": {"1": {"languages_fetched_at": _utc(2026, 5, 25).isoformat()}},
    }
    naive_future = datetime(2030, 1, 1)  # no tzinfo
    assert cache_manifest.is_stale(m, 1, "languages", naive_future, cache) is True


# ──────────────────────── mark_fetched / mark_seen ────────────────────────

def test_mark_fetched_writes_iso_utc_string():
    m = cache_manifest._empty_manifest()
    cache_manifest.mark_fetched(m, 42, "topics", _utc(2026, 5, 25, 6))
    assert m["repos"]["42"]["topics_fetched_at"] == "2026-05-25T06:00:00+00:00"


def test_mark_fetched_rejects_unknown_kind():
    m = cache_manifest._empty_manifest()
    with pytest.raises(ValueError):
        cache_manifest.mark_fetched(m, 1, "stars", _utc(2026, 5, 25))


def test_mark_seen_is_idempotent():
    m = cache_manifest._empty_manifest()
    cache_manifest.mark_seen(m, 7, date(2026, 5, 25))
    cache_manifest.mark_seen(m, 7, date(2026, 5, 25))
    assert m["repos"]["7"] == {"last_seen_at": "2026-05-25"}


# ──────────────────────── bootstrap_existing ────────────────────────

def test_bootstrap_existing_stamps_only_when_repos_empty(stub_caches):
    lang_dir, topic_dir = stub_caches
    _write_json(lang_dir / "1.json", {"Go": 50})
    _write_json(topic_dir / "1.json", ["bot"])

    m = cache_manifest._empty_manifest()
    n = cache_manifest.bootstrap_existing(m, date(2026, 5, 25), [1])
    assert n == 2
    assert m["repos"]["1"]["languages_fetched_at"]
    assert m["repos"]["1"]["topics_fetched_at"]
    assert m["repos"]["1"]["last_seen_at"] == "2026-05-25"

    # Second call: manifest already has repos → no-op
    m["repos"]["1"]["languages_fetched_at"] = "frozen"
    n2 = cache_manifest.bootstrap_existing(m, date(2026, 6, 1), [1])
    assert n2 == 0
    assert m["repos"]["1"]["languages_fetched_at"] == "frozen"


# ──────────────────────── prune ────────────────────────

def test_prune_evicts_stale_repos_and_files(stub_caches):
    lang_dir, topic_dir = stub_caches
    _write_json(lang_dir / "100.json", {"C": 1})
    _write_json(topic_dir / "100.json", ["x"])
    _write_json(lang_dir / "200.json", {"Rust": 1})

    today = date(2026, 5, 25)
    m = {
        "_manifest_version": 1,
        "repos": {
            "100": {"last_seen_at": (today - timedelta(days=70)).isoformat()},
            "200": {"last_seen_at": today.isoformat()},
        },
    }
    pruned = cache_manifest.prune(m, today, buffer_days=60)
    assert pruned == [100]
    assert not (lang_dir / "100.json").exists()
    assert not (topic_dir / "100.json").exists()
    assert (lang_dir / "200.json").exists()
    assert "100" not in m["repos"]
    assert "200" in m["repos"]


def test_prune_respects_max_pruned_ceiling(stub_caches):
    lang_dir, _ = stub_caches
    today = date(2026, 5, 25)
    old_iso = (today - timedelta(days=100)).isoformat()
    repos = {}
    for rid in range(1, 11):
        _write_json(lang_dir / f"{rid}.json", {"X": 1})
        repos[str(rid)] = {"last_seen_at": old_iso}
    m = {"_manifest_version": 1, "repos": repos}

    pruned = cache_manifest.prune(m, today, buffer_days=60, max_pruned=3)
    assert len(pruned) == 3
    # Remaining caches should equal 10 - 3 = 7
    remaining = list(lang_dir.glob("*.json"))
    assert len(remaining) == 7
