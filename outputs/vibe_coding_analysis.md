# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-10-14 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 111 | 11.1% |
| 訊號完整 | 877 | 87.7% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `liseami/CCBaga` | 2205 | 219 | 2d | **6** | desc:empty, high-attention-no-desc, overnight-surge:1102/day, topics:none |
| 2 | `h0m3us3r/w1700k-sdr` | 698 | 70 | 2d | **5** | desc:empty, license:none, overnight-surge:349/day, topics:none |
| 3 | `cloudflare/forge` | 1123 | 46 | 22d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 4 | `Dingo-Shenanigans/ReSkate` | 1068 | 181 | 11d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 5 | `vinnylarouge/jevlike` | 1353 | 120 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 6 | `Lumid-Off/AirCard-Windows` | 1367 | 110 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `fsiaonma/elpis` | 584 | 6 | 14d | **5** | desc:short, license:none, low-forks:0.010, topics:none |
| 8 | `google-research/rrsi` | 1499 | 144 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `wy51ai/floorplan-3d` | 2252 | 429 | 14d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `kargulstudio/sales-crm` | 1709 | 377 | 9d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `deadinside28/bloodborne_pc` | 2790 | 560 | 12d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `openai/math` | 14745 | 1680 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `YeonwooSung/llm-architecture-from-scratch` | 717 | 1 | 27d | **4** | license:none, low-forks:0.001, generic-name:llm-architecture-from-scratch |
| 14 | `LSPosed/ZygiskNext` | 895 | 17 | 24d | **4** | license:none, low-forks:0.019, topics:none |
| 15 | `slop-place/zulu` | 887 | 3 | 21d | **4** | license:none, low-forks:0.003, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 87 | 8.7% |
| description <20 chars | 15 | 1.5% |
| no license | 238 | 23.8% |
| high-attention no-desc (stars>1k + empty desc) | 10 | 1.0% |
| low fork ratio (stars>500 + fsr<0.02) | 19 | 1.9% |
| overnight surge (>300 spd + <7 days) | 35 | 3.5% |
| generic-AI-buzzword name | 102 | 10.2% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| TypeScript | 3 |
| Rust | 2 |
| C++ | 2 |
| Python | 2 |
| C | 1 |
| HTML | 1 |
| Lean | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 14 | 1 | 0 | 13 | 7.1% |
| 5000-9999 | 14 | 0 | 0 | 14 | 0.0% |
| 1000-4999 | 136 | 9 | 10 | 117 | 6.6% |
| 500-999 | 185 | 2 | 20 | 163 | 1.1% |
| 100-499 | 651 | 0 | 81 | 570 | 0.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `openai/math` | 14745 | 1680 | 7d | Lean | Apache-2.0 |
| `deadinside28/bloodborne_pc` | 2790 | 560 | 12d | C++ | GPL-2.0 |
| `wy51ai/floorplan-3d` | 2252 | 429 | 14d | HTML | MIT |
| `liseami/CCBaga` | 2205 | 219 | 2d | Rust | MIT |
| `kargulstudio/sales-crm` | 1709 | 377 | 9d | TypeScript | MIT |
| `google-research/rrsi` | 1499 | 144 | 27d | Python | Apache-2.0 |
| `Lumid-Off/AirCard-Windows` | 1367 | 110 | 25d | Rust | MIT |
| `vinnylarouge/jevlike` | 1353 | 120 | 27d | Python | MIT |
| `cloudflare/forge` | 1123 | 46 | 22d | TypeScript | Apache-2.0 |
| `Dingo-Shenanigans/ReSkate` | 1068 | 181 | 11d | C++ | GPL-3.0 |

### Generic-name pattern breakdown

Of 102 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 26 |
| `skill` | 19 |
| `agent` | 15 |
| `claude` | 13 |
| `skills` | 12 |
| `codex` | 5 |
| `llm` | 3 |
| `vibe` | 2 |
| `demo` | 2 |
| `cookbook` | 1 |
| `prompt` | 1 |
| `toolkit` | 1 |
| `gpt` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 535 (53.5%)
- Repos with at least one topic: 465 (46.5%)

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
