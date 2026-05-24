# Vibe-Coded Garbage Analysis

_Generated: 2026-05-24 | Sample size: 999 repos (with topics signal)_

## Definition

**Vibe-coded garbage** = a repo whose stars greatly exceed its visible substance.
Stars are easy to harvest; descriptions, tags, forks, and a license take effort.
The label targets the public artifact only — not the author, and not vibe-coding as a practice.

## Scoring rubric

| Signal | Points | Rationale |
|---|---:|---|
| `description` empty | +2 | Highest single signal of low effort |
| `description` < 20 chars | +1 | Marginal |
| No license declared | +1 | Careless OSS practice |
| stars > 1000 AND description empty | +2 | "Famous nothing" |
| fork_star_ratio < 0.02 AND stars > 500 | +2 | Stars but nobody forks |
| stars_per_day > 300 AND age_days < 7 | +1 | Overnight surge |
| Name matches generic-AI-buzzword pattern | +1 | `*-skills`, `*-agent`, `*-cookbook` ... |
| No topics tagged | +1 | Only when topics data present |

**Tiers**: 0-2 legitimate · 3-4 suspicious · 5+ garbage

## Findings

| Tier | Count | % of sample |
|---|---:|---:|
| garbage | 18 | 1.8% |
| suspicious | 132 | 13.2% |
| legitimate | 849 | 85.0% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 1918 | 255 | 3d | **8** | desc:empty, license:none, famous-nothing, overnight-surge:639/day, generic-name:9arm-skills, topics:none |
| 2 | `cursor/cookbook` | 3843 | 446 | 26d | **7** | desc:empty, license:none, famous-nothing, generic-name:cookbook, topics:none |
| 3 | `deepseek-ai/awesome-deepseek-agent` | 2145 | 234 | 26d | **7** | desc:empty, license:none, famous-nothing, generic-name:awesome-deepseek-agent, topics:none |
| 4 | `FoundZiGu/GuJumpgate` | 2143 | 612 | 4d | **6** | desc:empty, famous-nothing, overnight-surge:536/day, topics:none |
| 5 | `wrongly-cuddly-obsession/NTSB_FOIA_MU5735` | 1070 | 366 | 23d | **6** | desc:empty, license:none, famous-nothing, topics:none |
| 6 | `V4bel/dirtyfrag` | 4752 | 755 | 16d | **6** | desc:empty, license:none, famous-nothing, topics:none |
| 7 | `Ch1rpy2613/Mirrai` | 806 | 11 | 18d | **6** | desc:empty, license:none, low-forks:0.014, topics:none |
| 8 | `Achilng/floral-notepaper` | 2247 | 104 | 27d | **5** | desc:empty, famous-nothing, topics:none |
| 9 | `limin112/wechat-publish-template` | 154 | 17 | 5d | **5** | desc:empty, license:none, generic-name:wechat-publish-template, topics:none |
| 10 | `vibeshotclub/vsc-skills` | 131 | 24 | 26d | **5** | desc:empty, license:none, generic-name:vsc-skills, topics:none |
| 11 | `foyzulkarim/claude-lens` | 221 | 29 | 23d | **5** | desc:empty, license:none, generic-name:claude-lens, topics:none |
| 12 | `FULU-Foundation/OrcaSlicer-bambulab` | 6431 | 4993 | 12d | **5** | desc:empty, famous-nothing, topics:none |
| 13 | `Blueemi/codex-eu-patcher` | 122 | 8 | 17d | **5** | desc:empty, license:none, generic-name:codex-eu-patcher, topics:none |
| 14 | `himself65/trade-skills` | 268 | 28 | 29d | **5** | desc:empty, license:none, generic-name:trade-skills, topics:none |
| 15 | `Jiawei-Yang/FD-Loss` | 508 | 9 | 26d | **5** | desc:empty, low-forks:0.018, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 113 | 11.3% |
| description <20 chars | 28 | 2.8% |
| no license | 379 | 37.9% |
| famous-nothing (stars>1k + empty desc) | 8 | 0.8% |
| low fork ratio (stars>500 + fsr<0.02) | 11 | 1.1% |
| overnight surge (>300 spd + <7 days) | 23 | 2.3% |
| generic-AI-buzzword name | 142 | 14.2% |

### Garbage tier — by primary language

| Language | Garbage repos |
|---|---:|
| Unknown | 4 |
| Python | 4 |
| TypeScript | 3 |
| JavaScript | 2 |
| HTML | 2 |
| Shell | 1 |
| C | 1 |
| C++ | 1 |

### Garbage concentration by stars bucket

Where in the popularity distribution does the garbage cluster?

| Stars bucket | Total | Garbage | Suspicious | Legitimate | Garbage % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 2 | 1 | 0 | 1 | 50.0% |
| 1000-4999 | 71 | 7 | 3 | 61 | 9.9% |
| 500-999 | 108 | 2 | 14 | 92 | 1.9% |
| 100-499 | 815 | 8 | 115 | 692 | 1.0% |

### Famous-nothing zoom (stars > 1000 + empty description)

These are the most visible inflated artifacts — high stars, zero description.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `FULU-Foundation/OrcaSlicer-bambulab` | 6431 | 4993 | 12d | C++ | AGPL-3.0 |
| `V4bel/dirtyfrag` | 4752 | 755 | 16d | C | — |
| `cursor/cookbook` | 3843 | 446 | 26d | TypeScript | — |
| `Achilng/floral-notepaper` | 2247 | 104 | 27d | TypeScript | MIT |
| `deepseek-ai/awesome-deepseek-agent` | 2145 | 234 | 26d | Unknown | — |
| `FoundZiGu/GuJumpgate` | 2143 | 612 | 4d | JavaScript | MIT |
| `thananon/9arm-skills` | 1918 | 255 | 3d | Shell | — |
| `wrongly-cuddly-obsession/NTSB_FOIA_MU5735` | 1070 | 366 | 23d | Unknown | — |

### Generic-name pattern breakdown

Of 142 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 29 |
| `claude` | 25 |
| `skills` | 18 |
| `codex` | 16 |
| `skill` | 15 |
| `awesome` | 11 |
| `agents` | 7 |
| `prompt` | 5 |
| `gpt` | 5 |
| `llm` | 4 |
| `toolkit` | 2 |
| `copilot` | 2 |
| `cookbook` | 1 |
| `template` | 1 |
| `demo` | 1 |

### Topics coverage

- Repos with **zero topics**: 543 (54.4%)
- Repos with at least one topic: 456 (45.6%)

## Methodology limits

- Stars are not a proxy for code quality. A high score is a *suspicion*, not a verdict.
- The generic-name regex is intentionally narrow. False positives possible (e.g., a legitimate `awesome-*` list).
- 30-day creation window biases toward repos that haven't had time to accumulate forks.
- We do not inspect commit graph, contributor count, or README length — those would tighten the signal but cost extra API calls per repo.

## Reproduce

```bash
python -m src.analyze_vibe
```
