"""Unit tests for src.config — query string + date math."""

from datetime import date

from src import config


def test_search_query_format():
    q = config.search_query(today=date(2026, 5, 24))
    assert q == "created:2026-04-24..2026-05-24 stars:>10 fork:false"


def test_date_range_window():
    start, end = config.date_range(today=date(2026, 5, 24))
    assert end == date(2026, 5, 24)
    assert (end - start).days == config.WINDOW_DAYS


def test_get_token_raises_when_missing(monkeypatch):
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    try:
        config.get_token()
    except RuntimeError as e:
        assert "GITHUB_TOKEN" in str(e)
    else:
        raise AssertionError("expected RuntimeError")