# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-18 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 13 | 1.3% |
| 待檢視 | 173 | 17.3% |
| 訊號完整 | 814 | 81.4% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2826 | 381 | 28d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:9arm-skills, topics:none |
| 2 | `anomalyco/rift` | 607 | 11 | 17d | **6** | desc:empty, license:none, low-forks:0.018, topics:none |
| 3 | `intel/intel-performance-skills` | 167 | 21 | 29d | **5** | desc:empty, license:none, generic-name:intel-performance-skills, topics:none |
| 4 | `world-action-models/awesome-world-action-models` | 112 | 2 | 1d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 5 | `THUYRan/Legal-Skills-Chinese` | 287 | 39 | 28d | **5** | desc:empty, license:none, generic-name:Legal-Skills-Chinese, topics:none |
| 6 | `chaseai-yt/grill-me-codex` | 239 | 31 | 12d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 7 | `jmmy9609-design/gpt-pp` | 397 | 204 | 8d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 8 | `rosemarycox5334-debug/PA_Agent` | 336 | 140 | 29d | **5** | desc:empty, license:none, generic-name:PA_Agent, topics:none |
| 9 | `Tong89/smartNode` | 1985 | 175 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `deermiya/visio-skill` | 117 | 9 | 22d | **5** | desc:empty, license:none, generic-name:visio-skill, topics:none |
| 11 | `jiaran-king/Re-Zero---Starting-LLM-` | 200 | 7 | 21d | **5** | desc:empty, license:none, generic-name:Re-Zero---Starting-LLM-, topics:none |
| 12 | `FoundZiGu/GuJumpgate` | 3906 | 1000 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `qqfly1to19/awesome_proofreading_auto` | 142 | 24 | 26d | **5** | desc:empty, license:none, generic-name:awesome_proofreading_auto, topics:none |
| 14 | `ConiferKit/sage` | 295 | 12 | 16d | **4** | desc:empty, license:none, topics:none |
| 15 | `yashmulgaonkar/FlightScnr` | 135 | 13 | 11d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 142 | 14.2% |
| description <20 chars | 27 | 2.7% |
| no license | 382 | 38.2% |
| high-attention no-desc (stars>1k + empty desc) | 3 | 0.3% |
| low fork ratio (stars>500 + fsr<0.02) | 7 | 0.7% |
| overnight surge (>300 spd + <7 days) | 7 | 0.7% |
| generic-AI-buzzword name | 153 | 15.3% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 7 |
| Unknown | 3 |
| Shell | 1 |
| Rust | 1 |
| JavaScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 2 | 0 | 0 | 2 | 0.0% |
| 5000-9999 | 5 | 0 | 0 | 5 | 0.0% |
| 1000-4999 | 47 | 3 | 3 | 41 | 6.4% |
| 500-999 | 89 | 1 | 17 | 71 | 1.1% |
| 100-499 | 857 | 9 | 153 | 695 | 1.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `FoundZiGu/GuJumpgate` | 3906 | 1000 | 29d | JavaScript | MIT |
| `thananon/9arm-skills` | 2826 | 381 | 28d | Shell | — |
| `Tong89/smartNode` | 1985 | 175 | 27d | Python | MIT |

### Generic-name pattern breakdown

Of 153 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 30 |
| `skill` | 30 |
| `skills` | 25 |
| `awesome` | 17 |
| `claude` | 13 |
| `codex` | 12 |
| `llm` | 5 |
| `gpt` | 4 |
| `vibe` | 4 |
| `toolkit` | 3 |
| `demo` | 2 |
| `prompt` | 2 |
| `agents` | 2 |
| `template` | 1 |
| `starter` | 1 |
| `cookbook` | 1 |
| `copilot` | 1 |

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
