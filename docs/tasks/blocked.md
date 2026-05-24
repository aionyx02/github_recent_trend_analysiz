---
type: task_blockers
status: active
priority: p1
updated: 2026-05-24
context_policy: retrieve_when_planning
owner: project
---

# Blocked / Approval-Gated Work

## Blocked

- _none_ — TASK.002 (src scaffold) complete on 2026-05-24, TASK.003 unblocked.

## Requires Explicit Approval

- Adopting an HTTP client (`requests` vs `httpx`) — needs ADR-0001 acceptance.
- Choosing storage layer (CSV-only vs CSV+SQLite) — needs ADR-0002 acceptance.
- Adding any classification rule that uses ML / external model — would require a new ADR superseding ADR-0003.
- Committing the GitHub token to env files tracked by git — never; treat as approval-gated forever.
- Adding `releases` or `issues` collection in MVP — out of scope per proposal §20.2; approval needed to lift.