# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-10 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 165 | 16.5% |
| 訊號完整 | 819 | 81.9% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2723 | 375 | 20d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:9arm-skills, topics:none |
| 2 | `jmmy9609-design/gpt-pp` | 307 | 166 | 1d | **6** | desc:empty, license:none, overnight-surge:307/day, generic-name:gpt-pp, topics:none |
| 3 | `anomalyco/rift` | 562 | 10 | 9d | **6** | desc:empty, license:none, low-forks:0.018, topics:none |
| 4 | `OpenNSWM-Lab/FAROS` | 1026 | 172 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `ywnd1144/Gopay_plus_automatic` | 1315 | 637 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `THUYRan/Legal-Skills-Chinese` | 235 | 33 | 20d | **5** | desc:empty, license:none, generic-name:Legal-Skills-Chinese, topics:none |
| 7 | `Tong89/smartNode` | 1993 | 175 | 19d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `limin112/wechat-publish-template` | 204 | 21 | 22d | **5** | desc:empty, license:none, generic-name:wechat-publish-template, topics:none |
| 9 | `chaseai-yt/grill-me-codex` | 170 | 25 | 4d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 10 | `qqfly1to19/awesome_proofreading_auto` | 132 | 22 | 18d | **5** | desc:empty, license:none, generic-name:awesome_proofreading_auto, topics:none |
| 11 | `FoundZiGu/GuJumpgate` | 3759 | 974 | 21d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `mit-han-lab/kernel-design-agents` | 544 | 45 | 28d | **5** | desc:empty, license:none, generic-name:kernel-design-agents, topics:none |
| 13 | `jiaran-king/Re-Zero---Starting-LLM-` | 164 | 5 | 13d | **5** | desc:empty, license:none, generic-name:Re-Zero---Starting-LLM-, topics:none |
| 14 | `rulyone/Simple-ReAct-Agent` | 115 | 10 | 23d | **5** | desc:empty, license:none, generic-name:Simple-ReAct-Agent, topics:none |
| 15 | `rosemarycox5334-debug/PA_Agent` | 115 | 56 | 21d | **5** | desc:empty, license:none, generic-name:PA_Agent, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 134 | 13.4% |
| description <20 chars | 27 | 2.7% |
| no license | 376 | 37.6% |
| high-attention no-desc (stars>1k + empty desc) | 6 | 0.6% |
| low fork ratio (stars>500 + fsr<0.02) | 11 | 1.1% |
| overnight surge (>300 spd + <7 days) | 9 | 0.9% |
| generic-AI-buzzword name | 128 | 12.8% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 8 |
| Unknown | 3 |
| Shell | 1 |
| Rust | 1 |
| HTML | 1 |
| JavaScript | 1 |
| C++ | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 1 | 0 | 0 | 1 | 0.0% |
| 5000-9999 | 6 | 1 | 1 | 4 | 16.7% |
| 1000-4999 | 62 | 5 | 6 | 51 | 8.1% |
| 500-999 | 85 | 2 | 16 | 67 | 2.4% |
| 100-499 | 846 | 8 | 142 | 696 | 0.9% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `FULU-Foundation/OrcaSlicer-bambulab` | 6846 | 5163 | 29d | C++ | AGPL-3.0 |
| `FoundZiGu/GuJumpgate` | 3759 | 974 | 21d | JavaScript | MIT |
| `thananon/9arm-skills` | 2723 | 375 | 20d | Shell | — |
| `Tong89/smartNode` | 1993 | 175 | 19d | Python | MIT |
| `ywnd1144/Gopay_plus_automatic` | 1315 | 637 | 28d | Python | — |
| `OpenNSWM-Lab/FAROS` | 1026 | 172 | 27d | Python | — |

### Generic-name pattern breakdown

Of 128 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 27 |
| `skill` | 22 |
| `skills` | 20 |
| `awesome` | 12 |
| `claude` | 11 |
| `codex` | 10 |
| `gpt` | 4 |
| `llm` | 4 |
| `vibe` | 4 |
| `template` | 3 |
| `agents` | 3 |
| `demo` | 2 |
| `prompt` | 2 |
| `toolkit` | 2 |
| `starter` | 1 |
| `cookbook` | 1 |

### Topics coverage

- Repos with **zero topics**: 622 (62.2%)
- Repos with at least one topic: 378 (37.8%)

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
