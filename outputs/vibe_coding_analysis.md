# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-09 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 170 | 17.0% |
| 訊號完整 | 813 | 81.3% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2706 | 375 | 19d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:9arm-skills, topics:none |
| 2 | `ywnd1144/Gopay_plus_automatic` | 1316 | 636 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `OpenNSWM-Lab/FAROS` | 1025 | 172 | 26d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `anomalyco/rift` | 557 | 9 | 8d | **6** | desc:empty, license:none, low-forks:0.016, topics:none |
| 5 | `THUYRan/Legal-Skills-Chinese` | 223 | 31 | 19d | **5** | desc:empty, license:none, generic-name:Legal-Skills-Chinese, topics:none |
| 6 | `FoundZiGu/GuJumpgate` | 3500 | 897 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `vorpus/performativeUI` | 407 | 11 | 1d | **5** | desc:empty, license:none, overnight-surge:407/day, topics:none |
| 8 | `rulyone/Simple-ReAct-Agent` | 115 | 10 | 22d | **5** | desc:empty, license:none, generic-name:Simple-ReAct-Agent, topics:none |
| 9 | `rosemarycox5334-debug/PA_Agent` | 110 | 56 | 20d | **5** | desc:empty, license:none, generic-name:PA_Agent, topics:none |
| 10 | `qqfly1to19/awesome_proofreading_auto` | 130 | 22 | 17d | **5** | desc:empty, license:none, generic-name:awesome_proofreading_auto, topics:none |
| 11 | `UIengF/claude-codex-teamwork` | 151 | 9 | 29d | **5** | desc:empty, license:none, generic-name:claude-codex-teamwork, topics:none |
| 12 | `chaseai-yt/grill-me-codex` | 151 | 23 | 3d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 13 | `jiaran-king/Re-Zero---Starting-LLM-` | 159 | 5 | 12d | **5** | desc:empty, license:none, generic-name:Re-Zero---Starting-LLM-, topics:none |
| 14 | `limin112/wechat-publish-template` | 168 | 18 | 21d | **5** | desc:empty, license:none, generic-name:wechat-publish-template, topics:none |
| 15 | `mit-han-lab/kernel-design-agents` | 526 | 41 | 27d | **5** | desc:empty, license:none, generic-name:kernel-design-agents, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 141 | 14.1% |
| description <20 chars | 29 | 2.9% |
| no license | 387 | 38.7% |
| high-attention no-desc (stars>1k + empty desc) | 6 | 0.6% |
| low fork ratio (stars>500 + fsr<0.02) | 12 | 1.2% |
| overnight surge (>300 spd + <7 days) | 6 | 0.6% |
| generic-AI-buzzword name | 122 | 12.2% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 8 |
| Unknown | 3 |
| Shell | 1 |
| Rust | 1 |
| JavaScript | 1 |
| TypeScript | 1 |
| HTML | 1 |
| C++ | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 1 | 0 | 0 | 1 | 0.0% |
| 5000-9999 | 6 | 1 | 1 | 4 | 16.7% |
| 1000-4999 | 62 | 5 | 5 | 52 | 8.1% |
| 500-999 | 87 | 2 | 18 | 67 | 2.3% |
| 100-499 | 844 | 9 | 146 | 689 | 1.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `FULU-Foundation/OrcaSlicer-bambulab` | 6834 | 5159 | 28d | C++ | AGPL-3.0 |
| `FoundZiGu/GuJumpgate` | 3500 | 897 | 20d | JavaScript | MIT |
| `thananon/9arm-skills` | 2706 | 375 | 19d | Shell | — |
| `Tong89/smartNode` | 1994 | 175 | 18d | Python | MIT |
| `ywnd1144/Gopay_plus_automatic` | 1316 | 636 | 27d | Python | — |
| `OpenNSWM-Lab/FAROS` | 1025 | 172 | 26d | Python | — |

### Generic-name pattern breakdown

Of 122 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 25 |
| `skills` | 20 |
| `skill` | 19 |
| `claude` | 12 |
| `awesome` | 11 |
| `codex` | 11 |
| `llm` | 4 |
| `template` | 3 |
| `agents` | 3 |
| `vibe` | 3 |
| `gpt` | 3 |
| `demo` | 2 |
| `prompt` | 2 |
| `toolkit` | 2 |
| `cookbook` | 1 |
| `starter` | 1 |

### Topics coverage

- Repos with **zero topics**: 614 (61.4%)
- Repos with at least one topic: 386 (38.6%)

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
