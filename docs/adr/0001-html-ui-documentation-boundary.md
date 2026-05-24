---
type: adr
status: proposed
priority: p1
updated: 2026-05-24
context_policy: on_demand
owner: project
---

# ADR-0001: HTML And UI Documentation Boundary

## Status

Proposed

## Context

The project needs durable HTML and UI decision records without increasing startup context size.

## Decision

HTML, UI, design system, and accessibility rules will be stored in dedicated on-demand documents:

- `docs/ui.md`
- `docs/html-guidelines.md`
- `docs/design-system.md`
- `docs/accessibility.md`

`CLAUDE.md`, `docs/memory/current.md`, and `docs/tasks/active.md` must not contain long UI specifications.

## Consequences

### Positive

- Keeps startup context small.
- Makes UI decisions discoverable.
- Reduces repeated prompt cost.
- Separates temporary work from durable design rules.

### Negative

- Agents must follow routing rules correctly.
- More documentation files need maintenance.

### Neutral / Tradeoffs

- UI work requires reading one or more extra files, but only when relevant.

## Alternatives Considered

| Option | Pros | Cons | Reason not chosen |
|---|---|---|---|
| Put all UI rules in `CLAUDE.md` | Simple startup | High token cost | Too expensive and noisy |
| Put all UI rules in `current.md` | Easy to find | Pollutes working memory | Violates bloat prevention |
| Dedicated UI docs | Lower token use | More files | Best balance |

## Implementation Notes

- Update `docs/index.md` intent routing.
- Add size guard for frequently edited UI reference files.
- Keep UI docs short and structured.

## Rollback Plan

- Remove UI routing rows.
- Archive the UI-specific docs.
