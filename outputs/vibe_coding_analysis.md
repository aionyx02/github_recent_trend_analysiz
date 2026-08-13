# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-13 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 28 | 2.8% |
| 待檢視 | 135 | 13.5% |
| 訊號完整 | 837 | 83.7% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Zeejay0/gathered-scenes-zine-skill` | 3232 | 364 | 11d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 2 | `ZzzLc0405/photo-abstract-editorial` | 3246 | 196 | 8d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `SMNETSTUDIO/WeChat-AI` | 1634 | 1181 | 2d | **6** | desc:empty, high-attention-no-desc, overnight-surge:817/day, topics:none |
| 4 | `MiniMax-AI/MiniMax-H3` | 5557 | 346 | 13d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `OpenMouse-Project/openmouse` | 1187 | 78 | 16d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `sunny-glow/Auto-BenchMax` | 1097 | 28 | 20d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `X-EraAI/ActPhysCause-Challenge` | 693 | 0 | 27d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 8 | `chuspeeism/dashi-taskboard` | 1948 | 258 | 19d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `QAI-brain/awesome-QAI-Papers-QComputing` | 208 | 0 | 29d | **5** | desc:empty, license:none, generic-name:awesome-QAI-Papers-QComputing, topics:none |
| 10 | `h9-tec/Awesome_ai_learning` | 281 | 39 | 27d | **5** | desc:empty, license:none, generic-name:Awesome_ai_learning, topics:none |
| 11 | `QAI-brain/awesome-QAI-Papers-QDiffusion` | 207 | 0 | 29d | **5** | desc:empty, license:none, generic-name:awesome-QAI-Papers-QDiffusion, topics:none |
| 12 | `AML-memory/agent-memory-leaderboard` | 614 | 13 | 14d | **5** | desc:empty, license:none, generic-name:agent-memory-leaderboard, topics:none |
| 13 | `mikiarlo3/awesome-growth-hacking-skills` | 827 | 14 | 8d | **5** | license:none, low-forks:0.017, generic-name:awesome-growth-hacking-skills, topics:none |
| 14 | `andrewyng/openworker` | 14351 | 1970 | 23d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `QAI-brain/awesome-QAI-Papers-QRL` | 209 | 0 | 29d | **5** | desc:empty, license:none, generic-name:awesome-QAI-Papers-QRL, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 123 | 12.3% |
| description <20 chars | 94 | 9.4% |
| no license | 363 | 36.3% |
| high-attention no-desc (stars>1k + empty desc) | 11 | 1.1% |
| low fork ratio (stars>500 + fsr<0.02) | 16 | 1.6% |
| overnight surge (>300 spd + <7 days) | 12 | 1.2% |
| generic-AI-buzzword name | 127 | 12.7% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 15 |
| Python | 7 |
| TypeScript | 3 |
| JavaScript | 1 |
| Shell | 1 |
| HTML | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 1 | 1 | 4 | 16.7% |
| 5000-9999 | 6 | 2 | 0 | 4 | 33.3% |
| 1000-4999 | 77 | 7 | 6 | 64 | 9.1% |
| 500-999 | 103 | 4 | 19 | 80 | 3.9% |
| 100-499 | 808 | 14 | 109 | 685 | 1.7% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 14351 | 1970 | 23d | Python | MIT |
| `bashalarmistalt/decimen-optical-transfer` | 5913 | 717 | 13d | TypeScript | AGPL-3.0 |
| `MiniMax-AI/MiniMax-H3` | 5557 | 346 | 13d | Python | — |
| `slvDev/esp32-ai` | 3971 | 513 | 20d | Python | MIT |
| `ZzzLc0405/photo-abstract-editorial` | 3246 | 196 | 8d | Unknown | — |
| `Zeejay0/gathered-scenes-zine-skill` | 3232 | 364 | 11d | Unknown | — |
| `chuspeeism/dashi-taskboard` | 1948 | 258 | 19d | JavaScript | Apache-2.0 |
| `SMNETSTUDIO/WeChat-AI` | 1634 | 1181 | 2d | TypeScript | Apache-2.0 |
| `CluvexStudio/Aether` | 1460 | 92 | 29d | Rust | AGPL-3.0 |
| `OpenMouse-Project/openmouse` | 1187 | 78 | 16d | TypeScript | — |
| `sunny-glow/Auto-BenchMax` | 1097 | 28 | 20d | Python | — |

### Generic-name pattern breakdown

Of 127 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 24 |
| `skill` | 21 |
| `agent` | 20 |
| `codex` | 17 |
| `skills` | 15 |
| `claude` | 8 |
| `toolkit` | 5 |
| `template` | 4 |
| `agents` | 2 |
| `demo` | 2 |
| `gpt` | 2 |
| `prompt` | 2 |
| `copilot` | 1 |
| `llm` | 1 |
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
