---
type: presentation_script
status: active
priority: p2
updated: 2026-05-24
context_policy: on_demand
owner: project
---

# 5 分鐘簡報腳本

針對大數據導論期末報告口頭簡報設計。中文逐字稿 + 速度提示。**總長 5 分鐘**。

> **記得開場前**：先把 Streamlit dashboard 打開在後台 tab，講到 demo 才不會卡。
> URL: <https://apprecenttrendanalysiz-kn98grjnkut85j6dvxzfhb.streamlit.app>

---

## 🎬 (00:00 – 00:30) 開場 + 一句話總結

> 「老師、同學好。我這份作業在問一個問題：**GitHub 上最近一個月開始紅起來的開源專案，到底長什麼樣子？AI 真的全面壓倒了嗎？以及—— 有多少其實是水分？**
>
> 我從 GitHub 抓了 999 個近月新建立的熱門 repo 做分析，會用 5 分鐘帶大家看三個發現。」

**動作**：投影片切到 README hero（dashboard 截圖）。

---

## 🎬 (00:30 – 01:30) 研究動機 + 資料

> 「資料來源是 GitHub 官方 REST API，篩選條件三個：**最近 30 天建立、stars > 10、不是 fork**。為什麼這樣設？因為要看『正在崛起的新專案』，不是看老牌大廠。
>
> 抓了 10 頁、每頁 100 筆，共 999 個 unique repo，跑了 37 分鐘、約 2000 次 API。每個 repo 都補抓了它的程式語言分布跟 topic 標籤。
>
> 對每個 repo 我做了三件事：
> 1. 清資料、算衍生欄（stars/天、fork:star 比例、存在天數）
> 2. 用**規則式分類器**歸到 9 大類（AI/ML、Web、Data、DevOps、Security、Game、CLI、Mobile、Other），優先序 AI/ML > Security > DevOps...
> 3. 做了一個**獨家加碼分析**，等下再講。」

**動作**：投影片可放 architecture diagram（從 README 複製）。

---

## 🎬 (01:30 – 03:00) 三個主要發現

### 發現 1：AI 全面壓倒 trending

> 「先看分類分布。**AI/ML 占 35.7%、Other 占 42%，兩個加起來 77.7%**。其他 7 個傳統類別 — Web、Mobile、Data、DevOps — 加起來不到 25%。
>
> Topic 排行也呼應這個：`claude-code` 52 個、`ai-agents` 43 個、`llm` 34 個、`mcp` 26 個。**前 10 名有 7 個跟 AI 直接相關**。」

**動作**：切 `outputs/figures/category_distribution.png` + `outputs/figures/top_topics.png`。

### 發現 2：被星 ≠ 被用

> 「Stars 跟 Forks 的相關係數，Pearson 0.36、Spearman 0.43 — **只是中度相關**，比想像中弱。
>
> 更有趣的：**AI/ML 類的 fork:star 比例只有 17%，是全類別最低**。Web 是 124%（前端圈愛 fork），DevOps 50%。
>
> 也就是說：AI repo 大家很愛按星，但很少 fork。**這個訊號接到我下一個發現。**」

**動作**：切 `outputs/figures/forks_vs_stars.png`。

### 發現 3 (橋接到 vibe-coding)：

> 「為什麼 stars 高、forks 低？因為其中一些根本就是**空殼專案**。」

**動作**：停頓 1 秒製造效果，準備進補章。

---

## 🎬 (03:00 – 04:30) 🚨 原創貢獻：Vibe-Coding 水分專案分析

> 「我自己設計了一個嚴格評分機制叫 **vibe-coding garbage detection**。
>
> 定義：『一個 repo 的 stars 遠超它的可見實質』。**標籤針對的是公開產出，不是作者。**
>
> 8 個訊號加權打 0 到 10 分：description 是不是空的、有沒有 license、stars 大於 1000 但 description 空（叫 famous-nothing）、fork:star 異常低、隔夜暴衝、名字含 generic AI buzzword、沒任何 topics。
>
> 999 個 repo 跑下來：**1.8% (18 個) 判為 garbage、13.2% suspicious、85% legitimate**。
>
> 但**最有趣的發現在這裡** — 我把 garbage 按 stars 級距切：
> - **≥10000 stars：0% garbage**（太紅了，藏不住）
> - **1000-5000 stars：9.9% garbage**（farming 集中區）
> - **<500 stars：1% garbage**（沒人在乎）
>
> 也就是說：**farming 有個甜蜜點，就在中段** —— 夠 impressive 上 trending，又不會被嚴格審視。
>
> 點名 Top 7 garbage 含 `cursor/cookbook`、`deepseek-ai/awesome-deepseek-agent` 這種**官方 repo** — 不是惡意，是 2026 AI 公司『先發再說』文化的縮影。」

**動作**：切 `outputs/vibe_coding_analysis.md` 截圖，或直接展示 dashboard 的 vibe section（互動）。

---

## 🎬 (04:30 – 05:00) 限制 + Demo + 結尾

> 「兩個重要限制要講：
> 1. **54.4% 的 repo 完全沒填 topic** — 這是 GitHub 生態的結構性問題，不是抓取錯誤。
> 2. vibe-coding 評分目前是『嫌疑』不是『判決』，下一步要做人工驗證計算 precision/recall。
>
> Demo 在這個 URL，**現在打開就能玩**：可以篩選分類、互動圖、調 vibe 分數。**資料每天 14:00 自動重抓**，所以你看到的永遠是『最近 30 天』。
>
> 結論一句話：**2026 GitHub trending 是 AI 主導 + 一個值得警惕的 farming 現象**。
>
> 謝謝。」

**動作**：最後一張投影片放大 demo URL + GitHub repo 連結。等發問。

---

## 🤔 可能的問答準備

| 問題 | 一句話回應 |
|---|---|
| 為什麼只抓 1000 筆？ | GitHub Search API 單一 query 硬上限是 1000 筆，再多要切 stars 或日期。對「最近熱門」這個問題來說足夠。 |
| 分類器為什麼不用 ML？ | MVP 重可解釋性。每個 repo 為什麼歸到 AI/ML 都能追到具體關鍵字。ADR-0004 有完整理由。 |
| 1.8% garbage 是高還低？ | 整體看不高，但在 1000-5000 stars 這段是 9.9%，課程作業、企業情報、技術選型常用這個區段，**每 10 個有 1 個有水分**就值得警惕。 |
| 你怎麼確定不是 false positive？ | 我有舉手承認：`awesome-*` 列表、學術 paper repo 都可能誤判。所以叫『嫌疑』不是『判決』，TASK.007 正在做人工驗證。 |
| 為什麼 watchers 等於 stars？ | GitHub Search API 不回 `subscribers_count`，這是 API 限制不是 bug。所以分析全部避開用 watchers。 |
| 跟我從 GitHub Trending 頁直接看有什麼差？ | Trending 頁是 GitHub 不透明演算法選的；我這個是**完全可重現**的篩選 + 量化分析，包含 GitHub 自己不會跟你說的 farming 結構觀察。 |

---

## 📊 投影片建議結構（10 張）

1. **封面** — 題目 + 名字 + dashboard 截圖
2. **問題 + 一句話總結** — TL;DR
3. **資料來源** — GitHub API + 篩選條件 + 999 樣本
4. **方法 architecture** — pipeline 圖
5. **發現 1** — category_distribution.png
6. **發現 2** — forks_vs_stars.png + 相關係數
7. **🚨 Vibe-coding** — 評分機制 + 1.8% 結果
8. **🎯 Garbage 甜蜜點** — stars-bucket 表
9. **限制 + demo URL**
10. **結論 + Q&A**
