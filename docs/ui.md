---
type: ui_spec
status: active
priority: p1
updated: 2026-05-24
context_policy: retrieve_when_planning
owner: project
---

# UI Architecture

## UI Goals

- Keep user flows simple and predictable.
- Prefer semantic HTML before custom JavaScript behavior.
- Components should be reusable, testable, and minimally stateful.

## Page Structure

| Page / Area | Responsibility | Notes |
|---|---|---|
| `<PAGE_NAME>` | `<RESPONSIBILITY>` | `<NOTES>` |

## Component Boundary Rules

- A component should own one clear responsibility.
- Do not mix data fetching, validation, and rendering unless the framework requires it.
- Shared components go in `<COMPONENT_DIRECTORY>`.
- Page-specific components stay near the page.

## State Rules

| State Type | Preferred Location |
|---|---|
| Local UI state | Component |
| Form state | Form component or form library |
| Server/cache state | Data layer |
| Global app state | Only when multiple distant components require it |

## UI Decision Triggers

Create an ADR when changing layout system, component library, styling strategy, routing pattern, state management strategy, form validation strategy, or accessibility baseline.
