# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-05 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 164 | 16.4% |
| 訊號完整 | 820 | 82.0% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2670 | 372 | 15d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:9arm-skills, topics:none |
| 2 | `anomalyco/rift` | 515 | 8 | 4d | **6** | desc:empty, license:none, low-forks:0.016, topics:none |
| 3 | `V4bel/dirtyfrag` | 4817 | 773 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `ywnd1144/Gopay_plus_automatic` | 1314 | 639 | 23d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `qqfly1to19/awesome_proofreading_auto` | 120 | 20 | 13d | **5** | desc:empty, license:none, generic-name:awesome_proofreading_auto, topics:none |
| 6 | `FoundZiGu/GuJumpgate` | 3440 | 886 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `Blueemi/codex-eu-patcher` | 151 | 9 | 29d | **5** | desc:empty, license:none, generic-name:codex-eu-patcher, topics:none |
| 8 | `UIengF/claude-codex-teamwork` | 149 | 9 | 25d | **5** | desc:empty, license:none, generic-name:claude-codex-teamwork, topics:none |
| 9 | `mit-han-lab/kernel-design-agents` | 460 | 34 | 23d | **5** | desc:empty, license:none, generic-name:kernel-design-agents, topics:none |
| 10 | `THUYRan/Legal-Skills-Chinese` | 179 | 26 | 15d | **5** | desc:empty, license:none, generic-name:Legal-Skills-Chinese, topics:none |
| 11 | `rulyone/Simple-ReAct-Agent` | 115 | 10 | 18d | **5** | desc:empty, license:none, generic-name:Simple-ReAct-Agent, topics:none |
| 12 | `gtxx3600/GPTSession2CPAandSub2API` | 1109 | 302 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `limin112/wechat-publish-template` | 165 | 18 | 17d | **5** | desc:empty, license:none, generic-name:wechat-publish-template, topics:none |
| 14 | `jiaran-king/Re-Zero---Starting-LLM-` | 139 | 4 | 8d | **5** | desc:empty, license:none, generic-name:Re-Zero---Starting-LLM-, topics:none |
| 15 | `FULU-Foundation/OrcaSlicer-bambulab` | 6788 | 5144 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 139 | 13.9% |
| description <20 chars | 31 | 3.1% |
| no license | 381 | 38.1% |
| high-attention no-desc (stars>1k + empty desc) | 7 | 0.7% |
| low fork ratio (stars>500 + fsr<0.02) | 10 | 1.0% |
| overnight surge (>300 spd + <7 days) | 7 | 0.7% |
| generic-AI-buzzword name | 117 | 11.7% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| JavaScript | 3 |
| Unknown | 2 |
| Shell | 1 |
| Rust | 1 |
| C | 1 |
| HTML | 1 |
| C++ | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 4 | 1 | 1 | 2 | 25.0% |
| 1000-4999 | 66 | 6 | 4 | 56 | 9.1% |
| 500-999 | 91 | 1 | 15 | 75 | 1.1% |
| 100-499 | 836 | 8 | 144 | 684 | 1.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `FULU-Foundation/OrcaSlicer-bambulab` | 6788 | 5144 | 24d | C++ | AGPL-3.0 |
| `V4bel/dirtyfrag` | 4817 | 773 | 28d | C | — |
| `FoundZiGu/GuJumpgate` | 3440 | 886 | 16d | JavaScript | MIT |
| `thananon/9arm-skills` | 2670 | 372 | 15d | Shell | — |
| `Tong89/smartNode` | 2003 | 176 | 14d | Python | MIT |
| `ywnd1144/Gopay_plus_automatic` | 1314 | 639 | 23d | Python | — |
| `gtxx3600/GPTSession2CPAandSub2API` | 1109 | 302 | 27d | JavaScript | MIT |

### Generic-name pattern breakdown

Of 117 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 28 |
| `skills` | 16 |
| `codex` | 15 |
| `skill` | 15 |
| `claude` | 12 |
| `awesome` | 10 |
| `agents` | 5 |
| `llm` | 3 |
| `gpt` | 3 |
| `template` | 2 |
| `vibe` | 2 |
| `prompt` | 2 |
| `toolkit` | 2 |
| `demo` | 1 |
| `cookbook` | 1 |

### Topics coverage

- Repos with **zero topics**: 618 (61.8%)
- Repos with at least one topic: 382 (38.2%)

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
