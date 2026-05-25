# Other 類別深入分析 / Other Category Breakdown

_Sample: 1000 repos total · 420 repos in Other (42.0%)_

Other 桶（無法被現行 9 大規則式分類器歸類的 repo）占整體樣本約 4 成。本檔分析它的內部組成，協助判斷是否需要新增類別。

## 1. Other 內 Top 10 主要程式語言

| Rank | 語言 | Repos | Other 內占比 |
|---:|---|---:|---:|
| 1 | `Python` | 120 | 28.6% |
| 2 | `Unknown` | 80 | 19.0% |
| 3 | `TypeScript` | 79 | 18.8% |
| 4 | `JavaScript` | 32 | 7.6% |
| 5 | `C++` | 24 | 5.7% |
| 6 | `Go` | 18 | 4.3% |
| 7 | `C#` | 15 | 3.6% |
| 8 | `C` | 13 | 3.1% |
| 9 | `Rust` | 8 | 1.9% |
| 10 | `Java` | 7 | 1.7% |

## 2. Other 內 Top 20 description 關鍵字

簡易 regex 分詞、英文停用字過濾後的詞頻。代表「Other 內部專案在描述自己什麼」。

| Rank | 關鍵字 | 出現次數 |
|---:|---|---:|
| 1 | `bot` | 259 |
| 2 | `trading` | 193 |
| 3 | `polymarket` | 189 |
| 4 | `windows` | 33 |
| 5 | `download` | 33 |
| 6 | `weather` | 30 |
| 7 | `arbitrage` | 27 |
| 8 | `bundler` | 24 |
| 9 | `crypto` | 22 |
| 10 | `solana` | 20 |
| 11 | `mod` | 18 |
| 12 | `pumpfun` | 17 |
| 13 | `limitless` | 15 |
| 14 | `hyperliquid` | 15 |
| 15 | `latest` | 13 |
| 16 | `copy` | 13 |
| 17 | `google` | 11 |
| 18 | `video` | 11 |
| 19 | `setup` | 11 |
| 20 | `steam` | 11 |

## 3. Other 內 Top 10 GitHub topics

_Other 內 147 / 420 個 repo 有貼 topic (35.0%)_

| Rank | Topic | Repos |
|---:|---|---:|
| 1 | `bot` | 14 |
| 2 | `polymarket-trading-bot` | 11 |
| 3 | `trading` | 11 |
| 4 | `polymarket` | 7 |
| 5 | `polymarket-arbitrage-trading-bot` | 6 |
| 6 | `nintendo-switch` | 5 |
| 7 | `trading-bot` | 5 |
| 8 | `polymarket-arbitrage-bot` | 5 |
| 9 | `arbitrage-bot` | 4 |
| 10 | `arbitrage-trading-bot` | 4 |

## 4. 可能值得新增的類別 (Suggested new categories)

根據 §1-§3 觀察到的訊號，下列候選類別可能值得在未來版本納入分類規則：

| 候選類別 | 命中關鍵字 (description+topic) | 估計 repos |
|---|---|---:|
| Education / Learning | `course`(1), `tutorial`(2), `learn`(1), `learning`(6), `study`(1) | ~18 |
| Design / Creative | `design`(4), `icon`(2), `icons`(2), `art`(1), `wallpaper`(2) | ~11 |
| Blockchain / Web3 | `crypto`(23), `bitcoin`(1), `defi`(1), `wallet`(3) | ~28 |
| Finance / Trading | `trading`(204), `finance`(1), `market`(2), `portfolio`(2), `fintech`(2) | ~211 |
| Hardware / Embedded | `esp32`(3), `embedded`(1), `firmware`(2) | ~6 |
| Documentation / Awesome lists | `awesome`(1), `resources`(3), `list`(4), `curated`(1), `collection`(2) | ~11 |

_估計 repos 是「描述/topic 命中關鍵字的次數總和」，會略高於實際 repo 數__（一個 repo 可能命中多個 keyword）；用作粗略優先級排序。_

## 5. 限制

- Token 分詞使用簡易 regex，未處理複合詞、縮寫、CJK 文字；中文 description 的內部結構未被分析。
- 候選類別建議基於關鍵字命中，**不代表新增該類別後 Other 桶會大幅縮小** —— 需先設計具體 keyword + priority 規則並重跑 classify.py 才能評估效果。
- 本檔每次跑 `python -m src.analyze_other` 重新生成；資料每日由 daily-refresh 工作流自動重抓後可一併重算。
