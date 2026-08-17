# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-17 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 128 | 12.8% |
| 訊號完整 | 855 | 85.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Zeejay0/gathered-scenes-zine-skill` | 3794 | 422 | 15d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 2 | `sunny-glow/Auto-BenchMax` | 1096 | 27 | 24d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `ZzzLc0405/photo-abstract-editorial` | 3978 | 263 | 12d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `OpenMouse-Project/openmouse` | 1240 | 80 | 20d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `MiniMax-AI/MiniMax-H3` | 6038 | 370 | 17d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `bashalarmistalt/decimen-optical-transfer` | 6095 | 738 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `chuspeeism/dashi-taskboard` | 2269 | 295 | 23d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `naplesblue/apple-design-skill` | 142 | 18 | 29d | **5** | desc:empty, license:none, generic-name:apple-design-skill, topics:none |
| 9 | `T8mars/comfyui-minimax-h3-prompt-enhancer-T8` | 131 | 10 | 13d | **5** | desc:empty, license:none, generic-name:comfyui-minimax-h3-prompt-enhancer-T8, topics:none |
| 10 | `that-company/dat-skill` | 149 | 0 | 28d | **5** | desc:empty, license:none, generic-name:dat-skill, topics:none |
| 11 | `gvzdv/claudish-to-english` | 1254 | 81 | 6d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `SMNETSTUDIO/WeChat-AI` | 1769 | 1259 | 6d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `google-gemma/gemma-translator` | 1171 | 152 | 13d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `mikiarlo3/awesome-growth-hacking-skills` | 835 | 16 | 12d | **5** | license:none, low-forks:0.019, generic-name:awesome-growth-hacking-skills, topics:none |
| 15 | `slvDev/esp32-ai` | 4036 | 531 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 103 | 10.3% |
| description <20 chars | 94 | 9.4% |
| no license | 353 | 35.3% |
| high-attention no-desc (stars>1k + empty desc) | 12 | 1.2% |
| low fork ratio (stars>500 + fsr<0.02) | 10 | 1.0% |
| overnight surge (>300 spd + <7 days) | 18 | 1.8% |
| generic-AI-buzzword name | 120 | 12.0% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 7 |
| TypeScript | 3 |
| Unknown | 2 |
| JavaScript | 2 |
| Shell | 2 |
| HTML | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 1 | 0 | 5 | 16.7% |
| 5000-9999 | 7 | 2 | 0 | 5 | 28.6% |
| 1000-4999 | 78 | 9 | 7 | 62 | 11.5% |
| 500-999 | 107 | 2 | 17 | 88 | 1.9% |
| 100-499 | 802 | 3 | 104 | 695 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 14677 | 2037 | 27d | Python | MIT |
| `bashalarmistalt/decimen-optical-transfer` | 6095 | 738 | 17d | TypeScript | AGPL-3.0 |
| `MiniMax-AI/MiniMax-H3` | 6038 | 370 | 17d | Python | — |
| `slvDev/esp32-ai` | 4036 | 531 | 24d | Python | MIT |
| `ZzzLc0405/photo-abstract-editorial` | 3978 | 263 | 12d | Unknown | — |
| `Zeejay0/gathered-scenes-zine-skill` | 3794 | 422 | 15d | Unknown | — |
| `chuspeeism/dashi-taskboard` | 2269 | 295 | 23d | JavaScript | Apache-2.0 |
| `SMNETSTUDIO/WeChat-AI` | 1769 | 1259 | 6d | TypeScript | Apache-2.0 |
| `gvzdv/claudish-to-english` | 1254 | 81 | 6d | Shell | MIT |
| `OpenMouse-Project/openmouse` | 1240 | 80 | 20d | TypeScript | — |
| `google-gemma/gemma-translator` | 1171 | 152 | 13d | JavaScript | Apache-2.0 |
| `sunny-glow/Auto-BenchMax` | 1096 | 27 | 24d | Python | — |

### Generic-name pattern breakdown

Of 120 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 22 |
| `agent` | 18 |
| `codex` | 18 |
| `awesome` | 14 |
| `skills` | 14 |
| `claude` | 8 |
| `toolkit` | 6 |
| `template` | 4 |
| `gpt` | 4 |
| `vibe` | 3 |
| `prompt` | 2 |
| `agents` | 2 |
| `demo` | 2 |
| `copilot` | 1 |
| `llm` | 1 |
| `starter` | 1 |

### Topics coverage

- Repos with **zero topics**: 512 (51.2%)
- Repos with at least one topic: 488 (48.8%)

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
