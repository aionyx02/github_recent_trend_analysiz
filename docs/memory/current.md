---
type: working_memory
status: active
priority: p0
updated: 2026-05-24
context_policy: always_retrievable
owner: project
---

# Current Project Memory

## Current Strategy

- MVP complete and live. Remaining work is polish (Path A), rigor (Path B), and trend extension (Path D); visual wow items (Path C) live in backlog.
- Retrieval-first docs: keep this file and `tasks/active.md` short; detailed plans live in `docs/tasks/*.md`, narrative in session logs.
- Treat the proposal as the durable scope source; do not duplicate its tables here.

## Current Focus

- Active priority: TASK.008 (reviewer-facing polish) — hero shot + TL;DR + presentation script.
- Current phase: post-MVP polish. Live demo at <https://apprecenttrendanalysiz-kn98grjnkut85j6dvxzfhb.streamlit.app>.
- Current owner / handoff state: solo (`aionyx`).
- Awaiting user: hero screenshot from the live URL + `GH_DATA_TOKEN` repo secret for daily-refresh.

## Important Constraints

- GitHub API rate limit: 5000 req/h with token, 60 without. Token lives in `.env` locally and as `GH_DATA_TOKEN` repo secret for the daily-refresh workflow.
- Python 3.14 required (`pyproject.toml`). streamlit + plotly now in main dependencies (moved out of `[dashboard]` extras) so Streamlit Cloud's Poetry installer picks them up.
- **Confirmed scope (2026-05-24):** stars > 10; 1000 repos (10 pages × 100 = single-query API cap); AI/ML treated as one of nine equal categories.
- Do not analyze private repos, do not crawl all of GitHub, no ML model in classifier.

## Next Step

- TASK.008 (P1): hero screenshot + TL;DR + presentation script. Blocked partially on user-supplied screenshot.
- TASK.009 (P1, blocked 7 days): delta analysis once daily-refresh has accumulated 7 snapshots.
- TASK.007 (P2): manual vibe-coding scoring validation when time permits.

## Last Validation Snapshot

- Last docs refresh: 2026-05-24 (passes; only non-fatal placeholder warnings in unused UI template files).
- Last test command: `python -m pytest -q` → 22/22 passing; `ruff check .` clean.
- Live deploy: ✓ Streamlit Cloud build successful at commit `1f811bb`.
- Known failing checks: none.
- Awaiting first run: `daily-data-refresh` workflow (needs `GH_DATA_TOKEN` secret).
