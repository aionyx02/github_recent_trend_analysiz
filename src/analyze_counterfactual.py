"""Counterfactual / robustness analysis.

Question: if we drop the vibe-coding "garbage" tier from the dataset, do the
headline conclusions (AI/ML dominance, language ranking, Stars-Forks
correlation, per-category heat) still hold?

Output: `outputs/counterfactual.md` with paired "All repos" vs
"Excluding garbage" tables for each key aggregate.

Cheap to run — pure CSV manipulation, no network. Included in daily-refresh
so the answer stays current.
"""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

from src import config

log = logging.getLogger(__name__)


def load_inputs() -> tuple[pd.DataFrame, pd.DataFrame | None]:
    """Returns (repos_with_category, vibe_scores) — vibe may be None if not yet generated."""
    repos = pd.read_csv(config.PROCESSED_DIR / "repos.csv")
    repos["description"] = repos["description"].fillna("")
    repos["primary_language"] = repos["primary_language"].fillna("Unknown")
    vibe_path = config.PROCESSED_DIR / "vibe_scores.csv"
    vibe = pd.read_csv(vibe_path) if vibe_path.exists() else None
    return repos, vibe


def pct(num: float, den: float) -> str:
    return f"{num/den*100:.1f}%" if den > 0 else "—"


def render_dual_aggregate(
    name: str, all_df: pd.DataFrame, kept_df: pd.DataFrame,
    cols: list[str], head: int = 10,
) -> str:
    """Two side-by-side rankings for visual comparison."""
    out: list[str] = []
    out.append(f"### {name}")
    out.append("")
    out.append("| 排名 | 全樣本 (n={}) | 計數 / 占比 | 排除 garbage (n={}) | 計數 / 占比 |".format(
        len(all_df), len(kept_df)))
    out.append("|---:|---|---:|---|---:|")
    all_ranking = all_df[cols[0]].value_counts().head(head)
    kept_ranking = kept_df[cols[0]].value_counts().head(head)
    for i in range(max(len(all_ranking), len(kept_ranking))):
        a_name = all_ranking.index[i] if i < len(all_ranking) else "—"
        a_n = all_ranking.iloc[i] if i < len(all_ranking) else 0
        a_pct = pct(a_n, len(all_df)) if i < len(all_ranking) else "—"
        k_name = kept_ranking.index[i] if i < len(kept_ranking) else "—"
        k_n = kept_ranking.iloc[i] if i < len(kept_ranking) else 0
        k_pct = pct(k_n, len(kept_df)) if i < len(kept_ranking) else "—"
        moved = " ⬆" if a_name != k_name and a_name != "—" else ""
        out.append(f"| {i+1} | `{a_name}` | {a_n} ({a_pct}) | `{k_name}`{moved} | {k_n} ({k_pct}) |")
    out.append("")
    return "\n".join(out)


def render_correlation_block(all_df: pd.DataFrame, kept_df: pd.DataFrame) -> str:
    out: list[str] = []
    out.append("### Stars ↔ Forks 相關性")
    out.append("")
    out.append("| 量測 | 全樣本 | 排除 garbage | Δ |")
    out.append("|---|---:|---:|---:|")
    for method in ["pearson", "spearman"]:
        a = all_df[["stars", "forks"]].corr(method=method).iloc[0, 1]
        k = kept_df[["stars", "forks"]].corr(method=method).iloc[0, 1]
        out.append(f"| {method.title()} | {a:.3f} | {k:.3f} | {k - a:+.3f} |")
    out.append("")
    return "\n".join(out)


def render_category_heat(all_df: pd.DataFrame, kept_df: pd.DataFrame) -> str:
    out: list[str] = []
    out.append("### 各類別熱度")
    out.append("")
    out.append("| 類別 | 全樣本 n | 全樣本 平均 stars | 排除後 n | 排除後 平均 stars | Δn | Δ平均 |")
    out.append("|---|---:|---:|---:|---:|---:|---:|")
    a_grp = all_df.groupby("category").agg(n=("id", "count"), mean=("stars", "mean"))
    k_grp = kept_df.groupby("category").agg(n=("id", "count"), mean=("stars", "mean"))
    all_cats = sorted(set(a_grp.index) | set(k_grp.index),
                      key=lambda c: -a_grp["n"].get(c, 0))
    for cat in all_cats:
        a_n = int(a_grp["n"].get(cat, 0))
        k_n = int(k_grp["n"].get(cat, 0))
        a_m = float(a_grp["mean"].get(cat, 0))
        k_m = float(k_grp["mean"].get(cat, 0))
        out.append(
            f"| {cat} | {a_n} | {a_m:.0f} | {k_n} | {k_m:.0f} | "
            f"{k_n - a_n:+d} | {k_m - a_m:+.0f} |"
        )
    out.append("")
    return "\n".join(out)


def render_conclusion(all_df: pd.DataFrame, kept_df: pd.DataFrame) -> str:
    """Pick the conclusion sentence based on actual robustness measurements."""
    if len(kept_df) == 0:
        return "_樣本全部被排除，無法做穩健性檢驗。_"

    # Conclusion 1: does AI/ML+Other dominance still hold?
    a_ai = (all_df["category"] == "AI/ML").mean()
    a_other = (all_df["category"] == "Other").mean()
    k_ai = (kept_df["category"] == "AI/ML").mean()
    k_other = (kept_df["category"] == "Other").mean()
    a_top2 = a_ai + a_other
    k_top2 = k_ai + k_other

    # Conclusion 2: top language change?
    a_top_lang = all_df["primary_language"].value_counts().index[0]
    k_top_lang = kept_df["primary_language"].value_counts().index[0]
    top_lang_changed = a_top_lang != k_top_lang

    # Conclusion 3: correlation drift?
    a_p = all_df[["stars", "forks"]].corr().iloc[0, 1]
    k_p = kept_df[["stars", "forks"]].corr().iloc[0, 1]
    corr_drift = abs(k_p - a_p)

    lines: list[str] = []
    lines.append("## ✅ 結論：是否穩健？")
    lines.append("")
    if abs(k_top2 - a_top2) < 0.02 and not top_lang_changed and corr_drift < 0.05:
        lines.append(
            f"**穩健性高。** 移除 {len(all_df) - len(kept_df)} 個 garbage 後："
        )
        lines.append(f"- 第一語言：仍是 `{k_top_lang}` ✓")
        lines.append(f"- AI/ML+Other 占比：{a_top2*100:.1f}% → {k_top2*100:.1f}%（變動 < 2%）✓")
        lines.append(f"- Stars↔Forks Pearson：{a_p:.3f} → {k_p:.3f}（變動 < 0.05）✓")
        lines.append("")
        lines.append(
            "→ 主要分析結論**不受 vibe-coding garbage 影響**。"
            "報告 §9 可以直接寫『結論對 18 個 garbage 排除後仍成立』。"
        )
    else:
        lines.append(
            f"**部分結論不穩健。** 移除 {len(all_df) - len(kept_df)} 個 garbage 後："
        )
        lines.append(
            f"- 第一語言：{'**從 `' + a_top_lang + '` 變 `' + k_top_lang + '`** ⚠' if top_lang_changed else f'仍是 `{k_top_lang}` ✓'}"
        )
        lines.append(
            f"- AI/ML+Other 占比：{a_top2*100:.1f}% → {k_top2*100:.1f}% "
            f"（變動 {(k_top2-a_top2)*100:+.1f} 百分點）"
            + ("⚠" if abs(k_top2 - a_top2) >= 0.02 else "✓")
        )
        lines.append(
            f"- Stars↔Forks Pearson：{a_p:.3f} → {k_p:.3f} "
            f"({k_p-a_p:+.3f})"
            + ("⚠" if corr_drift >= 0.05 else "✓")
        )
        lines.append("")
        lines.append(
            "→ 報告 §9 應該主動陳述哪些結論變了，避免被質疑「結果是被少數 farming 拉抬」。"
        )
    return "\n".join(lines)


def main() -> Path:
    config.ensure_dirs()
    repos, vibe = load_inputs()

    if vibe is None or "tier" not in vibe.columns:
        raise RuntimeError(
            "Missing vibe_scores.csv with 'tier' column. "
            "Run `python -m src.analyze_vibe` first."
        )

    # vibe.full_name → tier mapping
    tier_by_repo = vibe.set_index("full_name")["tier"].to_dict()
    repos = repos.copy()
    repos["vibe_tier"] = repos["full_name"].map(tier_by_repo).fillna("unknown")

    kept = repos[repos["vibe_tier"] != "garbage"].copy()

    lines: list[str] = []
    from datetime import date
    lines.append("# Counterfactual: 排除 vibe-coding garbage 後的穩健性檢驗")
    lines.append("")
    lines.append(
        f"_生成日：{date.today().isoformat()} · 全樣本 {len(repos)} repos · "
        f"garbage tier {len(repos) - len(kept)} 個 · 保留 {len(kept)}_"
    )
    lines.append("")
    lines.append(
        "**問題**：報告的主要結論（AI/ML 主導、Python 第一、Stars↔Forks 中度相關、"
        "Other 比例 42%）是否會被少數高分 garbage 拉抬？"
        "我們把 garbage tier 整批移除，重新跑所有 headline aggregate，"
        "看哪些變、哪些不變。"
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append(render_conclusion(repos, kept))
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 各 headline 對照表")
    lines.append("")
    lines.append(render_dual_aggregate("分類分布", repos, kept, ["category"], head=9))
    lines.append("")
    lines.append(render_dual_aggregate("程式語言排名", repos, kept, ["primary_language"]))
    lines.append("")
    lines.append(render_correlation_block(repos, kept))
    lines.append("")
    lines.append(render_category_heat(repos, kept))
    lines.append("")

    lines.append("## 詮釋指引")
    lines.append("")
    lines.append(
        "- ✓ 兩欄一致 → 該結論「**不是被 farming 撐出來的**」，可信度高。"
    )
    lines.append(
        "- ⚠ 兩欄不一致 → 該結論對 garbage 敏感，**寫報告時要說明**「移除 garbage 後 X 變成 Y」。"
    )
    lines.append(
        "- ⬆ 在語言/分類排名旁邊出現 → 該位置的內容換了，注意是排名洗牌不是消失。"
    )
    lines.append("")

    out_path = config.OUTPUTS_DIR / "counterfactual.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")
    p = main()
    print(f"wrote {p}")
