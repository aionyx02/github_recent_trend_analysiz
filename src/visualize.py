"""Stage 5: required charts per proposal §12.1. matplotlib-only for MVP.

Each function takes a DataFrame and writes one PNG to outputs/figures/.
No interactive display — backend is forced to Agg-equivalent via savefig().
"""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from src import config


def _save(fig: plt.Figure, name: str) -> Path:
    config.ensure_dirs()
    path = config.FIGURES_DIR / name
    fig.savefig(path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    return path


def top_languages(repos: pd.DataFrame, n: int = 10) -> Path:
    counts = repos["primary_language"].value_counts().head(n)
    fig, ax = plt.subplots(figsize=(8, 5))
    counts.plot(kind="barh", ax=ax)
    ax.invert_yaxis()
    ax.set_title(f"Top {n} Primary Languages")
    ax.set_xlabel("Repository Count")
    return _save(fig, "top_languages.png")


def top_topics(topics: pd.DataFrame, n: int = 20) -> Path:
    counts = topics["topic"].value_counts().head(n)
    fig, ax = plt.subplots(figsize=(8, 7))
    counts.plot(kind="barh", ax=ax)
    ax.invert_yaxis()
    ax.set_title(f"Top {n} Topics")
    ax.set_xlabel("Repository Count")
    return _save(fig, "top_topics.png")


def stars_distribution(repos: pd.DataFrame) -> Path:
    fig, ax = plt.subplots(figsize=(8, 5))
    repos["stars"].plot(kind="hist", bins=40, ax=ax, log=True)
    ax.set_title("Stars Distribution (log y)")
    ax.set_xlabel("Stars")
    return _save(fig, "stars_distribution.png")


def forks_vs_stars(repos: pd.DataFrame) -> Path:
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(repos["stars"], repos["forks"], alpha=0.4)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title("Forks vs Stars")
    ax.set_xlabel("Stars (log)")
    ax.set_ylabel("Forks (log)")
    return _save(fig, "forks_vs_stars.png")


def category_distribution(repos: pd.DataFrame) -> Path:
    counts = repos["category"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    counts.plot(kind="bar", ax=ax)
    ax.set_title("Repositories by Category")
    ax.set_ylabel("Count")
    return _save(fig, "category_distribution.png")


def category_avg_stars(repos: pd.DataFrame) -> Path:
    avg = repos.groupby("category")["stars"].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5))
    avg.plot(kind="bar", ax=ax)
    ax.set_title("Average Stars by Category")
    ax.set_ylabel("Mean Stars")
    return _save(fig, "category_avg_stars.png")


def daily_new_repos(repos: pd.DataFrame) -> Path:
    series = repos["created_at"].dt.date.value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(9, 4))
    series.plot(ax=ax, marker="o")
    ax.set_title("New Trending Repositories per Day")
    ax.set_xlabel("Date")
    ax.set_ylabel("Count")
    return _save(fig, "daily_new_repos.png")