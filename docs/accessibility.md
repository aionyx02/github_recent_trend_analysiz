---
type: accessibility_policy
status: active
priority: p1
updated: 2026-05-24
context_policy: retrieve_when_planning
owner: project
---

# Accessibility Policy

## Baseline

- All interactive elements must be keyboard reachable.
- Focus state must be visible.
- Text and background contrast must be readable.
- Forms must expose labels and validation messages.
- Modals, menus, and dialogs must handle focus correctly.

## Keyboard Rules

| UI Pattern | Required Behavior |
|---|---|
| Button | Enter / Space activates |
| Link | Enter navigates |
| Modal | Focus trapped while open; Escape closes if safe |
| Menu | Arrow key behavior if using menu semantics |
| Form | Submit works from keyboard |

## ARIA Rules

- Prefer native HTML before ARIA.
- Do not add ARIA roles that conflict with native semantics.
- Use `aria-describedby` for helper or error text.
- Use `aria-expanded` for expandable controls.

## Testing Checklist

- [ ] Tab through the page.
- [ ] Submit forms with keyboard only.
- [ ] Check visible focus.
- [ ] Check labels and error messages.
- [ ] Check responsive layout.
