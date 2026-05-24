"""Stage 5 driver: classify + render the seven required charts + summary stats.

Reads:
    data/processed/repos.csv
    data/processed/repo_topics.csv
Writes:
    data/processed/repos.csv (with `category` column added)
    outputs/figures/*.png        (7 required charts)
    outputs/summary_stats.md     (per-category + overall stats)
"""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

from src import classify, config, visualize

log = logging.getLogger(__name__)


def load_inputs() -> tuple[pd.DataFrame, pd.DataFrame]:
    repos = pd.read_csv(config.PROCESSED_DIR / "repos.csv")
    repos["description"] = repos["description"].fillna("")
    repos["primary_language"] = repos["primary_language"].fillna("Unknown")
    repos["created_at"] = pd.to_datetime(repos["created_at"], utc=True)
    repos["pushed_at"] = pd.to_datetime(repos["pushed_at"], utc=True)

    topics_path = config.PROCESSED_DIR / "repo_topics.csv"
    topics = pd.read_csv(topics_path) if topics_path.exists() else pd.DataFrame(
        columns=["repo_id", "topic"])
    return repos, topics


def render_summary_md(repos: pd.DataFrame, topics: pd.DataFrame) -> str:
    lines: list[str] = []
    lines.append("# Summary Statistics")
    lines.append("")
    lines.append(f"_Sample size: {len(repos)} repos_")
    lines.append("")

    lines.append("## Overall")
    lines.append("")
    lines.append("| Metric | Mean | Median | Max |")
    lines.append("|---|---:|---:|---:|")
    for col in ["stars", "forks", "open_issues", "stars_per_day", "age_days"]:
        lines.append(
            f"| {col} | {repos[col].mean():.1f} | {repos[col].median():.1f} | {repos[col].max():.0f} |"
        )
    lines.append("")

    lines.append("## Top 10 by stars")
    lines.append("")
    lines.append("| Repo | Stars | Forks | Language | Category |")
    lines.append("|---|---:|---:|---|---|")
    for r in repos.nlargest(10, "stars").itertuples(index=False):
        safe = r.full_name.replace("|", "\\|")
        lines.append(f"| `{safe}` | {r.stars} | {r.forks} | {r.primary_language} | {r.category} |")
    lines.append("")

    lines.append("## Top 10 by stars_per_day (breakout)")
    lines.append("")
    lines.append("| Repo | Stars/day | Stars | Age | Category |")
    lines.append("|---|---:|---:|---:|---|")
    for r in repos.nlargest(10, "stars_per_day").itertuples(index=False):
        safe = r.full_name.replace("|", "\\|")
        lines.append(f"| `{safe}` | {r.stars_per_day:.1f} | {r.stars} | {r.age_days}d | {r.category} |")
    lines.append("")

    lines.append("## Per-category heat")
    lines.append("")
    cat_stats = repos.groupby("category").agg(
        count=("id", "count"),
        mean_stars=("stars", "mean"),
        median_stars=("stars", "median"),
        mean_forks=("forks", "mean"),
        mean_spd=("stars_per_day", "mean"),
        mean_issues=("open_issues", "mean"),
    ).sort_values("count", ascending=False)
    lines.append("| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for cat, r in cat_stats.iterrows():
        lines.append(
            f"| {cat} | {int(r['count'])} | {r['mean_stars']:.0f} | "
            f"{r['median_stars']:.0f} | {r['mean_forks']:.0f} | {r['mean_spd']:.1f} | "
            f"{r['mean_issues']:.1f} |"
        )
    lines.append("")

    lines.append("## Correlations")
    lines.append("")
    pearson = repos[["stars", "forks", "open_issues", "age_days"]].corr(method="pearson")
    spearman = repos[["stars", "forks", "open_issues", "age_days"]].corr(method="spearman")
    lines.append("**Pearson** (linear)")
    lines.append("")
    lines.append(pearson.round(3).to_markdown())
    lines.append("")
    lines.append("**Spearman** (rank)")
    lines.append("")
    lines.append(spearman.round(3).to_markdown())
    lines.append("")

    lines.append("## Top 20 topics")
    lines.append("")
    if not topics.empty:
        top_topics = topics["topic"].value_counts().head(20)
        lines.append("| Topic | Repos |")
        lines.append("|---|---:|")
        for topic, n in top_topics.items():
            lines.append(f"| `{topic}` | {n} |")
    else:
        lines.append("_No topics data._")
    lines.append("")
    return "\n".join(lines)


def main() -> dict[str, Path]:
    config.ensure_dirs()
    repos, topics = load_inputs()
    log.info("loaded %d repos, %d topic rows", len(repos), len(topics))

    log.info("classifying...")
    repos = classify.apply(repos, topics)
    cat_counts = repos["category"].value_counts()
    log.info("category counts: %s", dict(cat_counts))

    repos.to_csv(config.PROCESSED_DIR / "repos.csv", index=False, encoding="utf-8")

    log.info("rendering charts...")
    figs = {
        "top_languages": visualize.top_languages(repos),
        "top_topics": visualize.top_topics(topics) if not topics.empty else None,
        "stars_distribution": visualize.stars_distribution(repos),
        "forks_vs_stars": visualize.forks_vs_stars(repos),
        "category_distribution": visualize.category_distribution(repos),
        "category_avg_stars": visualize.category_avg_stars(repos),
        "daily_new_repos": visualize.daily_new_repos(repos),
    }

    summary_md = render_summary_md(repos, topics)
    summary_path = config.OUTPUTS_DIR / "summary_stats.md"
    summary_path.write_text(summary_md, encoding="utf-8")
    figs["summary_stats_md"] = summary_path

    return {k: v for k, v in figs.items() if v is not None}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")
    results = main()
    for name, path in results.items():
        print(f"{name}: {path}")