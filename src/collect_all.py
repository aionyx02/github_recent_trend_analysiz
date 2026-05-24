"""End-to-end collection orchestrator: search → languages → topics → CSVs.

Idempotent: existing pages, language caches, and topic caches are skipped.
Safe to re-run after a rate-limit stop — picks up where it left off.
Writes a `data/processed/_collection_progress.json` checkpoint after each stage
so you can inspect what was finished without re-parsing all the raw files.
"""

from __future__ import annotations

import json
import logging
import time
from datetime import date
from pathlib import Path

from src import config, collect_languages, collect_repos, collect_topics, clean_data
from src.github_api import GitHubClient, RateLimitExhausted

log = logging.getLogger(__name__)


def discover_repos_on_disk() -> list[dict]:
    """Parse every saved search_*.json and return a deduplicated repo list."""
    out: dict[int, dict] = {}
    for path in sorted(config.RAW_DIR.glob("search_*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for item in payload.get("items", []):
            out.setdefault(item["id"], {"id": item["id"], "full_name": item["full_name"]})
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


def collect_per_repo(repos: list[dict], kind: str, fetch_fn, cache_path_fn) -> tuple[int, int, int]:
    """Generic per-repo collector. kind ∈ {"languages","topics"}."""
    client = GitHubClient(accept=config.TOPICS_ACCEPT if kind == "topics" else config.API_ACCEPT)
    fetched = 0
    skipped = 0
    failed = 0
    try:
        for i, repo in enumerate(repos, 1):
            path: Path = cache_path_fn(repo["id"])
            if path.exists():
                skipped += 1
                continue
            try:
                data = fetch_fn(client, repo["full_name"])
                path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
                fetched += 1
            except RateLimitExhausted:
                raise
            except Exception as e:  # 404 from renamed repos, etc.
                log.warning("%s fetch failed for %s: %s", kind, repo["full_name"], e)
                failed += 1
            if i % 50 == 0:
                log.info("%s progress: %d/%d (fetched=%d skipped=%d failed=%d)",
                         kind, i, len(repos), fetched, skipped, failed)
    except RateLimitExhausted as e:
        log.error("rate-limit during %s: %s", kind, e)
    finally:
        client.close()
    return fetched, skipped, failed


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

    log.info("=== STAGE 2: languages ===")
    l_fetched, l_skipped, l_failed = collect_per_repo(
        repos, "languages", collect_languages.fetch, collect_languages.cache_path)
    log.info("languages: fetched=%d skipped=%d failed=%d", l_fetched, l_skipped, l_failed)

    log.info("=== STAGE 3: topics ===")
    t_fetched, t_skipped, t_failed = collect_per_repo(
        repos, "topics", collect_topics.fetch, collect_topics.cache_path)
    log.info("topics: fetched=%d skipped=%d failed=%d", t_fetched, t_skipped, t_failed)

    log.info("=== STAGE 4: build CSVs ===")
    paths = build_csvs(repos)
    elapsed = time.monotonic() - t0

    summary = {
        "elapsed_seconds": round(elapsed, 1),
        "repos_total": len(repos),
        "search": {"saved": s_saved, "skipped": s_skipped},
        "languages": {"fetched": l_fetched, "skipped": l_skipped, "failed": l_failed},
        "topics": {"fetched": t_fetched, "skipped": t_skipped, "failed": t_failed},
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