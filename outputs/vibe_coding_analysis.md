# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-16 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 133 | 13.3% |
| 訊號完整 | 849 | 84.9% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Zeejay0/gathered-scenes-zine-skill` | 3672 | 412 | 14d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 2 | `sunny-glow/Auto-BenchMax` | 1231 | 28 | 23d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `OpenMouse-Project/openmouse` | 1230 | 81 | 19d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `SMNETSTUDIO/WeChat-AI` | 1753 | 1253 | 5d | **6** | desc:empty, high-attention-no-desc, overnight-surge:351/day, topics:none |
| 5 | `ZzzLc0405/photo-abstract-editorial` | 3853 | 258 | 11d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `MiniMax-AI/MiniMax-H3` | 6127 | 364 | 16d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `andrewyng/openworker` | 14576 | 2020 | 26d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `milind-soni/OpenMausBot` | 1053 | 190 | 4d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `bashalarmistalt/decimen-optical-transfer` | 6062 | 733 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `naplesblue/apple-design-skill` | 136 | 18 | 28d | **5** | desc:empty, license:none, generic-name:apple-design-skill, topics:none |
| 11 | `slvDev/esp32-ai` | 4015 | 526 | 23d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `gvzdv/claudish-to-english` | 1209 | 79 | 5d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `that-company/dat-skill` | 177 | 0 | 27d | **5** | desc:empty, license:none, generic-name:dat-skill, topics:none |
| 14 | `google-gemma/gemma-translator` | 1133 | 146 | 12d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `mikiarlo3/awesome-growth-hacking-skills` | 834 | 16 | 11d | **5** | license:none, low-forks:0.019, generic-name:awesome-growth-hacking-skills, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 109 | 10.9% |
| description <20 chars | 95 | 9.5% |
| no license | 355 | 35.5% |
| high-attention no-desc (stars>1k + empty desc) | 13 | 1.3% |
| low fork ratio (stars>500 + fsr<0.02) | 10 | 1.0% |
| overnight surge (>300 spd + <7 days) | 19 | 1.9% |
| generic-AI-buzzword name | 117 | 11.7% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 7 |
| TypeScript | 4 |
| Unknown | 2 |
| Shell | 2 |
| JavaScript | 2 |
| HTML | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 5 | 1 | 0 | 4 | 20.0% |
| 5000-9999 | 8 | 2 | 0 | 6 | 25.0% |
| 1000-4999 | 79 | 10 | 7 | 62 | 12.7% |
| 500-999 | 104 | 2 | 18 | 84 | 1.9% |
| 100-499 | 804 | 3 | 108 | 693 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 14576 | 2020 | 26d | Python | MIT |
| `MiniMax-AI/MiniMax-H3` | 6127 | 364 | 16d | Python | — |
| `bashalarmistalt/decimen-optical-transfer` | 6062 | 733 | 16d | TypeScript | AGPL-3.0 |
| `slvDev/esp32-ai` | 4015 | 526 | 23d | Python | MIT |
| `ZzzLc0405/photo-abstract-editorial` | 3853 | 258 | 11d | Unknown | — |
| `Zeejay0/gathered-scenes-zine-skill` | 3672 | 412 | 14d | Unknown | — |
| `chuspeeism/dashi-taskboard` | 2219 | 289 | 22d | JavaScript | Apache-2.0 |
| `SMNETSTUDIO/WeChat-AI` | 1753 | 1253 | 5d | TypeScript | Apache-2.0 |
| `sunny-glow/Auto-BenchMax` | 1231 | 28 | 23d | Python | — |
| `OpenMouse-Project/openmouse` | 1230 | 81 | 19d | TypeScript | — |
| `gvzdv/claudish-to-english` | 1209 | 79 | 5d | Shell | MIT |
| `google-gemma/gemma-translator` | 1133 | 146 | 12d | JavaScript | Apache-2.0 |
| `milind-soni/OpenMausBot` | 1053 | 190 | 4d | TypeScript | MIT |

### Generic-name pattern breakdown

Of 117 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 22 |
| `agent` | 17 |
| `codex` | 16 |
| `awesome` | 15 |
| `skills` | 14 |
| `claude` | 8 |
| `toolkit` | 6 |
| `template` | 5 |
| `prompt` | 3 |
| `agents` | 2 |
| `demo` | 2 |
| `gpt` | 2 |
| `vibe` | 2 |
| `copilot` | 1 |
| `llm` | 1 |
| `starter` | 1 |

### Topics coverage

- Repos with **zero topics**: 517 (51.7%)
- Repos with at least one topic: 483 (48.3%)

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
