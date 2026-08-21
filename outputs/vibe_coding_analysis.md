# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-21 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 118 | 11.8% |
| 訊號完整 | 867 | 86.7% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Zeejay0/gathered-scenes-zine-skill` | 4167 | 434 | 19d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 2 | `sunny-glow/Auto-BenchMax` | 1176 | 27 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `OpenMouse-Project/openmouse` | 1344 | 86 | 24d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `elayadesign/ai-design-skills` | 1204 | 85 | 22d | **6** | desc:empty, high-attention-no-desc, generic-name:ai-design-skills, topics:none |
| 5 | `ZzzLc0405/photo-abstract-editorial` | 4507 | 293 | 16d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `MiniMax-AI/MiniMax-H3` | 6571 | 402 | 21d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `yjh051108/dsh-routing-suite` | 6486 | 119 | 6d | **5** | license:none, low-forks:0.018, overnight-surge:1081/day, topics:none |
| 8 | `AML-memory/agent-memory-leaderboard` | 829 | 31 | 22d | **5** | desc:empty, license:none, generic-name:agent-memory-leaderboard, topics:none |
| 9 | `T8mars/comfyui-minimax-h3-prompt-enhancer-T8` | 150 | 10 | 17d | **5** | desc:empty, license:none, generic-name:comfyui-minimax-h3-prompt-enhancer-T8, topics:none |
| 10 | `almendili/skills` | 343 | 24 | 4d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 11 | `bashalarmistalt/decimen-optical-transfer` | 6207 | 755 | 21d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `google-gemma/gemma-translator` | 1246 | 164 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `gvzdv/claudish-to-english` | 1922 | 96 | 10d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `mikiarlo3/awesome-growth-hacking-skills` | 816 | 16 | 16d | **5** | license:none, low-forks:0.020, generic-name:awesome-growth-hacking-skills, topics:none |
| 15 | `slvDev/esp32-ai` | 4121 | 546 | 28d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 85 | 8.5% |
| description <20 chars | 162 | 16.2% |
| no license | 437 | 43.7% |
| high-attention no-desc (stars>1k + empty desc) | 11 | 1.1% |
| low fork ratio (stars>500 + fsr<0.02) | 14 | 1.4% |
| overnight surge (>300 spd + <7 days) | 15 | 1.5% |
| generic-AI-buzzword name | 108 | 10.8% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| Unknown | 3 |
| TypeScript | 3 |
| Shell | 2 |
| PowerShell | 1 |
| JavaScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 0 | 0 | 6 | 0.0% |
| 5000-9999 | 7 | 3 | 0 | 4 | 42.9% |
| 1000-4999 | 86 | 8 | 6 | 72 | 9.3% |
| 500-999 | 119 | 2 | 17 | 100 | 1.7% |
| 100-499 | 782 | 2 | 95 | 685 | 0.3% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `MiniMax-AI/MiniMax-H3` | 6571 | 402 | 21d | Python | — |
| `bashalarmistalt/decimen-optical-transfer` | 6207 | 755 | 21d | TypeScript | AGPL-3.0 |
| `ZzzLc0405/photo-abstract-editorial` | 4507 | 293 | 16d | Unknown | — |
| `Zeejay0/gathered-scenes-zine-skill` | 4167 | 434 | 19d | Unknown | — |
| `slvDev/esp32-ai` | 4121 | 546 | 28d | Python | MIT |
| `chuspeeism/dashi-taskboard` | 2423 | 318 | 27d | JavaScript | Apache-2.0 |
| `gvzdv/claudish-to-english` | 1922 | 96 | 10d | Shell | MIT |
| `OpenMouse-Project/openmouse` | 1344 | 86 | 24d | TypeScript | — |
| `google-gemma/gemma-translator` | 1246 | 164 | 17d | JavaScript | Apache-2.0 |
| `elayadesign/ai-design-skills` | 1204 | 85 | 22d | Unknown | MIT |
| `sunny-glow/Auto-BenchMax` | 1176 | 27 | 28d | Python | — |

### Generic-name pattern breakdown

Of 108 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 17 |
| `agent` | 16 |
| `awesome` | 16 |
| `skills` | 14 |
| `codex` | 13 |
| `toolkit` | 9 |
| `template` | 4 |
| `claude` | 4 |
| `llm` | 3 |
| `gpt` | 3 |
| `vibe` | 3 |
| `prompt` | 2 |
| `demo` | 2 |
| `copilot` | 1 |
| `starter` | 1 |

### Topics coverage

- Repos with **zero topics**: 435 (43.5%)
- Repos with at least one topic: 565 (56.5%)

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
