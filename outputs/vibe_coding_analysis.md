# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-01 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 137 | 13.7% |
| 訊號完整 | 849 | 84.9% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2587 | 362 | 11d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:9arm-skills, topics:none |
| 2 | `V4bel/dirtyfrag` | 4795 | 774 | 24d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `Ch1rpy2613/Mirrai` | 890 | 12 | 26d | **6** | desc:empty, license:none, low-forks:0.013, topics:none |
| 4 | `ywnd1144/Gopay_plus_automatic` | 1273 | 633 | 19d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `UIengF/claude-codex-teamwork` | 149 | 8 | 21d | **5** | desc:empty, license:none, generic-name:claude-codex-teamwork, topics:none |
| 6 | `Tong89/smartNode` | 2010 | 176 | 10d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `rulyone/Simple-ReAct-Agent` | 115 | 10 | 14d | **5** | desc:empty, license:none, generic-name:Simple-ReAct-Agent, topics:none |
| 8 | `gtxx3600/GPTSession2CPAandSub2API` | 1055 | 292 | 23d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `mit-han-lab/kernel-design-agents` | 380 | 28 | 19d | **5** | desc:empty, license:none, generic-name:kernel-design-agents, topics:none |
| 10 | `FoundZiGu/GuJumpgate` | 3214 | 841 | 12d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `FULU-Foundation/OrcaSlicer-bambulab` | 6702 | 5118 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `Blueemi/codex-eu-patcher` | 129 | 9 | 25d | **5** | desc:empty, license:none, generic-name:codex-eu-patcher, topics:none |
| 13 | `limin112/wechat-publish-template` | 161 | 18 | 13d | **5** | desc:empty, license:none, generic-name:wechat-publish-template, topics:none |
| 14 | `asuojun/claude-vision-skill` | 160 | 5 | 29d | **5** | desc:empty, license:none, generic-name:claude-vision-skill, topics:none |
| 15 | `pony-maggie/computer-use-for-deepseek` | 130 | 5 | 14d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 122 | 12.2% |
| description <20 chars | 26 | 2.6% |
| no license | 352 | 35.2% |
| high-attention no-desc (stars>1k + empty desc) | 7 | 0.7% |
| low fork ratio (stars>500 + fsr<0.02) | 8 | 0.8% |
| overnight surge (>300 spd + <7 days) | 7 | 0.7% |
| generic-AI-buzzword name | 127 | 12.7% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 4 |
| JavaScript | 4 |
| Shell | 1 |
| C | 1 |
| TypeScript | 1 |
| Unknown | 1 |
| C++ | 1 |
| HTML | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 2 | 1 | 0 | 1 | 50.0% |
| 1000-4999 | 56 | 6 | 2 | 48 | 10.7% |
| 500-999 | 108 | 1 | 14 | 93 | 0.9% |
| 100-499 | 831 | 6 | 121 | 704 | 0.7% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `FULU-Foundation/OrcaSlicer-bambulab` | 6702 | 5118 | 20d | C++ | AGPL-3.0 |
| `V4bel/dirtyfrag` | 4795 | 774 | 24d | C | — |
| `FoundZiGu/GuJumpgate` | 3214 | 841 | 12d | JavaScript | MIT |
| `thananon/9arm-skills` | 2587 | 362 | 11d | Shell | — |
| `Tong89/smartNode` | 2010 | 176 | 10d | Python | MIT |
| `ywnd1144/Gopay_plus_automatic` | 1273 | 633 | 19d | Python | — |
| `gtxx3600/GPTSession2CPAandSub2API` | 1055 | 292 | 23d | JavaScript | MIT |

### Generic-name pattern breakdown

Of 127 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 31 |
| `claude` | 19 |
| `skills` | 18 |
| `skill` | 17 |
| `codex` | 13 |
| `agents` | 7 |
| `awesome` | 6 |
| `prompt` | 4 |
| `template` | 2 |
| `llm` | 2 |
| `vibe` | 2 |
| `demo` | 2 |
| `gpt` | 2 |
| `cookbook` | 1 |
| `toolkit` | 1 |

### Topics coverage

- Repos with **zero topics**: 562 (56.2%)
- Repos with at least one topic: 438 (43.8%)

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
