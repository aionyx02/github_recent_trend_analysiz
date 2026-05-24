"""Central configuration: env-only secrets, date range, pagination caps, output paths.

Importing this module must not perform any network I/O. Token loading is lazy so
unit tests can run without a real `GITHUB_TOKEN`.
"""

from __future__ import annotations

import os
from datetime import date, timedelta
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

DATA_VERSION = "v1"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"

WINDOW_DAYS = 30
STARS_THRESHOLD = 10
PAGE_SIZE = 100
MAX_PAGES = 10
TARGET_REPOS = PAGE_SIZE * MAX_PAGES

API_BASE = "https://api.github.com"
API_ACCEPT = "application/vnd.github+json"
TOPICS_ACCEPT = "application/vnd.github.mercy-preview+json"

REQUEST_SLEEP_SECONDS = 0.8
MAX_RETRIES = 3
RETRY_BACKOFF_SECONDS = 5


def get_token() -> str:
    """Read GITHUB_TOKEN from env. Raises if missing — never falls back to anonymous."""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise RuntimeError(
            "GITHUB_TOKEN not set. Export it in your shell or put it in .env "
            "(see .env.example). Never commit the token."
        )
    return token


def date_range(today: date | None = None) -> tuple[date, date]:
    """Return (start, end) covering the last WINDOW_DAYS days, inclusive."""
    end = today or date.today()
    start = end - timedelta(days=WINDOW_DAYS)
    return start, end


def search_query(today: date | None = None) -> str:
    """Build the GitHub Search query string per proposal §8.1."""
    start, end = date_range(today)
    return f"created:{start}..{end} stars:>{STARS_THRESHOLD} fork:false"


def ensure_dirs() -> None:
    """Create all output directories. Safe to call repeatedly."""
    for d in (RAW_DIR, RAW_DIR / "languages", RAW_DIR / "topics", PROCESSED_DIR, FIGURES_DIR):
        d.mkdir(parents=True, exist_ok=True)