# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-11 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 138 | 13.8% |
| 訊號完整 | 844 | 84.4% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `ZzzLc0405/photo-abstract-editorial` | 2366 | 120 | 6d | **7** | desc:empty, license:none, high-attention-no-desc, overnight-surge:394/day, topics:none |
| 2 | `Zeejay0/gathered-scenes-zine-skill` | 2328 | 144 | 9d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 3 | `OpenMouse-Project/openmouse` | 1143 | 75 | 14d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `chuspeeism/dashi-taskboard` | 1568 | 220 | 17d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `yuhuangerdi/InduSecAgent` | 770 | 15 | 7d | **6** | desc:empty, license:none, low-forks:0.019, topics:none |
| 6 | `SMNETSTUDIO/WeChat-AI` | 1115 | 828 | 1d | **6** | desc:empty, high-attention-no-desc, overnight-surge:1115/day, topics:none |
| 7 | `X-EraAI/ActPhysCause-Challenge` | 618 | 0 | 25d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 8 | `MiniMax-AI/MiniMax-H3` | 4778 | 293 | 11d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 9 | `that-company/dat-skill` | 178 | 0 | 22d | **5** | desc:empty, license:none, generic-name:dat-skill, topics:none |
| 10 | `h9-tec/Awesome_ai_learning` | 275 | 39 | 25d | **5** | desc:empty, license:none, generic-name:Awesome_ai_learning, topics:none |
| 11 | `slvDev/esp32-ai` | 3919 | 505 | 18d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `naplesblue/apple-design-skill` | 124 | 15 | 23d | **5** | desc:empty, license:none, generic-name:apple-design-skill, topics:none |
| 13 | `LanceZPF/awesome-papers-awesome` | 611 | 1 | 26d | **5** | license:none, low-forks:0.002, generic-name:awesome-papers-awesome, topics:none |
| 14 | `bashalarmistalt/decimen-optical-transfer` | 5739 | 697 | 11d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `mikiarlo3/awesome-growth-hacking-skills` | 822 | 15 | 6d | **5** | license:none, low-forks:0.018, generic-name:awesome-growth-hacking-skills, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 116 | 11.6% |
| description <20 chars | 74 | 7.4% |
| no license | 340 | 34.0% |
| high-attention no-desc (stars>1k + empty desc) | 10 | 1.0% |
| low fork ratio (stars>500 + fsr<0.02) | 15 | 1.5% |
| overnight surge (>300 spd + <7 days) | 9 | 0.9% |
| generic-AI-buzzword name | 125 | 12.5% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| Unknown | 5 |
| TypeScript | 3 |
| JavaScript | 1 |
| Vue | 1 |
| HTML | 1 |
| Shell | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 1 | 1 | 4 | 16.7% |
| 5000-9999 | 7 | 1 | 1 | 5 | 14.3% |
| 1000-4999 | 71 | 7 | 4 | 60 | 9.9% |
| 500-999 | 96 | 4 | 16 | 76 | 4.2% |
| 100-499 | 820 | 5 | 116 | 699 | 0.6% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 14125 | 1928 | 21d | Python | MIT |
| `bashalarmistalt/decimen-optical-transfer` | 5739 | 697 | 11d | TypeScript | AGPL-3.0 |
| `MiniMax-AI/MiniMax-H3` | 4778 | 293 | 11d | Python | — |
| `slvDev/esp32-ai` | 3919 | 505 | 18d | Python | MIT |
| `ZzzLc0405/photo-abstract-editorial` | 2366 | 120 | 6d | Unknown | — |
| `Zeejay0/gathered-scenes-zine-skill` | 2328 | 144 | 9d | Unknown | — |
| `chuspeeism/dashi-taskboard` | 1568 | 220 | 17d | JavaScript | — |
| `CluvexStudio/Aether` | 1453 | 95 | 27d | Rust | AGPL-3.0 |
| `OpenMouse-Project/openmouse` | 1143 | 75 | 14d | TypeScript | — |
| `SMNETSTUDIO/WeChat-AI` | 1115 | 828 | 1d | TypeScript | Apache-2.0 |

### Generic-name pattern breakdown

Of 125 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 22 |
| `codex` | 21 |
| `skill` | 18 |
| `skills` | 16 |
| `awesome` | 14 |
| `claude` | 9 |
| `toolkit` | 5 |
| `agents` | 3 |
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

- Repos with **zero topics**: 528 (52.8%)
- Repos with at least one topic: 472 (47.2%)

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
