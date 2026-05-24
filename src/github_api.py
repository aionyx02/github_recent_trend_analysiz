"""GitHub REST API wrapper: single chokepoint for headers, retry, and rate-limit handling.

All other collect_* modules MUST go through this module. Do not call `requests.get`
directly elsewhere — that would bypass token redaction and rate-limit accounting.
"""

from __future__ import annotations

import logging
import time
from typing import Any

import requests

from src import config

log = logging.getLogger(__name__)


class RateLimitExhausted(RuntimeError):
    """Raised when GitHub returns 403 with X-RateLimit-Remaining: 0."""


class GitHubClient:
    def __init__(self, token: str | None = None, accept: str = config.API_ACCEPT) -> None:
        self._token = token or config.get_token()
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {self._token}",
            "Accept": accept,
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "github-recent-trend-analysiz/0.1",
        })

    def get(self, path: str, params: dict[str, Any] | None = None,
            accept: str | None = None) -> requests.Response:
        url = path if path.startswith("http") else f"{config.API_BASE}{path}"
        headers = {"Accept": accept} if accept else None

        for attempt in range(1, config.MAX_RETRIES + 1):
            resp = self._session.get(url, params=params, headers=headers, timeout=30)
            if resp.status_code == 200:
                time.sleep(config.REQUEST_SLEEP_SECONDS)
                return resp
            if resp.status_code == 403 and resp.headers.get("X-RateLimit-Remaining") == "0":
                reset = resp.headers.get("X-RateLimit-Reset", "?")
                raise RateLimitExhausted(
                    f"Rate limit exhausted. Resets at unix ts {reset}. Stopping."
                )
            if resp.status_code in (502, 503, 504):
                wait = config.RETRY_BACKOFF_SECONDS * attempt
                log.warning("transient %s on %s, retry %d in %ds", resp.status_code, path, attempt, wait)
                time.sleep(wait)
                continue
            resp.raise_for_status()

        raise RuntimeError(f"Exceeded retries for {path}")

    def close(self) -> None:
        self._session.close()