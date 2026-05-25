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

> 「老師、同學好。我這份作業在問一個問題：**GitHub 上最近一個月開始紅起來的開源專案，到底長什麼樣子？AI 真的全面壓倒了嗎？以及—— 有多少 repo 公開 metadata 訊號相對於 stars 偏稀疏？**
>
> 我從 GitHub 抓了 1000 個近月新建立的熱門 repo 做分析，會用 5 分鐘帶大家看三個發現。」

**動作**：投影片切到 README hero（dashboard 截圖）。

---

## 🎬 (00:30 – 01:30) 研究動機 + 資料

> 「資料來源是 GitHub 官方 REST API，篩選條件三個：**最近 30 天建立、stars > 10、不是 fork**。為什麼這樣設？因為要看『正在崛起的新專案』，不是看老牌大廠。
>
> 抓了 10 頁、每頁 100 筆，共 1000 個 unique repo，跑了 37 分鐘、約 2000 次 API。每個 repo 都補抓了它的程式語言分布跟 topic 標籤。
>
> 對每個 repo 我做了三件事：
> 1. 清資料、算衍生欄（stars/天、fork:star 比例、存在天數）
> 2. 用**規則式分類器**歸到 10 大類（AI/ML、Web、Data、DevOps、Security、Game、CLI、Mobile、**Finance/Trading**、Other），優先序 AI/ML > Security > Finance/Trading > DevOps... — Finance/Trading 是這輪修訂從 Other 釋出的新類別。
> 3. 做了一個**獨家加碼分析**，等下再講。」

**動作**：投影片可放 architecture diagram（從 README 複製）。

---

## 🎬 (01:30 – 03:00) 三個主要發現

### 發現 1：AI 主導 + 加密交易暗流 + 長尾

> 「先看分類分布。**AI/ML 占 38.9%、Other 占 37.5%，兩個加起來 76.4%**。本輪我把分類器修訂了一輪，從 Other 桶釋出一個 **新類別 Finance/Trading，占 4.5%（45 筆）**，主要是 polymarket 和加密套利機器人聚落。其他 7 個傳統類別加起來不到 18%。
>
> Topic 排行也呼應這個：`claude-code` 52 個、`ai-agents` 43 個、`llm` 34 個、`mcp` 26 個。**前 10 名有 7 個跟 AI 直接相關**。」

**動作**：切 `outputs/figures/category_distribution.png` + `outputs/figures/top_topics.png`。

### 發現 2：fork:star 兩極化 — 被星不被 fork vs 沒人星卻爆 fork

> 「Stars 跟 Forks 的相關係數，Pearson 0.35、Spearman 0.43 — **只是中度相關**，比想像中弱。
>
> 但類別內部呈現**完全相反的兩種異常**：
>
> - **AI/ML 類 fork:star 只有 18%** — 高 stars 低 forks，「被星但少被用」的典型 vibe-coding 樣態。
>
> - **Finance/Trading 類 fork:star 高達 767%，中位數 9.9 倍** — 完全反過來，stars 才兩三百但 forks 上千。Top 5 polymarket bot 全部 forks 超過 3000，stars 只有 100-300。**沒有任何正常 repo 會有 30 倍 forks vs stars**，這個 cluster 幾乎可確定是**自動化 fork-farming**。但我無法 100% 證實，所以在報告裡寫的是『疑似』，並列出三種可能解釋。
>
> 這兩個極端剛好接到我下一個發現。」

**動作**：切 `outputs/figures/forks_vs_stars.png`。

### 發現 3 (橋接到 metadata 完整度補章)：

> 「為什麼 stars 高、forks 低？因為其中一部分 repo 的公開 metadata 訊號偏稀疏 —— 沒描述、沒 license、沒 topics。我設計了一個量化指標來測這件事。」

**動作**：停頓 1 秒製造效果，準備進補章。

---

## 🎬 (03:00 – 04:30) 🔬 原創貢獻：公開 Metadata 完整度風險評分

> 「我設計了一個量化指標叫 **Metadata Completeness Risk Score（公開 metadata 完整度風險評分）**。
>
> 定義：用 8 個訊號量化 repo 公開 metadata 相對於 stars 的稀疏程度。**指標衡量的是公開產出，不衡量作者本人，也不是對 vibe-coding 這個編程方式本身的價值評斷。**
>
> 8 個訊號加權打 0 到 10 分：description 是不是空的、有沒有 license、stars 大於 1000 但 description 空（高關注低描述）、fork:star 異常低、隔夜暴衝、名字含 generic AI buzzword、沒任何 topics。
>
> 三個 tier：5+ 為**低資訊密度**、3-4 為**待檢視**、0-2 為**訊號完整**。
>
> 1000 個 repo 跑下來：**1.8% (18 個) 落入低資訊密度 tier、13.2% 待檢視、85% 訊號完整**。
>
> 但**最有趣的發現在這裡** —— 我把低資訊密度 tier 按 stars 級距切：
> - **≥10000 stars：0%**（曝光高、受到較多檢視）
> - **1000-5000 stars：9.9%**（顯著集中區）
> - **<500 stars：1%**（關注度低，訊號不易被觀察）
>
> 也就是說：**中段 stars 區段是訊號集中區** —— 可能反映「足以上 trending、又不會被嚴格審視」的區段。請注意這是觀察性結論，不是因果推論。
>
> Top 7 名單中包含 `cursor/cookbook`、`deepseek-ai/awesome-deepseek-agent` 等**官方 repo** —— 反映的並非惡意，而是 2026 AI 公司『先發再說』的快速出貨文化在 metadata 完整度層面的體現。」

**動作**：切 `outputs/vibe_coding_analysis.md` 截圖，或直接展示 dashboard 的 metadata 完整度 section（互動）。

---

## 🎬 (04:30 – 05:00) 限制 + Demo + 結尾

> 「兩個重要限制要講：
> 1. **54.4% 的 repo 完全沒填 topic** — 這是 GitHub 生態的結構性問題，不是抓取錯誤。
> 2. Metadata 完整度評分目前是『訊號』不是『判決』，下一步要做人工驗證計算 precision/recall。
>
> Demo 在這個 URL，**現在打開就能玩**：可以篩選分類、互動圖、調 metadata 風險閾值。**資料每天 14:00 自動重抓**，所以你看到的永遠是『最近 30 天』。
>
> 結論一句話：**2026 GitHub trending 是 AI 主導 + 加密交易 fork-farming 暗流 + 一個值得警惕的「中段 stars 區段公開 metadata 訊號偏稀疏」現象**。
>
> 謝謝。」

**動作**：最後一張投影片放大 demo URL + GitHub repo 連結。等發問。

---

## 🤔 可能的問答準備

| 問題 | 一句話回應 |
|---|---|
| 為什麼只抓 1000 筆？ | GitHub Search API 單一 query 硬上限是 1000 筆，再多要切 stars 或日期。對「最近熱門」這個問題來說足夠。 |
| 分類器為什麼不用 ML？ | MVP 重可解釋性。每個 repo 為什麼歸到 AI/ML 都能追到具體關鍵字。ADR-0004 有完整理由。 |
| 1.8% 低資訊密度比例是高還低？ | 整體看不高，但在 1000-5000 stars 這段是 9.9%。課程作業、企業情報、技術選型常引用這個區段，**約每 10 個 repo 有 1 個公開 metadata 完整度偏低**，值得警惕，建議多參考 description、license、fork:star 比例等多項訊號。 |
| 你怎麼確定不是 false positive？ | 我有明確承認：`awesome-*` 列表、學術 paper repo、官方快速釋出 repo 都可能踩到訊號。所以指標定位是『訊號』不是『判決』，TASK.007 正在做人工驗證計算 precision/recall。 |
| 為什麼 watchers 等於 stars？ | GitHub Search API 不回 `subscribers_count`，這是 API 限制不是 bug。所以分析全部避開用 watchers。 |
| 跟我從 GitHub Trending 頁直接看有什麼差？ | Trending 頁是 GitHub 不透明演算法選的；我這個是**完全可重現**的篩選 + 量化分析，並提供 GitHub 介面不會呈現的公開 metadata 完整度量化指標。 |

---

## 📊 投影片建議結構（10 張）

1. **封面** — 題目 + 名字 + dashboard 截圖
2. **問題 + 一句話總結** — TL;DR
3. **資料來源** — GitHub API + 篩選條件 + 1000 樣本
4. **方法 architecture** — pipeline 圖
5. **發現 1** — category_distribution.png
6. **發現 2** — forks_vs_stars.png + 相關係數
7. **🚨 Vibe-coding** — 評分機制 + 1.8% 結果
8. **🎯 Garbage 甜蜜點** — stars-bucket 表
9. **限制 + demo URL**
10. **結論 + Q&A**
