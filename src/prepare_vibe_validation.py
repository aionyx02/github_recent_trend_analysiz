"""Prepare a stratified validation sample for TASK.007 — vibe-coding precision/recall.

Reads vibe_scores.csv + repos.csv, samples ~20 per tier (or all if tier has fewer),
joins description + URL so the labeller doesn't need to look anything up, and
writes `data/processed/vibe_validation_sample.csv` with an empty `label` column.

The labeller opens the CSV, clicks each `html_url`, then writes:
  - `TP` if they agree with the tier
  - `FP` if they disagree
  - `?`  if undecidable / borderline

After labelling, `python -m src.score_vibe_validation` (future) computes
precision / recall / F1 per tier.
"""

from __future__ import annotations

import logging

import pandas as pd

from src import config

log = logging.getLogger(__name__)

SAMPLE_PER_TIER = 20
RANDOM_SEED = 42


def main() -> None:
    config.ensure_dirs()

    vibe_path = config.PROCESSED_DIR / "vibe_scores.csv"
    repos_path = config.PROCESSED_DIR / "repos.csv"
    if not vibe_path.exists() or not repos_path.exists():
        raise RuntimeError(
            "Missing vibe_scores.csv or repos.csv. "
            "Run `python -m src.build_charts && python -m src.analyze_vibe` first."
        )

    vibe = pd.read_csv(vibe_path)
    # vibe already has primary_language + license — only need URL + description from repos.
    repos = pd.read_csv(repos_path)[["full_name", "html_url", "description"]]
    repos["description"] = repos["description"].fillna("").str.slice(0, 200)
    joined = vibe.merge(repos, on="full_name", how="left")

    chunks: list[pd.DataFrame] = []
    for tier in ["garbage", "suspicious", "legitimate"]:
        sub = joined[joined["tier"] == tier]
        n = min(SAMPLE_PER_TIER, len(sub))
        sampled = sub.sample(n=n, random_state=RANDOM_SEED) if n > 0 else sub
        log.info("tier=%s sampled=%d (of %d available)", tier, n, len(sub))
        chunks.append(sampled)

    sample = pd.concat(chunks, ignore_index=True)
    sample = sample[[
        "full_name", "html_url", "primary_language", "license",
        "stars", "forks", "age_days", "score", "tier", "reasons",
        "description",
    ]].copy()
    sample["label"] = ""           # human writes TP / FP / ?
    sample["notes"] = ""           # optional one-liner per row

    out_path = config.PROCESSED_DIR / "vibe_validation_sample.csv"
    sample.to_csv(out_path, index=False, encoding="utf-8-sig")
    log.info("wrote %s (%d rows)", out_path, len(sample))
    print(f"Wrote {out_path}")
    print(f"  garbage:    {(sample['tier']=='garbage').sum()} rows")
    print(f"  suspicious: {(sample['tier']=='suspicious').sum()} rows")
    print(f"  legitimate: {(sample['tier']=='legitimate').sum()} rows")
    print()
    print("Open the CSV in Excel / Google Sheets, click each html_url,")
    print("fill the `label` column with TP (agree) / FP (disagree) / ? (unsure).")
    print()
    print("Note: file uses utf-8-sig so Excel handles Chinese correctly.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")
    main()
