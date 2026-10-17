# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-10-17 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 12 | 1.2% |
| 待檢視 | 112 | 11.2% |
| 訊號完整 | 876 | 87.6% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `liseami/CCBaga` | 2483 | 248 | 5d | **6** | desc:empty, high-attention-no-desc, overnight-surge:497/day, topics:none |
| 2 | `openai/math` | 15063 | 1739 | 10d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 3 | `kargulstudio/sales-crm` | 1730 | 376 | 12d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 4 | `anthropics/oss-scanner` | 1068 | 583 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 5 | `cloudflare/forge` | 1136 | 48 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 6 | `Dingo-Shenanigans/ReSkate` | 1182 | 197 | 14d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `fyzugx/DEsk` | 1058 | 34 | 6d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `Lumid-Off/AirCard-Windows` | 1396 | 112 | 28d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `Tencent-Hunyuan/Hy-Memory` | 481 | 47 | 1d | **5** | desc:empty, license:none, overnight-surge:481/day, topics:none |
| 10 | `deadinside28/bloodborne_pc` | 3069 | 734 | 15d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `wy51ai/floorplan-3d` | 2364 | 450 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `fsiaonma/elpis` | 586 | 6 | 17d | **5** | desc:short, license:none, low-forks:0.010, topics:none |
| 13 | `extend-hq/jevbox` | 728 | 81 | 17d | **4** | desc:empty, license:none, topics:none |
| 14 | `pbs05/ponwrt` | 279 | 226 | 23d | **4** | desc:empty, license:none, topics:none |
| 15 | `corvofeng/atv-core` | 378 | 19 | 20d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 90 | 9.0% |
| description <20 chars | 14 | 1.4% |
| no license | 230 | 23.0% |
| high-attention no-desc (stars>1k + empty desc) | 10 | 1.0% |
| low fork ratio (stars>500 + fsr<0.02) | 18 | 1.8% |
| overnight surge (>300 spd + <7 days) | 18 | 1.8% |
| generic-AI-buzzword name | 102 | 10.2% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| TypeScript | 3 |
| Rust | 2 |
| C++ | 2 |
| Lean | 1 |
| Dockerfile | 1 |
| C | 1 |
| Python | 1 |
| HTML | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 13 | 1 | 0 | 12 | 7.7% |
| 5000-9999 | 15 | 0 | 0 | 15 | 0.0% |
| 1000-4999 | 139 | 9 | 8 | 122 | 6.5% |
| 500-999 | 182 | 1 | 24 | 157 | 0.5% |
| 100-499 | 651 | 1 | 80 | 570 | 0.2% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `openai/math` | 15063 | 1739 | 10d | Lean | Apache-2.0 |
| `deadinside28/bloodborne_pc` | 3069 | 734 | 15d | C++ | GPL-2.0 |
| `liseami/CCBaga` | 2483 | 248 | 5d | Rust | MIT |
| `wy51ai/floorplan-3d` | 2364 | 450 | 17d | HTML | MIT |
| `kargulstudio/sales-crm` | 1730 | 376 | 12d | TypeScript | MIT |
| `Lumid-Off/AirCard-Windows` | 1396 | 112 | 28d | Rust | MIT |
| `Dingo-Shenanigans/ReSkate` | 1182 | 197 | 14d | C++ | GPL-3.0 |
| `cloudflare/forge` | 1136 | 48 | 25d | TypeScript | Apache-2.0 |
| `anthropics/oss-scanner` | 1068 | 583 | 8d | Dockerfile | Apache-2.0 |
| `fyzugx/DEsk` | 1058 | 34 | 6d | C | MIT |

### Generic-name pattern breakdown

Of 102 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 25 |
| `skill` | 19 |
| `agent` | 16 |
| `claude` | 15 |
| `skills` | 10 |
| `codex` | 5 |
| `llm` | 3 |
| `prompt` | 2 |
| `vibe` | 2 |
| `demo` | 2 |
| `cookbook` | 1 |
| `gpt` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 522 (52.2%)
- Repos with at least one topic: 478 (47.8%)

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
