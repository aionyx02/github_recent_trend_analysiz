---
type: testing_policy
status: active
priority: p1
updated: 2026-05-24
context_policy: retrieve_when_debugging
owner: project
---

# Testing Strategy

## Required Checks

```bash
# Lint
ruff check .

# Unit tests (once src/ exists)
python -m pytest -q

# Optional: docs guards (needs Node.js)
npm run docs:refresh
```

## Test Layers

| Layer | Purpose | Command |
|---|---|---|
| Static checks | Lint, format. | `ruff check .` |
| Unit tests | Pure functions in `src/clean_data.py` and `src/classify.py`. | `python -m pytest tests/unit -q` |
| Integration tests | One-page Search API call using a recorded fixture (not live). | `python -m pytest tests/integration -q` |
| Smoke / E2E | Full pipeline against ≤5 real repos with a real token. | `python -m src.collect_repos --limit 5` |

## What to Test

- `clean_data`: missing-value rules (proposal §9.2), datetime parsing, derived column math.
- `classify`: every keyword bucket has at least one positive test + one Other fallback.
- `github_api`: rate-limit response handling, retry/backoff, header redaction in logs.

## What NOT to Test (yet)

- Plot rendering correctness — manual review is enough for MVP.
- Streamlit dashboard — out of MVP scope.
- Live API responses — use saved JSON fixtures from `data/raw/` to keep tests offline and deterministic.

## Regression Policy

When fixing a bug:

1. Reproduce against a saved fixture (or document why a live repro is needed).
2. Add a `pytest` case covering the bug or, if it's a structural edge case, a row in `docs/testing-edge-cases.md`.
3. Record root cause in `docs/memory/sessions/YYYY-MM-DD.md`.
4. Update reference docs only if behavior or active plan changed.

## Token Safety in Tests

- Never commit `.env`, `GITHUB_TOKEN`, or any header capture.
- Unit / integration tests must not require a real token. Smoke tests may, but must redact `Authorization` from logs.

## UI / HTML Validation

Not applicable in MVP. Revisit if BACKLOG.001 (Streamlit dashboard) is promoted.