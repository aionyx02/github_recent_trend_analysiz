# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-22 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 14 | 1.4% |
| 待檢視 | 133 | 13.3% |
| 訊號完整 | 853 | 85.3% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Mantitup-Org/vista` | 2378 | 43 | 17d | **8** | desc:empty, license:none, high-attention-no-desc, low-forks:0.018, topics:none |
| 2 | `NandhaKishorM/laya` | 13795 | 1118 | 3d | **6** | desc:empty, high-attention-no-desc, overnight-surge:4598/day, topics:none |
| 3 | `HEJustinSun/my-girlfriend-jingtian-latex` | 4211 | 634 | 25d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `azerioid/azerioid-stack-manager` | 531 | 1 | 20d | **6** | desc:empty, license:none, low-forks:0.002, topics:none |
| 5 | `kajisho5/ffmpeg-skill` | 1355 | 100 | 18d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 6 | `Faizpi/bank-sampah` | 647 | 1 | 10d | **6** | desc:empty, license:none, low-forks:0.002, topics:none |
| 7 | `cheng-haha/GPT-Policy` | 256 | 4 | 11d | **5** | desc:empty, license:none, generic-name:GPT-Policy, topics:none |
| 8 | `capncodes69/myfreebuff` | 649 | 3 | 17d | **5** | desc:empty, low-forks:0.005, topics:none |
| 9 | `vinnylarouge/jevlike` | 1198 | 108 | 5d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `inclusionAI/Choruz` | 789 | 9 | 19d | **5** | desc:empty, low-forks:0.011, topics:none |
| 11 | `Edge0-AI/Edge0` | 2041 | 181 | 13d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `Taichu-AI/ZDTaichu5.0-9B` | 1093 | 242 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `anthropics/fermats-last-theorem` | 1215 | 104 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `tobi/walgit` | 2548 | 155 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `www222fff/free-router-proxy` | 467 | 53 | 27d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 116 | 11.6% |
| description <20 chars | 22 | 2.2% |
| no license | 296 | 29.6% |
| high-attention no-desc (stars>1k + empty desc) | 9 | 0.9% |
| low fork ratio (stars>500 + fsr<0.02) | 18 | 1.8% |
| overnight surge (>300 spd + <7 days) | 25 | 2.5% |
| generic-AI-buzzword name | 111 | 11.1% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| PHP | 2 |
| Rust | 2 |
| TypeScript | 1 |
| TeX | 1 |
| PowerShell | 1 |
| Lean | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 1 | 0 | 2 | 33.3% |
| 5000-9999 | 6 | 0 | 0 | 6 | 0.0% |
| 1000-4999 | 84 | 8 | 4 | 72 | 9.5% |
| 500-999 | 136 | 4 | 26 | 106 | 2.9% |
| 100-499 | 771 | 1 | 103 | 667 | 0.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `NandhaKishorM/laya` | 13795 | 1118 | 3d | Python | Apache-2.0 |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 4211 | 634 | 25d | TeX | — |
| `tobi/walgit` | 2548 | 155 | 29d | Rust | MIT |
| `Mantitup-Org/vista` | 2378 | 43 | 17d | TypeScript | — |
| `Edge0-AI/Edge0` | 2041 | 181 | 13d | Python | Apache-2.0 |
| `kajisho5/ffmpeg-skill` | 1355 | 100 | 18d | Python | MIT |
| `anthropics/fermats-last-theorem` | 1215 | 104 | 17d | Lean | Apache-2.0 |
| `vinnylarouge/jevlike` | 1198 | 108 | 5d | Python | MIT |
| `Taichu-AI/ZDTaichu5.0-9B` | 1093 | 242 | 17d | Python | Apache-2.0 |

### Generic-name pattern breakdown

Of 111 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 26 |
| `awesome` | 25 |
| `agent` | 18 |
| `skills` | 11 |
| `gpt` | 8 |
| `codex` | 7 |
| `claude` | 5 |
| `agents` | 2 |
| `prompt` | 2 |
| `llm` | 2 |
| `toolkit` | 1 |
| `demo` | 1 |
| `vibe` | 1 |
| `starter` | 1 |
| `cookbook` | 1 |

### Topics coverage

- Repos with **zero topics**: 568 (56.8%)
- Repos with at least one topic: 432 (43.2%)

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
