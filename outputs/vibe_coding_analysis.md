# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-11 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 17 | 1.7% |
| 待檢視 | 112 | 11.2% |
| 訊號完整 | 871 | 87.1% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Faizpi/bank-sampah` | 918 | 0 | 1d | **7** | desc:empty, license:none, low-forks:0.000, overnight-surge:918/day, topics:none |
| 2 | `capncodes69/9r-bulk-add` | 922 | 1 | 20d | **6** | desc:empty, license:none, low-forks:0.001, topics:none |
| 3 | `Edge0-AI/Edge0` | 1185 | 99 | 2d | **6** | desc:empty, high-attention-no-desc, overnight-surge:592/day, topics:none |
| 4 | `rizqinrr/cv` | 899 | 0 | 22d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 5 | `amirh00sain/SpiderPanel` | 1121 | 4004 | 23d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `guithepc/mentor-prompt` | 136 | 0 | 25d | **5** | desc:empty, license:none, generic-name:mentor-prompt, topics:none |
| 7 | `inclusionAI/Choruz` | 626 | 9 | 8d | **5** | desc:empty, low-forks:0.014, topics:none |
| 8 | `anthropics/fermats-last-theorem` | 1089 | 90 | 6d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `tobi/walgit` | 2480 | 145 | 18d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `yczz/oc-english` | 837 | 15 | 9d | **5** | desc:short, license:none, low-forks:0.018, topics:none |
| 11 | `capncodes69/myfreebuff` | 920 | 2 | 6d | **5** | desc:empty, low-forks:0.002, topics:none |
| 12 | `MiniMax-AI/awesome-minimax-h3-integration` | 316 | 24 | 28d | **5** | desc:empty, license:none, generic-name:awesome-minimax-h3-integration, topics:none |
| 13 | `almendili/skills` | 382 | 29 | 25d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 14 | `FireRedTeam/FireRedAudio` | 846 | 15 | 19d | **5** | desc:empty, low-forks:0.018, topics:none |
| 15 | `lyt2003-yt/swarm-agent` | 142 | 0 | 20d | **5** | desc:empty, license:none, generic-name:swarm-agent, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 101 | 10.1% |
| description <20 chars | 19 | 1.9% |
| no license | 276 | 27.6% |
| high-attention no-desc (stars>1k + empty desc) | 4 | 0.4% |
| low fork ratio (stars>500 + fsr<0.02) | 23 | 2.3% |
| overnight surge (>300 spd + <7 days) | 14 | 1.4% |
| generic-AI-buzzword name | 112 | 11.2% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| Unknown | 3 |
| Rust | 2 |
| PHP | 1 |
| CSS | 1 |
| Lean | 1 |
| JavaScript | 1 |
| PowerShell | 1 |
| TypeScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 7 | 0 | 0 | 7 | 0.0% |
| 1000-4999 | 85 | 4 | 3 | 78 | 4.7% |
| 500-999 | 133 | 9 | 20 | 104 | 6.8% |
| 100-499 | 772 | 4 | 89 | 679 | 0.5% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `tobi/walgit` | 2480 | 145 | 18d | Rust | MIT |
| `Edge0-AI/Edge0` | 1185 | 99 | 2d | Python | Apache-2.0 |
| `amirh00sain/SpiderPanel` | 1121 | 4004 | 23d | Python | — |
| `anthropics/fermats-last-theorem` | 1089 | 90 | 6d | Lean | Apache-2.0 |

### Generic-name pattern breakdown

Of 112 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 26 |
| `skill` | 24 |
| `awesome` | 20 |
| `skills` | 13 |
| `codex` | 8 |
| `toolkit` | 4 |
| `prompt` | 3 |
| `claude` | 3 |
| `starter` | 2 |
| `vibe` | 2 |
| `llm` | 2 |
| `cookbook` | 1 |
| `agents` | 1 |
| `gpt` | 1 |
| `demo` | 1 |
| `template` | 1 |

### Topics coverage

- Repos with **zero topics**: 498 (49.8%)
- Repos with at least one topic: 502 (50.2%)

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
