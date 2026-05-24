# GitHub 近一個月新建立熱門開源專案之技術分類與趨勢分析

> 以程式語言、Topics、Stars、Forks 與規則式分類為核心
> 補章：Vibe-Coding 水分專案嚴格檢測

_資料區間：2026-04-24 ~ 2026-05-24（30 天）· 樣本：999 個 repo_

---

## 摘要

本研究蒐集 GitHub 最近 30 天新建立、Stars 大於 10、非 fork 的公開 repository 共 **999 筆**，分析其程式語言、主題標籤、熱度指標與類別分布。

主要發現：
1. **語言**：Python (34%)、TypeScript (21%)、JavaScript (8%) 占據前三，反映 AI 工具鏈與 Web 生態的雙重活躍。
2. **主題**：`claude-code` (52)、`ai-agents` (43)、`llm` (34) 等 AI 相關 topic 霸榜；但 **54.4% repo 完全未填 topic**。
3. **類別**：經規則式分類，**AI/ML (35.7%) 與 Other (42.0%) 合占 77.7%**，2026 上半年 trending 呈現雙峰結構。
4. **相關性**：Stars↔Forks 為中度正相關（Pearson 0.36 / Spearman 0.43），非強相關；AI/ML 類 fork:star 僅 17%，遠低於 Web 的 124%，呈「被星但少被用」模式。
5. **補章原創貢獻**：以 8 訊號嚴格評分機制檢測「vibe-coding 水分專案」，發現 1.8% (18 repos) 被判為 garbage，集中於 1000-4999 stars 級距 (9.9%) —— farming 的「甜蜜點」。

本研究使用 Python + pandas + matplotlib 完成，所有程式碼、資料集與互動 dashboard 公開於 [GitHub repo](https://github.com/aionyx02/github_recent_trend_analysiz)。

---

## 1. 研究動機與背景

GitHub 是全球最大的開源協作平台，新興技術與框架往往先在此公開後才擴散至整個產業。Repository 的 Stars、Forks、Topics 雖然不能完全代表程式碼品質，但作為「社群關注訊號」具有獨特的觀察價值。

本研究選擇「最近 30 天新建立」這個時間切片，目的不是評估專案品質，而是回答 **「2026 上半年開源社群當前在關注什麼？」**。透過明確的篩選條件（stars > 10、排除 fork、限縮時間範圍），我們將分析複雜度與資料量控制在課程作業可行範圍內，同時保留足夠的代表性。

額外動機：近年 AI 程式產生工具（GitHub Copilot、Claude Code、Cursor、Codex）已大量改變開源 repo 的產出方式。**「vibe-coding」**（即以自然語言指令 AI 產出程式碼，作者不一定深入理解）成為新興現象，但伴隨而來的是「stars 很高、實質很少」的水分專案 —— 本研究額外設計嚴格評分機制檢測此類專案。

---

## 2. 研究問題

| 編號 | 研究問題 | 章節 |
|---|---|---|
| **RQ1** | 最近一個月新建立的熱門 repo 中，最常見的程式語言是哪些？ | §7.1 |
| **RQ2** | 最近一個月最常見的 GitHub topics 是哪些？ | §7.2 |
| **RQ3** | 哪些專案在短時間內獲得較高關注？ | §7.3 |
| **RQ4** | Stars 與 Forks 是否具有相關性？ | §7.4 |
| **RQ5** | 不同類別的專案熱度是否不同？ | §7.5 |
| **RQ6** | 最近一個月 GitHub 技術趨勢是否偏向特定領域？ | §7.5、§7.6 |
| **RQ7（新增）** | 有多少 repo 屬於 vibe-coding 水分專案？ | §8 |

---

## 3. 資料來源與蒐集方式

### 3.1 資料來源

GitHub 官方 REST API（v2022-11-28），三個端點：

- `GET /search/repositories` — 搜尋符合條件的 repo
- `GET /repos/{owner}/{repo}/languages` — 取得語言 byte 分布
- `GET /repos/{owner}/{repo}/topics` — 取得 topic 標籤

### 3.2 查詢條件

```
q = created:2026-04-24..2026-05-24 stars:>10 fork:false
sort = stars
order = desc
per_page = 100
```

### 3.3 抓取規模

| 階段 | 請求數 | 結果 |
|---|---:|---|
| Search API（10 頁 × 100） | 10 | 999 unique repos |
| Languages（per repo） | 951 | 一個 repo 一個 JSON 檔 |
| Topics（per repo） | 999 | 4658 topic 行（長表） |
| **總計** | **~2000** | 耗時 37.7 分鐘 |

GitHub Search API 單一查詢硬上限為 1000 筆，本研究抓滿。實際符合條件總數約 9286 筆，未抓的 8000+ 筆 stars 均較低，對「熱門」分析無實質影響。

### 3.4 Rate Limit 處理

使用 Personal Access Token（`public_repo` 唯讀權限），每小時 5000 次配額。實作中：
- 每次請求後 sleep 0.8 秒（保守，遠低於配額上限）
- 偵測 `X-RateLimit-Remaining: 0` 時拋出 `RateLimitExhausted`，立即停止並保留已抓資料
- 對 502/503/504 採指數退避重試（最多 3 次）

本研究全程未觸發 rate limit。

---

## 4. 資料欄位

主資料表 `repos.csv`（999 列 × 19 欄）：

| 類別 | 欄位 |
|---|---|
| 識別 | `id`, `full_name`, `owner`, `name`, `html_url` |
| 描述 | `description`, `primary_language`, `license`, `size` |
| 時間 | `created_at`, `pushed_at` |
| 熱度 | `stars`, `forks`, `watchers`, `open_issues` |
| **衍生** | `age_days`, `stars_per_day`, `fork_star_ratio`, `issue_star_ratio` |
| 分類 | `category` |

另有兩個長表：
- `repo_languages.csv` — 多語言組成（每個 repo 多列）
- `repo_topics.csv` — topic 標籤（每個 repo 0~多列）

---

## 5. 資料前處理

### 5.1 缺失值處理

| 欄位 | 規則 |
|---|---|
| `description` | 空值 → 空字串 |
| `primary_language` | 空值 → `"Unknown"` |
| `license` | 空值 → `"None"` |
| `topics` | 空值 → 不產生長表行 |

### 5.2 衍生欄位

```
age_days        = max(today - created_at, 1)        # 避免除以 0
stars_per_day   = stars / age_days
fork_star_ratio = forks / max(stars, 1)
issue_star_ratio = open_issues / max(stars, 1)
```

### 5.3 離群值

保留全部離群值。本研究在分布類分析使用對數座標、在比較類分析同時呈現平均數與中位數，避免極端值誤導。

---

## 6. 分析方法

### 6.1 描述性統計

- 平均、中位數、最大值
- 百分位數（25/50/75）
- 排行榜（Top 10 by stars / forks / stars_per_day）

### 6.2 規則式分類

依 description + topics + primary_language 中的關鍵字，採**單一分類、優先順序匹配**：

```
AI/ML > Security > DevOps > Data > Web > Mobile > Game > CLI/Tooling > Other
```

決策理由與訊號表參見 [ADR-0004](../docs/adr/0004-rule-based-classification.md)。

### 6.3 相關性分析

- **Pearson 相關係數**：線性關係
- **Spearman 等級相關**：對極端值較不敏感
- 散佈圖（log-log 座標）

### 6.4 視覺化

matplotlib + Agg backend，避免 GUI 依賴。共 7 張必做圖（見 §7）。

### 6.5 Vibe-Coding 水分專案評分（補章方法）

8 訊號加權評分（0-10 分），詳見 §8。

---

## 7. 分析結果

### 7.1 程式語言分布（RQ1）

![Top Languages](figures/top_languages.png)

| 排名 | 語言 | repo 數 | 占比 |
|---:|---|---:|---:|
| 1 | Python | 339 | 34% |
| 2 | TypeScript | 215 | 22% |
| 3 | JavaScript | 80 | 8% |
| 4-10 | C / C++ / Rust / Go / Swift / HTML / Shell | 各 20-50 |  |

**結論**：Python 主導（AI 與資料科學優勢），TypeScript 緊追（前端 + AI 工具鏈整合），JS/Rust/Go 為第二梯隊。**前 3 名加總約 64%**，反映 trending repo 集中在少數主流語言。

### 7.2 Topics 趨勢（RQ2）

![Top Topics](figures/top_topics.png)

| 排名 | Topic | 出現次數 |
|---:|---|---:|
| 1 | `claude-code` | 52 |
| 2 | `ai-agents` | 43 |
| 3 | `typescript` | 39 |
| 4 | `llm` | 34 |
| 5 | `python` | 30 |
| 6 | `ai` | 30 |
| 7 | `claude` | 29 |
| 8 | `mcp` | 26 |
| 9 | `codex` | 25 |
| 10 | `cli` | 24 |
| 其他 | `trading-bot` / `polymarket` / `trading` | 各 18-19 |

**觀察**：
- 前 10 名中有 7 個與 AI 直接相關（claude-code、ai-agents、llm、ai、claude、mcp、codex）
- `claude-code` 為冠軍 topic，反映 Anthropic Claude Code CLI 工具生態 2026 的爆發
- `mcp`（Model Context Protocol）出現代表 AI 工具互通協議受到關注
- 隱藏小爆紅：`trading-bot` (19) + `polymarket` (18) + `trading` (18) 顯示金融自動化的小型復興

**重要限制**：**54.4% (543 個) repo 完全未填任何 topic**，topic 分析的廣度天然受限。

### 7.3 熱門 repository 排行（RQ3）

#### Top 5 by Stars

| Rank | Repo | Stars | Forks | Language |
|---:|---|---:|---:|---|
| 1 | `nexu-io/open-design` | 50,831 | 5,795 | TypeScript |
| 2 | `antirez/ds4` | 11,589 | 978 | C |
| 3 | `Yuan1z0825/nature-skills` | 11,075 | 702 | Python |
| 4 | `FULU-Foundation/OrcaSlicer-bambulab` | 6,431 | 4,993 | C++ |
| 5 | `freestylefly/awesome-gpt-image-2` | 6,211 | 838 | JavaScript |

#### Top 5 by Stars-per-day（短期爆紅）

| Rank | Repo | Stars/day | Age |
|---:|---|---:|---:|
| 1 | `nexu-io/open-design` | 2,033 | 25d |
| 2 | `antirez/ds4` | 682 | 17d |
| 3 | `thananon/9arm-skills` | 639 | 3d |
| 4 | `vercel-labs/zerolang` | 553 | 8d |
| 5 | `FULU-Foundation/OrcaSlicer-bambulab` | 536 | 12d |

#### Stars 分布

![Stars Distribution](figures/stars_distribution.png)

平均 stars **492**，中位數 **228**，平均被少數爆紅專案拉抬 **2.2 倍**。報告結論應採中位數較貼近真實。

### 7.4 Stars 與 Forks 的關係（RQ4）

![Forks vs Stars](figures/forks_vs_stars.png)

| 相關係數 | 值 | 詮釋 |
|---|---:|---|
| Pearson | **0.358** | 中度正相關 |
| Spearman | **0.425** | 中度正相關（對極端值更穩健） |

**結論**：星數高的 repo 通常 forks 也較高，但**相關性不算強**（< 0.7）。觀察散佈圖可見：
- AI/ML 類別有一明顯子群「stars 高但 forks 偏低」（左上方稀疏區）
- Web 類別 fork:star 比例最高（前端圈分叉文化）
- 結論：**Star ≠ 真實採用度**，這也是補章 vibe-coding 分析的理論基礎。

### 7.5 類別分布與熱度（RQ5、RQ6）

![Category Distribution](figures/category_distribution.png)

| 分類 | 數量 | 占比 | 平均 Stars | 中位數 Stars | 平均 Forks | 平均 Stars/day | fork:star |
|---|---:|---:|---:|---:|---:|---:|---:|
| Other | 420 | 42.0% | 426 | 223 | 201 | 53.1 | 47% |
| **AI/ML** | **357** | **35.7%** | **609** | **240** | **103** | **44.4** | **17%** |
| Web | 79 | 7.9% | 329 | 201 | 410 | 29.7 | **124%** |
| Mobile | 42 | 4.2% | 401 | 218 | 24 | 28.9 | 6% |
| CLI/Tooling | 29 | 2.9% | 426 | 229 | 121 | 48.8 | 28% |
| Game | 26 | 2.6% | 754 | 262 | 117 | 88.4 | 16% |
| Security | 21 | 2.1% | 460 | 234 | 133 | 39.0 | 29% |
| DevOps | 13 | 1.3% | 315 | 218 | 159 | 22.9 | 50% |
| Data | 12 | 1.2% | 607 | **316** | 80 | 73.2 | 13% |

![Category Avg Stars](figures/category_avg_stars.png)

**回答 RQ5（類別熱度差異）**：
- **Game** 平均 stars 最高 (754)，但被 `antirez/ds4` 異常值拉抬，看中位數 (262) 較中肯
- **Data** 樣本最少 (12) 但中位數最高 (316)，少而精
- **AI/ML** 平均 stars 高 (609) 但平均 forks 僅 103，fork:star 比例 17% 為全類別最低
- **Web** 中位數 stars 最低 (201) 但平均 forks 達 410，前端 fork 文化最旺

**回答 RQ6（趨勢偏向）**：
**AI/ML (35.7%) + Other (42.0%) 合計 77.7%**，2026 trending 呈**雙峰結構**：
1. AI 應用爆發（agent、LLM、claude-code 生態）
2. 大量未標籤、難分類的長尾 repo

其餘 7 個傳統類別合計不到 23%。**Web 已不再是 trending 主軸**（僅占 7.9%）。

### 7.6 時序分布（趨勢健康度）

![Daily New Repos](figures/daily_new_repos.png)

30 天內每日平均 4.0 個熱門 repo 新建立，高峰 10 個（4 月 27 日），低谷 0 個。**沒有觀察到明顯爆量日**，代表 trending 是「持續產出」而非「集中於某波發表會」。Age vs Stars 相關性接近 0（Pearson 0.068），確認 30 天視窗短到不會因為「新舊偏差」污染分析。

---

## 8. 補章：Vibe-Coding 水分專案分析（RQ7 — 原創貢獻）

### 8.1 動機

GitHub trending 充滿了「stars 很多但實質很少」的 repo —— 沒有 description、沒有 license、沒有 topics、forks 與 stars 嚴重失衡。我們將此定義為 **vibe-coding garbage**（水分專案）：

> 一個 repo 的 stars 遠超它的可見實質。標籤針對的是公開產出，不是作者本人，也不是 vibe-coding 這個編程方式本身。

### 8.2 評分機制（8 訊號加權，0-10 分）

| 訊號 | 加分 | 理由 |
|---|---:|---|
| description 完全空白 | +2 | 低用心度的最強單一訊號 |
| description < 20 字 | +1 | 輕度 |
| 沒設 license | +1 | 開源實踐疏忽 |
| stars > 1000 且 description 空 | +2 | 「famous nothing」 |
| stars > 500 且 fork:star < 2% | +2 | 被星但沒人 fork |
| stars/day > 300 且 age < 7 天 | +1 | 隔夜暴衝可疑 |
| 名字含 generic AI buzzword | +1 | `*-skills`, `*-agent`, `*-cookbook`, `*-claude` ... |
| 沒任何 topics | +1 | 標籤習慣缺失 |

**判定**：0-2 legitimate · 3-4 suspicious · **5+ garbage**

### 8.3 結果

| 等級 | 數量 | 比例 |
|---|---:|---:|
| 🟢 Legitimate | 849 | **85.0%** |
| 🟡 Suspicious | 132 | 13.2% |
| 🔴 **Garbage** | **18** | **1.8%** |

### 8.4 關鍵發現：farming 集中在 1000-4999 stars 級距

| Stars 級距 | 樣本 | Garbage 數 | Garbage % |
|---|---:|---:|---:|
| ≥10000 | 3 | 0 | 0.0% |
| 5000-9999 | 2 | 1 | 50.0%（樣本小） |
| **1000-4999** | **71** | **7** | **9.9%** ← 集中區 |
| 500-999 | 108 | 2 | 1.9% |
| 100-499 | 815 | 8 | 1.0% |

**詮釋**：
- ≥10000 stars 區段反而 0%，因為太高有人盯著看，水分易被揭穿
- < 500 stars 區段也低，因為沒人在意
- **1k-5k 是 farming 的甜蜜點**：夠 impressive 上 trending，又不會被嚴格審視

### 8.5 Top 7 最可疑專案

| Rank | Repo | Stars | Forks | Age | 分數 |
|---:|---|---:|---:|---:|---:|
| 1 | `thananon/9arm-skills` | 1918 | 255 | 3d | **8** |
| 2 | `cursor/cookbook` | 3843 | 446 | 26d | **7** |
| 3 | `deepseek-ai/awesome-deepseek-agent` | 2145 | 234 | 26d | **7** |
| 4 | `FoundZiGu/GuJumpgate` | 2143 | 612 | 4d | **6** |
| 5 | `wrongly-cuddly-obsession/NTSB_FOIA_MU5735` | 1070 | 366 | 23d | **6** |
| 6 | `V4bel/dirtyfrag` | 4752 | 755 | 16d | **6** |
| 7 | `Ch1rpy2613/Mirrai` | 806 | 11 | 18d | **6** |

榜中包含 `cursor/cookbook`、`deepseek-ai/awesome-*` 等**官方帳號** —— 並非惡意 farming，而是 2026 AI 公司「先發再說」的快速出貨文化縮影。

### 8.6 Generic-name 詞彙分布

142 個 repo 名字含 generic AI buzzword，token 分布：

| Token | repo 數 |
|---|---:|
| `agent` / `agents` | 36 |
| `skills` / `skill` | 33 |
| `claude` | 25 |
| `codex` | 16 |
| `awesome` | 11 |
| `gpt` / `llm` | 9 |

**「skills」是 2026 才大規模爆紅的命名模式**，反映 Anthropic Claude Skills、OpenAI Custom GPT 等可組合 AI 模組概念的擴散。

---

## 9. 討論

### 9.1 雙峰結構的意義

77.7% 的 trending repo 落在 AI/ML 與 Other 兩個桶，其他 7 個傳統類別加起來不到 23%。這不是分類器太粗糙的問題（已對 description + topics + language 三個來源做關鍵字匹配），而是**生態本身的真實偏移** —— 2026 上半年的開源動能集中在 AI 應用，且大量新 repo 因為快速出貨缺乏標準的 metadata。

### 9.2 為什麼 AI/ML 類 fork:star 異常低？

AI/ML 類別 fork:star = 17%，遠低於 Web 的 124%、Other 的 47%。可能解釋：
1. AI repo 多為 demo / playground，使用者「看」而不「fork」
2. AI 工具更新快，fork 後容易過時，社群偏向重新建立
3. 配合 vibe-coding 分析，部分 AI repo 本身就是 farming，本質沒被使用

### 9.3 Vibe-Coding 補章對主分析的意義

正體 1.8% garbage 比例看似不高，但若聚焦在 1000-4999 stars 區段就是 9.9% —— 也就是說，**在課程作業、企業情報、技術選型常引用的「中高熱度」區段，每 10 個就有 1 個有水分**。這對「以 stars 為單一指標」的決策有警示意義。

### 9.4 Topics 缺失的結構性問題

54.4% repo 完全沒 topic。這不是抓取錯誤，是 GitHub 生態的現實：topic 是選填欄位，新建 repo 通常不會立刻填。任何完全依賴 topic 的分類器都會嚴重低估覆蓋率。本研究的規則式分類器同時使用 description + topics + language 三個來源，部分緩解了此問題，但 42% 的 Other 比例仍反映了這個侷限。

---

## 10. 限制

| # | 限制 | 影響 |
|---|---|---|
| 1 | `watchers` 欄位等於 `stars`（Search API 不回 `subscribers_count`） | 不影響本研究結論，但 `watchers` 欄不可信，相關分析已避免使用 |
| 2 | 54.4% repo 無 topics | 限制 topic-based 分析的廣度；Other 桶比例偏高（42%） |
| 3 | 單一分類 MVP | React + LLM 的 repo 會被歸 AI/ML（優先順序高）而非 Web，可能低估 Web 熱度 |
| 4 | 規則式分類器主觀性 | 關鍵字表手寫，覆蓋率與 bias 取決於設計者；詳見 ADR-0004 |
| 5 | Search API 1000 筆硬上限 | 本研究抓滿，但若想跨更廣 stars 區間需切片查詢 |
| 6 | 30 天視窗 | 不適合做長期趨勢比較，僅作為「當前快照」 |
| 7 | Vibe-coding 評分是「嫌疑」非「判決」 | `awesome-*` 列表、學術研究 repo 可能誤判（如 `Jiawei-Yang/FD-Loss` 是合法 ML 論文 repo，僅因低 forks 而踩線） |
| 8 | 未驗證評分機制的 precision/recall | 後續工作建議從各 tier 各抽 20 個人工驗證 |
| 9 | Stars 不能直接代表程式碼品質或實際使用量 | 本研究全部數值僅反映「社群關注度」 |

---

## 11. 結論

本研究成功蒐集 999 個近月熱門 GitHub repo 並完成系統性分析。主要結論：

1. **語言層面**：Python / TypeScript / JavaScript 三足鼎立，前 3 名涵蓋 64% 樣本。
2. **主題層面**：AI 工具相關 topic 全面霸榜（`claude-code`、`ai-agents`、`llm` 等），但 54% repo 缺 topic 限制了分析廣度。
3. **熱度相關性**：Stars↔Forks 為中度正相關（0.36），但 AI/ML 類別呈現「被星但少被 fork」的獨特模式。
4. **類別趨勢**：AI/ML + Other 雙峰占 77.7%，傳統 Web/Mobile/Data 等類別不到 23%。**2026 上半年 GitHub trending 已被 AI 主導。**
5. **原創發現**：以 8 訊號嚴格評分檢測「vibe-coding 水分專案」，發現 1.8% 為 garbage，集中於 1000-4999 stars「farming 甜蜜點」。

研究成果包含：
- 999 筆 repo 資料集（CSV + 原始 JSON）
- 7 張視覺化圖表
- Streamlit 互動 dashboard
- Vibe-coding 評分機制與分析報告
- 全 pipeline 自動化程式碼（共 ~1100 LoC + 22 個 pytest 案例）

**後續工作建議**：
- 兩週後重抓一次，做 delta 分析（從一次性快照進化為「短期趨勢比較」）
- 對 vibe-coding 評分機制做人工驗證，計算 precision/recall
- 將分類器從單一分類擴充為多重分類，減少 Other 桶比例

---

## 12. 參考資料

- GitHub REST API 文件：<https://docs.github.com/rest>
- GitHub Search Repositories API：<https://docs.github.com/rest/search/search#search-repositories>
- pandas documentation：<https://pandas.pydata.org/docs/>
- matplotlib documentation：<https://matplotlib.org/stable/>
- Streamlit documentation：<https://docs.streamlit.io/>
- 本專案原始企畫書：[`github_recent_trend_analysis_project_proposal.md`](../github_recent_trend_analysis_project_proposal.md)
- 本專案完整原始碼：<https://github.com/aionyx02/github_recent_trend_analysiz>
- ADR-0004（規則式分類決策）：[`docs/adr/0004-rule-based-classification.md`](../docs/adr/0004-rule-based-classification.md)

---

_本報告由 Python pipeline 自動產出之 `outputs/summary_stats.md`、`outputs/vibe_coding_analysis.md`、`outputs/figures/*.png` 整合撰寫。執行 `python -m src.collect_all && python -m src.build_charts && python -m src.analyze_vibe` 可完整重現所有數值與圖表。_