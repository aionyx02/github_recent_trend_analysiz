"""Stage 2a: per-repo /languages call. One JSON per repo, cached on disk."""

from __future__ import annotations

import json
import logging
from pathlib import Path

from src import config
from src.github_api import GitHubClient

log = logging.getLogger(__name__)


def fetch(client: GitHubClient, full_name: str) -> dict[str, int]:
    resp = client.get(f"/repos/{full_name}/languages")
    return resp.json()


def cache_path(repo_id: int) -> Path:
    return config.RAW_DIR / "languages" / f"{repo_id}.json"


def run_for_repos(repos: list[dict]) -> int:
    """repos is a list of dicts with at least `id` and `full_name`. Returns count fetched."""
    config.ensure_dirs()
    client = GitHubClient()
    fetched = 0
    try:
        for repo in repos:
            path = cache_path(repo["id"])
            if path.exists():
                continue
            data = fetch(client, repo["full_name"])
            path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            fetched += 1
    finally:
        client.close()
    return fetched