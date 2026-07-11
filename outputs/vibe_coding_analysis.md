# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-11 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 72 | 7.2% |
| 訊號完整 | 914 | 91.4% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `x4gKing/X4G` | 4136 | 7844 | 6d | **7** | desc:empty, license:none, high-attention-no-desc, overnight-surge:689/day, topics:none |
| 2 | `withmarbleapp/os-taxonomy` | 2245 | 407 | 2d | **6** | desc:empty, high-attention-no-desc, overnight-surge:1122/day, topics:none |
| 3 | `huang-sir1/radiology-skills` | 686 | 10 | 22d | **6** | desc:empty, low-forks:0.015, generic-name:radiology-skills, topics:none |
| 4 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1754 | 465 | 12d | **6** | desc:empty, high-attention-no-desc, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 5 | `zhongerxin/Cowart` | 4345 | 332 | 22d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `kanavtwtgg/birds.cafe` | 521 | 2 | 19d | **6** | desc:empty, license:none, low-forks:0.004, topics:none |
| 7 | `deepreinforce-ai/Ornith-1` | 1466 | 142 | 19d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `google-research/tabfm` | 1667 | 154 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `jxnl/personal-monorepo-template` | 382 | 41 | 25d | **5** | desc:empty, license:none, generic-name:personal-monorepo-template, topics:none |
| 10 | `terrense/LLM_path_for_begginers` | 314 | 8 | 18d | **5** | desc:empty, license:none, generic-name:LLM_path_for_begginers, topics:none |
| 11 | `world-action-models/awesome-world-action-models` | 313 | 7 | 23d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 12 | `x4gKing/3x-ui-Upgrade` | 633 | 1268 | 2d | **5** | desc:empty, license:none, overnight-surge:316/day, topics:none |
| 13 | `jd-opensource/JoyAI-VL-Interaction` | 1229 | 110 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `JimLiu/science-skills` | 207 | 51 | 9d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |
| 15 | `nutshellai-tech/mobius` | 157 | 3 | 22d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 70 | 7.0% |
| description <20 chars | 14 | 1.4% |
| no license | 532 | 53.2% |
| high-attention no-desc (stars>1k + empty desc) | 7 | 0.7% |
| low fork ratio (stars>500 + fsr<0.02) | 10 | 1.0% |
| overnight surge (>300 spd + <7 days) | 6 | 0.6% |
| generic-AI-buzzword name | 141 | 14.1% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| JavaScript | 3 |
| Unknown | 3 |
| HTML | 2 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 2 | 0 | 0 | 2 | 0.0% |
| 1000-4999 | 58 | 7 | 3 | 48 | 12.1% |
| 500-999 | 87 | 3 | 15 | 69 | 3.4% |
| 100-499 | 850 | 4 | 54 | 792 | 0.5% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `zhongerxin/Cowart` | 4345 | 332 | 22d | JavaScript | — |
| `x4gKing/X4G` | 4136 | 7844 | 6d | Python | — |
| `withmarbleapp/os-taxonomy` | 2245 | 407 | 2d | JavaScript | ODbL-1.0 |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1754 | 465 | 12d | Python | MIT |
| `google-research/tabfm` | 1667 | 154 | 24d | Python | Apache-2.0 |
| `deepreinforce-ai/Ornith-1` | 1466 | 142 | 19d | Unknown | MIT |
| `jd-opensource/JoyAI-VL-Interaction` | 1229 | 110 | 29d | Python | Apache-2.0 |

### Generic-name pattern breakdown

Of 141 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 27 |
| `skill` | 24 |
| `skills` | 23 |
| `claude` | 19 |
| `codex` | 14 |
| `awesome` | 9 |
| `llm` | 4 |
| `template` | 3 |
| `starter` | 3 |
| `prompt` | 3 |
| `copilot` | 3 |
| `agents` | 3 |
| `toolkit` | 2 |
| `playground` | 2 |
| `demo` | 1 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 357 (35.7%)
- Repos with at least one topic: 643 (64.3%)

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
