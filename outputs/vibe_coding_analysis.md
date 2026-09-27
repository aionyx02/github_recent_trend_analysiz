# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-27 | Sample size: 1000 repos (with topics signal)_

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
| 1 | `Mantitup-Org/vista` | 2400 | 47 | 22d | **8** | desc:empty, license:none, high-attention-no-desc, low-forks:0.020, topics:none |
| 2 | `Contrastive-LM/CLM` | 1737 | 149 | 3d | **6** | desc:empty, high-attention-no-desc, overnight-surge:579/day, topics:none |
| 3 | `kajisho5/ffmpeg-skill` | 1417 | 110 | 23d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 4 | `azerioid/azerioid-stack-manager` | 725 | 3 | 25d | **6** | desc:empty, license:none, low-forks:0.004, topics:none |
| 5 | `NxcoreAI/NxMem` | 1056 | 107 | 16d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `Taichu-AI/ZDTaichu5.0-9B` | 1883 | 315 | 22d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `anthropics/fermats-last-theorem` | 1228 | 106 | 22d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `reladraw/reladraw` | 591 | 6 | 19d | **5** | desc:empty, low-forks:0.010, topics:none |
| 9 | `inclusionAI/Choruz` | 853 | 9 | 24d | **5** | desc:empty, low-forks:0.011, topics:none |
| 10 | `Edge0-AI/Edge0` | 2103 | 191 | 18d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `vinnylarouge/jevlike` | 1314 | 116 | 10d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `Observal/Axl` | 1152 | 698 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `Vodiwalker/vodiwalker_panel` | 905 | 2344 | 16d | **4** | desc:empty, license:none, topics:none |
| 14 | `niedachu/MateriaSim` | 293 | 11 | 12d | **4** | desc:empty, license:none, topics:none |
| 15 | `gireeshkumarreddy/cinematic-portofilo` | 149 | 61 | 21d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 111 | 11.1% |
| description <20 chars | 23 | 2.3% |
| no license | 282 | 28.2% |
| high-attention no-desc (stars>1k + empty desc) | 9 | 0.9% |
| low fork ratio (stars>500 + fsr<0.02) | 15 | 1.5% |
| overnight surge (>300 spd + <7 days) | 13 | 1.3% |
| generic-AI-buzzword name | 125 | 12.5% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| TypeScript | 4 |
| PHP | 1 |
| Lean | 1 |
| Rust | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 10 | 0 | 0 | 10 | 0.0% |
| 1000-4999 | 82 | 9 | 3 | 70 | 11.0% |
| 500-999 | 144 | 3 | 18 | 123 | 2.1% |
| 100-499 | 761 | 0 | 103 | 658 | 0.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `Mantitup-Org/vista` | 2400 | 47 | 22d | TypeScript | — |
| `Edge0-AI/Edge0` | 2103 | 191 | 18d | Python | Apache-2.0 |
| `Taichu-AI/ZDTaichu5.0-9B` | 1883 | 315 | 22d | Python | Apache-2.0 |
| `Contrastive-LM/CLM` | 1737 | 149 | 3d | Python | Apache-2.0 |
| `kajisho5/ffmpeg-skill` | 1417 | 110 | 23d | Python | MIT |
| `vinnylarouge/jevlike` | 1314 | 116 | 10d | Python | MIT |
| `anthropics/fermats-last-theorem` | 1228 | 106 | 22d | Lean | Apache-2.0 |
| `Observal/Axl` | 1152 | 698 | 27d | TypeScript | Apache-2.0 |
| `NxcoreAI/NxMem` | 1056 | 107 | 16d | TypeScript | — |

### Generic-name pattern breakdown

Of 125 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 33 |
| `skill` | 24 |
| `agent` | 22 |
| `skills` | 12 |
| `codex` | 9 |
| `gpt` | 6 |
| `claude` | 4 |
| `llm` | 4 |
| `prompt` | 3 |
| `agents` | 2 |
| `toolkit` | 1 |
| `vibe` | 1 |
| `demo` | 1 |
| `starter` | 1 |
| `cookbook` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 566 (56.6%)
- Repos with at least one topic: 434 (43.4%)

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
