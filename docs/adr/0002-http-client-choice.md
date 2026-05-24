---
type: adr
status: proposed
priority: p1
updated: 2026-05-24
context_policy: on_demand
owner: project
---

# ADR-0002: HTTP Client For GitHub REST API

## Status

Proposed

## Context

The pipeline must call the GitHub REST API ~1000 times per run (1 search × 5 pages + 500 languages + 500 topics — see proposal §8.3). We need consistent header injection (`Authorization`, `Accept`), rate-limit header parsing (`X-RateLimit-Remaining`, `Retry-After`), and retry-on-failure. Two viable stdlib-adjacent options:

- `requests` — mature, synchronous, ubiquitous, easy for a coursework reader to follow.
- `httpx` — modern, sync **and** async, near-identical API to `requests`.

Async parallelism could shorten the 1000-call run, but adds debugging complexity.

## Decision

Use **`requests`** for MVP. Keep the abstraction inside `src/github_api.py` so swapping to `httpx` later is a single-module change.

## Consequences

### Positive

- Lowest learning curve; the assignment audience (course reviewer) will recognize it.
- Synchronous control flow simplifies rate-limit logic.
- Smallest dep footprint (one wheel, no async runtime).

### Negative

- Single-threaded; ~1000 calls × ~0.5–2 s sleep = 8–30 minutes worst case.
- No native HTTP/2 (irrelevant for GitHub REST today).

### Neutral / Tradeoffs

- Sync vs async difference is invisible to downstream modules because everything routes through `github_api.py`.

## Alternatives Considered

| Option | Pros | Cons | Reason not chosen |
|---|---|---|---|
| `httpx` (sync) | Same API as `requests`, supports async upgrade. | One more dep to learn for reviewer. | Defer until async actually pays off. |
| `httpx` (async) | Could finish 1000 calls in ~1–2 min. | Needs `asyncio`, harder to debug rate-limit logic. | Premature for MVP. |
| `urllib` stdlib | Zero deps. | Verbose, no session reuse out of the box. | Cost > benefit. |

## Implementation Notes

- Pin `requests` in `pyproject.toml` once this ADR is accepted.
- All requests must use a single `requests.Session` to reuse the connection pool.
- Centralize sleep + retry in one function in `github_api.py`.

## Rollback Plan

- Replace `requests.Session` with `httpx.Client` inside `github_api.py`; downstream modules unchanged.