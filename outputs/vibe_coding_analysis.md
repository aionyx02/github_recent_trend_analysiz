# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-31 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 106 | 10.6% |
| 訊號完整 | 885 | 88.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Zeejay0/gathered-scenes-zine-skill` | 4640 | 469 | 29d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 2 | `HEJustinSun/my-girlfriend-jingtian-latex` | 4180 | 658 | 3d | **7** | desc:empty, license:none, high-attention-no-desc, overnight-surge:1393/day, topics:none |
| 3 | `ZzzLc0405/photo-abstract-editorial` | 5160 | 324 | 26d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `almendili/skills` | 375 | 27 | 14d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 5 | `MiniMax-AI/awesome-minimax-h3-integration` | 249 | 18 | 17d | **5** | desc:empty, license:none, generic-name:awesome-minimax-h3-integration, topics:none |
| 6 | `T8mars/comfyui-minimax-h3-prompt-enhancer-T8` | 213 | 14 | 27d | **5** | desc:empty, license:none, generic-name:comfyui-minimax-h3-prompt-enhancer-T8, topics:none |
| 7 | `google-gemma/gemma-translator` | 1393 | 182 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `gvzdv/claudish-to-english` | 2420 | 111 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `tobi/walgit` | 2355 | 128 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `boyang-hu/website-rebuild-skill` | 419 | 93 | 19d | **4** | desc:empty, generic-name:website-rebuild-skill, topics:none |
| 11 | `wildminder/awesome-minimax-H3` | 426 | 23 | 26d | **4** | desc:short, license:none, generic-name:awesome-minimax-H3, topics:none |
| 12 | `aashaexo/soundshuman` | 284 | 13 | 23d | **4** | desc:empty, license:none, topics:none |
| 13 | `fzakaria/selfdb` | 490 | 12 | 7d | **4** | desc:empty, license:none, topics:none |
| 14 | `usail-hkust/VibeWorlding-Gym` | 243 | 19 | 25d | **4** | desc:empty, license:none, topics:none |
| 15 | `sophiamyang/finger-frame-effect-lucy` | 238 | 57 | 27d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 74 | 7.4% |
| description <20 chars | 198 | 19.8% |
| no license | 476 | 47.6% |
| high-attention no-desc (stars>1k + empty desc) | 6 | 0.6% |
| low fork ratio (stars>500 + fsr<0.02) | 11 | 1.1% |
| overnight surge (>300 spd + <7 days) | 9 | 0.9% |
| generic-AI-buzzword name | 111 | 11.1% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 3 |
| TeX | 1 |
| TypeScript | 1 |
| Python | 1 |
| JavaScript | 1 |
| Shell | 1 |
| Rust | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 5 | 0 | 0 | 5 | 0.0% |
| 5000-9999 | 8 | 1 | 2 | 5 | 12.5% |
| 1000-4999 | 81 | 5 | 3 | 73 | 6.2% |
| 500-999 | 148 | 0 | 18 | 130 | 0.0% |
| 100-499 | 758 | 3 | 83 | 672 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `ZzzLc0405/photo-abstract-editorial` | 5160 | 324 | 26d | Unknown | — |
| `Zeejay0/gathered-scenes-zine-skill` | 4640 | 469 | 29d | Unknown | — |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 4180 | 658 | 3d | TeX | — |
| `gvzdv/claudish-to-english` | 2420 | 111 | 20d | Shell | MIT |
| `tobi/walgit` | 2355 | 128 | 7d | Rust | MIT |
| `google-gemma/gemma-translator` | 1393 | 182 | 27d | JavaScript | Apache-2.0 |

### Generic-name pattern breakdown

Of 111 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 20 |
| `awesome` | 17 |
| `skills` | 14 |
| `agent` | 14 |
| `toolkit` | 12 |
| `codex` | 8 |
| `claude` | 5 |
| `llm` | 4 |
| `prompt` | 3 |
| `gpt` | 3 |
| `template` | 3 |
| `vibe` | 2 |
| `starter` | 2 |
| `playground` | 1 |
| `test` | 1 |
| `demo` | 1 |
| `agents` | 1 |

### Topics coverage

- Repos with **zero topics**: 354 (35.4%)
- Repos with at least one topic: 646 (64.6%)

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
