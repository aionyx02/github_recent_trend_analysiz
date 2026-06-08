# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-08 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 167 | 16.7% |
| 訊號完整 | 817 | 81.7% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2692 | 375 | 18d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:9arm-skills, topics:none |
| 2 | `OpenNSWM-Lab/FAROS` | 1022 | 172 | 25d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `ywnd1144/Gopay_plus_automatic` | 1316 | 637 | 26d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `anomalyco/rift` | 556 | 9 | 7d | **6** | desc:empty, license:none, low-forks:0.016, topics:none |
| 5 | `THUYRan/Legal-Skills-Chinese` | 211 | 30 | 18d | **5** | desc:empty, license:none, generic-name:Legal-Skills-Chinese, topics:none |
| 6 | `qqfly1to19/awesome_proofreading_auto` | 128 | 22 | 16d | **5** | desc:empty, license:none, generic-name:awesome_proofreading_auto, topics:none |
| 7 | `FoundZiGu/GuJumpgate` | 3485 | 894 | 19d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `jiaran-king/Re-Zero---Starting-LLM-` | 151 | 5 | 11d | **5** | desc:empty, license:none, generic-name:Re-Zero---Starting-LLM-, topics:none |
| 9 | `mit-han-lab/kernel-design-agents` | 513 | 40 | 26d | **5** | desc:empty, license:none, generic-name:kernel-design-agents, topics:none |
| 10 | `rosemarycox5334-debug/PA_Agent` | 105 | 52 | 19d | **5** | desc:empty, license:none, generic-name:PA_Agent, topics:none |
| 11 | `limin112/wechat-publish-template` | 168 | 18 | 20d | **5** | desc:empty, license:none, generic-name:wechat-publish-template, topics:none |
| 12 | `FULU-Foundation/OrcaSlicer-bambulab` | 6825 | 5157 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `rulyone/Simple-ReAct-Agent` | 115 | 10 | 21d | **5** | desc:empty, license:none, generic-name:Simple-ReAct-Agent, topics:none |
| 14 | `UIengF/claude-codex-teamwork` | 151 | 9 | 28d | **5** | desc:empty, license:none, generic-name:claude-codex-teamwork, topics:none |
| 15 | `Tong89/smartNode` | 1995 | 175 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 137 | 13.7% |
| description <20 chars | 30 | 3.0% |
| no license | 390 | 39.0% |
| high-attention no-desc (stars>1k + empty desc) | 6 | 0.6% |
| low fork ratio (stars>500 + fsr<0.02) | 12 | 1.2% |
| overnight surge (>300 spd + <7 days) | 5 | 0.5% |
| generic-AI-buzzword name | 121 | 12.1% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 8 |
| Unknown | 3 |
| Shell | 1 |
| Rust | 1 |
| JavaScript | 1 |
| HTML | 1 |
| C++ | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 1 | 0 | 0 | 1 | 0.0% |
| 5000-9999 | 5 | 1 | 1 | 3 | 20.0% |
| 1000-4999 | 63 | 5 | 5 | 53 | 7.9% |
| 500-999 | 83 | 2 | 15 | 66 | 2.4% |
| 100-499 | 848 | 8 | 146 | 694 | 0.9% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `FULU-Foundation/OrcaSlicer-bambulab` | 6825 | 5157 | 27d | C++ | AGPL-3.0 |
| `FoundZiGu/GuJumpgate` | 3485 | 894 | 19d | JavaScript | MIT |
| `thananon/9arm-skills` | 2692 | 375 | 18d | Shell | — |
| `Tong89/smartNode` | 1995 | 175 | 17d | Python | MIT |
| `ywnd1144/Gopay_plus_automatic` | 1316 | 637 | 26d | Python | — |
| `OpenNSWM-Lab/FAROS` | 1022 | 172 | 25d | Python | — |

### Generic-name pattern breakdown

Of 121 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 28 |
| `skills` | 19 |
| `skill` | 17 |
| `claude` | 13 |
| `codex` | 12 |
| `awesome` | 10 |
| `llm` | 4 |
| `agents` | 3 |
| `template` | 3 |
| `gpt` | 3 |
| `vibe` | 2 |
| `prompt` | 2 |
| `toolkit` | 2 |
| `demo` | 1 |
| `cookbook` | 1 |
| `starter` | 1 |

### Topics coverage

- Repos with **zero topics**: 612 (61.2%)
- Repos with at least one topic: 388 (38.8%)

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
