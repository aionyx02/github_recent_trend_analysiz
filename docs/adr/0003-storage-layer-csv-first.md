---
type: adr
status: proposed
priority: p1
updated: 2026-05-24
context_policy: on_demand
owner: project
---

# ADR-0003: Storage Layer — CSV-First, SQLite Optional

## Status

Proposed

## Context

The proposal §13 lists Python + pandas + SQLite + Plotly + Streamlit as the recommended stack. The dataset is 300–500 rows for `repos`, plus ~1500–4000 rows total across `repo_languages` and `repo_topics`. At this scale:

- pandas + CSV gives a self-describing, diffable artifact that is easy to attach to the report.
- SQLite adds query power and is useful for a dashboard, but is a second source of truth that must be kept in sync.

We must avoid maintaining two write paths in MVP.

## Decision

**MVP:** CSV is the sole persisted format.
- `data/raw/*.json` (immutable raw layer)
- `data/processed/repos.csv`, `repo_languages.csv`, `repo_topics.csv`

**Stretch (BACKLOG.002):** Add SQLite as a *read-only derived view*, built from CSV by a one-shot script. Never write through SQLite back to CSV.

## Consequences

### Positive

- Single source of truth (CSV) at MVP scale.
- Reviewer can open the dataset in Excel without any tooling.
- Removes ORM / schema-migration concerns.

### Negative

- Cross-table queries (e.g., "top categories by total stars") require pandas joins instead of SQL.
- No transactional guarantees during a run — partial CSV writes possible if the process is killed; mitigated by writing to a `.tmp` file and renaming.

### Neutral / Tradeoffs

- If BACKLOG.001 (Streamlit) is promoted, the dashboard can read CSVs directly via pandas — SQLite still optional.

## Alternatives Considered

| Option | Pros | Cons | Reason not chosen |
|---|---|---|---|
| SQLite-first | SQL queries, one file. | Reviewer needs sqlite3 to inspect; harder diff. | Optimizes wrong axis for course assignment. |
| Parquet | Smaller, typed. | Binary, not diffable, requires `pyarrow`. | Diffability + reviewer ease outweigh size. |
| Both from day 1 | Best of both. | Two write paths to maintain. | Violates "no premature abstractions". |

## Implementation Notes

- Write CSVs via `df.to_csv(path, index=False, encoding="utf-8")`.
- Use the atomic `.tmp` + `os.replace` pattern to avoid half-written files.
- Schema version pinned by a `DATA_VERSION` constant in `src/config.py`; documented in `docs/data.md` migration rules.

## Rollback Plan

- Adding SQLite later is purely additive — no rollback needed.
- Removing SQLite later (if added) means deleting `data/processed/github_repos.db` and the build script.