---
type: coding_conventions
status: active
priority: p1
updated: 2026-05-24
context_policy: retrieve_when_planning
owner: project
---

# Coding Conventions

## Purpose

Durable Python style for this project. Ruff (`.idea/ruff.xml`) is the authoritative formatter.

## Naming

| Item | Convention |
|---|---|
| Files / modules | `snake_case.py` |
| Functions | `snake_case` |
| Classes | `PascalCase` |
| Constants | `UPPER_SNAKE_CASE` |
| Tests | `test_<module>_<behavior>` under `tests/unit/` or `tests/integration/` |

## Code Style

- Type hints on public functions (`def fetch_repos(page: int) -> list[dict]: ...`).
- One module per pipeline stage; do not collapse fetch + clean into a single script.
- Prefer pure functions in `clean_data` and `classify` — easier to unit-test.
- Side effects (HTTP, file I/O) live at module boundaries, not inside transform helpers.
- Use `pathlib.Path` for all file paths; never hard-code `\\` or `/`.
- Use `os.getenv("GITHUB_TOKEN")` once, in `src/config.py`; pass downstream as a parameter.

## Error Handling

- Network errors → catch in `src/github_api.py`, retry with backoff, surface a typed exception to callers.
- Rate-limit (HTTP 403 + `X-RateLimit-Remaining: 0`) → log, save partial progress, exit with a clear message; do **not** silently sleep for an hour.
- Missing keys in JSON → use `.get(key, default)` and let `clean_data` apply the §9.2 rules; do not crash on optional fields.
- Never swallow exceptions silently. Never let an exception expose the token in its message.

## Logging

- Use `logging` (stdlib), not `print`, in `src/`.
- Default level `INFO`; `DEBUG` for HTTP request paths (without headers).
- **Never** log `Authorization` headers or the token value.
- Long command output and HTTP body dumps go to `docs/memory/sessions/YYYY-MM-DD.md`, not into `src/` modules.

## Imports

- Stdlib → third-party → local, separated by blank lines.
- No wildcard imports.
- Avoid circular imports by keeping `config.py` dependency-free.
