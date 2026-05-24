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

### TASK.007 - Validate Vibe-Coding Scoring (precision/recall)

- Status: todo
- Priority: P2
- Owner: project
- Started: 2026-05-24
- Related docs:
  - `outputs/vibe_coding_analysis.md`
  - `data/processed/vibe_scores.csv`
- Acceptance criteria:
  - [ ] Manual sample 20 from each tier (garbage / suspicious / legitimate).
  - [ ] Label each as TP/FP based on subjective "is this actually low effort?" assessment.
  - [ ] Compute precision, recall, F1 per tier; write to `outputs/vibe_validation.md`.
  - [ ] Cite the result in the report's §10 limitations.
- Notes:
  - Discussed as the highest-leverage next step in the post-TASK.006 review.

## Strategy

Keep `active.md` compact. Put task-level details in dedicated `docs/tasks/*.md`, detailed implementation notes in `docs/memory/sessions/YYYY-MM-DD.md`, and future ideas in `docs/tasks/backlog.md`.

## Next Phase Candidates

- Phase 2 — enrich repos with `languages` + `topics` (proposal §15 Step 4).
- Phase 3 — rule-based classification + descriptive statistics (proposal §11).
- Phase 4 — required visualizations + report (proposal §12.1, §19).
- Stretch — Streamlit dashboard, SQLite layer, topic co-occurrence graph.