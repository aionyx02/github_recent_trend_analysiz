# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-04 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 150 | 15.0% |
| 訊號完整 | 833 | 83.3% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2651 | 372 | 14d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:9arm-skills, topics:none |
| 2 | `ywnd1144/Gopay_plus_automatic` | 1313 | 641 | 22d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `Ch1rpy2613/Mirrai` | 937 | 12 | 29d | **6** | desc:empty, license:none, low-forks:0.013, topics:none |
| 4 | `V4bel/dirtyfrag` | 4815 | 774 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `anomalyco/rift` | 501 | 7 | 3d | **6** | desc:empty, license:none, low-forks:0.014, topics:none |
| 6 | `Blueemi/codex-eu-patcher` | 137 | 9 | 28d | **5** | desc:empty, license:none, generic-name:codex-eu-patcher, topics:none |
| 7 | `Tong89/smartNode` | 2006 | 176 | 13d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `THUYRan/Legal-Skills-Chinese` | 162 | 25 | 14d | **5** | desc:empty, license:none, generic-name:Legal-Skills-Chinese, topics:none |
| 9 | `limin112/wechat-publish-template` | 164 | 18 | 16d | **5** | desc:empty, license:none, generic-name:wechat-publish-template, topics:none |
| 10 | `mit-han-lab/kernel-design-agents` | 449 | 34 | 22d | **5** | desc:empty, license:none, generic-name:kernel-design-agents, topics:none |
| 11 | `rulyone/Simple-ReAct-Agent` | 115 | 10 | 17d | **5** | desc:empty, license:none, generic-name:Simple-ReAct-Agent, topics:none |
| 12 | `UIengF/claude-codex-teamwork` | 149 | 9 | 24d | **5** | desc:empty, license:none, generic-name:claude-codex-teamwork, topics:none |
| 13 | `FULU-Foundation/OrcaSlicer-bambulab` | 6777 | 5139 | 23d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `FoundZiGu/GuJumpgate` | 3386 | 871 | 15d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `qqfly1to19/awesome_proofreading_auto` | 107 | 19 | 12d | **5** | desc:empty, license:none, generic-name:awesome_proofreading_auto, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 132 | 13.2% |
| description <20 chars | 30 | 3.0% |
| no license | 382 | 38.2% |
| high-attention no-desc (stars>1k + empty desc) | 7 | 0.7% |
| low fork ratio (stars>500 + fsr<0.02) | 10 | 1.0% |
| overnight surge (>300 spd + <7 days) | 8 | 0.8% |
| generic-AI-buzzword name | 122 | 12.2% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| JavaScript | 3 |
| Unknown | 2 |
| Shell | 1 |
| TypeScript | 1 |
| C | 1 |
| Rust | 1 |
| HTML | 1 |
| C++ | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 2 | 1 | 0 | 1 | 50.0% |
| 1000-4999 | 63 | 6 | 5 | 52 | 9.5% |
| 500-999 | 98 | 2 | 15 | 81 | 2.0% |
| 100-499 | 834 | 8 | 130 | 696 | 1.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `FULU-Foundation/OrcaSlicer-bambulab` | 6777 | 5139 | 23d | C++ | AGPL-3.0 |
| `V4bel/dirtyfrag` | 4815 | 774 | 27d | C | — |
| `FoundZiGu/GuJumpgate` | 3386 | 871 | 15d | JavaScript | MIT |
| `thananon/9arm-skills` | 2651 | 372 | 14d | Shell | — |
| `Tong89/smartNode` | 2006 | 176 | 13d | Python | MIT |
| `ywnd1144/Gopay_plus_automatic` | 1313 | 641 | 22d | Python | — |
| `gtxx3600/GPTSession2CPAandSub2API` | 1097 | 298 | 26d | JavaScript | MIT |

### Generic-name pattern breakdown

Of 122 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 31 |
| `claude` | 17 |
| `skills` | 16 |
| `skill` | 15 |
| `codex` | 13 |
| `awesome` | 9 |
| `agents` | 5 |
| `llm` | 3 |
| `prompt` | 3 |
| `template` | 2 |
| `vibe` | 2 |
| `demo` | 2 |
| `toolkit` | 2 |
| `cookbook` | 1 |
| `gpt` | 1 |

### Topics coverage

- Repos with **zero topics**: 605 (60.5%)
- Repos with at least one topic: 395 (39.5%)

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
