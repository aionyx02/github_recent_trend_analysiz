# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-03 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 17 | 1.7% |
| 待檢視 | 144 | 14.4% |
| 訊號完整 | 839 | 83.9% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2634 | 369 | 13d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:9arm-skills, topics:none |
| 2 | `ywnd1144/Gopay_plus_automatic` | 1305 | 638 | 21d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `V4bel/dirtyfrag` | 4811 | 775 | 26d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `Ch1rpy2613/Mirrai` | 925 | 12 | 28d | **6** | desc:empty, license:none, low-forks:0.013, topics:none |
| 5 | `THUYRan/Legal-Skills-Chinese` | 143 | 22 | 13d | **5** | desc:empty, license:none, generic-name:Legal-Skills-Chinese, topics:none |
| 6 | `Tong89/smartNode` | 2010 | 177 | 12d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `qiuqiubuchongle-cloud/chokepoint-atlas` | 478 | 112 | 1d | **5** | desc:empty, license:none, overnight-surge:478/day, topics:none |
| 8 | `mit-han-lab/kernel-design-agents` | 421 | 30 | 21d | **5** | desc:empty, license:none, generic-name:kernel-design-agents, topics:none |
| 9 | `UIengF/claude-codex-teamwork` | 149 | 9 | 23d | **5** | desc:empty, license:none, generic-name:claude-codex-teamwork, topics:none |
| 10 | `FULU-Foundation/OrcaSlicer-bambulab` | 6755 | 5137 | 22d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `rulyone/Simple-ReAct-Agent` | 115 | 10 | 16d | **5** | desc:empty, license:none, generic-name:Simple-ReAct-Agent, topics:none |
| 12 | `FoundZiGu/GuJumpgate` | 3320 | 859 | 14d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `limin112/wechat-publish-template` | 163 | 18 | 15d | **5** | desc:empty, license:none, generic-name:wechat-publish-template, topics:none |
| 14 | `tiantianGPU/reg-factory` | 302 | 151 | 1d | **5** | desc:empty, license:none, overnight-surge:302/day, topics:none |
| 15 | `jiaran-king/Re-Zero---Starting-LLM-` | 125 | 3 | 6d | **5** | desc:empty, license:none, generic-name:Re-Zero---Starting-LLM-, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 129 | 12.9% |
| description <20 chars | 29 | 2.9% |
| no license | 365 | 36.5% |
| high-attention no-desc (stars>1k + empty desc) | 7 | 0.7% |
| low fork ratio (stars>500 + fsr<0.02) | 8 | 0.8% |
| overnight surge (>300 spd + <7 days) | 10 | 1.0% |
| generic-AI-buzzword name | 124 | 12.4% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 7 |
| JavaScript | 3 |
| Unknown | 2 |
| Shell | 1 |
| C | 1 |
| TypeScript | 1 |
| C++ | 1 |
| HTML | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 2 | 1 | 0 | 1 | 50.0% |
| 1000-4999 | 59 | 6 | 3 | 50 | 10.2% |
| 500-999 | 99 | 1 | 15 | 83 | 1.0% |
| 100-499 | 837 | 9 | 126 | 702 | 1.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `FULU-Foundation/OrcaSlicer-bambulab` | 6755 | 5137 | 22d | C++ | AGPL-3.0 |
| `V4bel/dirtyfrag` | 4811 | 775 | 26d | C | — |
| `FoundZiGu/GuJumpgate` | 3320 | 859 | 14d | JavaScript | MIT |
| `thananon/9arm-skills` | 2634 | 369 | 13d | Shell | — |
| `Tong89/smartNode` | 2010 | 177 | 12d | Python | MIT |
| `ywnd1144/Gopay_plus_automatic` | 1305 | 638 | 21d | Python | — |
| `gtxx3600/GPTSession2CPAandSub2API` | 1083 | 295 | 25d | JavaScript | MIT |

### Generic-name pattern breakdown

Of 124 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 33 |
| `skills` | 16 |
| `skill` | 16 |
| `claude` | 15 |
| `codex` | 13 |
| `awesome` | 9 |
| `agents` | 6 |
| `llm` | 3 |
| `prompt` | 3 |
| `template` | 2 |
| `vibe` | 2 |
| `demo` | 2 |
| `toolkit` | 2 |
| `cookbook` | 1 |
| `gpt` | 1 |

### Topics coverage

- Repos with **zero topics**: 588 (58.8%)
- Repos with at least one topic: 412 (41.2%)

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
