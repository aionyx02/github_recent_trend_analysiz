# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-10 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 22 | 2.2% |
| 待檢視 | 139 | 13.9% |
| 訊號完整 | 839 | 83.9% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Zeejay0/gathered-scenes-zine-skill` | 1966 | 114 | 8d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 2 | `ZzzLc0405/photo-abstract-editorial` | 2063 | 104 | 5d | **7** | desc:empty, license:none, high-attention-no-desc, overnight-surge:413/day, topics:none |
| 3 | `chuspeeism/dashi-taskboard` | 1337 | 197 | 16d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `MiniMax-AI/MiniMax-H3` | 3235 | 193 | 10d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `x4gKing/Marzban-Panel` | 1471 | 2873 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `OpenMouse-Project/openmouse` | 1114 | 73 | 13d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `x4gKing/3x-ui-multi` | 1004 | 2852 | 8d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 8 | `x4gKing/Marzban-Node` | 1300 | 2622 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 9 | `yuhuangerdi/InduSecAgent` | 666 | 12 | 6d | **6** | desc:empty, license:none, low-forks:0.018, topics:none |
| 10 | `X-EraAI/ActPhysCause-Challenge` | 591 | 0 | 24d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 11 | `AML-memory/agent-memory-leaderboard` | 244 | 3 | 11d | **5** | desc:empty, license:none, generic-name:agent-memory-leaderboard, topics:none |
| 12 | `Subhan-code/Amicro--Micro-transitions-` | 1488 | 60 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `bashalarmistalt/decimen-optical-transfer` | 5623 | 684 | 10d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `andrewyng/openworker` | 14017 | 1912 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `h9-tec/Awesome_ai_learning` | 275 | 39 | 24d | **5** | desc:empty, license:none, generic-name:Awesome_ai_learning, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 119 | 11.9% |
| description <20 chars | 75 | 7.5% |
| no license | 339 | 33.9% |
| high-attention no-desc (stars>1k + empty desc) | 13 | 1.3% |
| low fork ratio (stars>500 + fsr<0.02) | 15 | 1.5% |
| overnight surge (>300 spd + <7 days) | 9 | 0.9% |
| generic-AI-buzzword name | 128 | 12.8% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| Unknown | 5 |
| TypeScript | 4 |
| JavaScript | 2 |
| Dockerfile | 2 |
| Vue | 1 |
| Shell | 1 |
| HTML | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 1 | 1 | 4 | 16.7% |
| 5000-9999 | 8 | 1 | 1 | 6 | 12.5% |
| 1000-4999 | 71 | 10 | 4 | 57 | 14.1% |
| 500-999 | 101 | 4 | 18 | 79 | 4.0% |
| 100-499 | 814 | 6 | 115 | 693 | 0.7% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 14017 | 1912 | 20d | Python | MIT |
| `bashalarmistalt/decimen-optical-transfer` | 5623 | 684 | 10d | TypeScript | AGPL-3.0 |
| `slvDev/esp32-ai` | 3880 | 498 | 17d | Python | MIT |
| `MiniMax-AI/MiniMax-H3` | 3235 | 193 | 10d | Python | — |
| `ZzzLc0405/photo-abstract-editorial` | 2063 | 104 | 5d | Unknown | — |
| `Zeejay0/gathered-scenes-zine-skill` | 1966 | 114 | 8d | Unknown | — |
| `CluvexStudio/Aether` | 1778 | 121 | 26d | Rust | AGPL-3.0 |
| `Subhan-code/Amicro--Micro-transitions-` | 1488 | 60 | 29d | TypeScript | MIT |
| `x4gKing/Marzban-Panel` | 1471 | 2873 | 28d | Dockerfile | — |
| `chuspeeism/dashi-taskboard` | 1337 | 197 | 16d | JavaScript | — |
| `x4gKing/Marzban-Node` | 1300 | 2622 | 28d | Dockerfile | — |
| `OpenMouse-Project/openmouse` | 1114 | 73 | 13d | TypeScript | — |
| `x4gKing/3x-ui-multi` | 1004 | 2852 | 8d | JavaScript | — |

### Generic-name pattern breakdown

Of 128 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 22 |
| `codex` | 21 |
| `skill` | 18 |
| `skills` | 16 |
| `awesome` | 14 |
| `claude` | 10 |
| `agents` | 5 |
| `toolkit` | 5 |
| `gpt` | 3 |
| `prompt` | 3 |
| `template` | 3 |
| `demo` | 2 |
| `llm` | 2 |
| `copilot` | 1 |
| `starter` | 1 |
| `playground` | 1 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 533 (53.3%)
- Repos with at least one topic: 467 (46.7%)

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
