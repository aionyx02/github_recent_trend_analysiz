"""Prepare a random validation sample for rule-based classifier precision check.

Reads repos.csv, draws a stratified random sample (~5-6 rows per category, 50
rows total or all available if a category is smaller), joins description + URL,
and writes `data/processed/classification_validation_sample.csv` with empty
`agree` / `correct_category` / `notes` columns for human labelling.

The labeller opens the CSV, clicks each `html_url` (or just reads the
description), and writes one of:

  - `agree` column:           TP (rule-based label looks right) /
                              FP (looks wrong) / ? (unsure)
  - `correct_category`:       if FP, the labeller writes the category that
                              should have been picked
  - `notes`:                  optional one-liner

After labelling, compute simple agreement rate per category:

    agreement_rate = TP_count / (TP_count + FP_count)

Report figures in the README / report §10 as classification validity evidence.

Random seed is pinned (42) so re-running this script produces the same 50 repos
unless `repos.csv` itself changes.
"""

from __future__ import annotations

import logging

import pandas as pd

from src import config

log = logging.getLogger(__name__)

TOTAL_SAMPLE = 50
RANDOM_SEED = 42


def main() -> None:
    config.ensure_dirs()

    repos_path = config.PROCESSED_DIR / "repos.csv"
    if not repos_path.exists():
        raise RuntimeError(
            f"Missing {repos_path}. "
            "Run `python -m src.collect_all && python -m src.build_charts` first."
        )

    repos = pd.read_csv(repos_path)
    if "category" not in repos.columns:
        raise RuntimeError(
            "`category` column missing — run `python -m src.build_charts` to classify."
        )

    repos["description"] = repos["description"].fillna("").str.slice(0, 200)
    repos["primary_language"] = repos["primary_language"].fillna("Unknown")

    # Stratified random sample: aim for proportional representation across
    # categories, but cap each category at ceil(TOTAL_SAMPLE / n_categories)
    # so a dominant category doesn't swallow the sample.
    categories = repos["category"].unique()
    per_cat = max(1, TOTAL_SAMPLE // len(categories))

    chunks: list[pd.DataFrame] = []
    for cat in sorted(categories):
        sub = repos[repos["category"] == cat]
        n = min(per_cat, len(sub))
        sampled = sub.sample(n=n, random_state=RANDOM_SEED) if n > 0 else sub
        log.info("category=%s sampled=%d (of %d available)", cat, n, len(sub))
        chunks.append(sampled)

    sample = pd.concat(chunks, ignore_index=True)

    # If stratified pull came up short, top up with random additions
    # (no replacement of already-chosen ids).
    if len(sample) < TOTAL_SAMPLE:
        remaining = repos[~repos["id"].isin(sample["id"])]
        topup = remaining.sample(
            n=min(TOTAL_SAMPLE - len(sample), len(remaining)),
            random_state=RANDOM_SEED,
        )
        sample = pd.concat([sample, topup], ignore_index=True)

    sample = sample[[
        "full_name", "html_url", "primary_language", "category",
        "stars", "forks", "age_days", "description",
    ]].copy()
    sample["agree"] = ""                # human writes TP / FP / ?
    sample["correct_category"] = ""     # if FP, the category the labeller would assign
    sample["notes"] = ""                # optional one-liner

    out_path = config.PROCESSED_DIR / "classification_validation_sample.csv"
    sample.to_csv(out_path, index=False, encoding="utf-8-sig")
    log.info("wrote %s (%d rows)", out_path, len(sample))

    print(f"Wrote {out_path} ({len(sample)} rows)")
    print()
    print("Per-category sample counts:")
    for cat, n in sample["category"].value_counts().items():
        print(f"  {cat}: {n}")
    print()
    print("Open in Excel / Google Sheets (file is utf-8-sig so Chinese works).")
    print("For each row, click `html_url`, read description, then fill:")
    print("  - `agree`           = TP (rule label correct) / FP (wrong) / ? (unsure)")
    print("  - `correct_category`= if FP, your suggested category")
    print("  - `notes`           = optional one-liner")
    print()
    print("After labelling, compute agreement rate per category and write to")
    print("README §限制與威脅 (or outputs/report.md §10).")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")
    main()