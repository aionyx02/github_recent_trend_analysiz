---
type: task_index
status: backlog
priority: p2
updated: 2026-05-24
context_policy: on_demand
owner: project
---

# Backlog

Future ideas, not scheduled. Promote to `active.md` when chosen.

## Stretch / Optional (from proposal §20.3)

 [ ]- **BACKLOG.001** — Streamlit dashboard (`dashboard/app.py`) with language ranking, topic ranking, category filter, top-repos table, scatter plot.
 [ ]- **BACKLOG.002** — SQLite persistence layer alongside CSV.
 [ ]- **BACKLOG.003** — Topic co-occurrence network graph (NetworkX + matplotlib or plotly).
 [ ]- **BACKLOG.004** — Multi-category classification (instead of single-category MVP).
 [ ]- **BACKLOG.005** — Releases API integration (`/repos/{owner}/{repo}/releases`).
 [ ]- **BACKLOG.006** — Issues API integration with PR filtering (`pull_request` key).
 [ ]- **BACKLOG.007** — GitHub Actions workflow that runs the collector weekly and commits the dataset.
 [ ]- **BACKLOG.008** — README usage guide with one-shot quickstart.
 [ ]- **BACKLOG.009** — License distribution pie/bar chart.
 [ ]- **BACKLOG.010** — Heatmap of language × category.

## Analysis Enhancements

- **BACKLOG.011** — Spearman correlation in addition to Pearson for Stars↔Forks (proposal §11.6).
- **BACKLOG.012** — Log-scale variants of Stars distribution histogram (proposal §9.4).
- **BACKLOG.013** — Median-centered category comparison (avoid mean skew from outliers).