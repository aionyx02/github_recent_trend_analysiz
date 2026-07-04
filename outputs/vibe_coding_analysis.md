# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-04 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 98 | 9.8% |
| 訊號完整 | 888 | 88.8% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1320 | 383 | 5d | **6** | desc:empty, high-attention-no-desc, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 2 | `zhongerxin/Cowart` | 3745 | 290 | 15d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `kanavtwtgg/birds.cafe` | 537 | 2 | 12d | **6** | desc:empty, license:none, low-forks:0.004, topics:none |
| 4 | `Harlihm/Your-Self-Improving-AI-Brain` | 718 | 1 | 26d | **6** | desc:empty, license:none, low-forks:0.001, topics:none |
| 5 | `levy-street/world-of-claudecraft` | 1443 | 447 | 23d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 6 | `google-research/tabfm` | 1065 | 101 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `deepreinforce-ai/Ornith-1` | 1131 | 108 | 12d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `JimLiu/science-skills` | 182 | 47 | 2d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |
| 9 | `jmmy9609-design/gpt-pp` | 404 | 203 | 24d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 10 | `Regert888/gpt-outlook-register` | 150 | 57 | 25d | **5** | desc:empty, license:none, generic-name:gpt-outlook-register, topics:none |
| 11 | `world-action-models/awesome-world-action-models` | 307 | 7 | 16d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 12 | `chaseai-yt/grill-me-codex` | 350 | 39 | 28d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 13 | `terrense/LLM_path_for_begginers` | 278 | 7 | 11d | **5** | desc:empty, license:none, generic-name:LLM_path_for_begginers, topics:none |
| 14 | `PlummersSoftwareLLC/TinyRetroPad` | 1116 | 66 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `Neph0s/Agentopia` | 156 | 19 | 28d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 85 | 8.5% |
| description <20 chars | 15 | 1.5% |
| no license | 561 | 56.1% |
| high-attention no-desc (stars>1k + empty desc) | 6 | 0.6% |
| low fork ratio (stars>500 + fsr<0.02) | 13 | 1.3% |
| overnight surge (>300 spd + <7 days) | 8 | 0.8% |
| generic-AI-buzzword name | 139 | 13.9% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 5 |
| Python | 4 |
| JavaScript | 2 |
| TypeScript | 1 |
| HTML | 1 |
| Assembly | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 6 | 0 | 2 | 4 | 0.0% |
| 1000-4999 | 46 | 6 | 5 | 35 | 13.0% |
| 500-999 | 84 | 2 | 12 | 70 | 2.4% |
| 100-499 | 861 | 6 | 79 | 776 | 0.7% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `zhongerxin/Cowart` | 3745 | 290 | 15d | JavaScript | — |
| `levy-street/world-of-claudecraft` | 1443 | 447 | 23d | TypeScript | MIT |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1320 | 383 | 5d | Python | MIT |
| `deepreinforce-ai/Ornith-1` | 1131 | 108 | 12d | Unknown | MIT |
| `PlummersSoftwareLLC/TinyRetroPad` | 1116 | 66 | 29d | Assembly | Apache-2.0 |
| `google-research/tabfm` | 1065 | 101 | 17d | Python | Apache-2.0 |

### Generic-name pattern breakdown

Of 139 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 26 |
| `skill` | 21 |
| `claude` | 20 |
| `skills` | 19 |
| `codex` | 12 |
| `awesome` | 11 |
| `llm` | 4 |
| `starter` | 4 |
| `gpt` | 3 |
| `demo` | 3 |
| `toolkit` | 3 |
| `copilot` | 3 |
| `agents` | 3 |
| `playground` | 2 |
| `prompt` | 2 |
| `template` | 2 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 365 (36.5%)
- Repos with at least one topic: 635 (63.5%)

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
