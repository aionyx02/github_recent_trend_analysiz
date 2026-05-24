"""Stage 2b: per-repo /topics call (requires mercy-preview accept header).

Topics are also present on Search results, but the dedicated endpoint returns the
canonical, full list. Cache one JSON per repo on disk.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path

from src import config
from src.github_api import GitHubClient

log = logging.getLogger(__name__)


def fetch(client: GitHubClient, full_name: str) -> list[str]:
    resp = client.get(f"/repos/{full_name}/topics", accept=config.TOPICS_ACCEPT)
    return resp.json().get("names", [])


def cache_path(repo_id: int) -> Path:
    return config.RAW_DIR / "topics" / f"{repo_id}.json"


def run_for_repos(repos: list[dict]) -> int:
    config.ensure_dirs()
    client = GitHubClient()
    fetched = 0
    try:
        for repo in repos:
            path = cache_path(repo["id"])
            if path.exists():
                continue
            topics = fetch(client, repo["full_name"])
            path.write_text(json.dumps(topics, ensure_ascii=False), encoding="utf-8")
            fetched += 1
    finally:
        client.close()
    return fetched