# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-17 | Sample size: 1000 repos (with topics signal)_

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
| 1 | `x4gKing/X4G` | 5705 | 10526 | 12d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1914 | 488 | 18d | **6** | desc:empty, high-attention-no-desc, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 3 | `x4gKing/3x-ui-Upgrade` | 1107 | 2287 | 8d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `huang-sir1/radiology-skills` | 860 | 10 | 28d | **6** | desc:empty, low-forks:0.012, generic-name:radiology-skills, topics:none |
| 5 | `kanavtwtgg/birds.cafe` | 509 | 2 | 25d | **6** | desc:empty, license:none, low-forks:0.004, topics:none |
| 6 | `deepreinforce-ai/Ornith-1` | 1586 | 151 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `withmarbleapp/os-taxonomy` | 3220 | 553 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `JimLiu/science-skills` | 212 | 53 | 15d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |
| 9 | `TobiasLee/Rebuttal-Skill` | 302 | 11 | 2d | **5** | desc:empty, license:none, generic-name:Rebuttal-Skill, topics:none |
| 10 | `terrense/LLM_path_for_begginers` | 314 | 8 | 24d | **5** | desc:empty, license:none, generic-name:LLM_path_for_begginers, topics:none |
| 11 | `Fei-Away/Codex-Dream-Skin` | 7480 | 818 | 1d | **5** | desc:short, license:none, overnight-surge:7480/day, generic-name:Codex-Dream-Skin, topics:none |
| 12 | `Ssupercoder/Salary-Negotiation-Skill` | 551 | 11 | 18d | **5** | license:none, low-forks:0.020, generic-name:Salary-Negotiation-Skill, topics:none |
| 13 | `world-action-models/awesome-world-action-models` | 319 | 7 | 29d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 14 | `zhongerxin/Cowart` | 4742 | 359 | 28d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `YangWang92/open-open-reasoning` | 163 | 162 | 5d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 87 | 8.7% |
| description <20 chars | 18 | 1.8% |
| no license | 536 | 53.6% |
| high-attention no-desc (stars>1k + empty desc) | 6 | 0.6% |
| low fork ratio (stars>500 + fsr<0.02) | 16 | 1.6% |
| overnight surge (>300 spd + <7 days) | 9 | 0.9% |
| generic-AI-buzzword name | 137 | 13.7% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 4 |
| JavaScript | 4 |
| Unknown | 4 |
| HTML | 2 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 0 | 0 | 4 | 0.0% |
| 5000-9999 | 4 | 2 | 0 | 2 | 50.0% |
| 1000-4999 | 48 | 5 | 4 | 39 | 10.4% |
| 500-999 | 102 | 3 | 29 | 70 | 2.9% |
| 100-499 | 842 | 4 | 65 | 773 | 0.5% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `x4gKing/X4G` | 5705 | 10526 | 12d | Python | — |
| `zhongerxin/Cowart` | 4742 | 359 | 28d | JavaScript | MIT |
| `withmarbleapp/os-taxonomy` | 3220 | 553 | 8d | JavaScript | ODbL-1.0 |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1914 | 488 | 18d | Python | MIT |
| `deepreinforce-ai/Ornith-1` | 1586 | 151 | 25d | Unknown | MIT |
| `x4gKing/3x-ui-Upgrade` | 1107 | 2287 | 8d | HTML | — |

### Generic-name pattern breakdown

Of 137 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 25 |
| `skills` | 22 |
| `skill` | 18 |
| `codex` | 17 |
| `claude` | 17 |
| `awesome` | 10 |
| `llm` | 5 |
| `prompt` | 4 |
| `agents` | 3 |
| `gpt` | 3 |
| `starter` | 3 |
| `template` | 3 |
| `copilot` | 3 |
| `toolkit` | 2 |
| `playground` | 1 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 371 (37.1%)
- Repos with at least one topic: 629 (62.9%)

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
