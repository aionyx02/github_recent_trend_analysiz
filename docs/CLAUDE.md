---
type: agent_policy
status: active
priority: p1
updated: 2026-05-24
context_policy: on_demand
owner: project
---

# AI Agent Governance And ADR Policy

Applies to project governance, ADR workflow, and documentation update behavior.

## 1. Core Principle

Safety > correctness > rollbackability > testability > performance > speed.

## 2. Retrieval-First Documentation Rule

- Do not inject all docs into prompt at once.
- Start from `docs/index.md`, then read `docs/memory/current.md` and `docs/tasks/active.md`.
- Retrieve additional files only by task intent.
- Use the smallest relevant heading section.
- Do not treat `docs/tasks/completed.md`, `docs/memory/sessions/*`, or `docs/memory/archive/*` as current instruction.


## 2.1 Context Policy Meaning

| Policy | Meaning |
|---|---|
| `always_retrievable` | Startup or near-startup state; must stay very small |
| `retrieve_when_planning` | Read before planning relevant implementation |
| `retrieve_when_debugging` | Read when fixing bugs or test failures |
| `retrieve_only` | Reference material; read only when directly relevant |
| `on_demand` | User, task, or index explicitly points to it |
| `historical` | Never treat as current instruction |

## 3. ADR Authority Rule

- AI can create ADRs with status `proposed` only.
- AI cannot mark ADRs as `accepted` unless the developer explicitly instructs it.
- Implementation that changes architecture, security, public data contracts, or irreversible behavior should wait for developer acceptance.

## 4. Documentation Conflict Resolution

When docs conflict, use this order:

1. Explicit developer instruction in the current conversation
2. `docs/tasks/active.md`
3. `docs/memory/current.md`
4. Accepted ADRs in `docs/adr/*`
5. `docs/security.md`
6. `docs/architecture.md`
7. Session or archive logs

## 5. Mandatory Documentation Sync

After meaningful changes, update the smallest matching document:

- Current strategy, focus, or durable constraint -> `docs/memory/current.md`
- Open task queue or phase status -> `docs/tasks/active.md`
- Detailed implementation notes, debugging narrative, command output, or root cause -> `docs/memory/sessions/YYYY-MM-DD.md`
- Completed task summary -> `docs/memory/sessions/YYYY-MM-DD.md` using `## COMPLETED: TASK_ID - summary`
- Future work -> `docs/tasks/backlog.md`
- Blocked or approval-gated work -> `docs/tasks/blocked.md`
- Architecture/security/testing/UI/data/dependency behavior -> the matching reference doc
- Decision boundary -> `docs/adr/*` plus `docs/decisions.md`

Before commit or handoff, run:

```bash
npm run docs:refresh
```

## 6. Documentation Bloat Prevention

Before writing to any `.md` file, answer three questions:

1. Is the target file marked `context_policy: always_retrievable`?
2. Is the content current state or historical narrative?
3. Does the content already exist elsewhere?

Strict routing:

- Strategy, focus, or durable constraint -> `docs/memory/current.md`
- Open task and task status -> `docs/tasks/active.md`
- Debugging narrative or root-cause analysis -> `docs/memory/sessions/YYYY-MM-DD.md`
- Completed task summary -> session `## COMPLETED:` marker; regenerated into `docs/tasks/completed.md`
- Edge case as reusable structured row -> `docs/testing-edge-cases.md`
- Edge case as story or incident -> session log, with a short reference if needed
- Architectural decision -> `docs/adr/NNNN-*.md`

Forbidden in `current.md` and `active.md`:

- `Recent Execution Notes`
- `Last Confirmed Progress`
- `Session History`
- `Detailed Notes`
- `Bugfix Round`
- Long dated narratives
- Full command-output dumps

Size discipline:

- `docs/memory/current.md` should stay under 5 KB.
- `docs/tasks/active.md` should stay under 5 KB.
- `docs/state/tasks-summary.json` should stay under 6 KB.
- `docs/state/decision-summary.json` should stay under 3 KB.
- If an edit would exceed a limit, move narrative to a session file first.

## 7. ADR Trigger Checklist

Create an ADR before implementation when any apply:

- New or removed core dependency
- Async model, IPC, queue, worker, actor, or concurrency boundary changes
- Security boundary, path permission, network permission, or credential handling changes
- Data format, schema, migration, or public contract changes
- Major algorithmic, indexing, ranking, caching, or storage model changes
- Destructive action behavior or approval flow changes

## 8. Minimal Agent Workflow

1. Classify user intent.
2. Retrieve minimal relevant docs.
3. Check ADR / approval / blocked constraints.
4. Implement the smallest safe change.
5. Run relevant tests/checks.
6. Update docs via routing rules.
7. Run `npm run docs:refresh`.
8. Report changed file paths, validation results, and remaining risk.
