# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-05-28 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 16 | 1.6% |
| 待檢視 | 117 | 11.7% |
| 訊號完整 | 867 | 86.7% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2466 | 341 | 7d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:9arm-skills, topics:none |
| 2 | `Ch1rpy2613/Mirrai` | 834 | 11 | 22d | **6** | desc:empty, license:none, low-forks:0.013, topics:none |
| 3 | `wrongly-cuddly-obsession/NTSB_FOIA_MU5735` | 1080 | 365 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `V4bel/dirtyfrag` | 4782 | 765 | 20d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `ywnd1144/Gopay_plus_automatic` | 1144 | 600 | 15d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `foyzulkarim/claude-lens` | 220 | 29 | 27d | **5** | desc:empty, license:none, generic-name:claude-lens, topics:none |
| 7 | `LLM-Mart/LLM-Mart` | 177 | 5 | 21d | **5** | desc:empty, license:none, generic-name:LLM-Mart, topics:none |
| 8 | `asuojun/claude-vision-skill` | 128 | 5 | 25d | **5** | desc:empty, license:none, generic-name:claude-vision-skill, topics:none |
| 9 | `limin112/wechat-publish-template` | 156 | 18 | 9d | **5** | desc:empty, license:none, generic-name:wechat-publish-template, topics:none |
| 10 | `UIengF/claude-codex-teamwork` | 144 | 8 | 17d | **5** | desc:empty, license:none, generic-name:claude-codex-teamwork, topics:none |
| 11 | `FoundZiGu/GuJumpgate` | 2868 | 778 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `cat9999aaa/thinshell` | 520 | 9 | 13d | **5** | desc:short, license:none, low-forks:0.017, topics:none |
| 13 | `Tong89/smartNode` | 1681 | 140 | 6d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `FULU-Foundation/OrcaSlicer-bambulab` | 6605 | 5078 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `mit-han-lab/kernel-design-agents` | 289 | 21 | 15d | **5** | desc:empty, license:none, generic-name:kernel-design-agents, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 109 | 10.9% |
| description <20 chars | 21 | 2.1% |
| no license | 372 | 37.2% |
| high-attention no-desc (stars>1k + empty desc) | 7 | 0.7% |
| low fork ratio (stars>500 + fsr<0.02) | 9 | 0.9% |
| overnight surge (>300 spd + <7 days) | 2 | 0.2% |
| generic-AI-buzzword name | 127 | 12.7% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 4 |
| Python | 3 |
| JavaScript | 3 |
| HTML | 2 |
| Shell | 1 |
| TypeScript | 1 |
| C | 1 |
| C++ | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 2 | 0 | 0 | 2 | 0.0% |
| 5000-9999 | 3 | 1 | 0 | 2 | 33.3% |
| 1000-4999 | 64 | 6 | 1 | 57 | 9.4% |
| 500-999 | 111 | 2 | 15 | 94 | 1.8% |
| 100-499 | 820 | 7 | 101 | 712 | 0.9% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `FULU-Foundation/OrcaSlicer-bambulab` | 6605 | 5078 | 16d | C++ | AGPL-3.0 |
| `V4bel/dirtyfrag` | 4782 | 765 | 20d | C | — |
| `FoundZiGu/GuJumpgate` | 2868 | 778 | 8d | JavaScript | MIT |
| `thananon/9arm-skills` | 2466 | 341 | 7d | Shell | — |
| `Tong89/smartNode` | 1681 | 140 | 6d | Python | MIT |
| `ywnd1144/Gopay_plus_automatic` | 1144 | 600 | 15d | Python | — |
| `wrongly-cuddly-obsession/NTSB_FOIA_MU5735` | 1080 | 365 | 27d | Unknown | — |

### Generic-name pattern breakdown

Of 127 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 30 |
| `claude` | 19 |
| `skill` | 18 |
| `skills` | 15 |
| `codex` | 15 |
| `awesome` | 7 |
| `agents` | 6 |
| `prompt` | 4 |
| `gpt` | 4 |
| `llm` | 3 |
| `template` | 2 |
| `toolkit` | 2 |
| `demo` | 1 |
| `copilot` | 1 |

### Topics coverage

- Repos with **zero topics**: 536 (53.6%)
- Repos with at least one topic: 464 (46.4%)

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
