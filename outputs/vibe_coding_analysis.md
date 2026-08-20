# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-20 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 126 | 12.6% |
| 訊號完整 | 860 | 86.0% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Zeejay0/gathered-scenes-zine-skill` | 4093 | 430 | 18d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 2 | `OpenMouse-Project/openmouse` | 1314 | 84 | 23d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `sunny-glow/Auto-BenchMax` | 1152 | 27 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `elayadesign/ai-design-skills` | 1055 | 72 | 21d | **6** | desc:empty, high-attention-no-desc, generic-name:ai-design-skills, topics:none |
| 5 | `MiniMax-AI/MiniMax-H3` | 6421 | 393 | 20d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `ZzzLc0405/photo-abstract-editorial` | 4422 | 286 | 15d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `almendili/skills` | 329 | 23 | 3d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 8 | `google-gemma/gemma-translator` | 1233 | 162 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `T8mars/comfyui-minimax-h3-prompt-enhancer-T8` | 140 | 10 | 16d | **5** | desc:empty, license:none, generic-name:comfyui-minimax-h3-prompt-enhancer-T8, topics:none |
| 10 | `bashalarmistalt/decimen-optical-transfer` | 6175 | 753 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `yjh051108/dsh-routing-suite` | 6367 | 114 | 5d | **5** | license:none, low-forks:0.018, overnight-surge:1273/day, topics:none |
| 12 | `slvDev/esp32-ai` | 4101 | 541 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `AML-memory/agent-memory-leaderboard` | 799 | 30 | 21d | **5** | desc:empty, license:none, generic-name:agent-memory-leaderboard, topics:none |
| 14 | `gvzdv/claudish-to-english` | 1373 | 89 | 9d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `Tencent-Hunyuan/Hunyuan3D-WorldClaw` | 887 | 55 | 14d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 90 | 9.0% |
| description <20 chars | 131 | 13.1% |
| no license | 401 | 40.1% |
| high-attention no-desc (stars>1k + empty desc) | 11 | 1.1% |
| low fork ratio (stars>500 + fsr<0.02) | 15 | 1.5% |
| overnight surge (>300 spd + <7 days) | 18 | 1.8% |
| generic-AI-buzzword name | 109 | 10.9% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| Unknown | 3 |
| TypeScript | 3 |
| JavaScript | 1 |
| PowerShell | 1 |
| Shell | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 0 | 0 | 6 | 0.0% |
| 5000-9999 | 6 | 3 | 0 | 3 | 50.0% |
| 1000-4999 | 86 | 8 | 7 | 71 | 9.3% |
| 500-999 | 116 | 1 | 22 | 93 | 0.9% |
| 100-499 | 786 | 2 | 97 | 687 | 0.3% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `MiniMax-AI/MiniMax-H3` | 6421 | 393 | 20d | Python | — |
| `bashalarmistalt/decimen-optical-transfer` | 6175 | 753 | 20d | TypeScript | AGPL-3.0 |
| `ZzzLc0405/photo-abstract-editorial` | 4422 | 286 | 15d | Unknown | — |
| `slvDev/esp32-ai` | 4101 | 541 | 27d | Python | MIT |
| `Zeejay0/gathered-scenes-zine-skill` | 4093 | 430 | 18d | Unknown | — |
| `chuspeeism/dashi-taskboard` | 2386 | 313 | 26d | JavaScript | Apache-2.0 |
| `gvzdv/claudish-to-english` | 1373 | 89 | 9d | Shell | MIT |
| `OpenMouse-Project/openmouse` | 1314 | 84 | 23d | TypeScript | — |
| `google-gemma/gemma-translator` | 1233 | 162 | 16d | JavaScript | Apache-2.0 |
| `sunny-glow/Auto-BenchMax` | 1152 | 27 | 27d | Python | — |
| `elayadesign/ai-design-skills` | 1055 | 72 | 21d | Unknown | MIT |

### Generic-name pattern breakdown

Of 109 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 17 |
| `agent` | 17 |
| `awesome` | 15 |
| `skills` | 13 |
| `codex` | 13 |
| `toolkit` | 8 |
| `claude` | 7 |
| `template` | 4 |
| `gpt` | 3 |
| `llm` | 3 |
| `vibe` | 3 |
| `prompt` | 2 |
| `demo` | 2 |
| `copilot` | 1 |
| `starter` | 1 |

### Topics coverage

- Repos with **zero topics**: 460 (46.0%)
- Repos with at least one topic: 540 (54.0%)

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
