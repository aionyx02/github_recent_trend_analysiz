# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-01 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 9 | 0.9% |
| 待檢視 | 111 | 11.1% |
| 訊號完整 | 880 | 88.0% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `HEJustinSun/my-girlfriend-jingtian-latex` | 4212 | 662 | 4d | **7** | desc:empty, license:none, high-attention-no-desc, overnight-surge:1053/day, topics:none |
| 2 | `ZzzLc0405/photo-abstract-editorial` | 5205 | 328 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `gry67673905/-AI-` | 520 | 10 | 16d | **5** | desc:short, license:none, low-forks:0.019, topics:none |
| 4 | `almendili/skills` | 375 | 28 | 15d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 5 | `T8mars/comfyui-minimax-h3-prompt-enhancer-T8` | 217 | 15 | 28d | **5** | desc:empty, license:none, generic-name:comfyui-minimax-h3-prompt-enhancer-T8, topics:none |
| 6 | `tobi/walgit` | 2373 | 130 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `MiniMax-AI/awesome-minimax-h3-integration` | 259 | 18 | 18d | **5** | desc:empty, license:none, generic-name:awesome-minimax-h3-integration, topics:none |
| 8 | `google-gemma/gemma-translator` | 1399 | 184 | 28d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `gvzdv/claudish-to-english` | 2453 | 113 | 21d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `b-nnett/codex-subscription-router` | 396 | 55 | 15d | **4** | desc:empty, generic-name:codex-subscription-router, topics:none |
| 11 | `x4gpanell/X4G` | 653 | 1733 | 16d | **4** | desc:empty, license:none, topics:none |
| 12 | `tluy/skill-zine-summary` | 232 | 17 | 26d | **4** | desc:short, license:none, generic-name:skill-zine-summary, topics:none |
| 13 | `Aether-0/Aether-0.github.io` | 336 | 0 | 29d | **4** | desc:empty, license:none, topics:none |
| 14 | `ganjoor/ganjoor-data` | 225 | 44 | 17d | **4** | desc:empty, license:none, topics:none |
| 15 | `ericzakariasson/scandinavian-design` | 363 | 18 | 19d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 79 | 7.9% |
| description <20 chars | 199 | 19.9% |
| no license | 478 | 47.8% |
| high-attention no-desc (stars>1k + empty desc) | 5 | 0.5% |
| low fork ratio (stars>500 + fsr<0.02) | 13 | 1.3% |
| overnight surge (>300 spd + <7 days) | 6 | 0.6% |
| generic-AI-buzzword name | 109 | 10.9% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 2 |
| Python | 2 |
| TeX | 1 |
| TypeScript | 1 |
| Rust | 1 |
| JavaScript | 1 |
| Shell | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 5 | 0 | 0 | 5 | 0.0% |
| 5000-9999 | 7 | 1 | 2 | 4 | 14.3% |
| 1000-4999 | 81 | 4 | 3 | 74 | 4.9% |
| 500-999 | 146 | 1 | 20 | 125 | 0.7% |
| 100-499 | 761 | 3 | 86 | 672 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `ZzzLc0405/photo-abstract-editorial` | 5205 | 328 | 27d | Unknown | — |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 4212 | 662 | 4d | TeX | — |
| `gvzdv/claudish-to-english` | 2453 | 113 | 21d | Shell | MIT |
| `tobi/walgit` | 2373 | 130 | 8d | Rust | MIT |
| `google-gemma/gemma-translator` | 1399 | 184 | 28d | JavaScript | Apache-2.0 |

### Generic-name pattern breakdown

Of 109 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 19 |
| `awesome` | 17 |
| `skills` | 15 |
| `agent` | 13 |
| `toolkit` | 13 |
| `codex` | 7 |
| `claude` | 5 |
| `llm` | 4 |
| `prompt` | 3 |
| `gpt` | 3 |
| `starter` | 2 |
| `template` | 2 |
| `vibe` | 2 |
| `playground` | 1 |
| `demo` | 1 |
| `test` | 1 |
| `agents` | 1 |

### Topics coverage

- Repos with **zero topics**: 355 (35.5%)
- Repos with at least one topic: 645 (64.5%)

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
