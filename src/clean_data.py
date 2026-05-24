"""Stage 3: JSON → flat CSV. Applies proposal §9.2 missing-value rules and §7.4 derived columns.

Pure functions where possible — `flatten_repo` and `derive_columns` are unit-testable
without disk or network.
"""

from __future__ import annotations

import json
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from src import config


REPO_COLUMNS = [
    "id", "full_name", "owner", "name", "html_url", "description",
    "created_at", "pushed_at", "stars", "forks", "watchers", "open_issues",
    "primary_language", "size", "license",
]


def flatten_repo(raw: dict[str, Any]) -> dict[str, Any]:
    """Flatten a Search-API repo item into the columns defined in docs/data.md."""
    license_obj = raw.get("license") or {}
    owner_obj = raw.get("owner") or {}
    return {
        "id": raw["id"],
        "full_name": raw["full_name"],
        "owner": owner_obj.get("login", ""),
        "name": raw.get("name", ""),
        "html_url": raw.get("html_url", ""),
        "description": raw.get("description") or "",
        "created_at": raw.get("created_at"),
        "pushed_at": raw.get("pushed_at"),
        "stars": raw.get("stargazers_count", 0),
        "forks": raw.get("forks_count", 0),
        "watchers": raw.get("subscribers_count", raw.get("watchers_count", 0)),
        "open_issues": raw.get("open_issues_count", 0),
        "primary_language": raw.get("language") or "Unknown",
        "size": raw.get("size", 0),
        "license": (license_obj.get("spdx_id") if license_obj else None) or "None",
    }


def load_search_pages(raw_dir: Path | None = None) -> pd.DataFrame:
    raw_dir = raw_dir or config.RAW_DIR
    rows: list[dict[str, Any]] = []
    seen: set[int] = set()
    for path in sorted(raw_dir.glob("search_*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for item in payload.get("items", []):
            if item["id"] in seen:
                continue
            seen.add(item["id"])
            rows.append(flatten_repo(item))
    return pd.DataFrame(rows, columns=REPO_COLUMNS)


def derive_columns(df: pd.DataFrame, today: date | None = None) -> pd.DataFrame:
    """Add age_days, stars_per_day, fork_star_ratio, issue_star_ratio (proposal §7.4)."""
    out = df.copy()
    out["created_at"] = pd.to_datetime(out["created_at"], utc=True)
    out["pushed_at"] = pd.to_datetime(out["pushed_at"], utc=True)
    reference = pd.Timestamp(today or date.today(), tz=timezone.utc)
    out["age_days"] = (reference - out["created_at"]).dt.days.clip(lower=1)
    out["stars_per_day"] = out["stars"] / out["age_days"]
    out["fork_star_ratio"] = out["forks"] / out["stars"].clip(lower=1)
    out["issue_star_ratio"] = out["open_issues"] / out["stars"].clip(lower=1)
    return out


def write_csv_atomic(df: pd.DataFrame, path: Path) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    df.to_csv(tmp, index=False, encoding="utf-8")
    tmp.replace(path)


def build_languages_csv(repo_ids: list[int]) -> pd.DataFrame:
    rows = []
    for rid in repo_ids:
        path = config.RAW_DIR / "languages" / f"{rid}.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        for lang, byte_count in data.items():
            rows.append({"repo_id": rid, "language": lang, "bytes": byte_count})
    return pd.DataFrame(rows, columns=["repo_id", "language", "bytes"])


def build_topics_csv(repo_ids: list[int]) -> pd.DataFrame:
    rows = []
    for rid in repo_ids:
        path = config.RAW_DIR / "topics" / f"{rid}.json"
        if not path.exists():
            continue
        topics = json.loads(path.read_text(encoding="utf-8"))
        for topic in topics:
            rows.append({"repo_id": rid, "topic": topic})
    return pd.DataFrame(rows, columns=["repo_id", "topic"])


def run() -> dict[str, Path]:
    """Build repos.csv (with derived columns) from all raw search pages.

    Returns paths of written CSVs.
    """
    config.ensure_dirs()
    repos = load_search_pages()
    if repos.empty:
        raise RuntimeError(
            f"No raw search pages found under {config.RAW_DIR}. Run collect_repos first."
        )
    repos = derive_columns(repos)
    repos_path = config.PROCESSED_DIR / "repos.csv"
    write_csv_atomic(repos, repos_path)
    return {"repos": repos_path}


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    paths = run()
    for name, path in paths.items():
        print(f"{name}: {path}")