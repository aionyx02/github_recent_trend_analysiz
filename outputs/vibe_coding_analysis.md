# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-29 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 97 | 9.7% |
| 訊號完整 | 889 | 88.9% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Zeejay0/gathered-scenes-zine-skill` | 4553 | 464 | 27d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 2 | `HEJustinSun/my-girlfriend-jingtian-latex` | 3832 | 611 | 1d | **7** | desc:empty, license:none, high-attention-no-desc, overnight-surge:3832/day, topics:none |
| 3 | `MiniMax-AI/MiniMax-H3` | 7371 | 483 | 29d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `ZzzLc0405/photo-abstract-editorial` | 5048 | 320 | 24d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `tobi/walgit` | 2311 | 124 | 5d | **6** | desc:empty, high-attention-no-desc, overnight-surge:462/day, topics:none |
| 6 | `google-gemma/gemma-translator` | 1361 | 179 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `tradecatlabs/shulihuazixuecongshu` | 405 | 77 | 1d | **5** | desc:empty, license:none, overnight-surge:405/day, topics:none |
| 8 | `T8mars/comfyui-minimax-h3-prompt-enhancer-T8` | 206 | 14 | 25d | **5** | desc:empty, license:none, generic-name:comfyui-minimax-h3-prompt-enhancer-T8, topics:none |
| 9 | `gvzdv/claudish-to-english` | 2383 | 109 | 18d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `mikiarlo3/awesome-growth-hacking-skills` | 720 | 14 | 24d | **5** | license:none, low-forks:0.019, generic-name:awesome-growth-hacking-skills, topics:none |
| 11 | `MiniMax-AI/awesome-minimax-h3-integration` | 219 | 16 | 15d | **5** | desc:empty, license:none, generic-name:awesome-minimax-h3-integration, topics:none |
| 12 | `almendili/skills` | 369 | 27 | 12d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 13 | `wide-trace/open-higgsfield` | 1026 | 11 | 2d | **5** | license:none, low-forks:0.011, overnight-surge:513/day, topics:none |
| 14 | `bashalarmistalt/decimen-optical-transfer` | 6566 | 796 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `AwaisShah75/Real-Time-Person-Elderly-Fall-Detection-System` | 188 | 48 | 14d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 71 | 7.1% |
| description <20 chars | 198 | 19.8% |
| no license | 479 | 47.9% |
| high-attention no-desc (stars>1k + empty desc) | 8 | 0.8% |
| low fork ratio (stars>500 + fsr<0.02) | 12 | 1.2% |
| overnight surge (>300 spd + <7 days) | 15 | 1.5% |
| generic-AI-buzzword name | 108 | 10.8% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 3 |
| Python | 3 |
| TypeScript | 3 |
| Shell | 2 |
| TeX | 1 |
| Rust | 1 |
| JavaScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 5 | 0 | 0 | 5 | 0.0% |
| 5000-9999 | 9 | 3 | 1 | 5 | 33.3% |
| 1000-4999 | 81 | 6 | 4 | 71 | 7.4% |
| 500-999 | 137 | 1 | 15 | 121 | 0.7% |
| 100-499 | 768 | 4 | 77 | 687 | 0.5% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `MiniMax-AI/MiniMax-H3` | 7371 | 483 | 29d | Python | — |
| `bashalarmistalt/decimen-optical-transfer` | 6566 | 796 | 29d | TypeScript | AGPL-3.0 |
| `ZzzLc0405/photo-abstract-editorial` | 5048 | 320 | 24d | Unknown | — |
| `Zeejay0/gathered-scenes-zine-skill` | 4553 | 464 | 27d | Unknown | — |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 3832 | 611 | 1d | TeX | — |
| `gvzdv/claudish-to-english` | 2383 | 109 | 18d | Shell | MIT |
| `tobi/walgit` | 2311 | 124 | 5d | Rust | MIT |
| `google-gemma/gemma-translator` | 1361 | 179 | 25d | JavaScript | Apache-2.0 |

### Generic-name pattern breakdown

Of 108 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 16 |
| `awesome` | 16 |
| `skills` | 15 |
| `agent` | 15 |
| `toolkit` | 11 |
| `codex` | 8 |
| `claude` | 6 |
| `llm` | 4 |
| `prompt` | 3 |
| `gpt` | 3 |
| `template` | 3 |
| `starter` | 2 |
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
