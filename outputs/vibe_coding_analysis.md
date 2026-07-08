# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-08 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 15 | 1.5% |
| 待檢視 | 74 | 7.4% |
| 訊號完整 | 911 | 91.1% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `x4gKing/X4G` | 1201 | 2598 | 3d | **7** | desc:empty, license:none, high-attention-no-desc, overnight-surge:400/day, topics:none |
| 2 | `kanavtwtgg/birds.cafe` | 538 | 2 | 16d | **6** | desc:empty, license:none, low-forks:0.004, topics:none |
| 3 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1621 | 448 | 9d | **6** | desc:empty, high-attention-no-desc, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 4 | `zhongerxin/Cowart` | 4116 | 325 | 19d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `huang-sir1/radiology-skills` | 601 | 10 | 19d | **6** | desc:empty, low-forks:0.017, generic-name:radiology-skills, topics:none |
| 6 | `terrense/LLM_path_for_begginers` | 314 | 8 | 15d | **5** | desc:empty, license:none, generic-name:LLM_path_for_begginers, topics:none |
| 7 | `jd-opensource/JoyAI-VL-Interaction` | 1167 | 104 | 26d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `jmmy9609-design/gpt-pp` | 403 | 205 | 28d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 9 | `levy-street/world-of-claudecraft` | 1530 | 477 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `deepreinforce-ai/Ornith-1` | 1396 | 132 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `JimLiu/science-skills` | 204 | 51 | 6d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |
| 12 | `Regert888/gpt-outlook-register` | 186 | 65 | 29d | **5** | desc:empty, license:none, generic-name:gpt-outlook-register, topics:none |
| 13 | `google-research/tabfm` | 1541 | 136 | 21d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `world-action-models/awesome-world-action-models` | 312 | 7 | 20d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 15 | `V4bel/Januscape` | 302 | 39 | 1d | **5** | desc:empty, license:none, overnight-surge:302/day, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 70 | 7.0% |
| description <20 chars | 13 | 1.3% |
| no license | 541 | 54.1% |
| high-attention no-desc (stars>1k + empty desc) | 7 | 0.7% |
| low fork ratio (stars>500 + fsr<0.02) | 12 | 1.2% |
| overnight surge (>300 spd + <7 days) | 10 | 1.0% |
| generic-AI-buzzword name | 142 | 14.2% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 7 |
| Unknown | 3 |
| JavaScript | 2 |
| TypeScript | 1 |
| HTML | 1 |
| C | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 5 | 0 | 0 | 5 | 0.0% |
| 1000-4999 | 52 | 7 | 4 | 41 | 13.5% |
| 500-999 | 93 | 2 | 12 | 79 | 2.2% |
| 100-499 | 847 | 6 | 58 | 783 | 0.7% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `zhongerxin/Cowart` | 4116 | 325 | 19d | JavaScript | — |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1621 | 448 | 9d | Python | MIT |
| `google-research/tabfm` | 1541 | 136 | 21d | Python | Apache-2.0 |
| `levy-street/world-of-claudecraft` | 1530 | 477 | 27d | TypeScript | MIT |
| `deepreinforce-ai/Ornith-1` | 1396 | 132 | 16d | Unknown | MIT |
| `x4gKing/X4G` | 1201 | 2598 | 3d | Python | — |
| `jd-opensource/JoyAI-VL-Interaction` | 1167 | 104 | 26d | Python | Apache-2.0 |

### Generic-name pattern breakdown

Of 142 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 29 |
| `skill` | 23 |
| `skills` | 21 |
| `claude` | 19 |
| `codex` | 10 |
| `awesome` | 10 |
| `agents` | 5 |
| `llm` | 4 |
| `gpt` | 3 |
| `starter` | 3 |
| `prompt` | 3 |
| `copilot` | 3 |
| `demo` | 2 |
| `template` | 2 |
| `toolkit` | 2 |
| `playground` | 2 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 366 (36.6%)
- Repos with at least one topic: 634 (63.4%)

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
