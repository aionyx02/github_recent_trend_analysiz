# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-10-09 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 16 | 1.6% |
| 待檢視 | 137 | 13.7% |
| 訊號完整 | 847 | 84.7% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `deillusion/Aha-Engine` | 572 | 4 | 28d | **6** | desc:empty, license:none, low-forks:0.007, topics:none |
| 2 | `wangmingxuan666/Tiersense` | 1179 | 199 | 14d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `Vodiwalker/vodiwalker_panel` | 1243 | 3322 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `ArasTey/lunel` | 1046 | 2498 | 29d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `openai/math` | 12770 | 1356 | 2d | **6** | desc:empty, high-attention-no-desc, overnight-surge:6385/day, topics:none |
| 6 | `kargulstudio/sales-crm` | 1666 | 362 | 4d | **6** | desc:empty, high-attention-no-desc, overnight-surge:416/day, topics:none |
| 7 | `fsiaonma/elpis` | 577 | 5 | 9d | **5** | desc:short, license:none, low-forks:0.009, topics:none |
| 8 | `cloudflare/forge` | 1088 | 44 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `deadinside28/bloodborne_pc` | 2064 | 261 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `storytold/effectcraft` | 3381 | 1437 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `storytold/designcraft` | 1898 | 1049 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `Contrastive-LM/CLM` | 2939 | 252 | 15d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `vinnylarouge/jevlike` | 1353 | 118 | 22d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `google-research/rrsi` | 1398 | 139 | 22d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `Lumid-Off/AirCard-Windows` | 1319 | 107 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 107 | 10.7% |
| description <20 chars | 15 | 1.5% |
| no license | 260 | 26.0% |
| high-attention no-desc (stars>1k + empty desc) | 14 | 1.4% |
| low fork ratio (stars>500 + fsr<0.02) | 25 | 2.5% |
| overnight surge (>300 spd + <7 days) | 25 | 2.5% |
| generic-AI-buzzword name | 106 | 10.6% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| TypeScript | 3 |
| Rust | 3 |
| JavaScript | 1 |
| Unknown | 1 |
| Lean | 1 |
| C++ | 1 |
| HTML | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 7 | 1 | 0 | 6 | 14.3% |
| 5000-9999 | 15 | 0 | 0 | 15 | 0.0% |
| 1000-4999 | 122 | 13 | 10 | 99 | 10.7% |
| 500-999 | 176 | 2 | 27 | 147 | 1.1% |
| 100-499 | 680 | 0 | 100 | 580 | 0.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `openai/math` | 12770 | 1356 | 2d | Lean | Apache-2.0 |
| `storytold/effectcraft` | 3381 | 1437 | 7d | Rust | Apache-2.0 |
| `Contrastive-LM/CLM` | 2939 | 252 | 15d | Python | Apache-2.0 |
| `deadinside28/bloodborne_pc` | 2064 | 261 | 7d | C++ | GPL-2.0 |
| `wy51ai/floorplan-3d` | 1956 | 362 | 9d | HTML | MIT |
| `storytold/designcraft` | 1898 | 1049 | 7d | Rust | Apache-2.0 |
| `kargulstudio/sales-crm` | 1666 | 362 | 4d | TypeScript | MIT |
| `google-research/rrsi` | 1398 | 139 | 22d | Python | Apache-2.0 |
| `vinnylarouge/jevlike` | 1353 | 118 | 22d | Python | MIT |
| `Lumid-Off/AirCard-Windows` | 1319 | 107 | 20d | Rust | MIT |
| `Vodiwalker/vodiwalker_panel` | 1243 | 3322 | 28d | Python | — |
| `wangmingxuan666/Tiersense` | 1179 | 199 | 14d | Unknown | — |
| `cloudflare/forge` | 1088 | 44 | 17d | TypeScript | Apache-2.0 |
| `ArasTey/lunel` | 1046 | 2498 | 29d | Python | — |

### Generic-name pattern breakdown

Of 106 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 29 |
| `skill` | 21 |
| `agent` | 16 |
| `skills` | 9 |
| `codex` | 7 |
| `claude` | 7 |
| `gpt` | 4 |
| `llm` | 3 |
| `demo` | 2 |
| `cookbook` | 2 |
| `vibe` | 2 |
| `agents` | 1 |
| `prompt` | 1 |
| `toolkit` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 561 (56.1%)
- Repos with at least one topic: 439 (43.9%)

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
