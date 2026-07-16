# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-16 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 15 | 1.5% |
| 待檢視 | 93 | 9.3% |
| 訊號完整 | 892 | 89.2% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1898 | 486 | 17d | **6** | desc:empty, high-attention-no-desc, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 2 | `zhongerxin/Cowart` | 4672 | 354 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `kanavtwtgg/birds.cafe` | 511 | 2 | 24d | **6** | desc:empty, license:none, low-forks:0.004, topics:none |
| 4 | `x4gKing/3x-ui-Upgrade` | 1069 | 2197 | 7d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `x4gKing/X4G` | 5517 | 10176 | 11d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `huang-sir1/radiology-skills` | 828 | 10 | 27d | **6** | desc:empty, low-forks:0.012, generic-name:radiology-skills, topics:none |
| 7 | `withmarbleapp/os-taxonomy` | 3156 | 544 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `google-research/tabfm` | 1799 | 168 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `Fei-Away/Codex-Dream-Skin` | 2620 | 334 | 1d | **5** | desc:short, license:none, overnight-surge:2620/day, generic-name:Codex-Dream-Skin, topics:none |
| 10 | `oracle/fusion-ai-studio` | 564 | 9 | 19d | **5** | desc:empty, low-forks:0.016, topics:none |
| 11 | `world-action-models/awesome-world-action-models` | 319 | 7 | 28d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 12 | `TobiasLee/Rebuttal-Skill` | 280 | 11 | 1d | **5** | desc:empty, license:none, generic-name:Rebuttal-Skill, topics:none |
| 13 | `terrense/LLM_path_for_begginers` | 314 | 8 | 23d | **5** | desc:empty, license:none, generic-name:LLM_path_for_begginers, topics:none |
| 14 | `JimLiu/science-skills` | 211 | 53 | 14d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |
| 15 | `deepreinforce-ai/Ornith-1` | 1568 | 150 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 86 | 8.6% |
| description <20 chars | 17 | 1.7% |
| no license | 540 | 54.0% |
| high-attention no-desc (stars>1k + empty desc) | 7 | 0.7% |
| low fork ratio (stars>500 + fsr<0.02) | 15 | 1.5% |
| overnight surge (>300 spd + <7 days) | 9 | 0.9% |
| generic-AI-buzzword name | 138 | 13.8% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 4 |
| Unknown | 4 |
| JavaScript | 3 |
| HTML | 2 |
| PowerShell | 1 |
| Shell | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 4 | 1 | 0 | 3 | 25.0% |
| 1000-4999 | 50 | 7 | 4 | 39 | 14.0% |
| 500-999 | 103 | 3 | 27 | 73 | 2.9% |
| 100-499 | 840 | 4 | 62 | 774 | 0.5% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `x4gKing/X4G` | 5517 | 10176 | 11d | Python | — |
| `zhongerxin/Cowart` | 4672 | 354 | 27d | JavaScript | — |
| `withmarbleapp/os-taxonomy` | 3156 | 544 | 7d | JavaScript | ODbL-1.0 |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1898 | 486 | 17d | Python | MIT |
| `google-research/tabfm` | 1799 | 168 | 29d | Python | Apache-2.0 |
| `deepreinforce-ai/Ornith-1` | 1568 | 150 | 24d | Unknown | MIT |
| `x4gKing/3x-ui-Upgrade` | 1069 | 2197 | 7d | HTML | — |

### Generic-name pattern breakdown

Of 138 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 24 |
| `skills` | 22 |
| `skill` | 20 |
| `claude` | 17 |
| `codex` | 16 |
| `awesome` | 11 |
| `llm` | 5 |
| `prompt` | 4 |
| `copilot` | 3 |
| `toolkit` | 3 |
| `starter` | 3 |
| `template` | 3 |
| `agents` | 2 |
| `gpt` | 2 |
| `playground` | 2 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 368 (36.8%)
- Repos with at least one topic: 632 (63.2%)

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
