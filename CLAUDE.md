---
type: agent_bootstrap
status: active
priority: p0
updated: 2026-05-24
context_policy: always_retrievable
owner: project
---

# CLAUDE.md

> Auto-loaded at session start. Detailed governance, ADR, and documentation-routing rules are in `docs/CLAUDE.md`.

## Session Start

1. Read `docs/index.md` for documentation routing.
2. Read `docs/memory/current.md` for current strategy, constraints, and next step.
3. Read `docs/tasks/active.md` for the active queue.
4. Retrieve additional documents by intent. Do not recursively load all docs.

## Session Close

Before final response, handoff, or commit:

1. Update only the smallest matching state document.
2. Put detailed execution notes, debugging narrative, and command-output history in `docs/memory/sessions/YYYY-MM-DD.md`.
3. Keep `docs/memory/current.md` and `docs/tasks/active.md` as current-state indexes only.
4. Put completed-task detail in the session log using `## COMPLETED: TASK_ID - summary`.
5. Run `npm run docs:refresh` when Node scripts are available.

## Project Overview

- Product: **GitHub Recent Trend Analyzer**
- Primary goal: Collect, classify, and analyze trending GitHub repositories created in the last 30 days, producing visual reports and (optionally) an interactive dashboard.
- Main users: Coursework reviewer (Big Data course) and the author; the report should be readable by non-technical audiences.
- Supported platforms: CLI / Jupyter Notebook on local Windows + Python 3.14; optional Streamlit dashboard.
- Reference proposal: `github_recent_trend_analysis_project_proposal.md` (durable scope, RQs, MVP boundary).

## Git Workflow Rules

```text
main <- always releasable
dev  <- integration (create when collaborating)
feature/<name> <- work branches
```

- Do not merge without explicit developer confirmation.
- Create feature branches from `main` (solo project) — switch to `dev` if multiple collaborators join.
- Show diffs and pass relevant checks before merge.
- Never rewrite shared history without explicit approval.
- Never commit `.env`, `GITHUB_TOKEN`, or raw API dumps containing sensitive payloads.

## Build / Test Commands

This project is Python-first. Node is only used for docs guard scripts.

```bash
# Python (primary)
python -m pip install -e .
python -m pytest                # once tests exist
ruff check .                    # lint (ruff is already configured under .idea/ruff.xml)

# Docs guard (optional, requires Node.js)
npm run docs:refresh
```

## Documentation Entry Points

- `docs/index.md` - documentation router
- `docs/project.md` - stable project facts
- `docs/memory/current.md` - short working memory
- `docs/tasks/active.md` - active work only
- `docs/CLAUDE.md` - governance and ADR rules
- `github_recent_trend_analysis_project_proposal.md` - original proposal (read-only reference)