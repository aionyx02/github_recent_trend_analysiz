# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-26 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 124 | 12.4% |
| 訊號完整 | 864 | 86.4% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Mantitup-Org/vista` | 2402 | 47 | 21d | **8** | desc:empty, license:none, high-attention-no-desc, low-forks:0.020, topics:none |
| 2 | `Contrastive-LM/CLM` | 1386 | 107 | 2d | **6** | desc:empty, high-attention-no-desc, overnight-surge:693/day, topics:none |
| 3 | `NxcoreAI/NxMem` | 1023 | 107 | 15d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `kajisho5/ffmpeg-skill` | 1409 | 109 | 22d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 5 | `azerioid/azerioid-stack-manager` | 721 | 3 | 24d | **6** | desc:empty, license:none, low-forks:0.004, topics:none |
| 6 | `HEJustinSun/my-girlfriend-jingtian-latex` | 4201 | 631 | 29d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `Taichu-AI/ZDTaichu5.0-9B` | 1587 | 271 | 21d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `inclusionAI/Choruz` | 844 | 9 | 23d | **5** | desc:empty, low-forks:0.011, topics:none |
| 9 | `Observal/Axl` | 1152 | 696 | 26d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `Edge0-AI/Edge0` | 2097 | 186 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `anthropics/fermats-last-theorem` | 1226 | 106 | 21d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `vinnylarouge/jevlike` | 1303 | 115 | 9d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `inclusionAI/LLaDA-Image` | 260 | 11 | 25d | **4** | desc:empty, license:none, topics:none |
| 14 | `TaoLiveAIGC/TaoMate-H3` | 473 | 45 | 20d | **4** | desc:empty, license:none, topics:none |
| 15 | `himdo/Fable-2-Recomp` | 256 | 7 | 26d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 112 | 11.2% |
| description <20 chars | 22 | 2.2% |
| no license | 287 | 28.7% |
| high-attention no-desc (stars>1k + empty desc) | 10 | 1.0% |
| low fork ratio (stars>500 + fsr<0.02) | 12 | 1.2% |
| overnight surge (>300 spd + <7 days) | 14 | 1.4% |
| generic-AI-buzzword name | 119 | 11.9% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| TypeScript | 3 |
| PHP | 1 |
| TeX | 1 |
| Rust | 1 |
| Lean | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 10 | 0 | 0 | 10 | 0.0% |
| 1000-4999 | 85 | 10 | 3 | 72 | 11.8% |
| 500-999 | 146 | 2 | 20 | 124 | 1.4% |
| 100-499 | 756 | 0 | 101 | 655 | 0.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `HEJustinSun/my-girlfriend-jingtian-latex` | 4201 | 631 | 29d | TeX | — |
| `Mantitup-Org/vista` | 2402 | 47 | 21d | TypeScript | — |
| `Edge0-AI/Edge0` | 2097 | 186 | 17d | Python | Apache-2.0 |
| `Taichu-AI/ZDTaichu5.0-9B` | 1587 | 271 | 21d | Python | Apache-2.0 |
| `kajisho5/ffmpeg-skill` | 1409 | 109 | 22d | Python | MIT |
| `Contrastive-LM/CLM` | 1386 | 107 | 2d | Python | Apache-2.0 |
| `vinnylarouge/jevlike` | 1303 | 115 | 9d | Python | MIT |
| `anthropics/fermats-last-theorem` | 1226 | 106 | 21d | Lean | Apache-2.0 |
| `Observal/Axl` | 1152 | 696 | 26d | TypeScript | Apache-2.0 |
| `NxcoreAI/NxMem` | 1023 | 107 | 15d | TypeScript | — |

### Generic-name pattern breakdown

Of 119 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 31 |
| `skill` | 22 |
| `agent` | 20 |
| `skills` | 12 |
| `codex` | 9 |
| `gpt` | 6 |
| `claude` | 4 |
| `llm` | 4 |
| `prompt` | 3 |
| `agents` | 2 |
| `toolkit` | 1 |
| `demo` | 1 |
| `starter` | 1 |
| `vibe` | 1 |
| `cookbook` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 558 (55.8%)
- Repos with at least one topic: 442 (44.2%)

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
