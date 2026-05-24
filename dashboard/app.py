"""GitHub Recent Trend Analyzer — Streamlit dashboard.

Run:
    streamlit run dashboard/app.py

Designed for non-technical readers. Every chart has a plain-language explainer
and a "so what" takeaway.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src import config  # noqa: E402

st.set_page_config(
    page_title="GitHub 近月開源趨勢",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data
def load_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame | None]:
    repos = pd.read_csv(config.PROCESSED_DIR / "repos.csv")
    repos["description"] = repos["description"].fillna("")
    repos["primary_language"] = repos["primary_language"].fillna("Unknown")
    repos["created_at"] = pd.to_datetime(repos["created_at"], utc=True)
    repos["created_day"] = repos["created_at"].dt.date
    topics = pd.read_csv(config.PROCESSED_DIR / "repo_topics.csv")
    langs = pd.read_csv(config.PROCESSED_DIR / "repo_languages.csv")
    vibe_path = config.PROCESSED_DIR / "vibe_scores.csv"
    vibe = pd.read_csv(vibe_path) if vibe_path.exists() else None
    return repos, topics, langs, vibe


def section(title: str, subtitle: str = "") -> None:
    st.markdown(f"## {title}")
    if subtitle:
        st.caption(subtitle)


def explainer(plain: str, takeaway: str) -> None:
    """Render a two-part explanation: what to look at, then the surprise."""
    st.markdown(f"**📖 怎麼看：** {plain}")
    st.markdown(f"**💡 重點：** {takeaway}")


# ──────────── narrative helpers ────────────
# These turn raw numbers into Chinese descriptions so the dashboard text
# stays accurate when the daily refresh rotates the dataset.

def label_correlation(r: float) -> str:
    """Return Chinese strength label for a correlation coefficient."""
    abs_r = abs(r)
    if abs_r < 0.2:
        return "幾乎無相關"
    if abs_r < 0.4:
        return "弱" + ("正" if r > 0 else "負") + "相關"
    if abs_r < 0.7:
        return "中度" + ("正" if r > 0 else "負") + "相關"
    return "強" + ("正" if r > 0 else "負") + "相關"


def label_skew(mean: float, median: float) -> str:
    """How skewed is the distribution? Used for Stars分布解說."""
    if median <= 0:
        return "中位數為 0，平均完全被少數值主導"
    ratio = mean / median
    if ratio < 1.2:
        return "分布相對均勻，平均跟中位數差不多"
    if ratio < 2:
        return f"輕度右偏（平均約是中位數的 {ratio:.1f} 倍）"
    if ratio < 5:
        return f"明顯右偏（平均約是中位數的 {ratio:.1f} 倍），少數爆紅顯著拉抬"
    return f"極端右偏（平均約是中位數的 {ratio:.1f} 倍），極少數超級爆紅完全主導"


def label_dominance(top_pct: float, second_pct: float = 0.0) -> str:
    """Describe how dominant the leading category/language is."""
    gap = top_pct - second_pct
    if top_pct >= 0.5:
        return "壓倒性主導"
    if top_pct >= 0.35 and gap >= 0.1:
        return "明顯領先"
    if gap < 0.05:
        return "與第二名並列"
    return "領先"


def language_diversity(repos_df: pd.DataFrame, lang: str) -> int:
    """How many distinct categories does this language appear in?"""
    return repos_df[repos_df["primary_language"] == lang]["category"].nunique()


def most_diverse_language(repos_df: pd.DataFrame, min_repos: int = 10) -> str | None:
    """Language with the highest category spread (entropy proxy)."""
    counts = repos_df["primary_language"].value_counts()
    eligible = counts[counts >= min_repos].index
    if len(eligible) == 0:
        return None
    return max(eligible, key=lambda lng: language_diversity(repos_df, lng))


def most_concentrated_language(repos_df: pd.DataFrame, min_repos: int = 5) -> tuple[str, str] | None:
    """Return (lang, category) where lang has ≥90% repos in one category."""
    for lng in repos_df["primary_language"].value_counts().index:
        sub = repos_df[repos_df["primary_language"] == lng]
        if len(sub) < min_repos:
            continue
        top_cat = sub["category"].value_counts()
        if top_cat.iloc[0] / len(sub) >= 0.9:
            return lng, top_cat.index[0]
    return None


repos, topics, langs, vibe = load_data()

st.title("📊 GitHub 近一個月開源趨勢分析")
st.markdown(
    f"_資料區間：最近 30 天新建立、Stars > 10、排除 fork 的公開 repository · "
    f"樣本：**{len(repos)}** 個 repo · 抓取日：{repos['created_at'].max().date()}_"
)

st.info(
    "**這個專案在做什麼？**\n\n"
    "我們從 GitHub 抓出最近一個月新建立且開始受到關注的開源專案，"
    "分析它們的程式語言、主題、熱度，以及一個獨家觀察——"
    "**到底有多少是 vibe-coding（即興 AI 產出）的水分專案。**"
)

st.markdown("---")

# ──────────── KEY METRICS ────────────
section("🔢 一眼看懂")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("樣本 repos", f"{len(repos)}")
c2.metric("中位數 stars", f"{int(repos['stars'].median()):,}")
c3.metric("最熱專案 stars", f"{int(repos['stars'].max()):,}")
c4.metric("最熱專案/天", f"{int(repos['stars_per_day'].max()):,}")
top_lang = repos["primary_language"].mode().iloc[0]
c5.metric("最常用語言", top_lang)

st.markdown("---")

# ──────────── LANGUAGES ────────────
section("1️⃣ 熱門程式語言", "前 10 名主要程式語言")
lang_counts = repos["primary_language"].value_counts().head(10).reset_index()
lang_counts.columns = ["語言", "repo 數"]
fig1 = px.bar(lang_counts, x="repo 數", y="語言", orientation="h",
              color="repo 數", color_continuous_scale="Blues",
              text="repo 數")
fig1.update_layout(yaxis={"categoryorder": "total ascending"}, height=400,
                   showlegend=False, coloraxis_showscale=False)
st.plotly_chart(fig1, use_container_width=True)
_top1_lang = lang_counts.iloc[0]["語言"]
_top1_lang_pct = lang_counts.iloc[0]["repo 數"] / len(repos)
_top2_lang_pct = lang_counts.iloc[1]["repo 數"] / len(repos) if len(lang_counts) > 1 else 0
_top3_share = lang_counts.head(3)["repo 數"].sum() / len(repos)
_lang_dom = label_dominance(_top1_lang_pct, _top2_lang_pct)
explainer(
    "每一條代表一種程式語言在近月熱門新專案中出現的次數。"
    "愈長代表該語言的開發者愈活躍。",
    f"**{_top1_lang}** 以 {_top1_lang_pct*100:.0f}% 占比{_lang_dom}。"
    f"前 3 名（{_top1_lang}／{lang_counts.iloc[1]['語言']}／{lang_counts.iloc[2]['語言']}）"
    f"加總占約 **{_top3_share*100:.0f}%**，"
    + (
        "顯示 trending 高度集中在少數主流語言。"
        if _top3_share > 0.5
        else "顯示熱門語言分散度頗高，並非由少數語言壟斷。"
    )
)

st.markdown("---")

# ──────────── TOPICS ────────────
section("2️⃣ 熱門主題標籤", "GitHub topic 出現頻率前 20 名")
top_topics = topics["topic"].value_counts().head(20).reset_index()
top_topics.columns = ["topic", "出現次數"]
fig2 = px.bar(top_topics, x="出現次數", y="topic", orientation="h",
              color="出現次數", color_continuous_scale="Viridis", text="出現次數")
fig2.update_layout(yaxis={"categoryorder": "total ascending"}, height=600,
                   showlegend=False, coloraxis_showscale=False)
st.plotly_chart(fig2, use_container_width=True)
_repos_with_topics = topics["repo_id"].nunique()
_no_topic_pct = (1 - _repos_with_topics / len(repos)) * 100

_ai_keywords = {"ai", "ai-agents", "ai-agent", "llm", "llms", "claude", "claude-code",
                "gpt", "codex", "mcp", "agent", "agents", "deep-learning",
                "machine-learning", "neural", "transformer", "rag"}
_top20_set = set(top_topics["topic"].head(20))
_ai_in_top20 = _top20_set & _ai_keywords
_ai_density = len(_ai_in_top20)
_top1_topic = top_topics.iloc[0]["topic"]
_top1_is_ai = _top1_topic in _ai_keywords

explainer(
    f"topic 是專案作者自己貼的標籤。出現次數高代表這個主題正在發燒。"
    f"注意：topic 是選填欄位，有 **{_no_topic_pct:.1f}%** 的 repo 完全沒貼任何 topic。",
    f"前 20 名 topic 中有 **{_ai_density} 個與 AI 直接相關**"
    f"（{'、'.join(sorted(_ai_in_top20)[:5])}{'…' if len(_ai_in_top20) > 5 else ''}）。"
    + (
        f"冠軍 `{_top1_topic}` 本身就是 AI 主題，"
        f"印證當前 LLM / AI agent 應用持續爆炸。"
        if _top1_is_ai
        else f"冠軍 `{_top1_topic}` 並非 AI 主題，"
              f"但 AI topic 仍占前段班，整體偏 AI 但不獨大。"
    )
)

st.markdown("---")

# ──────────── STARS DISTRIBUTION ────────────
section("3️⃣ Stars 分布", "看熱度是否集中在少數明星專案")
fig3 = px.histogram(repos, x="stars", nbins=40, log_y=True,
                    color_discrete_sequence=["#1f77b4"])
fig3.update_layout(height=400, yaxis_title="repo 數（對數）", xaxis_title="Stars")
st.plotly_chart(fig3, use_container_width=True)
mean_s = int(repos["stars"].mean())
median_s = int(repos["stars"].median())
_skew_label = label_skew(mean_s, median_s)
explainer(
    "X 軸是 stars 數量，Y 軸是該區間內的 repo 數（對數座標——意思是相隔一格代表 10 倍差距）。"
    "分布愈往右拉得長，代表少數爆紅專案拉開差距。",
    f"平均 **{mean_s:,}** ／ 中位數 **{median_s:,}** —— {_skew_label}。"
    + (
        "用中位數寫結論會比平均數更貼近大多數 repo 的真實情況。"
        if mean_s / max(median_s, 1) > 1.5
        else "平均與中位數接近，兩個指標的結論差不多。"
    )
)

st.markdown("---")

# ──────────── FORKS VS STARS ────────────
section("4️⃣ Stars vs Forks 散佈圖", "被收藏 vs 被複製延伸的相關性")
fig4 = px.scatter(repos, x="stars", y="forks", log_x=True, log_y=True,
                  hover_data=["full_name", "primary_language", "category"],
                  color="category", opacity=0.6, height=550)
fig4.update_layout(xaxis_title="Stars（對數）", yaxis_title="Forks（對數）")
st.plotly_chart(fig4, use_container_width=True)
pearson = repos[["stars", "forks"]].corr().iloc[0, 1]
spearman = repos[["stars", "forks"]].corr(method="spearman").iloc[0, 1]
_pearson_lbl = label_correlation(pearson)
_spearman_lbl = label_correlation(spearman)
_corr_callout = (
    "**強相關**——star 高的 repo 幾乎一定 fork 也高，兩個指標可以互相替代。"
    if abs(pearson) >= 0.7
    else (
        f"**{_pearson_lbl}**——星很多不一定就有人 fork。"
        if abs(pearson) >= 0.2
        else "**幾乎沒有線性關係**——stars 跟 forks 是兩個獨立指標，不能互相推論。"
    )
)
explainer(
    "每個點是一個 repo。X 軸是 stars，Y 軸是 forks，兩軸都是對數。"
    "顏色代表分類。對角線方向走就代表 stars 和 forks 一起長。",
    f"相關係數 Pearson **{pearson:.2f}**（{_pearson_lbl}）／ "
    f"Spearman **{spearman:.2f}**（{_spearman_lbl}）——{_corr_callout} "
    f"特別觀察 AI/ML 類別會發現有「stars 高但 forks 偏低」的子群，"
    f"後面 vibe-coding 章節會追究這個「被星但少被用」現象。"
)

st.markdown("---")

# ──────────── CATEGORY DISTRIBUTION ────────────
section("5️⃣ 專案分類分布", "用規則式分類器歸類後的結果")
cat_counts = repos["category"].value_counts().reset_index()
cat_counts.columns = ["分類", "repo 數"]
fig5 = px.bar(cat_counts, x="分類", y="repo 數", color="repo 數",
              color_continuous_scale="Reds", text="repo 數")
fig5.update_layout(height=400, showlegend=False, coloraxis_showscale=False)
st.plotly_chart(fig5, use_container_width=True)
total = len(repos)

def _cat_pct(cat: str) -> float:
    row = cat_counts.loc[cat_counts["分類"] == cat, "repo 數"]
    return float(row.iloc[0]) / total * 100 if not row.empty else 0.0

ai_pct = _cat_pct("AI/ML")
other_pct = _cat_pct("Other")
top2_pct = ai_pct + other_pct
rest_pct = 100 - top2_pct
top1_cat = cat_counts.iloc[0]["分類"]
top1_pct = cat_counts.iloc[0]["repo 數"] / total * 100

if top2_pct > 70:
    _cat_shape = (
        f"**AI/ML ({ai_pct:.0f}%) 與 Other ({other_pct:.0f}%) 合計 {top2_pct:.0f}%**——"
        f"當前 trending 非常雙峰：要嘛是 AI、要嘛是無法歸類的長尾。"
        f"其餘 7 個傳統類別加起來只有 {rest_pct:.0f}%。"
    )
elif top1_pct > 50:
    _cat_shape = (
        f"**{top1_cat} 一家獨大，占 {top1_pct:.0f}%**。"
        f"其他 8 個類別瓜分剩下的 {100-top1_pct:.0f}%。"
    )
else:
    _cat_shape = (
        f"分布相對均衡：第一名 **{top1_cat}** 也只占 {top1_pct:.0f}%，"
        f"AI/ML+Other 合計 {top2_pct:.0f}%。"
    )

explainer(
    "我們用關鍵字規則把每個 repo 分到 9 大類別。例如 description 出現 `llm`、`agent` 就歸 AI/ML，"
    "出現 `docker`、`kubernetes` 就歸 DevOps。優先順序是 AI/ML > Security > DevOps > Data > Web > "
    "Mobile > Game > CLI/Tooling > Other。",
    _cat_shape,
)

st.markdown("---")

# ──────────── SANKEY: LANGUAGE → CATEGORY ────────────
section("5️⃣b 語言 ↔ 分類 流向圖", "看哪種語言主要流向哪個類別")

_top_langs = repos["primary_language"].value_counts().head(10).index.tolist()
_lang_grouped = repos["primary_language"].where(
    repos["primary_language"].isin(_top_langs), "其他語言"
)
_matrix = pd.crosstab(_lang_grouped, repos["category"])
_langs = _matrix.index.tolist()
_cats = _matrix.columns.tolist()
_nodes = _langs + _cats
_idx = {name: i for i, name in enumerate(_nodes)}
_src, _tgt, _val = [], [], []
for lang in _langs:
    for cat in _cats:
        v = int(_matrix.loc[lang, cat])
        if v > 0:
            _src.append(_idx[lang])
            _tgt.append(_idx[cat])
            _val.append(v)

fig_sankey = go.Figure(go.Sankey(
    node=dict(
        label=_nodes,
        pad=18,
        thickness=22,
        color=["#1f77b4"] * len(_langs) + ["#ff7f0e"] * len(_cats),
    ),
    link=dict(source=_src, target=_tgt, value=_val),
))
fig_sankey.update_layout(height=560, font_size=12,
                         margin=dict(l=10, r=10, t=10, b=10))
st.plotly_chart(fig_sankey, use_container_width=True)
_diverse = most_diverse_language(repos, min_repos=10)
_concentrated = most_concentrated_language(repos, min_repos=5)
_insights: list[str] = []
if _diverse:
    _n_cats = language_diversity(repos, _diverse)
    _insights.append(
        f"**{_diverse}** 流向最分散——同一個語言出現在 **{_n_cats}** 個不同類別，"
        f"是這份資料的「萬用語言」。"
    )
if _concentrated:
    _lng, _cat = _concentrated
    _insights.append(
        f"**{_lng}** 流向最集中——它的 repo 有 90% 以上落在 **{_cat}** 一個類別。"
    )
if not _insights:
    _insights.append("樣本中沒有特別突出的「分散」或「集中」型語言，整體流向平均。")
explainer(
    "左邊是程式語言（前 10 + 其他語言合併），右邊是 9 大分類。"
    "線寬代表「這種語言被歸到這個類別」的 repo 數量。hover 看精確數字。",
    " ".join(_insights),
)

st.markdown("---")

# ──────────── CATEGORY HEAT ────────────
section("6️⃣ 各類別平均熱度比較", "看哪個類別比較容易爆")
cat_heat = repos.groupby("category").agg(
    repos=("id", "count"),
    mean_stars=("stars", "mean"),
    median_stars=("stars", "median"),
    mean_forks=("forks", "mean"),
    mean_spd=("stars_per_day", "mean"),
).reset_index().sort_values("mean_stars", ascending=False)
fig6 = px.bar(cat_heat, x="category", y="mean_stars",
              color="mean_spd", color_continuous_scale="Plasma",
              hover_data=["repos", "median_stars", "mean_forks"],
              labels={"mean_stars": "平均 Stars", "mean_spd": "平均 stars/天",
                      "category": "分類"})
fig6.update_layout(height=420)
st.plotly_chart(fig6, use_container_width=True)
st.dataframe(cat_heat.round(1), use_container_width=True, hide_index=True)
_hottest_cat = cat_heat.iloc[0]
_hottest_name = _hottest_cat["category"]
_hottest_mean = _hottest_cat["mean_stars"]
_hottest_median = _hottest_cat["mean_stars"]  # placeholder; use real median below
_hottest_median = float(cat_heat.iloc[0]["median_stars"])
_outlier_skew = _hottest_mean / max(_hottest_median, 1)
_top_repo_in_hottest = (
    repos[repos["category"] == _hottest_name]
    .sort_values("stars", ascending=False)
    .iloc[0]
)

_highest_median = cat_heat.loc[cat_heat["median_stars"].idxmax()]
_highest_forks_cat = cat_heat.loc[cat_heat["mean_forks"].idxmax()]

_insights = []
if _outlier_skew > 2:
    _insights.append(
        f"**{_hottest_name}** 平均 stars 最高（{_hottest_mean:.0f}），"
        f"但被 `{_top_repo_in_hottest['full_name']}`（{_top_repo_in_hottest['stars']:,}⭐）"
        f"這個極端值拉抬 —— 看中位數 {_hottest_median:.0f} 較中肯。"
    )
else:
    _insights.append(
        f"**{_hottest_name}** 平均 stars 最高（{_hottest_mean:.0f}），"
        f"中位數也有 {_hottest_median:.0f}，整類別都偏熱。"
    )

if _highest_median["category"] != _hottest_name:
    _insights.append(
        f"**{_highest_median['category']}** 中位數最高（{_highest_median['median_stars']:.0f}），"
        f"樣本 {int(_highest_median['repos'])} 個——少但精。"
    )

_insights.append(
    f"**{_highest_forks_cat['category']}** 平均 forks 最高 "
    f"({_highest_forks_cat['mean_forks']:.0f})，"
    f"fork 文化最旺。"
)

explainer(
    "棒高代表那一類別的平均 stars 高；顏色深淺代表平均每天新增 stars 速度（愈深愈快）。"
    "下面表格列出每個類別的 repo 數、平均值、中位數，可以對照看「樣本夠不夠多」。",
    " ".join(_insights),
)

st.markdown("---")

# ──────────── DAILY ────────────
section("7️⃣ 每日新增熱門 repo 數", "看 30 天內哪幾天突然出現很多熱門新專案")
daily = repos.groupby("created_day").size().reset_index(name="新增 repo 數")
fig7 = px.line(daily, x="created_day", y="新增 repo 數", markers=True)
fig7.update_layout(height=400, xaxis_title="建立日期", yaxis_title="當日新增的熱門 repo")
st.plotly_chart(fig7, use_container_width=True)
peak_day = daily.loc[daily["新增 repo 數"].idxmax()]
explainer(
    "每個點是該日有幾個「最後熱門起來」的 repo 在當天建立。"
    "波動會反映 GitHub 一週節律（週末通常較少）、特定事件（如重大發表會）。",
    f"高峰日是 **{peak_day['created_day']}** 共 **{int(peak_day['新增 repo 數'])}** 個，"
    f"低谷日只有 {int(daily['新增 repo 數'].min())} 個。"
    f"整體看不出明顯爆量，代表熱門專案是「持續產出」而不是集中在某一波發表會。"
)

st.markdown("#### 同一張圖按類別拆開")
daily_cat = repos.groupby(["created_day", "category"]).size().reset_index(name="新增 repo 數")
_cat_order = repos["category"].value_counts().index.tolist()
fig_stack = px.bar(
    daily_cat, x="created_day", y="新增 repo 數", color="category",
    category_orders={"category": _cat_order},
    color_discrete_sequence=px.colors.qualitative.Set2,
)
fig_stack.update_layout(
    height=420, xaxis_title="建立日期", yaxis_title="當日新增的熱門 repo",
    barmode="stack", legend_title="分類",
)
st.plotly_chart(fig_stack, use_container_width=True)
explainer(
    "把上面的折線圖按類別拆開堆疊。可以看出每天的「組成結構」而不只是總量。",
    "AI/ML 與 Other 兩個棕色 / 藍色塊幾乎每天都最厚，呼應雙峰結構結論。"
    "Web 與 Mobile 等小類別有些日子完全沒新熱門 repo —— 樣本量小、變動大。"
)

st.markdown("---")

# ──────────── VIBE CODING GARBAGE ────────────
section("🚨 原創發現：Vibe-Coding 水分專案分析",
        "本專案獨家——用嚴格規則辨識「星很高但內容空虛」的 repo")

if vibe is not None:
    st.markdown(
        "**什麼是 vibe-coding garbage？**  "
        "= 一個 repo 的 stars 遠遠超過它的「可見實質」。"
        "我們設計 8 個訊號（description 空、license 空、stars 暴衝但 fork 極少、名字是 generic AI buzzword……）"
        "為每個 repo 打 0-10 分。"
    )

    threshold = st.slider(
        "🎚️ Garbage 判定閾值（分數 ≥ 此值即判為 garbage）",
        min_value=3, max_value=8, value=5, step=1,
        help="預設 5（報告採用值）。調高 → 標準變嚴、garbage 變少；調低 → 標準變鬆、garbage 變多。"
              "Suspicious 範圍永遠是 3 分以上 garbage 以下。",
    )

    def _tier_at(score: int, thr: int) -> str:
        if score >= thr:
            return "garbage"
        if score >= 3:
            return "suspicious"
        return "legitimate"

    vibe_dyn = vibe.copy()
    vibe_dyn["tier"] = vibe_dyn["score"].apply(lambda s: _tier_at(int(s), threshold))

    tier_counts = vibe_dyn["tier"].value_counts().reindex(
        ["garbage", "suspicious", "legitimate"]).fillna(0).astype(int)

    # Show delta from default-threshold (5) so user sees how their slider moves things.
    if threshold != 5:
        default_garbage = int((vibe["score"] >= 5).sum())
        delta = int(tier_counts["garbage"]) - default_garbage
        delta_str = f"{delta:+d} vs 預設"
    else:
        delta_str = "預設"

    c1, c2, c3 = st.columns(3)
    c1.metric("🟢 Legitimate", f"{tier_counts['legitimate']}",
              f"{tier_counts['legitimate']/len(vibe_dyn)*100:.1f}%")
    c2.metric("🟡 Suspicious", f"{tier_counts['suspicious']}",
              f"{tier_counts['suspicious']/len(vibe_dyn)*100:.1f}%")
    c3.metric("🔴 Garbage", f"{tier_counts['garbage']}", delta_str,
              delta_color="off" if threshold == 5 else "inverse")

    vibe = vibe_dyn  # downstream sections all use the recomputed tier

    st.markdown("### 哪個 stars 級距藏最多 garbage？")
    buckets = [
        ("≥10000", vibe["stars"] >= 10000),
        ("5000-9999", (vibe["stars"] >= 5000) & (vibe["stars"] < 10000)),
        ("1000-4999", (vibe["stars"] >= 1000) & (vibe["stars"] < 5000)),
        ("500-999", (vibe["stars"] >= 500) & (vibe["stars"] < 1000)),
        ("100-499", (vibe["stars"] >= 100) & (vibe["stars"] < 500)),
    ]
    bucket_rows = []
    for label, mask in buckets:
        sub = vibe[mask]
        if sub.empty:
            continue
        bucket_rows.append({
            "stars 級距": label,
            "樣本數": len(sub),
            "garbage 數": int((sub["tier"] == "garbage").sum()),
            "garbage %": round((sub["tier"] == "garbage").sum() / len(sub) * 100, 1),
        })
    bucket_df = pd.DataFrame(bucket_rows)
    fig_b = px.bar(bucket_df, x="stars 級距", y="garbage %", text="garbage %",
                   color="garbage %", color_continuous_scale="Reds")
    fig_b.update_layout(height=400, showlegend=False, coloraxis_showscale=False)
    st.plotly_chart(fig_b, use_container_width=True)
    st.dataframe(bucket_df, use_container_width=True, hide_index=True)

    # Only highlight buckets with a meaningful sample size (≥20),
    # so a 50% rate over 2 repos doesn't masquerade as the headline.
    _significant = bucket_df[bucket_df["樣本數"] >= 20]
    if not _significant.empty:
        _max_row = _significant.loc[_significant["garbage %"].idxmax()]
        _min_row = _significant.loc[_significant["garbage %"].idxmin()]
        if _max_row["garbage %"] > _min_row["garbage %"] * 2:
            st.success(
                f"🎯 **核心發現**：garbage 比例最高在 "
                f"**{_max_row['stars 級距']} stars 級距（{_max_row['garbage %']}% — "
                f"{int(_max_row['garbage 數'])}/{int(_max_row['樣本數'])}）**；"
                f"最低在 **{_min_row['stars 級距']}（{_min_row['garbage %']}%）**。"
                f"差距 {_max_row['garbage %']/max(_min_row['garbage %'], 0.1):.1f}× —— "
                f"farming 在 stars 分布上**不是均勻分布**，集中在「夠 impressive 上 trending，"
                f"又不會被嚴格審視」的中段。"
            )
        else:
            st.info(
                f"📊 各 stars 級距的 garbage 比例相對均勻，"
                f"最高 {_max_row['stars 級距']}（{_max_row['garbage %']}%）／"
                f"最低 {_min_row['stars 級距']}（{_min_row['garbage %']}%），"
                f"沒有明顯的「farming 甜蜜點」現象。"
            )
    else:
        st.warning("樣本量不足以可靠評估各 stars 級距的差異。")

    st.markdown("### Top 15 最可疑專案")
    top_vibe = vibe.head(15)[
        ["full_name", "stars", "forks", "age_days", "score", "tier", "reasons"]
    ].copy()
    top_vibe.columns = ["repo", "stars", "forks", "天數", "分數", "tier", "扣分原因"]
    st.dataframe(top_vibe, use_container_width=True, hide_index=True)

    st.markdown("### Famous-Nothing — 高 stars + 完全沒描述")
    fn = vibe[(vibe["stars"] > 1000) & (vibe["desc_len"] == 0)].sort_values(
        "stars", ascending=False)
    if not fn.empty:
        fn_disp = fn[["full_name", "stars", "forks", "age_days",
                      "primary_language", "license"]].copy()
        fn_disp.columns = ["repo", "stars", "forks", "天數", "語言", "license"]
        st.dataframe(fn_disp, use_container_width=True, hide_index=True)
        # Detect "official-looking" accounts: owner is a known company / org
        # (heuristic: owner appears in the org-prefix portion and has common
        # corporate keywords or is on the curated list).
        _known_orgs = {"cursor", "openai", "anthropic", "deepseek-ai", "vercel",
                       "vercel-labs", "google", "microsoft", "meta", "huggingface",
                       "perplexityai", "datawhalechina"}
        fn_disp["owner"] = fn_disp["repo"].str.split("/").str[0]
        _official = fn_disp[fn_disp["owner"].isin(_known_orgs) |
                            fn_disp["owner"].str.contains("-ai$|^ai-", regex=True, case=False)]
        if not _official.empty:
            _examples = ", ".join(f"`{r}`" for r in _official["repo"].head(3))
            st.warning(
                f"這 **{len(fn)}** 個 repo 每個都 stars >1000 但連 description 都不寫一行。"
                f"其中 **{len(_official)} 個是官方 / 知名組織帳號**（例如 {_examples}）——"
                f"並非惡意，而是 AI 公司「先發再說」的快速出貨文化縮影。"
            )
        else:
            st.warning(
                f"這 **{len(fn)}** 個 repo 每個都 stars >1000 但連 description 都不寫一行。"
                f"這次 snapshot 沒有官方大廠 repo 上榜，全是個人 / 小眾組織。"
            )

else:
    st.error("沒讀到 vibe_scores.csv。請先跑 `python -m src.analyze_vibe`。")

st.markdown("---")

# ──────────── INTERACTIVE EXPLORER ────────────
section("🔍 自己探索資料", "依條件篩選 999 個 repo")
with st.sidebar:
    st.markdown("### 篩選條件")
    sel_cat = st.multiselect("分類", options=sorted(repos["category"].unique()),
                             default=sorted(repos["category"].unique()))
    sel_lang = st.multiselect("程式語言（前 15）",
                              options=repos["primary_language"].value_counts().head(15).index.tolist())
    min_stars = st.slider("最低 stars", 0, int(repos["stars"].max()), 0, step=50)
    sort_by = st.selectbox("排序依據", ["stars", "stars_per_day", "forks", "age_days"])

mask = repos["category"].isin(sel_cat) & (repos["stars"] >= min_stars)
if sel_lang:
    mask &= repos["primary_language"].isin(sel_lang)
filtered = repos[mask].sort_values(sort_by, ascending=False)

st.markdown(f"**符合條件：{len(filtered)} / {len(repos)} 個 repo**")
display_cols = ["full_name", "stars", "forks", "stars_per_day", "age_days",
                "primary_language", "category", "description"]
st.dataframe(
    filtered[display_cols].head(100),
    use_container_width=True, hide_index=True,
    column_config={
        "full_name": st.column_config.LinkColumn(
            "repo", display_text=r".*/(.*)$",
            help="點擊跳到 GitHub"),
        "stars_per_day": st.column_config.NumberColumn(format="%.1f"),
    },
)

st.markdown("---")
st.caption(
    "資料來源：GitHub REST API（Search + Languages + Topics）· "
    "規則式分類器，非 ML 模型 · "
    "限制：watchers 欄等於 stars（GitHub API 已知限制）；54% repo 無 topics；單一分類 MVP · "
    "原始程式碼：`src/`、`dashboard/app.py`、`outputs/`"
)