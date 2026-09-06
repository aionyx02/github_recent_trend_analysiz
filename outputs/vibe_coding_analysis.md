# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-06 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 7 | 0.7% |
| 待檢視 | 120 | 12.0% |
| 訊號完整 | 873 | 87.3% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `amirh00sain/SpiderPanel` | 1144 | 3852 | 18d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `tigerless-labs/agent-memory` | 299 | 19 | 4d | **5** | desc:empty, license:none, generic-name:agent-memory, topics:none |
| 3 | `MiniMax-AI/awesome-minimax-h3-integration` | 295 | 24 | 23d | **5** | desc:empty, license:none, generic-name:awesome-minimax-h3-integration, topics:none |
| 4 | `almendili/skills` | 377 | 28 | 20d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 5 | `gvzdv/claudish-to-english` | 2533 | 120 | 26d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 6 | `yczz/oc-english` | 826 | 9 | 4d | **5** | desc:short, license:none, low-forks:0.011, topics:none |
| 7 | `tobi/walgit` | 2438 | 138 | 13d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `lvgalvao/projeto-dados-ia-databricks` | 269 | 62 | 12d | **4** | desc:empty, license:none, topics:none |
| 9 | `AlloxOrg/allox-os` | 215 | 2 | 24d | **4** | desc:empty, license:none, topics:none |
| 10 | `hirotomasato/jiofarm` | 201 | 74 | 13d | **4** | desc:empty, license:none, topics:none |
| 11 | `soumatheusgomes/buscandomilhao` | 202 | 42 | 9d | **4** | desc:empty, license:none, topics:none |
| 12 | `QIYUEKURONG/ai-learning-planner` | 211 | 1 | 26d | **4** | desc:empty, license:none, topics:none |
| 13 | `Danzer1xxxxChan/H3-World` | 223 | 26 | 15d | **4** | desc:empty, license:none, topics:none |
| 14 | `KJGX66F/bot-hosting-vless` | 248 | 456 | 11d | **4** | desc:empty, license:none, topics:none |
| 15 | `AwaisShah75/Real-Time-Person-Elderly-Fall-Detection-System` | 234 | 58 | 22d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 96 | 9.6% |
| description <20 chars | 17 | 1.7% |
| no license | 265 | 26.5% |
| high-attention no-desc (stars>1k + empty desc) | 3 | 0.3% |
| low fork ratio (stars>500 + fsr<0.02) | 16 | 1.6% |
| overnight surge (>300 spd + <7 days) | 11 | 1.1% |
| generic-AI-buzzword name | 116 | 11.6% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 2 |
| Unknown | 1 |
| TypeScript | 1 |
| Shell | 1 |
| JavaScript | 1 |
| Rust | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 0 | 0 | 4 | 0.0% |
| 5000-9999 | 4 | 0 | 0 | 4 | 0.0% |
| 1000-4999 | 83 | 3 | 3 | 77 | 3.6% |
| 500-999 | 136 | 1 | 19 | 116 | 0.7% |
| 100-499 | 773 | 3 | 98 | 672 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `gvzdv/claudish-to-english` | 2533 | 120 | 26d | Shell | MIT |
| `tobi/walgit` | 2438 | 138 | 13d | Rust | MIT |
| `amirh00sain/SpiderPanel` | 1144 | 3852 | 18d | Python | — |

### Generic-name pattern breakdown

Of 116 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 25 |
| `agent` | 24 |
| `awesome` | 15 |
| `skills` | 14 |
| `codex` | 9 |
| `prompt` | 6 |
| `claude` | 4 |
| `toolkit` | 3 |
| `gpt` | 3 |
| `llm` | 3 |
| `agents` | 2 |
| `starter` | 2 |
| `vibe` | 2 |
| `template` | 2 |
| `cookbook` | 1 |
| `demo` | 1 |

### Topics coverage

- Repos with **zero topics**: 476 (47.6%)
- Repos with at least one topic: 524 (52.4%)

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
