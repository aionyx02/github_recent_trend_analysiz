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

## Done (kept for traceability)

- ✅ **BACKLOG.001** — Streamlit dashboard. Done in TASK.005-006 era; live at <https://apprecenttrendanalysiz-kn98grjnkut85j6dvxzfhb.streamlit.app>.
- ✅ **BACKLOG.007** — GitHub Actions periodic refresh. Done in commit `3ef7477`; runs daily (more frequent than originally planned weekly).
- ✅ **BACKLOG.008** — README quickstart. Done as part of the professional README.
- ✅ **BACKLOG.011** — Spearman correlation alongside Pearson. Already in `src/build_charts.py` summary.
- ✅ **BACKLOG.012** — Log-scale Stars distribution. Already in `src/visualize.py::stars_distribution`.
- ✅ **BACKLOG.014** — Sankey (language → category) added as section 5b in the dashboard.
- ✅ **BACKLOG.016** — Vibe-score threshold slider added in the dashboard; tiers recompute live with a delta-vs-default indicator.
- ✅ **BACKLOG.017** — Per-category stacked bar appended to section 7 (daily timeline) showing the daily mix by category.
- ✅ **BACKLOG.018** — Counterfactual robustness check (`src/analyze_counterfactual.py` → `outputs/counterfactual.md`). Conclusion on current data: **all headline findings are robust** to removing the 18 garbage repos.
- ✅ **BACKLOG.021** — `actions/cache@v4` added to the daily-refresh workflow caching `data/raw/languages` + `data/raw/topics`. Expected speedup ~40 min → ~5 min once the cache is populated.

## Visualization Wow (Path C)

- **BACKLOG.015** — _Deferred._ Treemap of categories. Skipped because it duplicates the existing category bar chart and would not add new insight at n=9.

## Stretch / Optional (from proposal §20.3)

- **BACKLOG.002** — SQLite persistence layer alongside CSV.
- **BACKLOG.003** — Topic co-occurrence network graph (NetworkX + plotly).
- **BACKLOG.004** — Multi-category classification (instead of single-category MVP). Would shrink the 42% Other bucket.
- **BACKLOG.005** — Releases API integration (`/repos/{owner}/{repo}/releases`).
- **BACKLOG.006** — Issues API integration with PR filtering (`pull_request` key).
- **BACKLOG.009** — License distribution pie/bar chart.
- **BACKLOG.010** — Heatmap of language × category.

## Analysis Enhancements

- **BACKLOG.013** — Median-centered category comparison (avoid mean skew from outliers).
- **BACKLOG.018** — Counterfactual: re-run all aggregates excluding the garbage tier. Does AI/ML dominance still hold? Probably yes — worth confirming.
- **BACKLOG.019** — Bootstrap confidence intervals for category means and Stars↔Forks correlation. Adds statistical rigor to RQ4/RQ5 claims.
- **BACKLOG.020** — Owner-level signals for vibe scoring: account age, total followers, public-repo count. Would tighten precision when promoting one-time accounts vs established orgs.

## Infrastructure

- **BACKLOG.021** — Cache `data/raw/languages/` and `data/raw/topics/` across daily-refresh runs using `actions/cache@v4`. Most repos overlap day-to-day, so this could cut a 40-min run to ~5 min.
- **BACKLOG.022** — Squash daily-refresh commits monthly to keep git history lean.
