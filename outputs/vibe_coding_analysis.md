# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-24 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 135 | 13.5% |
| 訊號完整 | 853 | 85.3% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `kajisho5/ffmpeg-skill` | 1392 | 105 | 20d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 2 | `azerioid/azerioid-stack-manager` | 580 | 3 | 22d | **6** | desc:empty, license:none, low-forks:0.005, topics:none |
| 3 | `Faizpi/bank-sampah` | 509 | 1 | 12d | **6** | desc:empty, license:none, low-forks:0.002, topics:none |
| 4 | `HEJustinSun/my-girlfriend-jingtian-latex` | 4206 | 632 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `Mantitup-Org/vista` | 2385 | 48 | 19d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `cheng-haha/GPT-Policy` | 270 | 4 | 13d | **5** | desc:empty, license:none, generic-name:GPT-Policy, topics:none |
| 7 | `inclusionAI/Choruz` | 821 | 9 | 21d | **5** | desc:empty, low-forks:0.011, topics:none |
| 8 | `vinnylarouge/jevlike` | 1279 | 113 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `capncodes69/myfreebuff` | 510 | 3 | 19d | **5** | desc:empty, low-forks:0.006, topics:none |
| 10 | `Edge0-AI/Edge0` | 2064 | 183 | 15d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `anthropics/fermats-last-theorem` | 1223 | 106 | 19d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `Taichu-AI/ZDTaichu5.0-9B` | 1767 | 346 | 19d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `kvmem/kvmem-llama.cpp` | 570 | 51 | 9d | **4** | desc:empty, license:none, topics:none |
| 14 | `NxcoreAI/NxMem` | 994 | 107 | 13d | **4** | desc:empty, license:none, topics:none |
| 15 | `peggykangkang02/xialingguo-ip` | 183 | 34 | 13d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 117 | 11.7% |
| description <20 chars | 21 | 2.1% |
| no license | 298 | 29.8% |
| high-attention no-desc (stars>1k + empty desc) | 7 | 0.7% |
| low fork ratio (stars>500 + fsr<0.02) | 16 | 1.6% |
| overnight surge (>300 spd + <7 days) | 24 | 2.4% |
| generic-AI-buzzword name | 119 | 11.9% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| PHP | 2 |
| TeX | 1 |
| TypeScript | 1 |
| Rust | 1 |
| PowerShell | 1 |
| Lean | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 10 | 0 | 0 | 10 | 0.0% |
| 1000-4999 | 76 | 7 | 4 | 65 | 9.2% |
| 500-999 | 152 | 4 | 28 | 120 | 2.6% |
| 100-499 | 759 | 1 | 103 | 655 | 0.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `HEJustinSun/my-girlfriend-jingtian-latex` | 4206 | 632 | 27d | TeX | — |
| `Mantitup-Org/vista` | 2385 | 48 | 19d | TypeScript | — |
| `Edge0-AI/Edge0` | 2064 | 183 | 15d | Python | Apache-2.0 |
| `Taichu-AI/ZDTaichu5.0-9B` | 1767 | 346 | 19d | Python | Apache-2.0 |
| `kajisho5/ffmpeg-skill` | 1392 | 105 | 20d | Python | MIT |
| `vinnylarouge/jevlike` | 1279 | 113 | 7d | Python | MIT |
| `anthropics/fermats-last-theorem` | 1223 | 106 | 19d | Lean | Apache-2.0 |

### Generic-name pattern breakdown

Of 119 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 29 |
| `skill` | 25 |
| `agent` | 20 |
| `skills` | 12 |
| `codex` | 9 |
| `gpt` | 7 |
| `claude` | 4 |
| `llm` | 3 |
| `prompt` | 2 |
| `agents` | 2 |
| `toolkit` | 1 |
| `vibe` | 1 |
| `demo` | 1 |
| `starter` | 1 |
| `cookbook` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 559 (55.9%)
- Repos with at least one topic: 441 (44.1%)

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
