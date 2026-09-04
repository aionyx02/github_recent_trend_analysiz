# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-04 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 6 | 0.6% |
| 待檢視 | 107 | 10.7% |
| 訊號完整 | 887 | 88.7% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `amirh00sain/SpiderPanel` | 1091 | 3663 | 16d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `MiniMax-AI/awesome-minimax-h3-integration` | 285 | 23 | 21d | **5** | desc:empty, license:none, generic-name:awesome-minimax-h3-integration, topics:none |
| 3 | `gvzdv/claudish-to-english` | 2510 | 119 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 4 | `itnann/Data-Analysis-Agent` | 187 | 5 | 28d | **5** | desc:empty, license:none, generic-name:Data-Analysis-Agent, topics:none |
| 5 | `almendili/skills` | 377 | 28 | 18d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 6 | `tobi/walgit` | 2417 | 133 | 11d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `Dlcccc71913/skill-make-photo-stamp-archive` | 329 | 15 | 29d | **4** | desc:empty, generic-name:skill-make-photo-stamp-archive, topics:none |
| 8 | `T8mars/comfyui-minimax-h3-audio-T8` | 934 | 57 | 29d | **4** | desc:empty, license:none, topics:none |
| 9 | `b-nnett/codex-subscription-router` | 402 | 56 | 18d | **4** | desc:empty, generic-name:codex-subscription-router, topics:none |
| 10 | `sjc88661/multi-agent-discuss` | 212 | 24 | 20d | **4** | desc:empty, generic-name:multi-agent-discuss, topics:none |
| 11 | `TheRealYT/git-knife` | 454 | 16 | 24d | **4** | desc:empty, license:none, topics:none |
| 12 | `fzakaria/selfdb` | 522 | 12 | 11d | **4** | desc:empty, license:none, topics:none |
| 13 | `memcode-in/memcode` | 528 | 0 | 18d | **4** | license:none, low-forks:0.000, topics:none |
| 14 | `Danzer1xxxxChan/H3-World` | 203 | 19 | 13d | **4** | desc:empty, license:none, topics:none |
| 15 | `kelvinfkr/company_skill` | 294 | 1 | 10d | **4** | desc:empty, generic-name:company_skill, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 80 | 8.0% |
| description <20 chars | 163 | 16.3% |
| no license | 416 | 41.6% |
| high-attention no-desc (stars>1k + empty desc) | 3 | 0.3% |
| low fork ratio (stars>500 + fsr<0.02) | 15 | 1.5% |
| overnight surge (>300 spd + <7 days) | 9 | 0.9% |
| generic-AI-buzzword name | 105 | 10.5% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 2 |
| Unknown | 1 |
| Shell | 1 |
| TypeScript | 1 |
| Rust | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 0 | 0 | 4 | 0.0% |
| 5000-9999 | 5 | 0 | 0 | 5 | 0.0% |
| 1000-4999 | 80 | 3 | 6 | 71 | 3.8% |
| 500-999 | 136 | 0 | 20 | 116 | 0.0% |
| 100-499 | 775 | 3 | 81 | 691 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `gvzdv/claudish-to-english` | 2510 | 119 | 24d | Shell | MIT |
| `tobi/walgit` | 2417 | 133 | 11d | Rust | MIT |
| `amirh00sain/SpiderPanel` | 1091 | 3663 | 16d | Python | — |

### Generic-name pattern breakdown

Of 105 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 20 |
| `agent` | 17 |
| `skills` | 16 |
| `awesome` | 14 |
| `codex` | 7 |
| `toolkit` | 7 |
| `claude` | 4 |
| `prompt` | 4 |
| `gpt` | 3 |
| `llm` | 3 |
| `agents` | 2 |
| `starter` | 2 |
| `template` | 2 |
| `vibe` | 2 |
| `playground` | 1 |
| `test` | 1 |

### Topics coverage

- Repos with **zero topics**: 380 (38.0%)
- Repos with at least one topic: 620 (62.0%)

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
