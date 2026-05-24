---
type: architecture_spec
status: active
priority: p1
updated: 2026-05-24
context_policy: retrieve_only
owner: project
---

# Architecture

## System Overview

A batch ETL pipeline. Each stage writes its output to disk so the next stage can resume without re-calling the GitHub API.

```text
GitHub REST API
        |
        v
src/collect_repos       -> data/raw/search_YYYY-MM-DD.json
src/collect_languages   -> data/raw/languages/<repo_id>.json
src/collect_topics      -> data/raw/topics/<repo_id>.json
        |
        v
src/clean_data          -> data/processed/repos.csv
                           data/processed/repo_languages.csv
                           data/processed/repo_topics.csv
        |
        v
src/classify            -> adds `category` column to repos.csv
        |
        v
src/visualize           -> outputs/figures/*.png  (+ optional Plotly HTML)
        |
        v
notebooks/analysis.ipynb + outputs/report.md
        |
        v
(optional) dashboard/app.py (Streamlit)
```

## Modules

Refer to proposal §14.2 for the full module list. Summary:

| Module | Responsibility | Notes |
|---|---|---|
| `src/config.py` | Load `GITHUB_TOKEN`, date range, pagination caps, output paths. | Env-only secrets. |
| `src/github_api.py` | HTTP wrapper: headers, retry, rate-limit detection, sleep between calls. | Pinned via ADR-0001. |
| `src/collect_repos.py` | Search API; paginate up to N pages; persist raw JSON. | 5 pages × 100 = 500 max. |
| `src/collect_languages.py` | Per-repo `/languages` calls. | 1 request per repo. |
| `src/collect_topics.py` | Per-repo `/topics` with `Accept: application/vnd.github.mercy-preview+json`. | 1 request per repo. |
| `src/clean_data.py` | JSON → flat CSV; type coercion; missing-value rules (proposal §9.2). | Pure functions, easy to unit-test. |
| `src/classify.py` | Rule-based classifier using description + topics + primary_language. | See ADR-0003. |
| `src/visualize.py` | Matplotlib figures for required charts (proposal §12.1). | Plotly for optional interactive figures. |
| `dashboard/app.py` | Streamlit UI (optional). | Only if BACKLOG.001 promoted. |

## Data Flow Contracts

- **Raw layer** (`data/raw/`) — read-only after write. Never overwrite; new runs get a dated filename. Allows full re-derivation of CSVs.
- **Processed layer** (`data/processed/`) — regeneratable CSVs. Safe to delete and rebuild from raw.
- **Output layer** (`outputs/`) — figures + report. Regeneratable from processed layer.

## Architecture Constraints

- One module per pipeline stage; do not collapse fetch + clean into a single script.
- All network calls go through `src/github_api.py` (single rate-limit chokepoint).
- No mutation of raw JSON files after they are written.
- Token must come from `os.getenv("GITHUB_TOKEN")`; never read from a tracked file.
- Pipeline must run in <10 minutes on the 500-repo cap (rate-limit-aware sleeps included).

## Open Architecture Questions

- Will SQLite live alongside CSV from the start, or be added later (BACKLOG.002)? Gated by ADR-0002.
- Should `collect_languages` and `collect_topics` run in parallel via `asyncio` + `httpx`? Defer until baseline timing is measured.
- Where to store classification rules — Python dict, YAML, or JSON? Default = Python dict embedded in `classify.py`; revisit if rules grow past ~50 keywords.