"""Break down the 'Other' category — what's actually inside the 42% that the
rule-based classifier couldn't pin down?

Outputs `outputs/other_breakdown.md` covering:

1. Top 10 primary languages in Other
2. Top 20 description keywords (simple regex tokenisation, English stopwords removed)
3. Top 10 GitHub topics among Other repos that *do* have topics
4. Suggested new categories the keyword/topic spread might justify
   (e.g., Education, Design, Blockchain, Finance, Hardware)

Reads:
    data/processed/repos.csv (must include `category` column from build_charts)
    data/processed/repo_topics.csv
Writes:
    outputs/other_breakdown.md
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import pandas as pd

from src import config


STOPWORDS = {
    # very common English
    "the", "a", "an", "and", "or", "but", "for", "of", "to", "in", "on", "at",
    "by", "with", "from", "as", "is", "are", "was", "were", "be", "been",
    "being", "this", "that", "these", "those", "it", "its", "your", "you",
    "we", "our", "us", "i", "my", "me", "they", "them", "their", "he", "she",
    "his", "her", "not", "no", "yes", "do", "does", "did", "doing", "have",
    "has", "had", "having", "can", "could", "will", "would", "should", "may",
    "might", "must", "shall", "than", "then", "so", "if", "because", "while",
    "when", "where", "what", "which", "who", "whom", "how", "why",
    # noisy fillers we don't want as "category candidates"
    "based", "using", "use", "used", "uses", "via", "more", "most", "very",
    "such", "any", "all", "some", "each", "every", "one", "two", "three",
    "first", "last", "new", "old", "open", "source", "free", "easy", "simple",
    "small", "big", "best", "good", "great", "modern", "powerful", "fast",
    "lightweight", "minimal", "official", "support", "supports", "supported",
    "make", "makes", "made", "build", "built", "create", "creates", "created",
    "let", "lets", "get", "gets", "got", "into", "out", "up", "down", "over",
    "under", "also", "yet", "etc",
    # too generic to drive new category suggestions
    "project", "projects", "code", "tool", "tools", "app", "apps", "library",
    "framework", "system", "platform", "service", "api", "data", "files",
    "file", "version", "release",
}

WORD_RE = re.compile(r"[A-Za-z][A-Za-z+\-#.]{2,}")


def _tokenise(text: str) -> list[str]:
    return [t.lower() for t in WORD_RE.findall(text) if t.lower() not in STOPWORDS]


def render(repos: pd.DataFrame, topics: pd.DataFrame | None) -> str:
    other = repos[repos["category"] == "Other"].copy()
    n_other = len(other)
    n_all = len(repos)

    lines: list[str] = []
    lines.append("# Other 類別深入分析 / Other Category Breakdown")
    lines.append("")
    lines.append(
        f"_Sample: {n_all} repos total · {n_other} repos in Other "
        f"({n_other / n_all * 100:.1f}%)_"
    )
    lines.append("")
    lines.append(
        "Other 桶（無法被現行 9 大規則式分類器歸類的 repo）占整體樣本約 4 成。"
        "本檔分析它的內部組成，協助判斷是否需要新增類別。"
    )
    lines.append("")
    lines.append("## 1. Other 內 Top 10 主要程式語言")
    lines.append("")
    lines.append("| Rank | 語言 | Repos | Other 內占比 |")
    lines.append("|---:|---|---:|---:|")
    lang_counts = other["primary_language"].fillna("Unknown").value_counts().head(10)
    for i, (lang, n) in enumerate(lang_counts.items(), 1):
        lines.append(f"| {i} | `{lang}` | {n} | {n / n_other * 100:.1f}% |")
    lines.append("")

    lines.append("## 2. Other 內 Top 20 description 關鍵字")
    lines.append("")
    lines.append("簡易 regex 分詞、英文停用字過濾後的詞頻。代表「Other 內部專案在描述自己什麼」。")
    lines.append("")
    desc_text = " ".join(other["description"].fillna("").astype(str).tolist())
    tokens = _tokenise(desc_text)
    top_tokens = Counter(tokens).most_common(20)
    lines.append("| Rank | 關鍵字 | 出現次數 |")
    lines.append("|---:|---|---:|")
    for i, (tok, n) in enumerate(top_tokens, 1):
        lines.append(f"| {i} | `{tok}` | {n} |")
    lines.append("")

    if topics is not None and not topics.empty:
        lines.append("## 3. Other 內 Top 10 GitHub topics")
        lines.append("")
        other_ids = set(other["id"].astype(int))
        other_topics = topics[topics["repo_id"].astype(int).isin(other_ids)]
        n_other_with_topics = other_topics["repo_id"].nunique()
        coverage = n_other_with_topics / n_other * 100 if n_other else 0
        lines.append(
            f"_Other 內 {n_other_with_topics} / {n_other} 個 repo 有貼 topic "
            f"({coverage:.1f}%)_"
        )
        lines.append("")
        top_topics = other_topics["topic"].value_counts().head(10)
        lines.append("| Rank | Topic | Repos |")
        lines.append("|---:|---|---:|")
        for i, (tp, n) in enumerate(top_topics.items(), 1):
            lines.append(f"| {i} | `{tp}` | {n} |")
        lines.append("")

    lines.append("## 4. 可能值得新增的類別 (Suggested new categories)")
    lines.append("")
    lines.append(
        "根據 §1-§3 觀察到的訊號，下列候選類別可能值得在未來版本納入分類規則："
    )
    lines.append("")

    # Heuristic candidate buckets — keyword/topic groups that, if popular in
    # Other, would justify a dedicated category.
    candidates: dict[str, list[str]] = {
        "Education / Learning": ["course", "tutorial", "learn", "learning", "study",
                                 "book", "books", "notes", "exam", "school"],
        "Design / Creative": ["design", "ui", "ux", "icon", "icons", "font",
                              "fonts", "art", "wallpaper", "wallpapers", "color"],
        "Blockchain / Web3": ["blockchain", "crypto", "ethereum", "bitcoin",
                              "web3", "smart-contract", "defi", "nft", "wallet"],
        "Finance / Trading": ["trading", "trade", "stock", "stocks", "finance",
                              "market", "portfolio", "investment", "fintech"],
        "Hardware / Embedded": ["arduino", "esp32", "raspberry", "embedded",
                                "iot", "firmware", "microcontroller", "stm32"],
        "Documentation / Awesome lists": ["awesome", "resources", "list", "lists",
                                          "curated", "collection"],
    }

    token_freq = dict(Counter(tokens))
    if topics is not None and not topics.empty:
        topic_freq: dict[str, int] = (
            other_topics["topic"].value_counts().to_dict()
        )
    else:
        topic_freq = {}

    lines.append("| 候選類別 | 命中關鍵字 (description+topic) | 估計 repos |")
    lines.append("|---|---|---:|")
    for cat, kws in candidates.items():
        hits = []
        repo_count = 0
        for kw in kws:
            d = token_freq.get(kw, 0)
            t = topic_freq.get(kw, 0)
            if d + t > 0:
                hits.append(f"`{kw}`({d + t})")
                repo_count += d + t  # over-counts repos with multiple hits;
                                      # acceptable as a rough heuristic
        if hits:
            lines.append(f"| {cat} | {', '.join(hits[:5])} | ~{repo_count} |")
    lines.append("")
    lines.append(
        "_估計 repos 是「描述/topic 命中關鍵字的次數總和」，會略高於實際 repo 數_"
        "_（一個 repo 可能命中多個 keyword）；用作粗略優先級排序。_"
    )
    lines.append("")

    lines.append("## 5. 限制")
    lines.append("")
    lines.append(
        "- Token 分詞使用簡易 regex，未處理複合詞、縮寫、CJK 文字；中文 description 的內部結構未被分析。"
    )
    lines.append(
        "- 候選類別建議基於關鍵字命中，**不代表新增該類別後 Other 桶會大幅縮小** —— "
        "需先設計具體 keyword + priority 規則並重跑 classify.py 才能評估效果。"
    )
    lines.append(
        "- 本檔每次跑 `python -m src.analyze_other` 重新生成；資料每日由 daily-refresh "
        "工作流自動重抓後可一併重算。"
    )
    lines.append("")
    return "\n".join(lines)


def main() -> Path:
    config.ensure_dirs()
    repos_path = config.PROCESSED_DIR / "repos.csv"
    topics_path = config.PROCESSED_DIR / "repo_topics.csv"
    if not repos_path.exists():
        raise RuntimeError(
            f"Missing {repos_path}. Run `python -m src.build_charts` first."
        )
    repos = pd.read_csv(repos_path)
    if "category" not in repos.columns:
        raise RuntimeError(
            "`category` column missing — run `python -m src.build_charts` to classify."
        )
    topics = pd.read_csv(topics_path) if topics_path.exists() else None

    md = render(repos, topics)
    out_path = config.OUTPUTS_DIR / "other_breakdown.md"
    out_path.write_text(md, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    p = main()
    print(f"wrote {p}")