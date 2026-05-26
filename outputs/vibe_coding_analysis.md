# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-05-26 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 19 | 1.9% |
| 待檢視 | 132 | 13.2% |
| 訊號完整 | 849 | 84.9% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2294 | 317 | 5d | **8** | desc:empty, license:none, high-attention-no-desc, overnight-surge:459/day, generic-name:9arm-skills, topics:none |
| 2 | `cursor/cookbook` | 3865 | 448 | 28d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:cookbook, topics:none |
| 3 | `deepseek-ai/awesome-deepseek-agent` | 2419 | 263 | 28d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:awesome-deepseek-agent, topics:none |
| 4 | `wrongly-cuddly-obsession/NTSB_FOIA_MU5735` | 1079 | 365 | 25d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `Ch1rpy2613/Mirrai` | 814 | 11 | 20d | **6** | desc:empty, license:none, low-forks:0.014, topics:none |
| 6 | `FoundZiGu/GuJumpgate` | 2643 | 713 | 6d | **6** | desc:empty, high-attention-no-desc, overnight-surge:440/day, topics:none |
| 7 | `V4bel/dirtyfrag` | 4766 | 760 | 18d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 8 | `vibeshotclub/vsc-skills` | 132 | 24 | 28d | **5** | desc:empty, license:none, generic-name:vsc-skills, topics:none |
| 9 | `UIengF/claude-codex-teamwork` | 143 | 8 | 15d | **5** | desc:empty, license:none, generic-name:claude-codex-teamwork, topics:none |
| 10 | `FULU-Foundation/OrcaSlicer-bambulab` | 6532 | 5050 | 14d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `foyzulkarim/claude-lens` | 220 | 29 | 25d | **5** | desc:empty, license:none, generic-name:claude-lens, topics:none |
| 12 | `cat9999aaa/thinshell` | 519 | 8 | 11d | **5** | desc:short, license:none, low-forks:0.015, topics:none |
| 13 | `energypantry/agent-browser-runtime` | 109 | 31 | 8d | **5** | desc:empty, license:none, generic-name:agent-browser-runtime, topics:none |
| 14 | `mit-han-lab/kernel-design-agents` | 215 | 18 | 13d | **5** | desc:empty, license:none, generic-name:kernel-design-agents, topics:none |
| 15 | `Blueemi/codex-eu-patcher` | 124 | 9 | 19d | **5** | desc:empty, license:none, generic-name:codex-eu-patcher, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 123 | 12.3% |
| description <20 chars | 26 | 2.6% |
| no license | 362 | 36.2% |
| high-attention no-desc (stars>1k + empty desc) | 8 | 0.8% |
| low fork ratio (stars>500 + fsr<0.02) | 8 | 0.8% |
| overnight surge (>300 spd + <7 days) | 5 | 0.5% |
| generic-AI-buzzword name | 139 | 13.9% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 5 |
| TypeScript | 3 |
| JavaScript | 3 |
| Python | 3 |
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
| 1000-4999 | 69 | 7 | 3 | 59 | 10.1% |
| 500-999 | 117 | 2 | 17 | 98 | 1.7% |
| 100-499 | 809 | 9 | 112 | 688 | 1.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `FULU-Foundation/OrcaSlicer-bambulab` | 6532 | 5050 | 14d | C++ | AGPL-3.0 |
| `V4bel/dirtyfrag` | 4766 | 760 | 18d | C | — |
| `cursor/cookbook` | 3865 | 448 | 28d | TypeScript | — |
| `FoundZiGu/GuJumpgate` | 2643 | 713 | 6d | JavaScript | MIT |
| `Achilng/floral-notepaper` | 2513 | 111 | 29d | TypeScript | MIT |
| `deepseek-ai/awesome-deepseek-agent` | 2419 | 263 | 28d | Unknown | — |
| `thananon/9arm-skills` | 2294 | 317 | 5d | Shell | — |
| `wrongly-cuddly-obsession/NTSB_FOIA_MU5735` | 1079 | 365 | 25d | Unknown | — |

### Generic-name pattern breakdown

Of 139 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 30 |
| `skill` | 20 |
| `skills` | 19 |
| `claude` | 19 |
| `codex` | 17 |
| `awesome` | 8 |
| `agents` | 8 |
| `gpt` | 5 |
| `prompt` | 4 |
| `llm` | 3 |
| `template` | 2 |
| `cookbook` | 1 |
| `demo` | 1 |
| `toolkit` | 1 |
| `copilot` | 1 |

### Topics coverage

- Repos with **zero topics**: 569 (56.9%)
- Repos with at least one topic: 431 (43.1%)

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
