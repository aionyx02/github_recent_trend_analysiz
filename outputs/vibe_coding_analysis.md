# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-10-12 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 11 | 1.1% |
| 待檢視 | 117 | 11.7% |
| 訊號完整 | 872 | 87.2% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `openai/math` | 14327 | 1617 | 5d | **6** | desc:empty, high-attention-no-desc, overnight-surge:2865/day, topics:none |
| 2 | `liseami/CCBaga` | 1426 | 136 | 1d | **6** | desc:empty, high-attention-no-desc, overnight-surge:1426/day, topics:none |
| 3 | `vinnylarouge/jevlike` | 1350 | 119 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 4 | `wy51ai/floorplan-3d` | 2180 | 415 | 12d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 5 | `kargulstudio/sales-crm` | 1702 | 376 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 6 | `cloudflare/forge` | 1116 | 45 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `jwuthri-cloud/Tracely-ai` | 481 | 69 | 1d | **5** | desc:empty, license:none, overnight-surge:481/day, topics:none |
| 8 | `Lumid-Off/AirCard-Windows` | 1350 | 107 | 23d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `google-research/rrsi` | 1467 | 142 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `fsiaonma/elpis` | 580 | 5 | 12d | **5** | desc:short, license:none, low-forks:0.009, topics:none |
| 11 | `deadinside28/bloodborne_pc` | 2564 | 407 | 10d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `HytidelLegend/ai-aug-edu` | 453 | 58 | 18d | **4** | desc:empty, license:none, topics:none |
| 13 | `raw13g/raw13g.github.io` | 205 | 204 | 22d | **4** | desc:empty, license:none, topics:none |
| 14 | `anthropics/claude-code-playground` | 212 | 18 | 16d | **4** | desc:empty, generic-name:claude-code-playground, topics:none |
| 15 | `extend-hq/jevbox` | 713 | 81 | 12d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 92 | 9.2% |
| description <20 chars | 12 | 1.2% |
| no license | 246 | 24.6% |
| high-attention no-desc (stars>1k + empty desc) | 9 | 0.9% |
| low fork ratio (stars>500 + fsr<0.02) | 18 | 1.8% |
| overnight surge (>300 spd + <7 days) | 33 | 3.3% |
| generic-AI-buzzword name | 96 | 9.6% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| TypeScript | 3 |
| Rust | 2 |
| Python | 2 |
| Lean | 1 |
| HTML | 1 |
| Unknown | 1 |
| C++ | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 12 | 1 | 0 | 11 | 8.3% |
| 5000-9999 | 15 | 0 | 0 | 15 | 0.0% |
| 1000-4999 | 130 | 8 | 9 | 113 | 6.2% |
| 500-999 | 181 | 1 | 26 | 154 | 0.6% |
| 100-499 | 662 | 1 | 82 | 579 | 0.2% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `openai/math` | 14327 | 1617 | 5d | Lean | Apache-2.0 |
| `deadinside28/bloodborne_pc` | 2564 | 407 | 10d | C++ | GPL-2.0 |
| `wy51ai/floorplan-3d` | 2180 | 415 | 12d | HTML | MIT |
| `kargulstudio/sales-crm` | 1702 | 376 | 7d | TypeScript | MIT |
| `google-research/rrsi` | 1467 | 142 | 25d | Python | Apache-2.0 |
| `liseami/CCBaga` | 1426 | 136 | 1d | Rust | MIT |
| `vinnylarouge/jevlike` | 1350 | 119 | 25d | Python | MIT |
| `Lumid-Off/AirCard-Windows` | 1350 | 107 | 23d | Rust | MIT |
| `cloudflare/forge` | 1116 | 45 | 20d | TypeScript | Apache-2.0 |

### Generic-name pattern breakdown

Of 96 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 27 |
| `skill` | 17 |
| `agent` | 14 |
| `skills` | 10 |
| `claude` | 9 |
| `codex` | 5 |
| `llm` | 4 |
| `gpt` | 2 |
| `vibe` | 2 |
| `demo` | 2 |
| `cookbook` | 1 |
| `toolkit` | 1 |
| `prompt` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 545 (54.5%)
- Repos with at least one topic: 455 (45.5%)

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
