# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-28 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 100 | 10.0% |
| 訊號完整 | 885 | 88.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `HEJustinSun/my-girlfriend-jingtian-latex` | 3644 | 575 | 1d | **7** | desc:empty, license:none, high-attention-no-desc, overnight-surge:3644/day, topics:none |
| 2 | `Zeejay0/gathered-scenes-zine-skill` | 4520 | 460 | 26d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 3 | `elayadesign/ai-design-skills` | 1460 | 101 | 29d | **6** | desc:empty, high-attention-no-desc, generic-name:ai-design-skills, topics:none |
| 4 | `tobi/walgit` | 2286 | 120 | 4d | **6** | desc:empty, high-attention-no-desc, overnight-surge:572/day, topics:none |
| 5 | `MiniMax-AI/MiniMax-H3` | 7322 | 478 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `ZzzLc0405/photo-abstract-editorial` | 5005 | 318 | 23d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `google-gemma/gemma-translator` | 1351 | 176 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `MiniMax-AI/awesome-minimax-h3-integration` | 218 | 16 | 14d | **5** | desc:empty, license:none, generic-name:awesome-minimax-h3-integration, topics:none |
| 9 | `gvzdv/claudish-to-english` | 2374 | 109 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `wide-trace/open-higgsfield` | 942 | 10 | 1d | **5** | license:none, low-forks:0.011, overnight-surge:942/day, topics:none |
| 11 | `T8mars/comfyui-minimax-h3-prompt-enhancer-T8` | 203 | 14 | 24d | **5** | desc:empty, license:none, generic-name:comfyui-minimax-h3-prompt-enhancer-T8, topics:none |
| 12 | `almendili/skills` | 369 | 27 | 11d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 13 | `AML-memory/agent-memory-leaderboard` | 963 | 49 | 29d | **5** | desc:empty, license:none, generic-name:agent-memory-leaderboard, topics:none |
| 14 | `bashalarmistalt/decimen-optical-transfer` | 6553 | 793 | 28d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `mikiarlo3/awesome-growth-hacking-skills` | 719 | 14 | 23d | **5** | license:none, low-forks:0.019, generic-name:awesome-growth-hacking-skills, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 73 | 7.3% |
| description <20 chars | 199 | 19.9% |
| no license | 473 | 47.3% |
| high-attention no-desc (stars>1k + empty desc) | 9 | 0.9% |
| low fork ratio (stars>500 + fsr<0.02) | 11 | 1.1% |
| overnight surge (>300 spd + <7 days) | 13 | 1.3% |
| generic-AI-buzzword name | 111 | 11.1% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 4 |
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
| ≥10000 | 6 | 0 | 0 | 6 | 0.0% |
| 5000-9999 | 9 | 3 | 1 | 5 | 33.3% |
| 1000-4999 | 86 | 6 | 4 | 76 | 7.0% |
| 500-999 | 140 | 3 | 16 | 121 | 2.1% |
| 100-499 | 759 | 3 | 79 | 677 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `MiniMax-AI/MiniMax-H3` | 7322 | 478 | 28d | Python | — |
| `bashalarmistalt/decimen-optical-transfer` | 6553 | 793 | 28d | TypeScript | AGPL-3.0 |
| `ZzzLc0405/photo-abstract-editorial` | 5005 | 318 | 23d | Unknown | — |
| `Zeejay0/gathered-scenes-zine-skill` | 4520 | 460 | 26d | Unknown | — |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 3644 | 575 | 1d | TeX | — |
| `gvzdv/claudish-to-english` | 2374 | 109 | 17d | Shell | MIT |
| `tobi/walgit` | 2286 | 120 | 4d | Rust | MIT |
| `elayadesign/ai-design-skills` | 1460 | 101 | 29d | Unknown | MIT |
| `google-gemma/gemma-translator` | 1351 | 176 | 24d | JavaScript | Apache-2.0 |

### Generic-name pattern breakdown

Of 111 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 17 |
| `skills` | 16 |
| `agent` | 16 |
| `skill` | 15 |
| `toolkit` | 11 |
| `codex` | 9 |
| `claude` | 6 |
| `llm` | 4 |
| `prompt` | 3 |
| `template` | 3 |
| `gpt` | 3 |
| `vibe` | 3 |
| `starter` | 2 |
| `playground` | 1 |
| `demo` | 1 |
| `test` | 1 |

### Topics coverage

- Repos with **zero topics**: 365 (36.5%)
- Repos with at least one topic: 635 (63.5%)

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
