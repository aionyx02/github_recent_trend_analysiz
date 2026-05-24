---
type: project_overview
status: active
priority: p1
updated: 2026-05-24
context_policy: always_retrievable
owner: project
---

# Project Overview

## Product

**GitHub Recent Trend Analyzer** is a coursework data-analysis pipeline that collects new GitHub repositories created in the last 30 days, classifies them by topic / language / description, and produces a visual + written report on short-term open-source trends.

## Goals

- Build a reproducible dataset (300–500 repos) of recently created, non-fork repos with `stars > 10`.
- Answer RQ1–RQ6 in the proposal: dominant languages, hottest topics, breakout repos, Stars↔Forks correlation, per-category heat differences, and overall direction (AI/ML vs Web vs Tooling …).
- Ship at least 6 required charts plus a Markdown/PDF report explaining limits and conclusions.

## Non-Goals

- No machine-learning models for classification — rules only (MVP).
- No full-GitHub crawl, no private repos, no long-term historical comparison.
- No production dashboard SLA — Streamlit is optional and best-effort.
- No PR / Issue deep analysis in MVP (rate-limit budget reserved for languages + topics).

## Stack

- Language / runtime: Python 3.14 (`pyproject.toml` already pinned).
- HTTP client: `requests` or `httpx` (decide via ADR when first needed).
- Data: `pandas` for processing; CSV as primary persistence; SQLite as optional add-on.
- Visualization: `matplotlib` (required) + `plotly` (interactive, optional).
- Notebook: Jupyter for exploratory analysis.
- Dashboard (optional): Streamlit.
- Docs tooling: Node.js scripts under `scripts/` (only for `npm run docs:*` guards).

## Platform Targets

- Local Windows 11 development (current environment).
- Should run on macOS / Linux without code change (use pathlib, env vars, no Windows-only deps).

## Engineering Priorities

1. Safety and correctness (no leaked tokens; no rate-limit abuse).
2. Reproducibility and rollback (raw JSON backed up before any cleaning).
3. Explainability of results (rules and limitations stated in report).
4. Performance and developer speed.

## Current Strategy

- Retrieval-first docs workflow; startup context stays small.
- Use ADRs for: HTTP-client choice, storage layer (CSV vs SQLite vs both), classification rules schema, and any move away from rule-based classification.
- Treat the proposal (`github_recent_trend_analysis_project_proposal.md`) as the durable scope source — do not duplicate its content here; link to it.

## Scope Boundary (from proposal §20 MVP)

- Time window: last 30 days, recomputed at run time.
- Filters: `stars > 10`, `fork:false`, public only.
- Volume cap: 300–500 repos (5 pages × 100).
- Required outputs: dataset CSV, cleaned CSV, ≥6 charts, written report.
- Optional: SQLite, Streamlit, topic co-occurrence network, releases / issues data.