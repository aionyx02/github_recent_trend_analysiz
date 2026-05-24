---
type: release_policy
status: active
priority: p2
updated: 2026-05-24
context_policy: retrieve_when_planning
owner: project
---

# Release And Deployment

## Purpose

Record release, deployment, and rollback expectations. Keep environment-specific secrets out of this file.

## Release Checklist

- [ ] Documentation is current.
- [ ] Tests or validation commands pass.
- [ ] Configuration changes are documented.
- [ ] Migration and rollback notes are documented when relevant.
- [ ] User-visible changes are summarized.

## Validation Commands

```bash
npm run docs:refresh
npm run lint --if-present
npm run test --if-present
npm run build --if-present
```

## Rollback Notes

- `<ROLLBACK_RULE>`
