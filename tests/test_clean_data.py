"""Unit tests for src.clean_data — pure transforms, no network."""

from datetime import date

import pandas as pd

from src.clean_data import derive_columns, flatten_repo


def test_flatten_repo_full_payload():
    raw = {
        "id": 42,
        "full_name": "octo/cat",
        "owner": {"login": "octo"},
        "name": "cat",
        "html_url": "https://github.com/octo/cat",
        "description": "purr",
        "created_at": "2026-05-01T00:00:00Z",
        "pushed_at": "2026-05-20T00:00:00Z",
        "stargazers_count": 100,
        "forks_count": 10,
        "subscribers_count": 5,
        "watchers_count": 100,
        "open_issues_count": 3,
        "language": "Python",
        "size": 1234,
        "license": {"spdx_id": "MIT"},
    }
    row = flatten_repo(raw)
    assert row["id"] == 42
    assert row["owner"] == "octo"
    assert row["stars"] == 100
    assert row["watchers"] == 5  # prefer subscribers_count over watchers_count
    assert row["primary_language"] == "Python"
    assert row["license"] == "MIT"


def test_flatten_repo_applies_missing_value_rules():
    raw = {
        "id": 1,
        "full_name": "a/b",
        "owner": {"login": "a"},
        "name": "b",
        "html_url": "",
        "description": None,
        "created_at": "2026-05-01T00:00:00Z",
        "pushed_at": "2026-05-01T00:00:00Z",
        "stargazers_count": 50,
        "forks_count": 0,
        "watchers_count": 50,
        "open_issues_count": 0,
        "language": None,
        "size": 0,
        "license": None,
    }
    row = flatten_repo(raw)
    assert row["description"] == ""
    assert row["primary_language"] == "Unknown"
    assert row["license"] == "None"


def test_flatten_repo_falls_back_to_watchers_count_when_subscribers_missing():
    raw = {
        "id": 1, "full_name": "a/b", "owner": {"login": "a"}, "name": "b",
        "html_url": "", "description": "",
        "created_at": "2026-05-01T00:00:00Z", "pushed_at": "2026-05-01T00:00:00Z",
        "stargazers_count": 10, "forks_count": 0,
        "watchers_count": 7,
        "open_issues_count": 0, "language": "Go", "size": 0, "license": None,
    }
    assert flatten_repo(raw)["watchers"] == 7


def test_derive_columns_math():
    df = pd.DataFrame([{
        "id": 1, "full_name": "a/b", "owner": "a", "name": "b", "html_url": "",
        "description": "", "created_at": "2026-05-01T00:00:00Z",
        "pushed_at": "2026-05-20T00:00:00Z",
        "stars": 100, "forks": 20, "watchers": 100, "open_issues": 5,
        "primary_language": "Python", "size": 0, "license": "MIT",
    }])
    out = derive_columns(df, today=date(2026, 5, 21))
    assert out.loc[0, "age_days"] == 20
    assert out.loc[0, "stars_per_day"] == 5.0
    assert out.loc[0, "fork_star_ratio"] == 0.2
    assert out.loc[0, "issue_star_ratio"] == 0.05


def test_derive_columns_clips_age_to_at_least_one_day():
    """Repo created today should not divide by zero."""
    df = pd.DataFrame([{
        "id": 1, "full_name": "a/b", "owner": "a", "name": "b", "html_url": "",
        "description": "", "created_at": "2026-05-24T00:00:00Z",
        "pushed_at": "2026-05-24T00:00:00Z",
        "stars": 50, "forks": 0, "watchers": 50, "open_issues": 0,
        "primary_language": "Rust", "size": 0, "license": "MIT",
    }])
    out = derive_columns(df, today=date(2026, 5, 24))
    assert out.loc[0, "age_days"] == 1
    assert out.loc[0, "stars_per_day"] == 50.0


def test_derive_columns_zero_stars_doesnt_divide_by_zero():
    df = pd.DataFrame([{
        "id": 1, "full_name": "a/b", "owner": "a", "name": "b", "html_url": "",
        "description": "", "created_at": "2026-05-01T00:00:00Z",
        "pushed_at": "2026-05-01T00:00:00Z",
        "stars": 0, "forks": 3, "watchers": 0, "open_issues": 1,
        "primary_language": "C", "size": 0, "license": "MIT",
    }])
    out = derive_columns(df, today=date(2026, 5, 21))
    assert out.loc[0, "fork_star_ratio"] == 3.0
    assert out.loc[0, "issue_star_ratio"] == 1.0