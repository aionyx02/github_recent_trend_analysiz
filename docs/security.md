---
type: security_policy
status: active
priority: p1
updated: 2026-05-24
context_policy: retrieve_only
owner: project
---

# Security And Permission Boundary

## Security Principles

- Least privilege: the `GITHUB_TOKEN` should be a fine-scoped Personal Access Token with only `public_repo` (read-only) scope. Classic tokens with `repo` write scope are forbidden.
- Token lives only in `.env` or shell env — **never** in committed files.
- All HTTP requests pass through `src/github_api.py` so logging, redaction, and rate-limit handling stay centralized.
- Destructive actions (file deletion, repo writes) are out of scope and must be approval-gated if proposed later.

## Data Classification

| Data | Sensitivity | Handling |
|---|---|---|
| GitHub Personal Access Token | **Critical** | env var only; redacted from logs; never persisted to disk. |
| Public repo metadata (`repos.csv`, raw JSON) | Low | Safe to commit if dataset size is acceptable; otherwise gitignore `data/`. |
| GitHub API response headers (`X-RateLimit-*`) | Low | Safe to log. |
| `Authorization` request header | Critical | Must never appear in logs, error messages, or saved fixtures. |

## Approval-Gated Changes

- Adding any code path that writes to GitHub (issues, comments, repo edits).
- Switching token scope from read-only to anything broader.
- Logging request/response bodies that may include the token.
- Adding telemetry that sends data outside the local machine.
- Committing collected datasets that contain user emails (the Search API may return owner email if public — confirm before committing).

## .gitignore Requirements

The repo `.gitignore` should at minimum exclude:

```
.env
.env.*
__pycache__/
.venv/
data/raw/
*.log
.ipynb_checkpoints/
```

`data/processed/` and `outputs/` may be committed if the assignment requires the dataset to be reviewable; decide in TASK.001.