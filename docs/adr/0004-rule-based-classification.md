---
type: adr
status: proposed
priority: p1
updated: 2026-05-24
context_policy: on_demand
owner: project
---

# ADR-0004: Rule-Based Classification, Single-Category, Priority-Ordered

## Status

Proposed

## Context

Proposal §10 requires classifying each repo into one of: `AI/ML, Web, Data, DevOps, Security, Game, CLI/Tooling, Mobile, Other`. Three classifier families were considered:

- Rule-based keyword matching over `description + topics + primary_language`.
- Supervised ML (would need labeled training data we don't have).
- LLM-based zero-shot classification (token cost, reproducibility risk, opaque to reviewer).

The classifier must be explainable in the written report and reproducible from CSV alone.

## Decision

Use a **rule-based, single-category classifier** with the priority order from proposal §10.3:

```
AI/ML > Security > DevOps > Data > Web > Mobile > Game > CLI/Tooling > Other
```

Match against: `description` (lowercased), `topics` (canonical), `primary_language` (lowercased). First matching bucket wins.

Multi-category support is **BACKLOG.004**, not MVP.

## Consequences

### Positive

- Fully explainable: each classification can be traced to a specific keyword hit.
- Zero training cost; no labeled data needed.
- Deterministic and reproducible — same CSV input always yields same `category`.
- Reviewer can audit and edit the rule table directly.

### Negative

- Ambiguous repos (e.g., "ML platform with a React dashboard") are forced into one bucket.
- Keyword coverage is the bottleneck — gaps land in `Other`, inflating that bucket.
- Subjectivity bias must be acknowledged in the report (proposal §17 risk row).

### Neutral / Tradeoffs

- Priority order is itself a value judgment (AI/ML ranked highest). The report must state this.

## Alternatives Considered

| Option | Pros | Cons | Reason not chosen |
|---|---|---|---|
| Multi-category (BACKLOG.004) | More accurate for cross-domain repos. | Harder to chart and aggregate. | MVP requires single category for clean bar charts. |
| TF-IDF + logistic regression | Higher accuracy with labels. | No labeled data; out of MVP scope. | Cost > benefit. |
| LLM zero-shot | Handles fuzzy descriptions. | Token cost, non-deterministic, hard to defend. | Violates reproducibility goal. |

## Implementation Notes

- Rule table lives as a Python dict in `src/classify.py` for MVP. Promote to YAML/JSON only if it grows past ~50 keywords per bucket.
- Match order is fixed in code, but each bucket's keyword list can be edited freely without touching logic.
- Unit tests must cover at least one positive case per bucket and one `Other` fallback.

## Rollback Plan

- The `category` column is derived, not source. Removing or changing the classifier only requires re-running `src/classify.py` against `repos.csv`.