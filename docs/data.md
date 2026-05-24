---
type: data_contracts
status: active
priority: p1
updated: 2026-05-24
context_policy: retrieve_when_planning
owner: project
---

# Data Contracts

## Purpose

Define durable data shapes for the GitHub trend pipeline. The proposal §7 is the source of truth for column meanings; this file pins file paths, types, and missing-value rules.

## Core Entities

| Entity | Meaning | Owner | Notes |
|---|---|---|---|
| `repo` | One GitHub repository observed in the 30-day window. | `src/collect_repos` → `src/clean_data` | Primary key = `id` (GitHub repo ID). |
| `repo_language` | A language used in a repo, with byte count. | `src/collect_languages` | Many rows per repo. |
| `repo_topic` | A topic tag assigned to a repo. | `src/collect_topics` | Many rows per repo. |
| `category` | Rule-based classification result. | `src/classify` | Single value per repo in MVP. |

## File Layout

| Path | Format | Producer |
|---|---|---|
| `data/raw/search_<YYYY-MM-DD>.json` | Raw GitHub Search API response, per page. | `collect_repos` |
| `data/raw/languages/<repo_id>.json` | Raw `/repos/.../languages` response. | `collect_languages` |
| `data/raw/topics/<repo_id>.json` | Raw `/repos/.../topics` response. | `collect_topics` |
| `data/processed/repos.csv` | Flat repo table (proposal §7.1) + derived columns (§7.4). | `clean_data` + `classify` |
| `data/processed/repo_languages.csv` | Long-format language usage. | `clean_data` |
| `data/processed/repo_topics.csv` | Long-format topics. | `clean_data` |

## `repos.csv` Schema

Columns and types — see proposal §7.1 for descriptions:

| Column | Type | Required | Notes |
|---|---|---|---|
| `id` | int64 | yes | GitHub repo ID, primary key. |
| `full_name` | string | yes | `owner/repo`. |
| `owner` | string | yes | |
| `name` | string | yes | |
| `html_url` | string | yes | |
| `description` | string | no | Empty string if missing (proposal §9.2). |
| `created_at` | datetime (UTC) | yes | ISO 8601 from API; parsed to pandas datetime. |
| `pushed_at` | datetime (UTC) | yes | |
| `stars` | int64 | yes | `stargazers_count`. |
| `forks` | int64 | yes | `forks_count`. |
| `watchers` | int64 | yes | `subscribers_count` if available; fallback to `watchers_count`. |
| `open_issues` | int64 | yes | `open_issues_count` — includes PRs (noted as a known limitation in report). |
| `primary_language` | string | no | `"Unknown"` if missing. |
| `size` | int64 | yes | KB. |
| `license` | string | no | `"None"` if missing. |
| `age_days` | int64 | derived | `today - created_at` in days. |
| `stars_per_day` | float64 | derived | `stars / max(age_days, 1)`. |
| `fork_star_ratio` | float64 | derived | `forks / max(stars, 1)`. |
| `issue_star_ratio` | float64 | derived | `open_issues / max(stars, 1)`. |
| `category` | string | derived | One of `AI/ML, Web, Data, DevOps, Security, Game, CLI/Tooling, Mobile, Other`. |

## `repo_languages.csv` Schema

| Column | Type | Notes |
|---|---|---|
| `repo_id` | int64 | FK → `repos.id`. |
| `language` | string | |
| `bytes` | int64 | |

## `repo_topics.csv` Schema

| Column | Type | Notes |
|---|---|---|
| `repo_id` | int64 | FK → `repos.id`. |
| `topic` | string | Lowercase, hyphenated (GitHub returns canonical form). |

## Missing Value Rules

From proposal §9.2:

| Field | Rule |
|---|---|
| `description` | empty string |
| `primary_language` | `"Unknown"` |
| `license` | `"None"` |
| `topics` | empty list (no rows in `repo_topics`) |

## Persistence Rules

- Raw JSON is **immutable**. Re-runs write to a new dated file; never overwrite.
- Processed CSVs are **regeneratable** from raw — safe to delete.
- All timestamps stored as UTC ISO 8601 in raw; converted to timezone-aware pandas datetime in processed.
- Numeric ratios (`stars_per_day`, etc.) computed at clean time, not at chart time, so reports stay consistent.

## Migration Rules

- Schema changes to `repos.csv` require either (a) a header migration script or (b) bumping a `data_version` constant in `src/config.py` and writing the new CSV to a versioned subfolder.
- Adding columns is backward-compatible; renaming or removing columns is breaking → needs ADR.

## Cache Rules

- The raw layer **is** the cache. No in-memory caching needed for MVP.
- If a repo appears in `data/raw/languages/<id>.json` and the file mtime is within the current 30-day window, skip the API call.