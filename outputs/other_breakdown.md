# Other 類別深入分析 / Other Category Breakdown

_Sample: 1000 repos total · 374 repos in Other (37.4%)_

Other 桶（無法被現行 9 大規則式分類器歸類的 repo）占整體樣本約 4 成。本檔分析它的內部組成，協助判斷是否需要新增類別。

## 1. Other 內 Top 10 主要程式語言

| Rank | 語言 | Repos | Other 內占比 |
|---:|---|---:|---:|
| 1 | `Python` | 108 | 28.9% |
| 2 | `Unknown` | 78 | 20.9% |
| 3 | `TypeScript` | 51 | 13.6% |
| 4 | `JavaScript` | 30 | 8.0% |
| 5 | `C++` | 23 | 6.1% |
| 6 | `Go` | 18 | 4.8% |
| 7 | `C#` | 14 | 3.7% |
| 8 | `C` | 13 | 3.5% |
| 9 | `Rust` | 8 | 2.1% |
| 10 | `Java` | 7 | 1.9% |

## 2. Other 內 Top 20 description 關鍵字

簡易 regex 分詞、英文停用字過濾後的詞頻。代表「Other 內部專案在描述自己什麼」。

| Rank | 關鍵字 | 出現次數 |
|---:|---|---:|
| 1 | `windows` | 32 |
| 2 | `download` | 32 |
| 3 | `mod` | 18 |
| 4 | `latest` | 13 |
| 5 | `google` | 11 |
| 6 | `generation` | 11 |
| 7 | `video` | 11 |
| 8 | `setup` | 11 |
| 9 | `steam` | 11 |
| 10 | `script` | 10 |
| 11 | `pro` | 10 |
| 12 | `esp` | 10 |
| 13 | `full` | 10 |
| 14 | `bypass` | 9 |
| 15 | `audio` | 9 |
| 16 | `menu` | 9 |
| 17 | `loader` | 8 |
| 18 | `desktop` | 8 |
| 19 | `linux` | 8 |
| 20 | `markdown` | 8 |

## 3. Other 內 Top 10 GitHub topics

_Other 內 117 / 374 個 repo 有貼 topic (31.3%)_

| Rank | Topic | Repos |
|---:|---|---:|
| 1 | `nintendo-switch` | 5 |
| 2 | `nintendo-switch-hacking` | 3 |
| 3 | `vpn` | 3 |
| 4 | `autocad-addins` | 3 |
| 5 | `mod` | 3 |
| 6 | `autocad-install` | 3 |
| 7 | `auto-cad-free` | 3 |
| 8 | `cad-software` | 3 |
| 9 | `steam` | 3 |
| 10 | `minecraft-client` | 3 |

## 4. 可能值得新增的類別 (Suggested new categories)

根據 §1-§3 觀察到的訊號，下列候選類別可能值得在未來版本納入分類規則：

| 候選類別 | 命中關鍵字 (description+topic) | 估計 repos |
|---|---|---:|
| Education / Learning | `course`(1), `tutorial`(2), `learn`(1), `learning`(6), `study`(1) | ~18 |
| Design / Creative | `design`(4), `icon`(2), `icons`(2), `art`(1), `wallpaper`(2) | ~11 |
| Blockchain / Web3 | `bitcoin`(1) | ~1 |
| Hardware / Embedded | `esp32`(3), `embedded`(1), `firmware`(2) | ~6 |
| Documentation / Awesome lists | `awesome`(1), `resources`(1), `list`(3), `collection`(2) | ~7 |

_估計 repos 是「描述/topic 命中關鍵字的次數總和」，會略高於實際 repo 數__（一個 repo 可能命中多個 keyword）；用作粗略優先級排序。_

## 5. 限制

- Token 分詞使用簡易 regex，未處理複合詞、縮寫、CJK 文字；中文 description 的內部結構未被分析。
- 候選類別建議基於關鍵字命中，**不代表新增該類別後 Other 桶會大幅縮小** —— 需先設計具體 keyword + priority 規則並重跑 classify.py 才能評估效果。
- 本檔每次跑 `python -m src.analyze_other` 重新生成；資料每日由 daily-refresh 工作流自動重抓後可一併重算。
