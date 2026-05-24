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

- MVP first: rule-based classification, CSV-first storage, matplotlib charts, no dashboard until §11 charts are done.
- Retrieval-first docs: keep this file and `tasks/active.md` short; detailed plans live in `docs/tasks/*.md`, narrative in session logs.
- Treat the proposal as the durable scope source; do not duplicate its tables here.

## Current Focus

- Active priority: Bootstrap the project skeleton so the next session can start collecting data.
- Current phase: Phase 0 — context engineering setup (this session); next is Phase 1 (data collection from proposal §15 Step 1–5).
- Current owner / handoff state: solo (`aionyx`).

## Important Constraints

- GitHub API rate limit: 5000 req/h with token, 60 without. Must use Personal Access Token; never commit it.
- Python 3.14 required (`pyproject.toml`); no runtime deps added yet.
- **Confirmed scope (2026-05-24):** stars > 10; target 1000 repos (10 pages × 100 = single-query API cap); Streamlit dashboard is stretch-only (BACKLOG.001); AI/ML treated as one of nine equal categories, no special weighting.
- Do not analyze private repos, do not crawl all of GitHub, no ML model.

## Next Step

- TASK.007: manually validate the vibe-coding scoring (20 from each tier), compute precision/recall, cite in report. Highest-leverage rigor step before final submission.
- Optional follow-ups: re-collect in two weeks for delta analysis; multi-category classification to shrink Other bucket.

## Last Validation Snapshot

- Last docs refresh: 2026-05-24 (`npm run docs:refresh` passes; only non-fatal placeholder warnings remain in unused UI/template files).
- Last test command: none (no Python source yet).
- Known failing checks: none.