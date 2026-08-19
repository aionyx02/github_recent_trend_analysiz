# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-19 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 16 | 1.6% |
| 待檢視 | 129 | 12.9% |
| 訊號完整 | 855 | 85.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Zeejay0/gathered-scenes-zine-skill` | 4026 | 429 | 17d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 2 | `OpenMouse-Project/openmouse` | 1270 | 83 | 22d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `MiniMax-AI/MiniMax-H3` | 6318 | 386 | 19d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `ZzzLc0405/photo-abstract-editorial` | 4265 | 279 | 14d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `sunny-glow/Auto-BenchMax` | 1133 | 27 | 26d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `slvDev/esp32-ai` | 4073 | 539 | 26d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `andrewyng/openworker` | 14796 | 2046 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `gvzdv/claudish-to-english` | 1335 | 86 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `bashalarmistalt/decimen-optical-transfer` | 6156 | 746 | 19d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `T8mars/comfyui-minimax-h3-prompt-enhancer-T8` | 137 | 10 | 15d | **5** | desc:empty, license:none, generic-name:comfyui-minimax-h3-prompt-enhancer-T8, topics:none |
| 11 | `zeronsh/comet` | 1001 | 112 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `almendili/skills` | 247 | 13 | 2d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 13 | `SMNETSTUDIO/WeChat-AI` | 1787 | 1266 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `AML-memory/agent-memory-leaderboard` | 760 | 28 | 20d | **5** | desc:empty, license:none, generic-name:agent-memory-leaderboard, topics:none |
| 15 | `yjh051108/dsh-routing-suite` | 6153 | 108 | 4d | **5** | license:none, low-forks:0.018, overnight-surge:1538/day, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 97 | 9.7% |
| description <20 chars | 116 | 11.6% |
| no license | 376 | 37.6% |
| high-attention no-desc (stars>1k + empty desc) | 13 | 1.3% |
| low fork ratio (stars>500 + fsr<0.02) | 13 | 1.3% |
| overnight surge (>300 spd + <7 days) | 16 | 1.6% |
| generic-AI-buzzword name | 113 | 11.3% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| TypeScript | 4 |
| Unknown | 2 |
| Shell | 1 |
| Rust | 1 |
| PowerShell | 1 |
| JavaScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 1 | 0 | 5 | 16.7% |
| 5000-9999 | 7 | 3 | 0 | 4 | 42.9% |
| 1000-4999 | 86 | 9 | 9 | 68 | 10.5% |
| 500-999 | 108 | 1 | 18 | 89 | 0.9% |
| 100-499 | 793 | 2 | 102 | 689 | 0.3% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 14796 | 2046 | 29d | Python | MIT |
| `MiniMax-AI/MiniMax-H3` | 6318 | 386 | 19d | Python | — |
| `bashalarmistalt/decimen-optical-transfer` | 6156 | 746 | 19d | TypeScript | AGPL-3.0 |
| `ZzzLc0405/photo-abstract-editorial` | 4265 | 279 | 14d | Unknown | — |
| `slvDev/esp32-ai` | 4073 | 539 | 26d | Python | MIT |
| `Zeejay0/gathered-scenes-zine-skill` | 4026 | 429 | 17d | Unknown | — |
| `chuspeeism/dashi-taskboard` | 2344 | 307 | 25d | JavaScript | Apache-2.0 |
| `SMNETSTUDIO/WeChat-AI` | 1787 | 1266 | 8d | TypeScript | Apache-2.0 |
| `gvzdv/claudish-to-english` | 1335 | 86 | 8d | Shell | MIT |
| `OpenMouse-Project/openmouse` | 1270 | 83 | 22d | TypeScript | — |
| `google-gemma/gemma-translator` | 1211 | 160 | 15d | JavaScript | Apache-2.0 |
| `sunny-glow/Auto-BenchMax` | 1133 | 27 | 26d | Python | — |
| `zeronsh/comet` | 1001 | 112 | 29d | Rust | MIT |

### Generic-name pattern breakdown

Of 113 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 19 |
| `skill` | 18 |
| `awesome` | 16 |
| `skills` | 14 |
| `codex` | 13 |
| `toolkit` | 7 |
| `claude` | 7 |
| `template` | 4 |
| `gpt` | 3 |
| `vibe` | 3 |
| `prompt` | 2 |
| `demo` | 2 |
| `llm` | 2 |
| `copilot` | 1 |
| `agents` | 1 |
| `starter` | 1 |

### Topics coverage

- Repos with **zero topics**: 477 (47.7%)
- Repos with at least one topic: 523 (52.3%)

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
