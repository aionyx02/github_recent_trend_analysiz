# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-18 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 17 | 1.7% |
| 待檢視 | 150 | 15.0% |
| 訊號完整 | 833 | 83.3% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Zeejay0/gathered-scenes-zine-skill` | 3942 | 427 | 16d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 2 | `sunny-glow/Auto-BenchMax` | 1115 | 27 | 25d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `OpenMouse-Project/openmouse` | 1258 | 82 | 21d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `ZzzLc0405/photo-abstract-editorial` | 4068 | 267 | 13d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `MiniMax-AI/MiniMax-H3` | 6192 | 378 | 18d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `google-gemma/gemma-translator` | 1192 | 154 | 14d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `SMNETSTUDIO/WeChat-AI` | 1776 | 1265 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `AML-memory/agent-memory-leaderboard` | 716 | 26 | 19d | **5** | desc:empty, license:none, generic-name:agent-memory-leaderboard, topics:none |
| 9 | `that-company/dat-skill` | 149 | 0 | 29d | **5** | desc:empty, license:none, generic-name:dat-skill, topics:none |
| 10 | `LaurentiuGabriel/unreal-game-assets-creation-skill` | 123 | 3 | 24d | **5** | desc:empty, license:none, generic-name:unreal-game-assets-creation-skill, topics:none |
| 11 | `andrewyng/openworker` | 14749 | 2045 | 28d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `T8mars/comfyui-minimax-h3-prompt-enhancer-T8` | 136 | 10 | 14d | **5** | desc:empty, license:none, generic-name:comfyui-minimax-h3-prompt-enhancer-T8, topics:none |
| 13 | `slvDev/esp32-ai` | 4062 | 536 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `yjh051108/dsh-routing-suite` | 5650 | 93 | 3d | **5** | license:none, low-forks:0.016, overnight-surge:1883/day, topics:none |
| 15 | `bashalarmistalt/decimen-optical-transfer` | 6131 | 741 | 18d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 121 | 12.1% |
| description <20 chars | 41 | 4.1% |
| no license | 304 | 30.4% |
| high-attention no-desc (stars>1k + empty desc) | 12 | 1.2% |
| low fork ratio (stars>500 + fsr<0.02) | 11 | 1.1% |
| overnight surge (>300 spd + <7 days) | 16 | 1.6% |
| generic-AI-buzzword name | 125 | 12.5% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 8 |
| TypeScript | 3 |
| Unknown | 2 |
| Shell | 2 |
| JavaScript | 1 |
| PowerShell | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 1 | 0 | 5 | 16.7% |
| 5000-9999 | 8 | 3 | 0 | 5 | 37.5% |
| 1000-4999 | 79 | 8 | 8 | 63 | 10.1% |
| 500-999 | 112 | 2 | 17 | 93 | 1.8% |
| 100-499 | 795 | 3 | 125 | 667 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 14749 | 2045 | 28d | Python | MIT |
| `MiniMax-AI/MiniMax-H3` | 6192 | 378 | 18d | Python | — |
| `bashalarmistalt/decimen-optical-transfer` | 6131 | 741 | 18d | TypeScript | AGPL-3.0 |
| `ZzzLc0405/photo-abstract-editorial` | 4068 | 267 | 13d | Unknown | — |
| `slvDev/esp32-ai` | 4062 | 536 | 25d | Python | MIT |
| `Zeejay0/gathered-scenes-zine-skill` | 3942 | 427 | 16d | Unknown | — |
| `chuspeeism/dashi-taskboard` | 2299 | 300 | 24d | JavaScript | Apache-2.0 |
| `SMNETSTUDIO/WeChat-AI` | 1776 | 1265 | 7d | TypeScript | Apache-2.0 |
| `gvzdv/claudish-to-english` | 1297 | 84 | 7d | Shell | MIT |
| `OpenMouse-Project/openmouse` | 1258 | 82 | 21d | TypeScript | — |
| `google-gemma/gemma-translator` | 1192 | 154 | 14d | JavaScript | Apache-2.0 |
| `sunny-glow/Auto-BenchMax` | 1115 | 27 | 25d | Python | — |

### Generic-name pattern breakdown

Of 125 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 22 |
| `agent` | 21 |
| `awesome` | 19 |
| `codex` | 18 |
| `skills` | 13 |
| `claude` | 7 |
| `gpt` | 5 |
| `template` | 4 |
| `agents` | 3 |
| `toolkit` | 3 |
| `vibe` | 3 |
| `prompt` | 2 |
| `demo` | 2 |
| `copilot` | 1 |
| `llm` | 1 |
| `starter` | 1 |

### Topics coverage

- Repos with **zero topics**: 568 (56.8%)
- Repos with at least one topic: 432 (43.2%)

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
