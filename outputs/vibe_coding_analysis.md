# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-02 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 10 | 1.0% |
| 待檢視 | 106 | 10.6% |
| 訊號完整 | 884 | 88.4% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `ZzzLc0405/photo-abstract-editorial` | 5253 | 329 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `amirh00sain/SpiderPanel` | 1024 | 3438 | 14d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `google-gemma/gemma-translator` | 1411 | 186 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 4 | `subsy/skill-cabinet` | 336 | 21 | 1d | **5** | desc:empty, overnight-surge:336/day, generic-name:skill-cabinet, topics:none |
| 5 | `Tiger3807861189/DeepSeek-V4-J-Space-Capability-Realization-Report` | 1030 | 63 | 16d | **5** | desc:empty, license:none, high-attention-no-desc |
| 6 | `MiniMax-AI/awesome-minimax-h3-integration` | 268 | 19 | 19d | **5** | desc:empty, license:none, generic-name:awesome-minimax-h3-integration, topics:none |
| 7 | `tobi/walgit` | 2394 | 132 | 9d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `gvzdv/claudish-to-english` | 2474 | 116 | 22d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `almendili/skills` | 376 | 28 | 16d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 10 | `T8mars/comfyui-minimax-h3-prompt-enhancer-T8` | 219 | 17 | 29d | **5** | desc:empty, license:none, generic-name:comfyui-minimax-h3-prompt-enhancer-T8, topics:none |
| 11 | `sophiamyang/finger-frame-effect-lucy` | 238 | 57 | 29d | **4** | desc:empty, license:none, topics:none |
| 12 | `aashaexo/soundshuman` | 289 | 13 | 25d | **4** | desc:empty, license:none, topics:none |
| 13 | `x4gpanell/3x-ui` | 279 | 825 | 17d | **4** | desc:empty, license:none, topics:none |
| 14 | `Sidiora-Labs/LayerX-Protocol` | 384 | 72 | 18d | **4** | desc:empty, license:none, topics:none |
| 15 | `TheRealYT/git-knife` | 452 | 16 | 22d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 76 | 7.6% |
| description <20 chars | 195 | 19.5% |
| no license | 468 | 46.8% |
| high-attention no-desc (stars>1k + empty desc) | 6 | 0.6% |
| low fork ratio (stars>500 + fsr<0.02) | 13 | 1.3% |
| overnight surge (>300 spd + <7 days) | 9 | 0.9% |
| generic-AI-buzzword name | 110 | 11.0% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 3 |
| Python | 2 |
| JavaScript | 2 |
| Rust | 1 |
| Shell | 1 |
| TypeScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 0 | 1 | 5 | 0.0% |
| 5000-9999 | 6 | 1 | 1 | 4 | 16.7% |
| 1000-4999 | 83 | 5 | 4 | 74 | 6.0% |
| 500-999 | 141 | 0 | 19 | 122 | 0.0% |
| 100-499 | 764 | 4 | 81 | 679 | 0.5% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `ZzzLc0405/photo-abstract-editorial` | 5253 | 329 | 28d | Unknown | — |
| `gvzdv/claudish-to-english` | 2474 | 116 | 22d | Shell | MIT |
| `tobi/walgit` | 2394 | 132 | 9d | Rust | MIT |
| `google-gemma/gemma-translator` | 1411 | 186 | 29d | JavaScript | Apache-2.0 |
| `Tiger3807861189/DeepSeek-V4-J-Space-Capability-Realization-Report` | 1030 | 63 | 16d | Unknown | — |
| `amirh00sain/SpiderPanel` | 1024 | 3438 | 14d | Python | — |

### Generic-name pattern breakdown

Of 110 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 18 |
| `awesome` | 16 |
| `skills` | 15 |
| `agent` | 15 |
| `toolkit` | 13 |
| `codex` | 7 |
| `claude` | 5 |
| `llm` | 4 |
| `prompt` | 3 |
| `gpt` | 3 |
| `starter` | 3 |
| `template` | 2 |
| `vibe` | 2 |
| `playground` | 1 |
| `test` | 1 |
| `demo` | 1 |
| `agents` | 1 |

### Topics coverage

- Repos with **zero topics**: 348 (34.8%)
- Repos with at least one topic: 652 (65.2%)

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
