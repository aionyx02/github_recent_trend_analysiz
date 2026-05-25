# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-05-25 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 18 | 1.8% |
| 待檢視 | 124 | 12.4% |
| 訊號完整 | 858 | 85.8% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2009 | 267 | 4d | **8** | desc:empty, license:none, high-attention-no-desc, overnight-surge:502/day, generic-name:9arm-skills, topics:none |
| 2 | `deepseek-ai/awesome-deepseek-agent` | 2246 | 247 | 27d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:awesome-deepseek-agent, topics:none |
| 3 | `cursor/cookbook` | 3846 | 447 | 27d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:cookbook, topics:none |
| 4 | `wrongly-cuddly-obsession/NTSB_FOIA_MU5735` | 1073 | 366 | 24d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `V4bel/dirtyfrag` | 4753 | 758 | 17d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `Ch1rpy2613/Mirrai` | 821 | 11 | 19d | **6** | desc:empty, license:none, low-forks:0.013, topics:none |
| 7 | `FoundZiGu/GuJumpgate` | 2382 | 659 | 5d | **6** | desc:empty, high-attention-no-desc, overnight-surge:476/day, topics:none |
| 8 | `limin112/wechat-publish-template` | 155 | 17 | 6d | **5** | desc:empty, license:none, generic-name:wechat-publish-template, topics:none |
| 9 | `Jiawei-Yang/FD-Loss` | 509 | 9 | 27d | **5** | desc:empty, low-forks:0.018, topics:none |
| 10 | `mit-han-lab/kernel-design-agents` | 145 | 12 | 12d | **5** | desc:empty, license:none, generic-name:kernel-design-agents, topics:none |
| 11 | `pheohu-42/Claude_zh-CN_LanguagePack` | 246 | 11 | 29d | **5** | desc:empty, license:none, generic-name:Claude_zh-CN_LanguagePack, topics:none |
| 12 | `h9-tec/LLM-Math-Handbook` | 214 | 27 | 28d | **5** | desc:empty, license:none, generic-name:LLM-Math-Handbook, topics:none |
| 13 | `foyzulkarim/claude-lens` | 221 | 29 | 24d | **5** | desc:empty, license:none, generic-name:claude-lens, topics:none |
| 14 | `Achilng/floral-notepaper` | 2374 | 108 | 28d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `Blueemi/codex-eu-patcher` | 123 | 8 | 18d | **5** | desc:empty, license:none, generic-name:codex-eu-patcher, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 110 | 11.0% |
| description <20 chars | 26 | 2.6% |
| no license | 378 | 37.8% |
| high-attention no-desc (stars>1k + empty desc) | 8 | 0.8% |
| low fork ratio (stars>500 + fsr<0.02) | 12 | 1.2% |
| overnight surge (>300 spd + <7 days) | 5 | 0.5% |
| generic-AI-buzzword name | 139 | 13.9% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 4 |
| Python | 4 |
| TypeScript | 3 |
| JavaScript | 2 |
| HTML | 2 |
| Shell | 1 |
| C | 1 |
| C++ | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 2 | 0 | 0 | 2 | 0.0% |
| 5000-9999 | 3 | 1 | 0 | 2 | 33.3% |
| 1000-4999 | 70 | 7 | 4 | 59 | 10.0% |
| 500-999 | 106 | 2 | 14 | 90 | 1.9% |
| 100-499 | 819 | 8 | 106 | 705 | 1.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `FULU-Foundation/OrcaSlicer-bambulab` | 6471 | 5017 | 13d | C++ | AGPL-3.0 |
| `V4bel/dirtyfrag` | 4753 | 758 | 17d | C | — |
| `cursor/cookbook` | 3846 | 447 | 27d | TypeScript | — |
| `FoundZiGu/GuJumpgate` | 2382 | 659 | 5d | JavaScript | MIT |
| `Achilng/floral-notepaper` | 2374 | 108 | 28d | TypeScript | MIT |
| `deepseek-ai/awesome-deepseek-agent` | 2246 | 247 | 27d | Unknown | — |
| `thananon/9arm-skills` | 2009 | 267 | 4d | Shell | — |
| `wrongly-cuddly-obsession/NTSB_FOIA_MU5735` | 1073 | 366 | 24d | Unknown | — |

### Generic-name pattern breakdown

Of 139 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 28 |
| `claude` | 24 |
| `skills` | 17 |
| `codex` | 16 |
| `skill` | 16 |
| `awesome` | 9 |
| `agents` | 8 |
| `prompt` | 6 |
| `gpt` | 5 |
| `llm` | 4 |
| `toolkit` | 2 |
| `cookbook` | 1 |
| `template` | 1 |
| `demo` | 1 |
| `copilot` | 1 |

### Topics coverage

- Repos with **zero topics**: 541 (54.1%)
- Repos with at least one topic: 459 (45.9%)

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
