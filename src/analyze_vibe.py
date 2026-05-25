"""Metadata-completeness risk scoring for GitHub trending repos.

This module computes a **public-metadata completeness risk score** (0..10) for
each repository in the sample. Higher score = more public-facing metadata
signals are missing (no description, no license, no topics, fork-to-star
imbalance, etc.).

Neutral framing (research-grade): the score measures *visible* metadata
completeness only. A high score does **not** mean the project has no value —
just that its public artifact carries fewer of the conventional OSS hygiene
signals relative to its attention. This is a quantifiable proxy for the broader
question "how much of recent GitHub trending is well-documented vs. metadata-
sparse?" — not a quality judgment of any individual repo or its author, and not
a judgment of vibe-coding as a practice.

Scoring (0..10, higher = more metadata signals missing):

    +2  description empty
    +1  description present but <20 chars
    +1  no license declared
    +2  stars > 1000 AND description empty           (high-attention low-description)
    +2  fork_star_ratio < 0.02 AND stars > 500        (stars but very few forks)
    +1  stars_per_day > 300 AND age_days < 7          (overnight surge)
    +1  name matches generic-AI-buzzword pattern      (*-skills, *-agent, ...)
    +1  no topics                                     (only when topics data present)

Tiers (neutral Chinese labels):
    0-2  訊號完整      (signals complete — well-documented)
    3-4  待檢視        (needs review — borderline)
    5+   低資訊密度    (low-information-density — high-attention low-metadata)
"""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

from src import config


TIER_LOW = "低資訊密度"
TIER_REVIEW = "待檢視"
TIER_COMPLETE = "訊號完整"


GENERIC_AI_PATTERN = re.compile(
    r"(?:^|[-_])(?:skills?|agents?|cookbook|prompt|gpt|claude|llm|vibe|codex|"
    r"awesome|toolkit|playground|demo|test|starter|template|copilot)(?:$|[-_])",
    re.IGNORECASE,
)


def score_repo(row: pd.Series, topics_by_id: dict[int, list[str]] | None = None) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []
    raw_desc = row.get("description")
    desc = "" if pd.isna(raw_desc) else str(raw_desc).strip()
    desc_len = len(desc)
    stars = int(row["stars"])
    forks = int(row["forks"])
    age_days = int(row["age_days"])
    stars_per_day = float(row["stars_per_day"])
    license_val = row.get("license")
    name = row.get("name", "")

    if desc_len == 0:
        score += 2
        reasons.append("desc:empty")
    elif desc_len < 20:
        score += 1
        reasons.append("desc:short")

    if not license_val or str(license_val) in ("None", "NOASSERTION", "nan"):
        score += 1
        reasons.append("license:none")

    if stars > 1000 and desc_len == 0:
        score += 2
        reasons.append("high-attention-no-desc")

    fsr = forks / max(stars, 1)
    if stars > 500 and fsr < 0.02:
        score += 2
        reasons.append(f"low-forks:{fsr:.3f}")

    if stars_per_day > 300 and age_days < 7:
        score += 1
        reasons.append(f"overnight-surge:{stars_per_day:.0f}/day")

    if GENERIC_AI_PATTERN.search(name):
        score += 1
        reasons.append(f"generic-name:{name}")

    if topics_by_id is not None:
        if not topics_by_id.get(int(row["id"])):
            score += 1
            reasons.append("topics:none")

    return min(score, 10), reasons


def tier(score: int) -> str:
    if score >= 5:
        return TIER_LOW
    if score >= 3:
        return TIER_REVIEW
    return TIER_COMPLETE


def analyze(repos: pd.DataFrame, topics: pd.DataFrame | None = None) -> pd.DataFrame:
    topics_by_id: dict[int, list[str]] | None = None
    if topics is not None and not topics.empty:
        topics_by_id = topics.groupby("repo_id")["topic"].apply(list).to_dict()
    scored = []
    for _, row in repos.iterrows():
        s, reasons = score_repo(row, topics_by_id)
        raw_desc = row.get("description")
        clean_desc = "" if pd.isna(raw_desc) else str(raw_desc).strip()
        scored.append({
            "full_name": row["full_name"],
            "stars": int(row["stars"]),
            "forks": int(row["forks"]),
            "age_days": int(row["age_days"]),
            "stars_per_day": round(float(row["stars_per_day"]), 1),
            "primary_language": row["primary_language"],
            "license": row["license"],
            "desc_len": len(clean_desc),
            "score": s,
            "tier": tier(s),
            "reasons": ", ".join(reasons),
        })
    return pd.DataFrame(scored).sort_values("score", ascending=False)


def render_markdown(scored: pd.DataFrame, repos: pd.DataFrame, total_repos: int,
                    has_topics: bool, run_date: str) -> str:
    counts = scored["tier"].value_counts().reindex(
        [TIER_LOW, TIER_REVIEW, TIER_COMPLETE]).fillna(0).astype(int)
    pct = (counts / total_repos * 100).round(1)

    lines: list[str] = []
    lines.append("# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)")
    lines.append("")
    lines.append(f"_Generated: {run_date} | Sample size: {total_repos} repos "
                 f"({'with' if has_topics else 'without'} topics signal)_")
    lines.append("")
    lines.append("## 定義 / Definition")
    lines.append("")
    lines.append("**公開 metadata 完整度** = repo 的可見 metadata 訊號（description、license、")
    lines.append("topics、fork-star 比例等）相對於其 stars 數的「完整程度」。")
    lines.append("")
    lines.append("我們將高分組命名為 **低資訊密度 (low-information-density candidate)**：")
    lines.append("stars 不需太多努力就能累積，但 description、tags、forks、license 都需要實際付出。")
    lines.append("**高分代表公開 metadata 訊號可疑，不代表該 repo 一定無價值** —— ")
    lines.append("`awesome-*` 列表、學術研究 repo、官方快速釋出 repo 都可能踩到訊號。")
    lines.append("此指標衡量公開產出，不衡量作者本人，也不是對 vibe-coding 這個編程方式的評價。")
    lines.append("")
    lines.append("## 評分機制 / Scoring rubric")
    lines.append("")
    lines.append("| Signal | Points | Rationale |")
    lines.append("|---|---:|---|")
    lines.append("| `description` empty | +2 | Highest single signal of metadata gap |")
    lines.append("| `description` < 20 chars | +1 | Marginal |")
    lines.append("| No license declared | +1 | Common OSS-hygiene gap |")
    lines.append("| stars > 1000 AND description empty | +2 | High-attention low-description |")
    lines.append("| fork_star_ratio < 0.02 AND stars > 500 | +2 | Stars but very few forks |")
    lines.append("| stars_per_day > 300 AND age_days < 7 | +1 | Overnight surge |")
    lines.append("| Name matches generic-AI-buzzword pattern | +1 | `*-skills`, `*-agent`, `*-cookbook` ... |")
    lines.append("| No topics tagged | +1 | Only when topics data present |")
    lines.append("")
    lines.append(f"**Tiers**: 0-2 {TIER_COMPLETE} · 3-4 {TIER_REVIEW} · 5+ {TIER_LOW}")
    lines.append("")
    lines.append("## 結果 / Findings")
    lines.append("")
    lines.append("| Tier | Count | % of sample |")
    lines.append("|---|---:|---:|")
    for t in [TIER_LOW, TIER_REVIEW, TIER_COMPLETE]:
        lines.append(f"| {t} | {counts[t]} | {pct[t]}% |")
    lines.append("")

    lines.append("### Top 15 highest-scoring repos")
    lines.append("")
    top = scored.head(15)
    lines.append("| Rank | Repo | Stars | Forks | Age | Score | Reasons |")
    lines.append("|---:|---|---:|---:|---:|---:|---|")
    for i, row in enumerate(top.itertuples(index=False), 1):
        safe_name = row.full_name.replace("|", "\\|")
        safe_reasons = row.reasons.replace("|", "\\|")
        lines.append(
            f"| {i} | `{safe_name}` | {row.stars} | {row.forks} | "
            f"{row.age_days}d | **{row.score}** | {safe_reasons} |"
        )
    lines.append("")

    lines.append("### Signal frequency (independent of tier)")
    lines.append("")
    desc_empty = int((scored["desc_len"] == 0).sum())
    desc_short = int(((scored["desc_len"] > 0) & (scored["desc_len"] < 20)).sum())
    no_license = int((scored["license"].isin(["None", "NOASSERTION"]) |
                      scored["license"].isna()).sum())
    famous_nothing = int(((scored["stars"] > 1000) & (scored["desc_len"] == 0)).sum())
    low_forks = int(((scored["stars"] > 500) &
                     (scored["forks"] / scored["stars"].clip(lower=1) < 0.02)).sum())
    overnight = int(((scored["stars_per_day"] > 300) & (scored["age_days"] < 7)).sum())
    generic = int(scored["full_name"].apply(
        lambda fn: bool(GENERIC_AI_PATTERN.search(fn.split("/")[-1]))).sum())

    lines.append("| Signal | Count | % |")
    lines.append("|---|---:|---:|")
    rows = [
        ("description empty", desc_empty),
        ("description <20 chars", desc_short),
        ("no license", no_license),
        ("high-attention no-desc (stars>1k + empty desc)", famous_nothing),
        ("low fork ratio (stars>500 + fsr<0.02)", low_forks),
        ("overnight surge (>300 spd + <7 days)", overnight),
        ("generic-AI-buzzword name", generic),
    ]
    for label, n in rows:
        lines.append(f"| {label} | {n} | {n/total_repos*100:.1f}% |")
    lines.append("")

    lines.append(f"### {TIER_LOW} tier — by primary language")
    lines.append("")
    low_density = scored[scored["tier"] == TIER_LOW]
    if not low_density.empty:
        lang_breakdown = low_density["primary_language"].value_counts()
        lines.append("| Language | Repos in 低資訊密度 tier |")
        lines.append("|---|---:|")
        for lang, n in lang_breakdown.items():
            lines.append(f"| {lang} | {n} |")
    else:
        lines.append("_No 低資訊密度 tier repos in this sample._")
    lines.append("")

    lines.append(f"### {TIER_LOW} concentration by stars bucket")
    lines.append("")
    lines.append("Where in the popularity distribution does the low-metadata cohort cluster?")
    lines.append("")
    buckets = [
        ("≥10000", scored["stars"] >= 10000),
        ("5000-9999", (scored["stars"] >= 5000) & (scored["stars"] < 10000)),
        ("1000-4999", (scored["stars"] >= 1000) & (scored["stars"] < 5000)),
        ("500-999", (scored["stars"] >= 500) & (scored["stars"] < 1000)),
        ("100-499", (scored["stars"] >= 100) & (scored["stars"] < 500)),
        ("<100", scored["stars"] < 100),
    ]
    lines.append(f"| Stars bucket | Total | {TIER_LOW} | {TIER_REVIEW} | {TIER_COMPLETE} | 低資訊密度 % |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    for label, mask in buckets:
        sub = scored[mask]
        if sub.empty:
            continue
        g = int((sub["tier"] == TIER_LOW).sum())
        s = int((sub["tier"] == TIER_REVIEW).sum())
        leg = int((sub["tier"] == TIER_COMPLETE).sum())
        pct = g / len(sub) * 100 if len(sub) else 0
        lines.append(f"| {label} | {len(sub)} | {g} | {s} | {leg} | {pct:.1f}% |")
    lines.append("")

    lines.append("### High-attention no-description zoom (stars > 1000 + empty description)")
    lines.append("")
    fn_mask = (scored["stars"] > 1000) & (scored["desc_len"] == 0)
    fn = scored[fn_mask].sort_values("stars", ascending=False)
    if fn.empty:
        lines.append("_No repos match._")
    else:
        lines.append("These are the most visible high-attention low-metadata artifacts —")
        lines.append("high stars with zero description text.")
        lines.append("")
        lines.append("| Repo | Stars | Forks | Age | Language | License |")
        lines.append("|---|---:|---:|---:|---|---|")
        for r in fn.itertuples(index=False):
            safe_name = r.full_name.replace("|", "\\|")
            lic = "—" if str(r.license) in ("None", "NOASSERTION", "nan") else r.license
            lines.append(
                f"| `{safe_name}` | {r.stars} | {r.forks} | {r.age_days}d | "
                f"{r.primary_language} | {lic} |"
            )
    lines.append("")

    lines.append("### Generic-name pattern breakdown")
    lines.append("")
    name_only = scored["full_name"].str.split("/").str[-1]
    matched = name_only[name_only.apply(lambda n: bool(GENERIC_AI_PATTERN.search(n)))]
    pattern_hits: dict[str, int] = {}
    for name in matched:
        m = GENERIC_AI_PATTERN.search(name)
        if m:
            key = m.group(0).strip("-_").lower()
            pattern_hits[key] = pattern_hits.get(key, 0) + 1
    if pattern_hits:
        lines.append(f"Of {len(matched)} repos with a generic-AI-buzzword token in the name, "
                     f"the token distribution is:")
        lines.append("")
        lines.append("| Token | Repos |")
        lines.append("|---|---:|")
        for token, n in sorted(pattern_hits.items(), key=lambda x: -x[1]):
            lines.append(f"| `{token}` | {n} |")
    lines.append("")

    lines.append("### Topics coverage")
    lines.append("")
    if "topics:none" in scored["reasons"].str.cat(sep=" "):
        no_topics_count = int(scored["reasons"].str.contains("topics:none").sum())
        with_topics = total_repos - no_topics_count
        lines.append(f"- Repos with **zero topics**: {no_topics_count} ({no_topics_count/total_repos*100:.1f}%)")
        lines.append(f"- Repos with at least one topic: {with_topics} ({with_topics/total_repos*100:.1f}%)")
    else:
        lines.append("_Topics signal not active in this run._")
    lines.append("")

    lines.append("## Methodology limits")
    lines.append("")
    lines.append("- Stars are not a proxy for code quality. A high score is a *signal-level*")
    lines.append("  suspicion that public metadata is sparse, not a verdict that the repo lacks value.")
    lines.append("- The generic-name regex is intentionally narrow. False positives are possible")
    lines.append("  (e.g., a legitimate `awesome-*` curated list).")
    lines.append("- 30-day creation window biases toward repos that haven't had time to accumulate forks.")
    lines.append("- We do not inspect commit graph, contributor count, or README length — those would")
    lines.append("  tighten the signal but cost extra API calls per repo.")
    if not has_topics:
        lines.append("- **Topics signal missing in this run.** Re-run after topics collection completes")
        lines.append("  for the full ±1 point.")
    lines.append("")
    lines.append("## Reproduce")
    lines.append("")
    lines.append("```bash")
    lines.append("python -m src.analyze_vibe")
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def main() -> Path:
    config.ensure_dirs()
    repos_path = config.PROCESSED_DIR / "repos.csv"
    if not repos_path.exists():
        raise RuntimeError(f"Missing {repos_path}. Run `python -m src.clean_data` first.")
    repos = pd.read_csv(repos_path)
    topics_path = config.PROCESSED_DIR / "repo_topics.csv"
    topics = pd.read_csv(topics_path) if topics_path.exists() else None

    scored = analyze(repos, topics)
    from datetime import date
    md = render_markdown(scored, repos, total_repos=len(repos),
                         has_topics=topics is not None, run_date=date.today().isoformat())
    out_path = config.OUTPUTS_DIR / "vibe_coding_analysis.md"
    out_path.write_text(md, encoding="utf-8")
    scored_csv = config.PROCESSED_DIR / "vibe_scores.csv"
    scored.to_csv(scored_csv, index=False, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    p = main()
    print(f"wrote {p}")