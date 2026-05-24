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
explainer(
    "每一條代表一種程式語言在近月熱門新專案中出現的次數。"
    "愈長代表該語言的開發者愈活躍。",
    f"**{lang_counts.iloc[0]['語言']}** 是當之無愧的冠軍，"
    f"反映 AI 工具鏈與資料科學的主流地位。前 3 名加總占了約 "
    f"{(lang_counts.head(3)['repo 數'].sum() / len(repos) * 100):.0f}% 的新熱門專案。"
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
explainer(
    "topic 是專案作者自己貼的標籤。出現次數高代表這個主題正在發燒。"
    "注意：topic 是選填欄位，有 **54.4%** 的 repo 完全沒貼任何 topic。",
    f"`{top_topics.iloc[0]['topic']}` 跟 `ai-agents` 等 AI 相關 topic 霸榜，"
    "印證 2026 上半年仍是 LLM／AI agent 應用爆炸期。"
    "注意 `trading-bot` / `polymarket` 出現也提示金融自動化的小型復興。"
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
explainer(
    "X 軸是 stars 數量，Y 軸是該區間內的 repo 數（對數座標——意思是相隔一格代表 10 倍差距）。"
    "分布愈往右拉得長，代表少數爆紅專案拉開差距。",
    f"平均數 **{mean_s:,}** 但中位數只有 **{median_s:,}**——"
    f"差距 **{mean_s/median_s:.1f}x**。代表少數爆紅專案大幅拉抬平均，"
    f"絕大多數熱門 repo 其實 stars 並沒有那麼誇張。"
    f"報告寫結論用「中位數」會比「平均數」更貼近真實。"
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
explainer(
    "每個點是一個 repo。X 軸是 stars，Y 軸是 forks，兩軸都是對數。"
    "顏色代表分類。對角線方向走就代表 stars 和 forks 一起長。",
    f"相關係數 Pearson **{pearson:.2f}** / Spearman **{spearman:.2f}**——"
    f"**中度正相關**，不是強相關。"
    f"也就是：星很多不一定就有人 fork。"
    f"特別觀察 AI/ML 類別（顏色），會發現有明顯一群「stars 高但 forks 偏低」的點，"
    f"這就是後面 vibe-coding 章節要追究的「被星但少被用」現象。"
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
ai_pct = (cat_counts.loc[cat_counts["分類"] == "AI/ML", "repo 數"].iloc[0] / total * 100)
other_pct = (cat_counts.loc[cat_counts["分類"] == "Other", "repo 數"].iloc[0] / total * 100)
explainer(
    "我們用關鍵字規則把每個 repo 分到 9 大類別。例如 description 出現 `llm`、`agent` 就歸 AI/ML，"
    "出現 `docker`、`kubernetes` 就歸 DevOps。優先順序是 AI/ML > Security > DevOps > Data > Web > "
    "Mobile > Game > CLI/Tooling > Other。",
    f"**AI/ML ({ai_pct:.0f}%) 與 Other ({other_pct:.0f}%) 合計 {ai_pct+other_pct:.0f}%**——"
    f"當前 trending 非常雙峰：要嘛是 AI，要嘛是根本沒打標籤、無法歸類的長尾。"
    f"其餘 7 個類別加起來只有不到 25%。"
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
explainer(
    "棒高代表那一類別的平均 stars 高；顏色深淺代表平均每天新增 stars 速度（愈深愈快）。"
    "下面表格列出每個類別的 repo 數、平均值、中位數，可以對照看「樣本夠不夠多」。",
    "**Game** 類別的平均 stars 異常高，主要被 `antirez/ds4`（C 語言推理引擎）這個極端值拉抬，"
    "點開表格看「中位數」會比較中肯。**Data** 類別樣本只有 12 個但中位數最高（316），代表少而精。"
    "**Web** 平均 forks 高達 410——前端圈的 fork 文化最旺。"
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

st.markdown("---")

# ──────────── VIBE CODING GARBAGE ────────────
section("🚨 原創發現：Vibe-Coding 水分專案分析",
        "本專案獨家——用嚴格規則辨識「星很高但內容空虛」的 repo")

if vibe is not None:
    st.markdown(
        "**什麼是 vibe-coding garbage？**  "
        "= 一個 repo 的 stars 遠遠超過它的「可見實質」。"
        "我們設計 8 個訊號（description 空、license 空、stars 暴衝但 fork 極少、名字是 generic AI buzzword……）"
        "為每個 repo 打 0-10 分。**5 分以上判定為 garbage。**"
    )

    tier_counts = vibe["tier"].value_counts().reindex(
        ["garbage", "suspicious", "legitimate"]).fillna(0).astype(int)
    c1, c2, c3 = st.columns(3)
    c1.metric("🟢 Legitimate", f"{tier_counts['legitimate']}",
              f"{tier_counts['legitimate']/len(vibe)*100:.1f}%")
    c2.metric("🟡 Suspicious", f"{tier_counts['suspicious']}",
              f"{tier_counts['suspicious']/len(vibe)*100:.1f}%")
    c3.metric("🔴 Garbage", f"{tier_counts['garbage']}",
              f"{tier_counts['garbage']/len(vibe)*100:.1f}%", delta_color="inverse")

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
    st.success(
        "🎯 **核心發現**：garbage 高度集中在 **1000-4999 stars 級距（9.9%）**。"
        "太高（≥10000）有人盯著看，找不到；太低（<500）沒人在乎，找不到。"
        "中段是 farming 的甜蜜點——「夠 impressive 上 trending，又不會被嚴格審視」。"
    )

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
        st.warning(
            f"這 **{len(fn)}** 個 repo 每個都 stars >1000 但連 description 都不寫一行。"
            "其中不乏 `cursor/cookbook`、`deepseek-ai/awesome-deepseek-agent` 這種"
            "官方帳號——並非惡意，而是 2026 AI 公司「先發再說」的快速出貨文化縮影。"
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