# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-25 | Sample size: 1000 repos (with topics signal)_

## 定義 / Definition

**公開 metadata 完整度** = repo 的可見 metadata 訊號（description、license、
topics、fork-star 比例等）相對於其 stars 數的「完整程度」。

我們將高分組命名為 **低資訊密度 (low-information-density candidate)**：
stars 不需太多努力就能累積，但 description、tags、forks、license 都需要實際付出。
**高分代表公開 metadata 訊號可疑，不代表該 repo 一定無價值** —— 
`awesome-*` 列表、學術研究 repo、官方快速釋出 repo 都可能踩到訊號。
此指標衡量公開產出，不衡量作者本人，也不是對 vibe-coding 這個編程方式的評價。

## 評分機制 / Scoring rubric

| Signal | Points | Rationale |
|---|---:|---|
| `description` empty | +2 | Highest single signal of metadata gap |
| `description` < 20 chars | +1 | Marginal |
| No license declared | +1 | Common OSS-hygiene gap |
| stars > 1000 AND description empty | +2 | High-attention low-description |
| fork_star_ratio < 0.02 AND stars > 500 | +2 | Stars but very few forks |
| stars_per_day > 300 AND age_days < 7 | +1 | Overnight surge |
| Name matches generic-AI-buzzword pattern | +1 | `*-skills`, `*-agent`, `*-cookbook` ... |
| No topics tagged | +1 | Only when topics data present |

**Tiers**: 0-2 訊號完整 · 3-4 待檢視 · 5+ 低資訊密度

## 結果 / Findings

| Tier | Count | % of sample |
|---|---:|---:|
| 低資訊密度 | 13 | 1.3% |
| 待檢視 | 123 | 12.3% |
| 訊號完整 | 864 | 86.4% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `kajisho5/ffmpeg-skill` | 1401 | 107 | 21d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 2 | `azerioid/azerioid-stack-manager` | 674 | 3 | 23d | **6** | desc:empty, license:none, low-forks:0.004, topics:none |
| 3 | `Contrastive-LM/CLM` | 1041 | 74 | 1d | **6** | desc:empty, high-attention-no-desc, overnight-surge:1041/day, topics:none |
| 4 | `HEJustinSun/my-girlfriend-jingtian-latex` | 4204 | 632 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `Mantitup-Org/vista` | 2388 | 48 | 20d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `Faizpi/bank-sampah` | 505 | 1 | 13d | **6** | desc:empty, license:none, low-forks:0.002, topics:none |
| 7 | `Observal/Axl` | 1147 | 692 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `capncodes69/myfreebuff` | 506 | 3 | 20d | **5** | desc:empty, low-forks:0.006, topics:none |
| 9 | `vinnylarouge/jevlike` | 1298 | 114 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `Taichu-AI/ZDTaichu5.0-9B` | 2086 | 398 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `Edge0-AI/Edge0` | 2071 | 183 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `inclusionAI/Choruz` | 834 | 9 | 22d | **5** | desc:empty, low-forks:0.011, topics:none |
| 13 | `anthropics/fermats-last-theorem` | 1226 | 106 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `TaoLiveAIGC/TaoMate-H3` | 457 | 43 | 19d | **4** | desc:empty, license:none, topics:none |
| 15 | `taeold/djev-run` | 544 | 32 | 4d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 109 | 10.9% |
| description <20 chars | 21 | 2.1% |
| no license | 289 | 28.9% |
| high-attention no-desc (stars>1k + empty desc) | 9 | 0.9% |
| low fork ratio (stars>500 + fsr<0.02) | 16 | 1.6% |
| overnight surge (>300 spd + <7 days) | 21 | 2.1% |
| generic-AI-buzzword name | 120 | 12.0% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| PHP | 2 |
| TypeScript | 2 |
| TeX | 1 |
| PowerShell | 1 |
| Rust | 1 |
| Lean | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 11 | 0 | 0 | 11 | 0.0% |
| 1000-4999 | 81 | 9 | 3 | 69 | 11.1% |
| 500-999 | 154 | 4 | 26 | 124 | 2.6% |
| 100-499 | 751 | 0 | 94 | 657 | 0.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `HEJustinSun/my-girlfriend-jingtian-latex` | 4204 | 632 | 28d | TeX | — |
| `Mantitup-Org/vista` | 2388 | 48 | 20d | TypeScript | — |
| `Taichu-AI/ZDTaichu5.0-9B` | 2086 | 398 | 20d | Python | Apache-2.0 |
| `Edge0-AI/Edge0` | 2071 | 183 | 16d | Python | Apache-2.0 |
| `kajisho5/ffmpeg-skill` | 1401 | 107 | 21d | Python | MIT |
| `vinnylarouge/jevlike` | 1298 | 114 | 8d | Python | MIT |
| `anthropics/fermats-last-theorem` | 1226 | 106 | 20d | Lean | Apache-2.0 |
| `Observal/Axl` | 1147 | 692 | 25d | TypeScript | Apache-2.0 |
| `Contrastive-LM/CLM` | 1041 | 74 | 1d | Python | Apache-2.0 |

### Generic-name pattern breakdown

Of 120 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 31 |
| `skill` | 25 |
| `agent` | 19 |
| `skills` | 12 |
| `codex` | 9 |
| `gpt` | 7 |
| `claude` | 3 |
| `prompt` | 3 |
| `llm` | 3 |
| `agents` | 2 |
| `toolkit` | 1 |
| `starter` | 1 |
| `vibe` | 1 |
| `demo` | 1 |
| `cookbook` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 552 (55.2%)
- Repos with at least one topic: 448 (44.8%)

## Methodology limits

- Stars are not a proxy for code quality. A high score is a *signal-level*
  suspicion that public metadata is sparse, not a verdict that the repo lacks value.
- The generic-name regex is intentionally narrow. False positives are possible
  (e.g., a legitimate `awesome-*` curated list).
- 30-day creation window biases toward repos that haven't had time to accumulate forks.
- We do not inspect commit graph, contributor count, or README length — those would
  tighten the signal but cost extra API calls per repo.

## Reproduce

```bash
python -m src.analyze_vibe
```
