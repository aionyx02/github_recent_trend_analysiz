---
type: adr
status: proposed
priority: p1
updated: 2026-05-25
context_policy: on_demand
owner: project
---

# ADR-0004: Rule-Based Classification, Single-Category, Priority-Ordered

## Status

Proposed (revised 2026-05-25 — Finance/Trading added as 10th category; keyword gaps filled in AI/ML, Web, Mobile, Security; see Revision Log at bottom).

## Context

Proposal §10 requires classifying each repo into one of: `AI/ML, Web, Data, DevOps, Security, Game, CLI/Tooling, Mobile, Other`. Three classifier families were considered:

- Rule-based keyword matching over `description + topics + primary_language`.
- Supervised ML (would need labeled training data we don't have).
- LLM-based zero-shot classification (token cost, reproducibility risk, opaque to reviewer).

The classifier must be explainable in the written report and reproducible from CSV alone.

## Decision

Use a **rule-based, single-category classifier** with the priority order (revised 2026-05-25):

```
AI/ML > Security > Finance/Trading > DevOps > Data > Web > Mobile > Game > CLI/Tooling > Other
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

## Revision Log

### 2026-05-25 — Add Finance/Trading; fill keyword gaps

**Trigger**: `outputs/other_breakdown.md` revealed an unhandled cluster — `trading` (193 hits), `polymarket` (189), `arbitrage` (27), `pumpfun` (17), `hyperliquid` (15) — entirely in the Other bucket. Existing AI/ML keywords also missed the README's own top topics (`claude-code` 52, `mcp` 26, `codex` 25, `cursor`).

**Changes**:

1. **New category Finance/Trading** placed third in priority (between Security and DevOps). Keywords include `trading`, `polymarket`, `arbitrage`, `pumpfun`, `hyperliquid`, `trading-bot` family, `defi`, `dex`, `mev`, `hft`, `crypto`, `solana`, `wallet`, `fintech`, `finance`.
   - **Blockchain/Web3 signals (`crypto`/`solana`/`wallet`) are folded in here** rather than as a separate Blockchain category. Rationale: avoid two new categories in one pass; many polymarket bots also touch Solana/crypto wallets so the bucket overlaps. If validation shows a clean Web3 cluster distinct from Trading, a future ADR can split.
   - **Priority placement** (third) chosen so that AI-driven trading agents (containing `llm`/`agent` AND `trading`) stay in AI/ML — the AI component is what differentiates them. Pure rule-based polymarket arbitrage bots fall to Finance/Trading.

2. **Filled keyword gaps in existing categories**:
   - AI/ML: `claude-code`, `mcp`, `codex`, `cursor`, `langchain`, `langgraph`, `vector-database`, `vector-search`
   - Web: `shadcn`, `tailwindcss`, `astro`, `nuxt`, `remix`, `solidjs`, `vite`
   - Mobile: `swiftui`, `jetpack-compose`, `expo`, `compose-multiplatform`
   - Security: `oauth`, `oauth2`, `sso`, `siem`, `waf`, `zero-trust`

**Observed effect on classifier output (1000-repo snapshot, 2026-05-25)**:

| Category | Before | After | Δ |
|---|---:|---:|---:|
| AI/ML | 365 (36.5%) | 389 (38.9%) | +24 |
| Other | 420 (42.0%) | 375 (37.5%) | **−45** |
| Web | 74 (7.4%) | 50 (5.0%) | −24 |
| **Finance/Trading** | — | **45 (4.5%)** | new |
| (other categories) | (small drift) | | |

- Other bucket reduction modest (−4.5pp) — the `outputs/other_breakdown.md` "~211 candidates" estimate was inflated by multi-keyword counting (a single polymarket bot hits `trading` + `polymarket` + `arbitrage` simultaneously).
- Web bucket shrank by 24 — trading-themed React/dashboards moved to Finance/Trading. Consistent with the existing ADR-0004 trade-off about ambiguous repos being forced into one bucket.

**Trade-offs introduced**:

- A pure-Web "trading dashboard" repo will now classify as Finance/Trading (domain wins over tech stack). Reviewers should know the bucket is by **domain**, not technology, for those edge cases.
- `crypto` is a broad keyword — could capture non-financial cryptography repos. None observed in spot-check of 1000-repo snapshot, but flagged for future re-validation.

**New finding surfaced by the revision**:

- Finance/Trading category has **median fork:star = 9.9** (mean 7.67×), and top 5 polymarket repos show 30× forks-vs-stars. This pattern is the opposite of every other category and is suspicious of automated fork-farming / astroturfing. Worth a dedicated section in `outputs/report.md`.

**Validation status**: 41/41 unit tests pass including three new tests for Finance/Trading classification and AI/ML > Finance priority order. Manual labelling of `data/processed/classification_validation_sample.csv` (50 rows, 5 per category × 10 categories) still pending — TASK.010.