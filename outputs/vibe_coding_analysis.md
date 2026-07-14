# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-14 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 82 | 8.2% |
| 訊號完整 | 904 | 90.4% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `withmarbleapp/os-taxonomy` | 2976 | 525 | 5d | **6** | desc:empty, high-attention-no-desc, overnight-surge:595/day, topics:none |
| 2 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1842 | 476 | 15d | **6** | desc:empty, high-attention-no-desc, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 3 | `x4gKing/X4G` | 5084 | 9474 | 9d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `huang-sir1/radiology-skills` | 773 | 10 | 25d | **6** | desc:empty, low-forks:0.013, generic-name:radiology-skills, topics:none |
| 5 | `kanavtwtgg/birds.cafe` | 515 | 2 | 22d | **6** | desc:empty, license:none, low-forks:0.004, topics:none |
| 6 | `zhongerxin/Cowart` | 4543 | 344 | 25d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `google-research/tabfm` | 1742 | 164 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `deepreinforce-ai/Ornith-1` | 1525 | 147 | 22d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `terrense/LLM_path_for_begginers` | 314 | 8 | 21d | **5** | desc:empty, license:none, generic-name:LLM_path_for_begginers, topics:none |
| 10 | `world-action-models/awesome-world-action-models` | 315 | 7 | 26d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 11 | `jxnl/personal-monorepo-template` | 387 | 42 | 28d | **5** | desc:empty, license:none, generic-name:personal-monorepo-template, topics:none |
| 12 | `x4gKing/Marzban-Node` | 431 | 822 | 1d | **5** | desc:empty, license:none, overnight-surge:431/day, topics:none |
| 13 | `JimLiu/science-skills` | 209 | 53 | 12d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |
| 14 | `x4gKing/Marzban-Panel` | 518 | 912 | 1d | **5** | desc:empty, license:none, overnight-surge:518/day, topics:none |
| 15 | `pengchujin/esp8266-ai` | 168 | 23 | 11d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 79 | 7.9% |
| description <20 chars | 14 | 1.4% |
| no license | 538 | 53.8% |
| high-attention no-desc (stars>1k + empty desc) | 6 | 0.6% |
| low fork ratio (stars>500 + fsr<0.02) | 12 | 1.2% |
| overnight surge (>300 spd + <7 days) | 7 | 0.7% |
| generic-AI-buzzword name | 137 | 13.7% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| JavaScript | 3 |
| Unknown | 3 |
| Dockerfile | 2 |
| HTML | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 2 | 1 | 0 | 1 | 50.0% |
| 1000-4999 | 48 | 5 | 3 | 40 | 10.4% |
| 500-999 | 94 | 3 | 22 | 69 | 3.2% |
| 100-499 | 853 | 5 | 57 | 791 | 0.6% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `x4gKing/X4G` | 5084 | 9474 | 9d | Python | — |
| `zhongerxin/Cowart` | 4543 | 344 | 25d | JavaScript | — |
| `withmarbleapp/os-taxonomy` | 2976 | 525 | 5d | JavaScript | ODbL-1.0 |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1842 | 476 | 15d | Python | MIT |
| `google-research/tabfm` | 1742 | 164 | 27d | Python | Apache-2.0 |
| `deepreinforce-ai/Ornith-1` | 1525 | 147 | 22d | Unknown | MIT |

### Generic-name pattern breakdown

Of 137 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skills` | 23 |
| `skill` | 21 |
| `agent` | 21 |
| `claude` | 17 |
| `codex` | 16 |
| `awesome` | 10 |
| `prompt` | 5 |
| `llm` | 4 |
| `template` | 4 |
| `starter` | 3 |
| `toolkit` | 3 |
| `agents` | 3 |
| `copilot` | 3 |
| `playground` | 2 |
| `gpt` | 1 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 359 (35.9%)
- Repos with at least one topic: 641 (64.1%)

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
