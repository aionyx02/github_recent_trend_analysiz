# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-26 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 13 | 1.3% |
| 待檢視 | 102 | 10.2% |
| 訊號完整 | 885 | 88.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Zeejay0/gathered-scenes-zine-skill` | 4392 | 448 | 24d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 2 | `elayadesign/ai-design-skills` | 1399 | 94 | 27d | **6** | desc:empty, high-attention-no-desc, generic-name:ai-design-skills, topics:none |
| 3 | `tobi/walgit` | 1656 | 90 | 2d | **6** | desc:empty, high-attention-no-desc, overnight-surge:828/day, topics:none |
| 4 | `ZzzLc0405/photo-abstract-editorial` | 4817 | 307 | 21d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `OpenMouse-Project/openmouse` | 1402 | 89 | 29d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `MiniMax-AI/MiniMax-H3` | 7110 | 462 | 26d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `gvzdv/claudish-to-english` | 2272 | 106 | 15d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `AML-memory/agent-memory-leaderboard` | 904 | 33 | 27d | **5** | desc:empty, license:none, generic-name:agent-memory-leaderboard, topics:none |
| 9 | `MiniMax-AI/awesome-minimax-h3-integration` | 157 | 12 | 12d | **5** | desc:empty, license:none, generic-name:awesome-minimax-h3-integration, topics:none |
| 10 | `google-gemma/gemma-translator` | 1332 | 175 | 22d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `T8mars/comfyui-minimax-h3-prompt-enhancer-T8` | 190 | 13 | 22d | **5** | desc:empty, license:none, generic-name:comfyui-minimax-h3-prompt-enhancer-T8, topics:none |
| 12 | `almendili/skills` | 366 | 27 | 9d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 13 | `bashalarmistalt/decimen-optical-transfer` | 6432 | 779 | 26d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `b-nnett/codex-subscription-router` | 386 | 48 | 9d | **4** | desc:empty, generic-name:codex-subscription-router, topics:none |
| 15 | `wildminder/awesome-minimax-H3` | 386 | 20 | 21d | **4** | desc:short, license:none, generic-name:awesome-minimax-H3, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 76 | 7.6% |
| description <20 chars | 191 | 19.1% |
| no license | 471 | 47.1% |
| high-attention no-desc (stars>1k + empty desc) | 9 | 0.9% |
| low fork ratio (stars>500 + fsr<0.02) | 10 | 1.0% |
| overnight surge (>300 spd + <7 days) | 8 | 0.8% |
| generic-AI-buzzword name | 108 | 10.8% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 4 |
| TypeScript | 3 |
| Python | 3 |
| Rust | 1 |
| Shell | 1 |
| JavaScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 0 | 0 | 6 | 0.0% |
| 5000-9999 | 9 | 2 | 1 | 6 | 22.2% |
| 1000-4999 | 80 | 7 | 4 | 69 | 8.8% |
| 500-999 | 126 | 1 | 15 | 110 | 0.8% |
| 100-499 | 779 | 3 | 82 | 694 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `MiniMax-AI/MiniMax-H3` | 7110 | 462 | 26d | Python | — |
| `bashalarmistalt/decimen-optical-transfer` | 6432 | 779 | 26d | TypeScript | AGPL-3.0 |
| `ZzzLc0405/photo-abstract-editorial` | 4817 | 307 | 21d | Unknown | — |
| `Zeejay0/gathered-scenes-zine-skill` | 4392 | 448 | 24d | Unknown | — |
| `gvzdv/claudish-to-english` | 2272 | 106 | 15d | Shell | MIT |
| `tobi/walgit` | 1656 | 90 | 2d | Rust | MIT |
| `OpenMouse-Project/openmouse` | 1402 | 89 | 29d | TypeScript | — |
| `elayadesign/ai-design-skills` | 1399 | 94 | 27d | Unknown | MIT |
| `google-gemma/gemma-translator` | 1332 | 175 | 22d | JavaScript | Apache-2.0 |

### Generic-name pattern breakdown

Of 108 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 18 |
| `awesome` | 18 |
| `skill` | 15 |
| `skills` | 14 |
| `toolkit` | 10 |
| `codex` | 8 |
| `claude` | 4 |
| `prompt` | 3 |
| `gpt` | 3 |
| `template` | 3 |
| `llm` | 3 |
| `vibe` | 3 |
| `demo` | 2 |
| `starter` | 2 |
| `playground` | 1 |
| `test` | 1 |

### Topics coverage

- Repos with **zero topics**: 389 (38.9%)
- Repos with at least one topic: 611 (61.1%)

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
