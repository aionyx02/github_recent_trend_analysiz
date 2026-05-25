---
type: working_memory
status: active
priority: p0
updated: 2026-05-25
context_policy: always_retrievable
owner: project
---

# Current Project Memory

## Current Strategy

- MVP complete and live. Remaining work is polish (Path A), rigor (Path B), and trend extension (Path D); visual wow items (Path C) live in backlog.
- Retrieval-first docs: keep this file and `tasks/active.md` short; detailed plans live in `docs/tasks/*.md`, narrative in session logs.
- Treat the proposal as the durable scope source; do not duplicate its tables here.

## Current Focus

- Active priority: external review fixes (用詞中性化、限制章節、Other 分析、Data Dictionary) — done 2026-05-25.
- Next priority: TASK.008 (hero shot) + manual labelling of validation samples (classification 50 + metadata 58).
- Current phase: post-MVP polish + research-grade framing. Live demo at <https://apprecenttrendanalysiz-kn98grjnkut85j6dvxzfhb.streamlit.app>.
- Current owner / handoff state: solo (`aionyx`).
- Awaiting user: hero screenshot from the live URL + `GH_DATA_TOKEN` repo secret for daily-refresh + manual labels for two validation CSVs.

## Important Constraints

- GitHub API rate limit: 5000 req/h with token, 60 without. Token lives in `.env` locally and as `GH_DATA_TOKEN` repo secret for the daily-refresh workflow.
- Python **3.11+** required (`pyproject.toml`; relaxed from `>=3.14` after grep confirmed no 3.14-specific syntax). Streamlit Cloud Poetry installer reads streamlit + plotly + tabulate from main deps.
- **Confirmed scope (2026-05-24):** stars > 10; 1000 repos (10 pages × 100 = single-query API cap); AI/ML treated as one of nine equal categories.
- Do not analyze private repos, do not crawl all of GitHub, no ML model in classifier.

## Next Step

- TASK.008 (P1): hero screenshot + TL;DR (TL;DR done 2026-05-24; hero shot still blocked on user-supplied screenshot).
- TASK.009 (P1, blocked 7 days): delta analysis once daily-refresh has accumulated 7 snapshots.
- TASK.007 (P2): manual metadata-completeness scoring validation when time permits (sample at `data/processed/vibe_validation_sample.csv`).
- TASK.010 (P2, new): manual rule-based classification validation (sample at `data/processed/classification_validation_sample.csv`, 50 rows).

## Last Validation Snapshot

- Last test command: `python -m pytest -q` → **38/38** passing (2026-05-25; +16 new cache_manifest tests).
- All touched Python files `ast.parse()` clean; workflow YAML parses + cache step includes manifest path.
- Live deploy: ✓ Streamlit Cloud built at commit `1f811bb`; new commits pending.
- Known failing checks: none.
- Awaiting first run: `daily-data-refresh` workflow (needs `GH_DATA_TOKEN` secret).
- Daily-refresh now stale-aware: per-repo data is re-fetched only when `pushed_at > cached fetched_at`; auto-prunes cache after 60 days absent from search window.
