# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-14 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 18 | 1.8% |
| 待檢視 | 143 | 14.3% |
| 訊號完整 | 839 | 83.9% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Zeejay0/gathered-scenes-zine-skill` | 3450 | 391 | 12d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 2 | `X-EraAI/ActPhysCause-Challenge` | 735 | 0 | 28d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 3 | `sunny-glow/Auto-BenchMax` | 1146 | 28 | 21d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `OpenMouse-Project/openmouse` | 1201 | 80 | 17d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `SMNETSTUDIO/WeChat-AI` | 1698 | 1224 | 3d | **6** | desc:empty, high-attention-no-desc, overnight-surge:566/day, topics:none |
| 6 | `ZzzLc0405/photo-abstract-editorial` | 3604 | 235 | 9d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `MiniMax-AI/MiniMax-H3` | 5867 | 355 | 14d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 8 | `chuspeeism/dashi-taskboard` | 2120 | 276 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `mikiarlo3/awesome-growth-hacking-skills` | 825 | 14 | 9d | **5** | license:none, low-forks:0.017, generic-name:awesome-growth-hacking-skills, topics:none |
| 10 | `andrewyng/openworker` | 14458 | 1995 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `h9-tec/Awesome_ai_learning` | 284 | 39 | 28d | **5** | desc:empty, license:none, generic-name:Awesome_ai_learning, topics:none |
| 12 | `that-company/dat-skill` | 177 | 0 | 25d | **5** | desc:empty, license:none, generic-name:dat-skill, topics:none |
| 13 | `bashalarmistalt/decimen-optical-transfer` | 5988 | 727 | 14d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `AML-memory/agent-memory-leaderboard` | 686 | 14 | 15d | **5** | desc:empty, license:none, generic-name:agent-memory-leaderboard, topics:none |
| 15 | `LanceZPF/awesome-papers-awesome` | 657 | 1 | 29d | **5** | license:none, low-forks:0.002, generic-name:awesome-papers-awesome, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 113 | 11.3% |
| description <20 chars | 93 | 9.3% |
| no license | 360 | 36.0% |
| high-attention no-desc (stars>1k + empty desc) | 11 | 1.1% |
| low fork ratio (stars>500 + fsr<0.02) | 18 | 1.8% |
| overnight surge (>300 spd + <7 days) | 21 | 2.1% |
| generic-AI-buzzword name | 123 | 12.3% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 7 |
| Unknown | 4 |
| TypeScript | 3 |
| JavaScript | 2 |
| Shell | 1 |
| HTML | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 1 | 1 | 4 | 16.7% |
| 5000-9999 | 7 | 2 | 0 | 5 | 28.6% |
| 1000-4999 | 80 | 8 | 5 | 67 | 10.0% |
| 500-999 | 112 | 4 | 25 | 83 | 3.6% |
| 100-499 | 795 | 3 | 112 | 680 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 14458 | 1995 | 24d | Python | MIT |
| `bashalarmistalt/decimen-optical-transfer` | 5988 | 727 | 14d | TypeScript | AGPL-3.0 |
| `MiniMax-AI/MiniMax-H3` | 5867 | 355 | 14d | Python | — |
| `slvDev/esp32-ai` | 3983 | 514 | 21d | Python | MIT |
| `ZzzLc0405/photo-abstract-editorial` | 3604 | 235 | 9d | Unknown | — |
| `Zeejay0/gathered-scenes-zine-skill` | 3450 | 391 | 12d | Unknown | — |
| `chuspeeism/dashi-taskboard` | 2120 | 276 | 20d | JavaScript | Apache-2.0 |
| `SMNETSTUDIO/WeChat-AI` | 1698 | 1224 | 3d | TypeScript | Apache-2.0 |
| `OpenMouse-Project/openmouse` | 1201 | 80 | 17d | TypeScript | — |
| `sunny-glow/Auto-BenchMax` | 1146 | 28 | 21d | Python | — |
| `google-gemma/gemma-translator` | 1042 | 136 | 10d | JavaScript | Apache-2.0 |

### Generic-name pattern breakdown

Of 123 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 20 |
| `agent` | 19 |
| `codex` | 18 |
| `skills` | 17 |
| `awesome` | 16 |
| `claude` | 8 |
| `toolkit` | 6 |
| `template` | 5 |
| `gpt` | 3 |
| `agents` | 2 |
| `demo` | 2 |
| `prompt` | 2 |
| `copilot` | 1 |
| `llm` | 1 |
| `starter` | 1 |
| `playground` | 1 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 527 (52.7%)
- Repos with at least one topic: 473 (47.3%)

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
