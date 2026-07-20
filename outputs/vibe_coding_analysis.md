# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-20 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 102 | 10.2% |
| 訊號完整 | 885 | 88.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1960 | 494 | 21d | **6** | desc:empty, high-attention-no-desc, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 2 | `x4gKing/X4G` | 5907 | 10854 | 15d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `kanavtwtgg/birds.cafe` | 506 | 2 | 28d | **6** | desc:empty, license:none, low-forks:0.004, topics:none |
| 4 | `x4gKing/3x-ui-Upgrade` | 1113 | 2294 | 11d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `withmarbleapp/os-taxonomy` | 3405 | 585 | 11d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 6 | `TobiasLee/Rebuttal-Skill` | 316 | 12 | 5d | **5** | desc:empty, license:none, generic-name:Rebuttal-Skill, topics:none |
| 7 | `deepreinforce-ai/Ornith-1` | 1626 | 154 | 28d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `terrense/LLM_path_for_begginers` | 307 | 8 | 27d | **5** | desc:empty, license:none, generic-name:LLM_path_for_begginers, topics:none |
| 9 | `h9-tec/Awesome_ai_learning` | 218 | 28 | 3d | **5** | desc:empty, license:none, generic-name:Awesome_ai_learning, topics:none |
| 10 | `Ssupercoder/Salary-Negotiation-Skill` | 526 | 10 | 21d | **5** | license:none, low-forks:0.019, generic-name:Salary-Negotiation-Skill, topics:none |
| 11 | `CluvexStudio/Aether` | 1339 | 81 | 5d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `Fei-Away/Codex-Dream-Skin` | 10844 | 1110 | 4d | **5** | desc:short, license:none, overnight-surge:2711/day, generic-name:Codex-Dream-Skin, topics:none |
| 13 | `JimLiu/science-skills` | 216 | 53 | 18d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |
| 14 | `akihitohyh/chatgpt-register-sub2api` | 287 | 109 | 17d | **4** | desc:empty, license:none, topics:none |
| 15 | `x4gKing/All-Project` | 189 | 39 | 5d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 88 | 8.8% |
| description <20 chars | 20 | 2.0% |
| no license | 512 | 51.2% |
| high-attention no-desc (stars>1k + empty desc) | 6 | 0.6% |
| low fork ratio (stars>500 + fsr<0.02) | 15 | 1.5% |
| overnight surge (>300 spd + <7 days) | 6 | 0.6% |
| generic-AI-buzzword name | 136 | 13.6% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 4 |
| Python | 3 |
| JavaScript | 3 |
| HTML | 2 |
| Rust | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 1 | 0 | 3 | 25.0% |
| 5000-9999 | 4 | 1 | 0 | 3 | 25.0% |
| 1000-4999 | 44 | 5 | 2 | 37 | 11.4% |
| 500-999 | 112 | 2 | 30 | 80 | 1.8% |
| 100-499 | 836 | 4 | 70 | 762 | 0.5% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `x4gKing/X4G` | 5907 | 10854 | 15d | Python | — |
| `withmarbleapp/os-taxonomy` | 3405 | 585 | 11d | JavaScript | ODbL-1.0 |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1960 | 494 | 21d | Python | MIT |
| `deepreinforce-ai/Ornith-1` | 1626 | 154 | 28d | Unknown | MIT |
| `CluvexStudio/Aether` | 1339 | 81 | 5d | Rust | AGPL-3.0 |
| `x4gKing/3x-ui-Upgrade` | 1113 | 2294 | 11d | HTML | — |

### Generic-name pattern breakdown

Of 136 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 24 |
| `skills` | 20 |
| `skill` | 19 |
| `codex` | 17 |
| `claude` | 17 |
| `awesome` | 10 |
| `prompt` | 6 |
| `llm` | 5 |
| `starter` | 4 |
| `agents` | 3 |
| `template` | 3 |
| `gpt` | 3 |
| `toolkit` | 2 |
| `copilot` | 2 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 384 (38.4%)
- Repos with at least one topic: 616 (61.6%)

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
