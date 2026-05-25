"""Stage 1: paginate GitHub Search API and persist raw JSON pages.

Output: data/raw/search_<YYYY-MM-DD>_pageN.json (one file per page, never overwritten).
Caps at config.MAX_PAGES (10 by default → 1000 repos, the GitHub Search API hard limit).
"""

from __future__ import annotations

import json
import logging
from datetime import date

from src import config
from src.github_api import GitHubClient, RateLimitExhausted

log = logging.getLogger(__name__)


def fetch_search_page(client: GitHubClient, query: str, page: int) -> dict:
    resp = client.get(
        "/search/repositories",
        params={"q": query, "sort": "stars", "order": "desc",
                "per_page": config.PAGE_SIZE, "page": page},
    )
    return resp.json()


def save_page(payload: dict, run_date: date, page: int) -> str:
    config.ensure_dirs()
    path = config.RAW_DIR / f"search_{run_date.isoformat()}_page{page}.json"
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return str(path)


def run(max_pages: int | None = None) -> list[str]:
    """Fetch up to `max_pages` of search results. Returns list of saved file paths."""
    run_date = date.today()
    query = config.search_query(run_date)
    cap = max_pages or config.MAX_PAGES
    client = GitHubClient()
    saved: list[str] = []
    try:
        for page in range(1, cap + 1):
            payload = fetch_search_page(client, query, page)
            saved.append(save_page(payload, run_date, page))
            if len(payload.get("items", [])) < config.PAGE_SIZE:
                break
    except RateLimitExhausted as e:
        log.error("%s — saved %d page(s) so far", e, len(saved))
    finally:
        client.close()
    return saved


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    files = run()
    print(f"saved {len(files)} page(s)")
    for f in files:
        print(f"  {f}")