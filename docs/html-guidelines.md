---
type: html_guidelines
status: active
priority: p1
updated: 2026-05-24
context_policy: retrieve_when_planning
owner: project
---

# HTML Guidelines

## Core Rules

- Prefer semantic HTML elements: `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`.
- Use `button` for actions and `a` for navigation.
- Every form control should have a visible or programmatically associated label.
- Avoid clickable `div` unless there is a strong reason and keyboard behavior is implemented.
- Keep DOM structure simple before adding JavaScript behavior.

## Forms

- Use `label` with `for` and matching `id` where appropriate.
- Provide validation messages close to the field.
- Use appropriate input types: `email`, `number`, `date`, `search`, `password`.
- Do not rely on placeholder text as the only label.

## Tables

- Use `table` only for tabular data.
- Use `thead`, `tbody`, `th`, and `scope` when appropriate.

## Images

- Meaningful images need descriptive `alt` text.
- Decorative images should use empty `alt=""`.
- Avoid embedding text in images unless unavoidable.

## Forbidden Patterns

- No interactive `div` without keyboard support.
- No unlabeled inputs.
- No layout-only tables.
- No hardcoded secrets or tokens in HTML.
