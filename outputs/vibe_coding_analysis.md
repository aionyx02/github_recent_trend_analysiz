# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-24 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 10 | 1.0% |
| 待檢視 | 179 | 17.9% |
| 訊號完整 | 811 | 81.1% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `kanavtwtgg/birds.cafe` | 739 | 1 | 2d | **7** | desc:empty, license:none, low-forks:0.001, overnight-surge:370/day, topics:none |
| 2 | `zhongerxin/Cowart` | 2540 | 199 | 5d | **7** | desc:empty, license:none, high-attention-no-desc, overnight-surge:508/day, topics:none |
| 3 | `world-action-models/awesome-world-action-models` | 264 | 5 | 6d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 4 | `chaseai-yt/grill-me-codex` | 271 | 33 | 18d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 5 | `Regert888/gpt-outlook-register` | 112 | 43 | 15d | **5** | desc:empty, license:none, generic-name:gpt-outlook-register, topics:none |
| 6 | `jiaran-king/Re-Zero---Starting-LLM-` | 216 | 8 | 27d | **5** | desc:empty, license:none, generic-name:Re-Zero---Starting-LLM-, topics:none |
| 7 | `jmmy9609-design/gpt-pp` | 402 | 206 | 14d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 8 | `levy-street/world-of-claudecraft` | 1208 | 361 | 13d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `gakiyukr/Codex_team_auto` | 107 | 53 | 6d | **5** | desc:empty, license:none, generic-name:Codex_team_auto, topics:none |
| 10 | `deermiya/visio-skill` | 122 | 10 | 28d | **5** | desc:empty, license:none, generic-name:visio-skill, topics:none |
| 11 | `johnmiddleton12/wearable` | 285 | 140 | 25d | **4** | desc:empty, license:none, topics:none |
| 12 | `zarazhangrui/zarazhangrui` | 239 | 5 | 22d | **4** | desc:empty, license:none, topics:none |
| 13 | `safeboundai/vibe-scanner` | 244 | 61 | 27d | **4** | desc:empty, generic-name:vibe-scanner, topics:none |
| 14 | `pzr2508/RL_for_Game` | 119 | 2 | 9d | **4** | desc:empty, license:none, topics:none |
| 15 | `Michaelliv/pi-dynamic-workflows` | 994 | 57 | 26d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 140 | 14.0% |
| description <20 chars | 24 | 2.4% |
| no license | 349 | 34.9% |
| high-attention no-desc (stars>1k + empty desc) | 2 | 0.2% |
| low fork ratio (stars>500 + fsr<0.02) | 13 | 1.3% |
| overnight surge (>300 spd + <7 days) | 6 | 0.6% |
| generic-AI-buzzword name | 162 | 16.2% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| JavaScript | 2 |
| Unknown | 2 |
| TypeScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 4 | 0 | 2 | 2 | 0.0% |
| 1000-4999 | 48 | 2 | 3 | 43 | 4.2% |
| 500-999 | 93 | 1 | 18 | 74 | 1.1% |
| 100-499 | 852 | 7 | 156 | 689 | 0.8% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `zhongerxin/Cowart` | 2540 | 199 | 5d | JavaScript | — |
| `levy-street/world-of-claudecraft` | 1208 | 361 | 13d | TypeScript | MIT |

### Generic-name pattern breakdown

Of 162 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 35 |
| `agent` | 31 |
| `skills` | 26 |
| `claude` | 17 |
| `awesome` | 15 |
| `codex` | 12 |
| `gpt` | 6 |
| `llm` | 4 |
| `vibe` | 3 |
| `agents` | 3 |
| `demo` | 2 |
| `prompt` | 2 |
| `toolkit` | 2 |
| `copilot` | 2 |
| `template` | 1 |
| `starter` | 1 |

### Topics coverage

- Repos with **zero topics**: 602 (60.2%)
- Repos with at least one topic: 398 (39.8%)

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
