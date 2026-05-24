# GitHub 近一個月開源專案趨勢分析企畫書

## 一、企畫名稱

**GitHub 近一個月新建立熱門開源專案之技術分類與趨勢分析**

---

## 二、企畫摘要

本企畫預計使用 GitHub 官方 REST API 蒐集最近一個月新建立且具有一定熱度的公開 repository 資料，針對程式語言、主題標籤、Stars、Forks、Issues、更新時間與專案分類進行分析，最後產出資料視覺化圖表與分析報告。

本專案以「可行性」為最高優先，因此不嘗試分析整個 GitHub 平台，而是設定明確篩選條件，例如：最近 30 天新建立、Stars 大於一定門檻、排除 fork repository。此設計能有效控制資料量、API 請求次數與分析難度，同時仍能呈現近期開源技術趨勢。

預期成果包含：

1. GitHub repository 資料集
2. 資料清理與分析程式
3. 視覺化圖表
4. 專案分類結果
5. 趨勢分析報告
6. 若時間允許，製作簡易互動式 Dashboard

---

## 三、研究背景與動機

GitHub 是全球重要的開源協作平台，許多新技術、框架、工具與 AI 專案都會先在 GitHub 上公開。Repository 的 Stars、Forks、Topics、Issues、程式語言與更新頻率，雖然不能完全代表專案品質或實際使用量，但可以作為觀察開源社群關注方向的重要指標。

對於大數據導論課程而言，本題目具備以下優點：

1. **資料來源公開且具公信力**：GitHub 提供官方 API，可取得公開 repository 資料。
2. **資料量可控**：透過時間範圍、Stars 門檻、fork 篩選控制資料量。
3. **分析目標明確**：可分析語言分布、topic 趨勢、熱度排名、分類差異與相關性。
4. **不需要複雜模型**：即使不使用機器學習，也能透過統計與視覺化完成完整分析。
5. **適合作業展示**：能產出圖表、排行榜、分類表與結論，容易寫成報告。

---

## 四、研究目標

本企畫的主要目標如下：

### 4.1 建立 GitHub 近期開源專案資料集

使用 GitHub REST API 擷取最近一個月新建立的公開 repository，並記錄其基本資訊、熱度指標、程式語言與主題標籤。

### 4.2 分析近期熱門技術分布

統計最近一個月熱門新專案中最常見的程式語言、topics 與專案類型。

### 4.3 建立專案分類方法

根據 repository 的 description、topics 與 primary language，將專案分成 AI/ML、Web、Data、DevOps、Security、Game、CLI/Tooling、Mobile、Other 等類別。

### 4.4 比較不同類別的熱度差異

使用 Stars、Forks、Issues、Stars per day 等指標，比較不同類別專案的受關注程度。

### 4.5 產出可解釋的視覺化報告

透過長條圖、散佈圖、折線圖、熱度排行榜等方式，讓結果可以被非技術背景的人理解。

---

## 五、研究問題

本專案主要回答以下問題：

### RQ1：最近一個月新建立的熱門 GitHub repository 中，最常見的程式語言是哪些？

觀察近期開源專案主要使用 Python、TypeScript、JavaScript、Go、Rust、C++ 或其他語言的比例。

### RQ2：最近一個月最常見的 GitHub topics 是哪些？

透過 topics 分析近期專案關注的方向，例如 AI、LLM、React、CLI、Docker、Data、Security 等。

### RQ3：哪些專案在短時間內獲得較高關注？

使用 Stars、Stars per day、Forks 等指標找出短期爆紅專案。

### RQ4：Stars 與 Forks 是否具有相關性？

分析 repository 被收藏與被複製延伸之間是否存在明顯關聯。

### RQ5：不同類別的專案熱度是否不同？

比較 AI/ML、Web、Data、DevOps、Security 等不同分類的平均 Stars、平均 Forks 與 Stars per day。

### RQ6：最近一個月 GitHub 技術趨勢是否偏向特定領域？

例如 AI/ML 是否明顯高於其他類別，或 Web、CLI、Developer Tools 是否仍是主要類型。

---

## 六、資料來源

### 6.1 主要資料來源

資料來源為 GitHub 官方 REST API。

主要會使用以下 API：

1. Search repositories API
2. Repository details API
3. Repository languages API
4. Repository topics API
5. Releases API，視時間與 API 額度決定是否納入
6. Issues API，視時間與 API 額度決定是否納入

### 6.2 資料範圍

建議資料範圍如下：

- 時間範圍：最近 30 天新建立的 repository
- 篩選條件：
  - `created` 在最近 30 天內
  - `stars > 10`
  - `fork:false`
  - public repository
- 排序方式：依 Stars 由高到低排序
- 預計資料量：300 至 500 筆 repository

### 6.3 為什麼不抓全 GitHub？

不抓全 GitHub 的原因：

1. GitHub 全站資料量過大，不適合作為短期課程作業。
2. API 有 rate limit，無法無限制抓取。
3. 搜尋結果分頁與排序會受到 API 限制。
4. 全站資料會包含大量低活躍、無描述、無 topics 的 repository，會降低分析品質。
5. 作業重點應放在可解釋分析，而不是盲目堆疊資料量。

---

## 七、資料欄位設計

### 7.1 Repository 基本資料表：`repos`

| 欄位名稱 | 說明 | 用途 |
|---|---|---|
| id | GitHub repository ID | 唯一識別 |
| full_name | owner/repo 格式名稱 | 顯示與查詢 |
| owner | 擁有者名稱 | 分析使用者或組織 |
| name | repository 名稱 | 顯示 |
| html_url | GitHub 網址 | 報告參考 |
| description | 專案描述 | 分類依據 |
| created_at | 建立時間 | 時間範圍分析 |
| pushed_at | 最近更新時間 | 活躍程度分析 |
| stars | Stars 數量 | 熱度指標 |
| forks | Forks 數量 | 擴散程度指標 |
| watchers | Watchers 數量 | 關注程度 |
| open_issues | 開啟中的 Issues 數量 | 維護狀態 |
| primary_language | 主要程式語言 | 語言分析 |
| size | repository 大小 | 輔助分析 |
| license | 授權條款 | 開源狀態參考 |

### 7.2 程式語言資料表：`repo_languages`

| 欄位名稱 | 說明 |
|---|---|
| repo_id | 對應 repository ID |
| language | 程式語言名稱 |
| bytes | 該語言程式碼位元組數 |

用途：

- 分析一個 repository 的多語言組成
- 補足 primary_language 過於簡化的問題
- 統計整體語言使用量

### 7.3 Topic 資料表：`repo_topics`

| 欄位名稱 | 說明 |
|---|---|
| repo_id | 對應 repository ID |
| topic | GitHub topic 標籤 |

用途：

- 分析熱門主題
- 做專案分類
- 做 topic 共現分析

### 7.4 分析後衍生欄位

| 欄位名稱 | 計算方式 | 用途 |
|---|---|---|
| age_days | 今天日期 - created_at | 專案存在天數 |
| stars_per_day | stars / age_days | 短期爆紅程度 |
| fork_star_ratio | forks / stars | 被延伸比例 |
| issue_star_ratio | open_issues / stars | issue 活躍度 |
| category | 規則分類結果 | 類別趨勢分析 |

---

## 八、資料蒐集方法

### 8.1 API 查詢條件

範例查詢：

```text
created:2026-04-24..2026-05-24 stars:>10 fork:false
```

API URL 範例：

```text
https://api.github.com/search/repositories?q=created:2026-04-24..2026-05-24 stars:>10 fork:false&sort=stars&order=desc&per_page=100&page=1
```

實作時不應把日期寫死，而是用 Python 自動計算：

```python
from datetime import date, timedelta

end_date = date.today()
start_date = end_date - timedelta(days=30)
query = f"created:{start_date}..{end_date} stars:>10 fork:false"
```

### 8.2 預計抓取頁數

GitHub Search API 每頁最多可抓 100 筆資料。

MVP 階段建議：

```text
5 pages × 100 repos = 500 repos
```

這個資料量已經足夠完成統計、分類與視覺化。

### 8.3 API 請求規模估算

假設抓 500 個 repository：

| 項目 | 請求次數 |
|---|---:|
| Search repositories | 5 |
| Languages | 500 |
| Topics | 500 |
| Releases，選做 | 500 |
| Issues，選做 | 500 |
| 合計，不含選做 | 約 1005 |
| 合計，含選做 | 約 2005 |

使用 GitHub token 後，這個請求量在作業規模內可接受。

### 8.4 Rate limit 風險控制

為降低 API 限制風險，採取以下策略：

1. 使用 Personal Access Token。
2. 每次請求間加入短暫 sleep，例如 0.5 至 2 秒。
3. 儲存原始 JSON 或 CSV，避免重複抓同一批資料。
4. 先抓 100 筆測試，再擴大到 500 筆。
5. Issues、Releases 屬於加分資料，不納入 MVP 必要項目。
6. 若 API 回傳 rate limit error，停止抓取並保存目前結果。

---

## 九、資料前處理規劃

### 9.1 清理重複資料

使用 repository id 作為唯一識別，避免同一 repository 重複出現。

### 9.2 處理缺失值

可能缺失的欄位包括：

- description
- primary_language
- license
- topics

處理方式：

| 欄位 | 處理方式 |
|---|---|
| description | 空值改為空字串 |
| primary_language | 空值改為 Unknown |
| license | 空值改為 None |
| topics | 空值視為空列表 |

### 9.3 時間格式轉換

將 `created_at` 與 `pushed_at` 轉成 datetime 格式，方便計算：

- 專案存在天數
- 最近更新距今天數
- 每日新增 repository 數量

### 9.4 離群值處理

有些 repository 可能在短時間內獲得極高 stars，這是重要現象，不應直接刪除。

處理方式：

1. 保留離群值。
2. 在圖表中使用 log scale 或另外標註。
3. 分析時同時使用平均數與中位數，避免極端值誤導。

---

## 十、專案分類方法

本企畫採用「規則式分類」作為 MVP 方法，不使用機器學習模型。

理由：

1. 實作簡單。
2. 可解釋性高。
3. 適合作業報告說明。
4. 不需要標註資料。
5. 不會增加模型訓練成本。

### 10.1 分類依據

分類會根據以下文字資料：

1. repository description
2. topics
3. primary_language
4. repository name，選用

### 10.2 預設分類表

| 分類 | 關鍵字範例 |
|---|---|
| AI/ML | ai, artificial-intelligence, machine-learning, deep-learning, llm, neural, transformer, diffusion, agent |
| Web | react, vue, nextjs, frontend, backend, web, html, css, api, nodejs |
| Data | data, database, analytics, visualization, dashboard, etl, pandas, spark |
| DevOps | docker, kubernetes, ci, cd, devops, deployment, terraform, ansible |
| Security | security, vulnerability, pentest, malware, exploit, authentication, encryption |
| Game | game, unity, unreal, graphics, engine, shader |
| CLI/Tooling | cli, terminal, command-line, developer-tools, productivity, automation |
| Mobile | android, ios, flutter, react-native, mobile |
| Other | 無法歸類者 |

### 10.3 單一分類與多重分類

MVP 採用單一分類：

- 每個 repository 只分到一個主要類別。
- 如果同時符合多個類別，按照優先順序分配。

優先順序建議：

```text
AI/ML > Security > DevOps > Data > Web > Mobile > Game > CLI/Tooling > Other
```

若時間足夠，可以改成多重分類，使一個 repository 可以同時屬於 AI/ML 與 Web。

---

## 十一、分析方法設計

### 11.1 描述性統計

統計內容：

1. repository 總數
2. stars 平均數、中位數、最大值
3. forks 平均數、中位數、最大值
4. open issues 平均數、中位數
5. 主要程式語言數量排行
6. topics 出現次數排行
7. 分類數量排行

### 11.2 熱門專案排行

產出以下排行榜：

1. Stars Top 10
2. Forks Top 10
3. Stars per day Top 10
4. Open issues Top 10

### 11.3 語言趨勢分析

分析：

1. 最常見 primary language
2. 不同語言的平均 stars
3. 不同語言的平均 forks
4. 不同語言的 repository 數量

### 11.4 Topic 趨勢分析

分析：

1. Top 20 topics
2. AI 相關 topic 是否佔比高
3. Web 相關 topic 是否仍然常見
4. topic 與 stars 的關係

### 11.5 分類趨勢分析

分析：

1. 各類別 repository 數量
2. 各類別平均 stars
3. 各類別 stars per day
4. 各類別平均 forks
5. 各類別 open issues 平均值

### 11.6 相關性分析

分析指標：

1. stars 與 forks 的相關性
2. stars 與 open issues 的相關性
3. repository age 與 stars 的相關性

使用方法：

- Pearson correlation
- Spearman correlation
- 散佈圖

---

## 十二、視覺化規劃

### 12.1 必做圖表

| 圖表名稱 | 圖表類型 | 說明 |
|---|---|---|
| Top 10 程式語言 | 長條圖 | 顯示熱門語言分布 |
| Top 20 topics | 長條圖 | 顯示近期主題趨勢 |
| Stars 分布 | 直方圖 | 觀察熱度是否集中於少數專案 |
| Forks vs Stars | 散佈圖 | 觀察兩者相關性 |
| 專案類別分布 | 長條圖 | 顯示 AI/Web/Data 等類別數量 |
| 類別平均 Stars | 長條圖 | 比較不同類別受關注程度 |
| 每日新增熱門 repo 數 | 折線圖 | 顯示最近一個月時間趨勢 |

### 12.2 選做圖表

| 圖表名稱 | 圖表類型 | 說明 |
|---|---|---|
| Topic 共現圖 | Network graph | 觀察 topic 之間關聯 |
| 語言與類別交叉表 | Heatmap | 觀察語言與分類關係 |
| Stars per day Top 10 | 長條圖 | 找出短期爆紅專案 |
| License 分布 | 圓餅圖或長條圖 | 分析授權狀況 |

---

## 十三、技術架構規劃

### 13.1 MVP 技術棧

| 功能 | 技術 |
|---|---|
| API 抓取 | Python requests 或 httpx |
| 資料處理 | pandas |
| 資料儲存 | CSV + SQLite |
| 視覺化 | matplotlib / plotly |
| 分析環境 | Jupyter Notebook |
| 報告 | Markdown / PDF |

### 13.2 加分版技術棧

| 功能 | 技術 |
|---|---|
| Dashboard | Streamlit |
| 互動式圖表 | Plotly |
| 後端 API | FastAPI，選做 |
| 前端 | Next.js，選做 |

### 13.3 建議採用方案

本作業建議採用：

```text
Python + pandas + SQLite + Plotly + Streamlit
```

理由：

1. 開發速度快。
2. 資料分析方便。
3. Streamlit 可以快速做出展示頁面。
4. 不需要花太多時間處理前後端架構。
5. 符合作業可行性優先的原則。

---

## 十四、系統流程設計

### 14.1 資料流程

```text
GitHub REST API
        ↓
Python crawler
        ↓
Raw JSON backup
        ↓
Data cleaning
        ↓
CSV / SQLite
        ↓
Data analysis
        ↓
Visualization
        ↓
Report / Dashboard
```

### 14.2 程式模組規劃

```text
project/
├── data/
│   ├── raw/
│   ├── processed/
│   └── github_repos.db
├── notebooks/
│   └── analysis.ipynb
├── src/
│   ├── config.py
│   ├── github_api.py
│   ├── collect_repos.py
│   ├── collect_languages.py
│   ├── collect_topics.py
│   ├── clean_data.py
│   ├── classify.py
│   └── visualize.py
├── dashboard/
│   └── app.py
├── outputs/
│   ├── figures/
│   └── report.md
├── requirements.txt
└── README.md
```

### 14.3 模組說明

| 檔案 | 功能 |
|---|---|
| config.py | 管理 token、日期、API 設定 |
| github_api.py | 封裝 GitHub API 請求 |
| collect_repos.py | 抓 repository 搜尋結果 |
| collect_languages.py | 抓每個 repository 的語言資料 |
| collect_topics.py | 抓每個 repository 的 topics |
| clean_data.py | 資料清理與轉換 |
| classify.py | repository 分類 |
| visualize.py | 產生圖表 |
| app.py | Streamlit Dashboard |

---

## 十五、實作步驟

### Step 1：申請 GitHub Token

申請 Personal Access Token，用於提高 API rate limit。

Token 不應寫死在程式中，應放在 `.env` 或系統環境變數中。

範例：

```bash
export GITHUB_TOKEN="your_token_here"
```

Python 讀取：

```python
import os
TOKEN = os.getenv("GITHUB_TOKEN")
```

### Step 2：建立 API 請求函式

建立通用 request function，處理：

1. headers
2. params
3. error handling
4. rate limit 檢查
5. retry
6. sleep

### Step 3：抓取 repository 清單

使用 Search repositories API 抓取最近 30 天新建立的熱門 repository。

MVP 抓取 500 筆以內即可。

### Step 4：補抓 languages 與 topics

對每個 repository 補抓：

1. languages
2. topics

這兩項資料是分類與趨勢分析的核心。

### Step 5：儲存資料

至少儲存三份資料：

1. `repos.csv`
2. `repo_languages.csv`
3. `repo_topics.csv`

建議同時存入 SQLite，方便查詢與展示。

### Step 6：資料清理

處理：

1. 空值
2. 日期格式
3. 重複 repository
4. topics 拆分
5. 衍生欄位計算

### Step 7：分類

使用規則式方法進行分類。

分類結果寫入 `category` 欄位。

### Step 8：分析與視覺化

完成必做圖表：

1. 語言排行
2. topics 排行
3. stars 分布
4. stars vs forks
5. 分類分布
6. 類別平均 stars
7. 每日新增趨勢

### Step 9：撰寫報告

報告包含：

1. 研究動機
2. 資料來源
3. 資料蒐集方式
4. 資料前處理
5. 分析結果
6. 圖表解釋
7. 限制與未來改進
8. 結論

### Step 10：選做 Dashboard

若時間足夠，使用 Streamlit 製作簡易 Dashboard。

功能包括：

1. 顯示總資料數
2. 顯示語言排行
3. 顯示 topics 排行
4. 篩選分類
5. 顯示 Top repositories
6. 顯示散佈圖

---

## 十六、可行性分析

### 16.1 技術可行性

本企畫使用 GitHub 官方 API、Python、pandas 與常見視覺化工具，技術成熟度高，沒有高度不確定性。

需要掌握的技術包括：

1. REST API request
2. JSON parsing
3. pandas 資料處理
4. SQLite 或 CSV 儲存
5. 基礎統計分析
6. 圖表視覺化

這些技術皆屬於大數據導論作業可接受範圍。

### 16.2 時間可行性

若以一人完成，建議時程如下：

| 時間 | 工作內容 |
|---|---|
| 第 1 天 | API 測試、抓 repository、存 CSV |
| 第 2 天 | 補抓 languages/topics、資料清理 |
| 第 3 天 | 分類、統計分析、產圖 |
| 第 4 天 | 寫報告、整理結論 |
| 第 5 天，選做 | Streamlit Dashboard、優化圖表 |

若時間只有兩天，則縮小範圍：

| 時間 | 工作內容 |
|---|---|
| 第 1 天 | 抓 300 筆資料、清理、分類 |
| 第 2 天 | 圖表、報告、結論 |

### 16.3 資料可行性

GitHub 上每天都有大量新 repository。透過 stars 門檻與 fork 排除條件，可以取得品質較高、較有分析價值的資料。

### 16.4 分析可行性

本企畫不依賴複雜模型，主要使用：

1. 次數統計
2. 排行榜
3. 平均數與中位數
4. 相關性分析
5. 規則式分類
6. 視覺化解釋

因此完成風險較低。

### 16.5 展示可行性

成果可以用 Jupyter Notebook、PDF 報告或 Streamlit Dashboard 呈現。即使 Dashboard 沒完成，仍可用圖表與報告完成作業。

---

## 十七、風險評估與解決方案

| 風險 | 影響 | 解決方案 |
|---|---|---|
| API rate limit | 無法抓完資料 | 使用 token、減少資料量、保存中間結果 |
| repository topics 缺失 | 分類不準 | 同時使用 description 與 language |
| description 太短或空白 | 分類困難 | 無法分類者歸為 Other |
| stars 不代表真實使用量 | 結論可能偏誤 | 報告中明確說明 stars 只是關注度指標 |
| 熱門專案受到宣傳影響 | 產生偏差 | 使用 stars_per_day 與中位數輔助分析 |
| 資料量太大 | 時間不足 | 限制 300 至 500 筆 |
| Issues API 混入 PR | issue 分析錯誤 | MVP 不抓詳細 issue，或用 pull_request key 區分 |
| 分類規則主觀 | 分析有偏差 | 在報告中列出分類規則與限制 |

---

## 十八、預期成果

### 18.1 必交成果

1. Python 程式碼
2. GitHub repository 資料集 CSV
3. 資料清理後 CSV
4. Jupyter Notebook 分析檔
5. 視覺化圖表
6. 分析報告 PDF 或 Markdown

### 18.2 加分成果

1. SQLite 資料庫
2. Streamlit Dashboard
3. Topic 共現圖
4. 多重分類版本
5. README 使用說明
6. API rate limit 處理說明

---

## 十九、報告建議架構

最終報告建議如下：

```text
1. 摘要
2. 研究動機
3. 研究問題
4. 資料來源與蒐集方式
5. 資料欄位說明
6. 資料前處理
7. 分析方法
8. 分析結果
   8.1 程式語言分布
   8.2 Topics 趨勢
   8.3 熱門 repository 排行
   8.4 Stars 與 Forks 關係
   8.5 專案分類趨勢
   8.6 類別熱度比較
9. 討論
10. 限制
11. 結論
12. 參考資料
```

---

## 二十、MVP 範圍定義

為確保作業可完成，本企畫將 MVP 定義如下。

### 20.1 MVP 必做

1. 抓取最近 30 天新建立、stars > 10、fork:false 的 repository。
2. 資料量至少 300 筆，最多 500 筆。
3. 抓取 repository 基本欄位。
4. 補抓 languages。
5. 補抓 topics。
6. 產出至少 6 張圖表。
7. 完成規則式分類。
8. 完成分析報告。

### 20.2 MVP 不做

1. 不訓練機器學習模型。
2. 不抓全 GitHub。
3. 不分析 private repository。
4. 不做長期歷史資料分析。
5. 不保證分類完全正確。
6. 不把 Dashboard 視為必要交付項目。

### 20.3 加分項目

1. Streamlit Dashboard。
2. Topic network graph。
3. GitHub Actions 自動更新資料。
4. 使用 SQLite 儲存完整資料。
5. 加入 release 分析。
6. 加入 PR / issue 分析。

---

## 二十一、預期分析結論形式

最後報告不應只列出圖表，而要能形成類似以下的結論：

1. 最近一個月熱門新 repository 中，Python 與 TypeScript 可能是主要語言。
2. AI/ML、Web、CLI/Tooling 類型可能是近期較活躍的方向。
3. Stars 與 Forks 通常呈正相關，但高 Stars 不一定代表高 Forks。
4. 部分專案雖然建立時間短，但 stars_per_day 很高，可能代表短期爆紅。
5. GitHub topics 對分類有幫助，但因為 topics 由作者自行填寫，所以存在缺漏與主觀性。

實際結論需以抓取後的資料為準。

---

## 二十二、可行性總結

本企畫具備高度可行性，原因如下：

1. 資料來源明確：GitHub 官方 REST API。
2. 資料範圍可控：限制最近 30 天、stars > 10、排除 fork。
3. 技術門檻合理：Python、pandas、API、圖表即可完成。
4. 成果容易展示：可產出圖表、排行榜、分類表與報告。
5. 不依賴高風險技術：不需要模型訓練、不需要大型資料平台。
6. 可擴充：有時間可加 Dashboard、topic network、issue/release 分析。

因此，本題目適合作為大數據導論作業，且能在有限時間內完成具有分析價值的成果。

---

## 二十三、建議最終題目

建議正式題目使用：

**GitHub 近一個月新建立熱門開源專案之技術分類與趨勢分析**

副標題可使用：

**以程式語言、Topics、Stars、Forks 與規則式分類為核心**

---

## 二十四、下一步工作清單

### 第一階段：確認題目與範圍

- [ ] 確認是否使用最近 30 天新建立 repository
- [ ] 確認 stars 門檻，例如 stars > 10 或 stars > 50
- [ ] 確認資料量，例如 300 或 500 筆
- [ ] 確認是否要做 Dashboard

### 第二階段：資料蒐集

- [ ] 申請 GitHub token
- [ ] 測試 Search API
- [ ] 抓 repository 基本資料
- [ ] 補抓 languages
- [ ] 補抓 topics
- [ ] 儲存 CSV / SQLite

### 第三階段：資料分析

- [ ] 清理缺失值
- [ ] 計算 stars_per_day
- [ ] 計算 fork_star_ratio
- [ ] 建立分類欄位
- [ ] 產生統計摘要

### 第四階段：視覺化與報告

- [ ] 產出語言排行圖
- [ ] 產出 topics 排行圖
- [ ] 產出 stars 分布圖
- [ ] 產出 stars vs forks 散佈圖
- [ ] 產出分類分布圖
- [ ] 產出類別平均 stars 圖
- [ ] 撰寫分析結論
- [ ] 整理限制與未來改進

---

## 二十五、審閱重點建議

你可以優先審閱以下幾點：

1. 題目是否太大或太小。
2. stars 門檻是否合理。
3. 資料量 300 至 500 筆是否符合課程要求。
4. 是否需要加入 Dashboard。
5. 分類類別是否需要調整。
6. 是否要把 AI/ML 設為主分析重點。
7. 老師是否要求一定要有資料庫或前端。
8. 報告是否需要 PDF、簡報或 Demo。

