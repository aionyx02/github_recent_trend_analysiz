# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-10-16 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 117 | 11.7% |
| 訊號完整 | 870 | 87.0% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `liseami/CCBaga` | 2382 | 239 | 4d | **6** | desc:empty, high-attention-no-desc, overnight-surge:596/day, topics:none |
| 2 | `openai/math` | 14990 | 1721 | 9d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 3 | `vinnylarouge/jevlike` | 1352 | 121 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 4 | `wy51ai/floorplan-3d` | 2341 | 446 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 5 | `kargulstudio/sales-crm` | 1714 | 376 | 11d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 6 | `fsiaonma/elpis` | 585 | 6 | 16d | **5** | desc:short, license:none, low-forks:0.010, topics:none |
| 7 | `Hiveporattle/tvemltxa` | 567 | 0 | 14d | **5** | desc:empty, license:none, low-forks:0.000 |
| 8 | `deadinside28/bloodborne_pc` | 2990 | 685 | 14d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `cloudflare/forge` | 1131 | 48 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `anthropics/oss-scanner` | 1040 | 565 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `Dingo-Shenanigans/ReSkate` | 1158 | 191 | 13d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `Lumid-Off/AirCard-Windows` | 1385 | 111 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `google-research/rrsi` | 1525 | 147 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `slop-place/zulu` | 888 | 3 | 23d | **4** | license:none, low-forks:0.003, topics:none |
| 15 | `pbs05/ponwrt` | 276 | 222 | 22d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 96 | 9.6% |
| description <20 chars | 15 | 1.5% |
| no license | 244 | 24.4% |
| high-attention no-desc (stars>1k + empty desc) | 11 | 1.1% |
| low fork ratio (stars>500 + fsr<0.02) | 19 | 1.9% |
| overnight surge (>300 spd + <7 days) | 19 | 1.9% |
| generic-AI-buzzword name | 103 | 10.3% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| TypeScript | 3 |
| Rust | 2 |
| Python | 2 |
| C++ | 2 |
| Lean | 1 |
| HTML | 1 |
| Unknown | 1 |
| Dockerfile | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 15 | 1 | 0 | 14 | 6.7% |
| 5000-9999 | 16 | 0 | 0 | 16 | 0.0% |
| 1000-4999 | 140 | 10 | 8 | 122 | 7.1% |
| 500-999 | 192 | 2 | 23 | 167 | 1.0% |
| 100-499 | 637 | 0 | 86 | 551 | 0.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `openai/math` | 14990 | 1721 | 9d | Lean | Apache-2.0 |
| `deadinside28/bloodborne_pc` | 2990 | 685 | 14d | C++ | GPL-2.0 |
| `liseami/CCBaga` | 2382 | 239 | 4d | Rust | MIT |
| `wy51ai/floorplan-3d` | 2341 | 446 | 16d | HTML | MIT |
| `kargulstudio/sales-crm` | 1714 | 376 | 11d | TypeScript | MIT |
| `google-research/rrsi` | 1525 | 147 | 29d | Python | Apache-2.0 |
| `Lumid-Off/AirCard-Windows` | 1385 | 111 | 27d | Rust | MIT |
| `vinnylarouge/jevlike` | 1352 | 121 | 29d | Python | MIT |
| `Dingo-Shenanigans/ReSkate` | 1158 | 191 | 13d | C++ | GPL-3.0 |
| `cloudflare/forge` | 1131 | 48 | 24d | TypeScript | Apache-2.0 |
| `anthropics/oss-scanner` | 1040 | 565 | 7d | Dockerfile | Apache-2.0 |

### Generic-name pattern breakdown

Of 103 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 25 |
| `skill` | 19 |
| `agent` | 16 |
| `claude` | 14 |
| `skills` | 12 |
| `llm` | 4 |
| `codex` | 4 |
| `vibe` | 2 |
| `demo` | 2 |
| `cookbook` | 1 |
| `prompt` | 1 |
| `gpt` | 1 |
| `toolkit` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 517 (51.7%)
- Repos with at least one topic: 483 (48.3%)

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
