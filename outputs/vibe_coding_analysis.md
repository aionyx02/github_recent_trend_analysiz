# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-29 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 115 | 11.5% |
| 訊號完整 | 871 | 87.1% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Mantitup-Org/vista` | 2392 | 47 | 24d | **8** | desc:empty, license:none, high-attention-no-desc, low-forks:0.020, topics:none |
| 2 | `Contrastive-LM/CLM` | 2410 | 212 | 5d | **6** | desc:empty, high-attention-no-desc, overnight-surge:482/day, topics:none |
| 3 | `kajisho5/ffmpeg-skill` | 1432 | 117 | 25d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 4 | `azerioid/azerioid-stack-manager` | 721 | 4 | 27d | **6** | desc:empty, license:none, low-forks:0.006, topics:none |
| 5 | `NxcoreAI/NxMem` | 1091 | 107 | 18d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `Observal/Axl` | 1153 | 698 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `xikhar/spiderbench` | 417 | 74 | 1d | **5** | desc:empty, license:none, overnight-surge:417/day, topics:none |
| 8 | `anthropics/fermats-last-theorem` | 1237 | 106 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `Edge0-AI/Edge0` | 2132 | 192 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `inclusionAI/Choruz` | 873 | 9 | 26d | **5** | desc:empty, low-forks:0.010, topics:none |
| 11 | `Lumid-Off/AirCard-Windows` | 1027 | 71 | 10d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `Taichu-AI/ZDTaichu5.0-9B` | 1944 | 359 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `vinnylarouge/jevlike` | 1332 | 118 | 12d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `reladraw/reladraw` | 954 | 16 | 21d | **5** | desc:empty, low-forks:0.017, topics:none |
| 15 | `leoliu0/ratex` | 172 | 3 | 12d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 106 | 10.6% |
| description <20 chars | 20 | 2.0% |
| no license | 299 | 29.9% |
| high-attention no-desc (stars>1k + empty desc) | 10 | 1.0% |
| low fork ratio (stars>500 + fsr<0.02) | 16 | 1.6% |
| overnight surge (>300 spd + <7 days) | 13 | 1.3% |
| generic-AI-buzzword name | 124 | 12.4% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| TypeScript | 4 |
| Rust | 2 |
| PHP | 1 |
| JavaScript | 1 |
| Lean | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 8 | 0 | 0 | 8 | 0.0% |
| 1000-4999 | 84 | 10 | 2 | 72 | 11.9% |
| 500-999 | 156 | 3 | 22 | 131 | 1.9% |
| 100-499 | 749 | 1 | 91 | 657 | 0.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `Contrastive-LM/CLM` | 2410 | 212 | 5d | Python | Apache-2.0 |
| `Mantitup-Org/vista` | 2392 | 47 | 24d | TypeScript | — |
| `Edge0-AI/Edge0` | 2132 | 192 | 20d | Python | Apache-2.0 |
| `Taichu-AI/ZDTaichu5.0-9B` | 1944 | 359 | 24d | Python | Apache-2.0 |
| `kajisho5/ffmpeg-skill` | 1432 | 117 | 25d | Python | MIT |
| `vinnylarouge/jevlike` | 1332 | 118 | 12d | Python | MIT |
| `anthropics/fermats-last-theorem` | 1237 | 106 | 24d | Lean | Apache-2.0 |
| `Observal/Axl` | 1153 | 698 | 29d | TypeScript | Apache-2.0 |
| `NxcoreAI/NxMem` | 1091 | 107 | 18d | TypeScript | — |
| `Lumid-Off/AirCard-Windows` | 1027 | 71 | 10d | Rust | MIT |

### Generic-name pattern breakdown

Of 124 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 34 |
| `skill` | 25 |
| `agent` | 20 |
| `skills` | 10 |
| `codex` | 9 |
| `gpt` | 6 |
| `claude` | 6 |
| `llm` | 5 |
| `prompt` | 2 |
| `agents` | 2 |
| `toolkit` | 1 |
| `demo` | 1 |
| `vibe` | 1 |
| `cookbook` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 564 (56.4%)
- Repos with at least one topic: 436 (43.6%)

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
