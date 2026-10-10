# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-10-10 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 134 | 13.4% |
| 訊號完整 | 850 | 85.0% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `openai/math` | 13459 | 1477 | 3d | **6** | desc:empty, high-attention-no-desc, overnight-surge:4486/day, topics:none |
| 2 | `deillusion/Aha-Engine` | 586 | 4 | 29d | **6** | desc:empty, license:none, low-forks:0.007, topics:none |
| 3 | `Vodiwalker/vodiwalker_panel` | 1264 | 3376 | 29d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `wangmingxuan666/Tiersense` | 1300 | 212 | 15d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `kargulstudio/sales-crm` | 1683 | 368 | 5d | **6** | desc:empty, high-attention-no-desc, overnight-surge:337/day, topics:none |
| 6 | `wy51ai/floorplan-3d` | 2084 | 391 | 10d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `storytold/effectcraft` | 4222 | 1841 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `vinnylarouge/jevlike` | 1351 | 117 | 23d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `Spearmintai/mintocode` | 627 | 9 | 9d | **5** | desc:empty, low-forks:0.014, topics:none |
| 10 | `Lumid-Off/AirCard-Windows` | 1329 | 108 | 21d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `Contrastive-LM/CLM` | 2953 | 255 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `google-research/rrsi` | 1427 | 139 | 23d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `deadinside28/bloodborne_pc` | 2229 | 323 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `cloudflare/forge` | 1100 | 45 | 18d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `storytold/designcraft` | 2356 | 1358 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 99 | 9.9% |
| description <20 chars | 14 | 1.4% |
| no license | 290 | 29.0% |
| high-attention no-desc (stars>1k + empty desc) | 13 | 1.3% |
| low fork ratio (stars>500 + fsr<0.02) | 32 | 3.2% |
| overnight surge (>300 spd + <7 days) | 48 | 4.8% |
| generic-AI-buzzword name | 102 | 10.2% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| TypeScript | 3 |
| Rust | 3 |
| Lean | 1 |
| JavaScript | 1 |
| Unknown | 1 |
| HTML | 1 |
| C++ | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 7 | 1 | 0 | 6 | 14.3% |
| 5000-9999 | 16 | 0 | 0 | 16 | 0.0% |
| 1000-4999 | 126 | 12 | 11 | 103 | 9.5% |
| 500-999 | 188 | 3 | 35 | 150 | 1.6% |
| 100-499 | 663 | 0 | 88 | 575 | 0.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `openai/math` | 13459 | 1477 | 3d | Lean | Apache-2.0 |
| `storytold/effectcraft` | 4222 | 1841 | 8d | Rust | Apache-2.0 |
| `Contrastive-LM/CLM` | 2953 | 255 | 16d | Python | Apache-2.0 |
| `storytold/designcraft` | 2356 | 1358 | 8d | Rust | Apache-2.0 |
| `deadinside28/bloodborne_pc` | 2229 | 323 | 8d | C++ | GPL-2.0 |
| `wy51ai/floorplan-3d` | 2084 | 391 | 10d | HTML | MIT |
| `kargulstudio/sales-crm` | 1683 | 368 | 5d | TypeScript | MIT |
| `google-research/rrsi` | 1427 | 139 | 23d | Python | Apache-2.0 |
| `vinnylarouge/jevlike` | 1351 | 117 | 23d | Python | MIT |
| `Lumid-Off/AirCard-Windows` | 1329 | 108 | 21d | Rust | MIT |
| `wangmingxuan666/Tiersense` | 1300 | 212 | 15d | Unknown | — |
| `Vodiwalker/vodiwalker_panel` | 1264 | 3376 | 29d | Python | — |
| `cloudflare/forge` | 1100 | 45 | 18d | TypeScript | Apache-2.0 |

### Generic-name pattern breakdown

Of 102 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 27 |
| `skill` | 18 |
| `agent` | 17 |
| `skills` | 9 |
| `claude` | 8 |
| `codex` | 6 |
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

- Repos with **zero topics**: 527 (52.7%)
- Repos with at least one topic: 473 (47.3%)

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
