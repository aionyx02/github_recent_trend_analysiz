# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-15 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 175 | 17.5% |
| 訊號完整 | 811 | 81.1% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2793 | 379 | 25d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:9arm-skills, topics:none |
| 2 | `XiaomiMiMo/MiMo-Code` | 8827 | 762 | 4d | **6** | desc:empty, high-attention-no-desc, overnight-surge:2207/day, topics:none |
| 3 | `anomalyco/rift` | 571 | 11 | 14d | **6** | desc:empty, license:none, low-forks:0.019, topics:none |
| 4 | `Tong89/smartNode` | 1987 | 176 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 5 | `FoundZiGu/GuJumpgate` | 3881 | 997 | 26d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 6 | `limin112/wechat-publish-template` | 230 | 26 | 27d | **5** | desc:empty, license:none, generic-name:wechat-publish-template, topics:none |
| 7 | `chaseai-yt/grill-me-codex` | 216 | 28 | 9d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 8 | `rulyone/Simple-ReAct-Agent` | 114 | 10 | 28d | **5** | desc:empty, license:none, generic-name:Simple-ReAct-Agent, topics:none |
| 9 | `qqfly1to19/awesome_proofreading_auto` | 141 | 24 | 23d | **5** | desc:empty, license:none, generic-name:awesome_proofreading_auto, topics:none |
| 10 | `jmmy9609-design/gpt-pp` | 397 | 204 | 5d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 11 | `deermiya/visio-skill` | 106 | 9 | 19d | **5** | desc:empty, license:none, generic-name:visio-skill, topics:none |
| 12 | `THUYRan/Legal-Skills-Chinese` | 272 | 37 | 25d | **5** | desc:empty, license:none, generic-name:Legal-Skills-Chinese, topics:none |
| 13 | `rosemarycox5334-debug/PA_Agent` | 263 | 119 | 26d | **5** | desc:empty, license:none, generic-name:PA_Agent, topics:none |
| 14 | `jiaran-king/Re-Zero---Starting-LLM-` | 183 | 5 | 18d | **5** | desc:empty, license:none, generic-name:Re-Zero---Starting-LLM-, topics:none |
| 15 | `piyushgarg-dev/trpc-monorepo` | 118 | 97 | 29d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 143 | 14.3% |
| description <20 chars | 26 | 2.6% |
| no license | 383 | 38.3% |
| high-attention no-desc (stars>1k + empty desc) | 4 | 0.4% |
| low fork ratio (stars>500 + fsr<0.02) | 7 | 0.7% |
| overnight surge (>300 spd + <7 days) | 11 | 1.1% |
| generic-AI-buzzword name | 130 | 13.0% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 7 |
| Unknown | 2 |
| Shell | 1 |
| TypeScript | 1 |
| Rust | 1 |
| JavaScript | 1 |
| HTML | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 2 | 0 | 0 | 2 | 0.0% |
| 5000-9999 | 4 | 1 | 1 | 2 | 25.0% |
| 1000-4999 | 50 | 3 | 5 | 42 | 6.0% |
| 500-999 | 83 | 1 | 19 | 63 | 1.2% |
| 100-499 | 861 | 9 | 150 | 702 | 1.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `XiaomiMiMo/MiMo-Code` | 8827 | 762 | 4d | TypeScript | MIT |
| `FoundZiGu/GuJumpgate` | 3881 | 997 | 26d | JavaScript | MIT |
| `thananon/9arm-skills` | 2793 | 379 | 25d | Shell | — |
| `Tong89/smartNode` | 1987 | 176 | 24d | Python | MIT |

### Generic-name pattern breakdown

Of 130 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 30 |
| `skill` | 25 |
| `skills` | 20 |
| `awesome` | 12 |
| `claude` | 10 |
| `codex` | 8 |
| `llm` | 5 |
| `gpt` | 4 |
| `vibe` | 4 |
| `toolkit` | 3 |
| `template` | 2 |
| `demo` | 2 |
| `agents` | 1 |
| `copilot` | 1 |
| `cookbook` | 1 |
| `prompt` | 1 |
| `starter` | 1 |

### Topics coverage

- Repos with **zero topics**: 635 (63.5%)
- Repos with at least one topic: 365 (36.5%)

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
