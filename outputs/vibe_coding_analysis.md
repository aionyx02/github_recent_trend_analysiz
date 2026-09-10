# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-10 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 115 | 11.5% |
| 訊號完整 | 875 | 87.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `amirh00sain/SpiderPanel` | 1243 | 4230 | 22d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `MiniMax-AI/awesome-minimax-h3-integration` | 314 | 24 | 27d | **5** | desc:empty, license:none, generic-name:awesome-minimax-h3-integration, topics:none |
| 3 | `almendili/skills` | 381 | 29 | 24d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 4 | `tobi/walgit` | 2469 | 142 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 5 | `yczz/oc-english` | 834 | 15 | 8d | **5** | desc:short, license:none, low-forks:0.018, topics:none |
| 6 | `inclusionAI/Choruz` | 592 | 9 | 7d | **5** | desc:empty, low-forks:0.015, topics:none |
| 7 | `lyt2003-yt/swarm-agent` | 132 | 0 | 19d | **5** | desc:empty, license:none, generic-name:swarm-agent, topics:none |
| 8 | `guithepc/mentor-prompt` | 135 | 0 | 24d | **5** | desc:empty, license:none, generic-name:mentor-prompt, topics:none |
| 9 | `jtydhr88/screenwriting-skills` | 443 | 53 | 3d | **5** | desc:empty, license:none, generic-name:screenwriting-skills, topics:none |
| 10 | `anthropics/fermats-last-theorem` | 1005 | 83 | 5d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `mufengyuan6/CodeMason` | 183 | 0 | 23d | **4** | desc:empty, license:none, topics:none |
| 12 | `nishantsaini2331/PW-Earners-code` | 174 | 30 | 19d | **4** | desc:empty, license:none, topics:none |
| 13 | `x4gpanell/PasarGuard` | 197 | 534 | 23d | **4** | desc:empty, license:none, topics:none |
| 14 | `mio-cc/freepp` | 180 | 105 | 29d | **4** | desc:empty, license:none, topics:none |
| 15 | `XinXie-Condex/DeepSeek-Harness-Desktop` | 198 | 5 | 25d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 97 | 9.7% |
| description <20 chars | 17 | 1.7% |
| no license | 271 | 27.1% |
| high-attention no-desc (stars>1k + empty desc) | 3 | 0.3% |
| low fork ratio (stars>500 + fsr<0.02) | 13 | 1.3% |
| overnight surge (>300 spd + <7 days) | 15 | 1.5% |
| generic-AI-buzzword name | 116 | 11.6% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 3 |
| Python | 2 |
| Rust | 2 |
| TypeScript | 1 |
| JavaScript | 1 |
| Lean | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 0 | 0 | 4 | 0.0% |
| 5000-9999 | 6 | 0 | 0 | 6 | 0.0% |
| 1000-4999 | 89 | 3 | 3 | 83 | 3.4% |
| 500-999 | 134 | 2 | 18 | 114 | 1.5% |
| 100-499 | 767 | 5 | 94 | 668 | 0.7% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `tobi/walgit` | 2469 | 142 | 17d | Rust | MIT |
| `amirh00sain/SpiderPanel` | 1243 | 4230 | 22d | Python | — |
| `anthropics/fermats-last-theorem` | 1005 | 83 | 5d | Lean | Apache-2.0 |

### Generic-name pattern breakdown

Of 116 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 27 |
| `skill` | 26 |
| `awesome` | 17 |
| `skills` | 15 |
| `codex` | 8 |
| `toolkit` | 4 |
| `claude` | 4 |
| `prompt` | 3 |
| `template` | 2 |
| `llm` | 2 |
| `starter` | 2 |
| `vibe` | 2 |
| `cookbook` | 1 |
| `agents` | 1 |
| `demo` | 1 |
| `gpt` | 1 |

### Topics coverage

- Repos with **zero topics**: 488 (48.8%)
- Repos with at least one topic: 512 (51.2%)

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
