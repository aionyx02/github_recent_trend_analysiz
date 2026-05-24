---
type: dependency_policy
status: active
priority: p1
updated: 2026-05-24
context_policy: retrieve_when_planning
owner: project
---

# Dependencies

## Dependency Rules

- Prefer Python standard library first; reach for a dep only when stdlib is awkward (e.g., GitHub API + pagination).
- Any new runtime dependency requires a one-line justification in this file's table.
- Large dependencies (web framework, ORM, dashboard, ML lib) require an ADR before adoption.
- Pin major versions in `pyproject.toml`; let minor/patch float.
- Token-handling libraries are security-sensitive — require explicit review.

## Current Dependencies (planned)

`pyproject.toml` is currently empty. The MVP plan adds:

| Dependency | Purpose | Scope | Replaceable? | Notes |
|---|---|---|---|---|
| `requests` *or* `httpx` | GitHub REST API client. | runtime | yes (either) | Choice gated by **ADR-0001**. |
| `pandas` | DataFrame + CSV I/O. | runtime | no | Core analysis lib; cannot be replaced without rewriting all of `clean_data` / `classify` / `visualize`. |
| `matplotlib` | Required static charts (proposal §12.1). | runtime | partially | `plotly` covers interactive but not all required outputs. |
| `python-dotenv` | Load `.env` so `GITHUB_TOKEN` doesn't need shell export. | runtime (dev convenience) | yes | Optional; can stick to `os.getenv` only. |
| `pytest` | Unit tests for `clean_data` / `classify`. | dev | yes | Standard. |
| `ruff` | Lint + format (already configured under `.idea/ruff.xml`). | dev | yes | |
| `jupyter` | Exploratory notebook (`notebooks/analysis.ipynb`). | dev | yes | Optional if all analysis ends up in `src/`. |

## Optional / Stretch (only if matching BACKLOG promoted)

| Dependency | Triggers | Notes |
|---|---|---|
| `plotly` | BACKLOG.001 dashboard, BACKLOG.010 heatmap. | Interactive charts. |
| `streamlit` | BACKLOG.001. | Dashboard. |
| `networkx` | BACKLOG.003. | Topic co-occurrence graph. |
| `sqlalchemy` *or* stdlib `sqlite3` | BACKLOG.002. | Prefer `sqlite3` to avoid a heavy dep. |

## Rejected Dependencies

| Dependency | Reason rejected | Date |
|---|---|---|
| `scikit-learn` | MVP uses rule-based classification only (proposal §10). Adding ML would require new ADR superseding ADR-0003. | 2026-05-24 |
| `scrapy` / `playwright` | Not needed — the GitHub REST API is the only data source. | 2026-05-24 |

## Dependency Change Checklist

- [ ] Existing dependency cannot solve the need.
- [ ] License and maintenance status are acceptable (check PyPI).
- [ ] Security implications are understood (does it handle the token?).
- [ ] Install cost is acceptable (no 100 MB transitive dep tree for a one-line helper).
- [ ] Tests or a smoke script cover the new dependency path.
- [ ] Listed in `pyproject.toml` under the correct group (`dependencies` vs `optional-dependencies`).