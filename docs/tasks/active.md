---
type: task_index
status: active
priority: p0
updated: 2026-05-24
context_policy: always_retrievable
owner: project
---

# Active Tasks

## Active Queue

### TASK.006 - Write Final Report (proposal §19 structure)

- Status: todo
- Priority: P1
- Owner: project
- Started: 2026-05-24
- Related docs:
  - `outputs/summary_stats.md`
  - `outputs/vibe_coding_analysis.md`
  - `outputs/figures/*.png`
  - `github_recent_trend_analysis_project_proposal.md` §19
- Acceptance criteria:
  - [ ] `outputs/report.md` follows §19 structure (摘要 → 動機 → RQs → method → results → discussion → limits → conclusion).
  - [ ] Each RQ1–RQ6 has a paragraph + at least one figure or table reference.
  - [ ] Vibe-coding analysis cited as supplemental finding.
  - [ ] Limitations section calls out: watchers=stars API quirk, 54% zero-topics, single-category MVP, rule-based classifier subjectivity.

## Strategy

Keep `active.md` compact. Put task-level details in dedicated `docs/tasks/*.md`, detailed implementation notes in `docs/memory/sessions/YYYY-MM-DD.md`, and future ideas in `docs/tasks/backlog.md`.

## Next Phase Candidates

- Phase 2 — enrich repos with `languages` + `topics` (proposal §15 Step 4).
- Phase 3 — rule-based classification + descriptive statistics (proposal §11).
- Phase 4 — required visualizations + report (proposal §12.1, §19).
- Stretch — Streamlit dashboard, SQLite layer, topic co-occurrence graph.