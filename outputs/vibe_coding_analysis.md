# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-05 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 91 | 9.1% |
| 訊號完整 | 893 | 89.3% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `huang-sir1/radiology-skills` | 508 | 10 | 16d | **6** | desc:empty, low-forks:0.020, generic-name:radiology-skills, topics:none |
| 2 | `Harlihm/Your-Self-Improving-AI-Brain` | 751 | 1 | 27d | **6** | desc:empty, license:none, low-forks:0.001, topics:none |
| 3 | `kanavtwtgg/birds.cafe` | 537 | 2 | 13d | **6** | desc:empty, license:none, low-forks:0.004, topics:none |
| 4 | `zhongerxin/Cowart` | 3831 | 298 | 16d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1399 | 394 | 6d | **6** | desc:empty, high-attention-no-desc, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 6 | `levy-street/world-of-claudecraft` | 1462 | 456 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `terrense/LLM_path_for_begginers` | 284 | 7 | 12d | **5** | desc:empty, license:none, generic-name:LLM_path_for_begginers, topics:none |
| 8 | `Regert888/gpt-outlook-register` | 161 | 60 | 26d | **5** | desc:empty, license:none, generic-name:gpt-outlook-register, topics:none |
| 9 | `chaseai-yt/grill-me-codex` | 353 | 40 | 29d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 10 | `google-research/tabfm` | 1189 | 109 | 18d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `jd-opensource/JoyAI-VL-Interaction` | 1020 | 88 | 23d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `JimLiu/science-skills` | 191 | 51 | 3d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |
| 13 | `Kulaxyz/token-diet` | 528 | 0 | 1d | **5** | license:none, low-forks:0.000, overnight-surge:528/day, topics:none |
| 14 | `deepreinforce-ai/Ornith-1` | 1207 | 110 | 13d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `world-action-models/awesome-world-action-models` | 309 | 7 | 17d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 76 | 7.6% |
| description <20 chars | 14 | 1.4% |
| no license | 559 | 55.9% |
| high-attention no-desc (stars>1k + empty desc) | 6 | 0.6% |
| low fork ratio (stars>500 + fsr<0.02) | 16 | 1.6% |
| overnight surge (>300 spd + <7 days) | 7 | 0.7% |
| generic-AI-buzzword name | 144 | 14.4% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| Unknown | 5 |
| JavaScript | 2 |
| TypeScript | 1 |
| HTML | 1 |
| Shell | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 6 | 0 | 2 | 4 | 0.0% |
| 1000-4999 | 44 | 6 | 4 | 34 | 13.6% |
| 500-999 | 86 | 4 | 12 | 70 | 4.7% |
| 100-499 | 861 | 6 | 73 | 782 | 0.7% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `zhongerxin/Cowart` | 3831 | 298 | 16d | JavaScript | — |
| `levy-street/world-of-claudecraft` | 1462 | 456 | 24d | TypeScript | MIT |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1399 | 394 | 6d | Python | MIT |
| `deepreinforce-ai/Ornith-1` | 1207 | 110 | 13d | Unknown | MIT |
| `google-research/tabfm` | 1189 | 109 | 18d | Python | Apache-2.0 |
| `jd-opensource/JoyAI-VL-Interaction` | 1020 | 88 | 23d | Python | Apache-2.0 |

### Generic-name pattern breakdown

Of 144 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 26 |
| `skill` | 23 |
| `claude` | 21 |
| `skills` | 20 |
| `codex` | 13 |
| `awesome` | 11 |
| `llm` | 4 |
| `starter` | 4 |
| `gpt` | 3 |
| `demo` | 3 |
| `agents` | 3 |
| `copilot` | 3 |
| `toolkit` | 3 |
| `template` | 2 |
| `playground` | 2 |
| `prompt` | 2 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 355 (35.5%)
- Repos with at least one topic: 645 (64.5%)

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
