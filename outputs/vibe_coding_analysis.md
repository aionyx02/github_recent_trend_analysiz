# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-25 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 12 | 1.2% |
| 待檢視 | 106 | 10.6% |
| 訊號完整 | 882 | 88.2% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Zeejay0/gathered-scenes-zine-skill` | 4349 | 445 | 23d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 2 | `ZzzLc0405/photo-abstract-editorial` | 4734 | 302 | 20d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `MiniMax-AI/MiniMax-H3` | 6985 | 451 | 25d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `OpenMouse-Project/openmouse` | 1390 | 87 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `elayadesign/ai-design-skills` | 1330 | 89 | 26d | **6** | desc:empty, high-attention-no-desc, generic-name:ai-design-skills, topics:none |
| 6 | `tobi/walgit` | 1219 | 68 | 1d | **6** | desc:empty, high-attention-no-desc, overnight-surge:1219/day, topics:none |
| 7 | `T8mars/comfyui-minimax-h3-prompt-enhancer-T8` | 181 | 12 | 21d | **5** | desc:empty, license:none, generic-name:comfyui-minimax-h3-prompt-enhancer-T8, topics:none |
| 8 | `google-gemma/gemma-translator` | 1319 | 175 | 21d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `almendili/skills` | 364 | 26 | 8d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 10 | `bashalarmistalt/decimen-optical-transfer` | 6299 | 767 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `gvzdv/claudish-to-english` | 2228 | 103 | 14d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `AML-memory/agent-memory-leaderboard` | 888 | 32 | 26d | **5** | desc:empty, license:none, generic-name:agent-memory-leaderboard, topics:none |
| 13 | `pingmike2/freebuff2api-wokers` | 346 | 206 | 18d | **4** | desc:empty, license:none, topics:none |
| 14 | `x4gpanell/X4G` | 417 | 1100 | 9d | **4** | desc:empty, license:none, topics:none |
| 15 | `deedy/qr-data-transfer` | 454 | 87 | 24d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 78 | 7.8% |
| description <20 chars | 188 | 18.8% |
| no license | 477 | 47.7% |
| high-attention no-desc (stars>1k + empty desc) | 9 | 0.9% |
| low fork ratio (stars>500 + fsr<0.02) | 11 | 1.1% |
| overnight surge (>300 spd + <7 days) | 9 | 0.9% |
| generic-AI-buzzword name | 108 | 10.8% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 3 |
| Python | 3 |
| TypeScript | 3 |
| Rust | 1 |
| JavaScript | 1 |
| Shell | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 0 | 0 | 6 | 0.0% |
| 5000-9999 | 8 | 2 | 1 | 5 | 25.0% |
| 1000-4999 | 79 | 7 | 5 | 67 | 8.9% |
| 500-999 | 123 | 1 | 15 | 107 | 0.8% |
| 100-499 | 784 | 2 | 85 | 697 | 0.3% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `MiniMax-AI/MiniMax-H3` | 6985 | 451 | 25d | Python | — |
| `bashalarmistalt/decimen-optical-transfer` | 6299 | 767 | 25d | TypeScript | AGPL-3.0 |
| `ZzzLc0405/photo-abstract-editorial` | 4734 | 302 | 20d | Unknown | — |
| `Zeejay0/gathered-scenes-zine-skill` | 4349 | 445 | 23d | Unknown | — |
| `gvzdv/claudish-to-english` | 2228 | 103 | 14d | Shell | MIT |
| `OpenMouse-Project/openmouse` | 1390 | 87 | 28d | TypeScript | — |
| `elayadesign/ai-design-skills` | 1330 | 89 | 26d | Unknown | MIT |
| `google-gemma/gemma-translator` | 1319 | 175 | 21d | JavaScript | Apache-2.0 |
| `tobi/walgit` | 1219 | 68 | 1d | Rust | MIT |

### Generic-name pattern breakdown

Of 108 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 17 |
| `awesome` | 16 |
| `skill` | 15 |
| `skills` | 14 |
| `codex` | 10 |
| `toolkit` | 10 |
| `claude` | 5 |
| `template` | 4 |
| `prompt` | 3 |
| `gpt` | 3 |
| `llm` | 3 |
| `vibe` | 3 |
| `demo` | 2 |
| `starter` | 2 |
| `test` | 1 |

### Topics coverage

- Repos with **zero topics**: 391 (39.1%)
- Repos with at least one topic: 609 (60.9%)

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
