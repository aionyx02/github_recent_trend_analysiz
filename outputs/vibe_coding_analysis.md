# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-13 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 21 | 2.1% |
| 待檢視 | 123 | 12.3% |
| 訊號完整 | 856 | 85.6% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `rizqinrr/viserys-agent` | 627 | 0 | 1d | **8** | desc:empty, license:none, low-forks:0.000, overnight-surge:627/day, generic-name:viserys-agent, topics:none |
| 2 | `Faizpi/bank-sampah` | 646 | 1 | 1d | **7** | desc:empty, license:none, low-forks:0.002, overnight-surge:646/day, topics:none |
| 3 | `FireRedTeam/FireRedAudio` | 1164 | 15 | 21d | **7** | desc:empty, high-attention-no-desc, low-forks:0.013, topics:none |
| 4 | `Edge0-AI/Edge0` | 1522 | 125 | 4d | **6** | desc:empty, high-attention-no-desc, overnight-surge:380/day, topics:none |
| 5 | `rizqinrr/cv` | 641 | 0 | 24d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 6 | `kajisho5/ffmpeg-skill` | 1014 | 76 | 9d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 7 | `amirh00sain/SpiderPanel` | 1179 | 4319 | 25d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 8 | `Mantitup-Org/vista` | 795 | 15 | 8d | **6** | desc:empty, license:none, low-forks:0.019, topics:none |
| 9 | `capncodes69/9r-bulk-add` | 647 | 1 | 22d | **6** | desc:empty, license:none, low-forks:0.002, topics:none |
| 10 | `jtydhr88/screenwriting-skills` | 952 | 114 | 6d | **5** | desc:empty, license:none, generic-name:screenwriting-skills, topics:none |
| 11 | `tobi/walgit` | 2492 | 145 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `capncodes69/myfreebuff` | 646 | 3 | 8d | **5** | desc:empty, low-forks:0.005, topics:none |
| 13 | `guithepc/mentor-prompt` | 136 | 0 | 27d | **5** | desc:empty, license:none, generic-name:mentor-prompt, topics:none |
| 14 | `lyt2003-yt/swarm-agent` | 156 | 0 | 22d | **5** | desc:empty, license:none, generic-name:swarm-agent, topics:none |
| 15 | `yczz/oc-english` | 839 | 15 | 11d | **5** | desc:short, license:none, low-forks:0.018, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 117 | 11.7% |
| description <20 chars | 17 | 1.7% |
| no license | 291 | 29.1% |
| high-attention no-desc (stars>1k + empty desc) | 6 | 0.6% |
| low fork ratio (stars>500 + fsr<0.02) | 24 | 2.4% |
| overnight surge (>300 spd + <7 days) | 10 | 1.0% |
| generic-AI-buzzword name | 103 | 10.3% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 8 |
| JavaScript | 3 |
| TypeScript | 3 |
| Rust | 2 |
| Unknown | 2 |
| PHP | 1 |
| PowerShell | 1 |
| Lean | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| 5000-9999 | 5 | 0 | 0 | 5 | 0.0% |
| 1000-4999 | 83 | 6 | 2 | 75 | 7.2% |
| 500-999 | 124 | 12 | 17 | 95 | 9.7% |
| 100-499 | 788 | 3 | 104 | 681 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `tobi/walgit` | 2492 | 145 | 20d | Rust | MIT |
| `Edge0-AI/Edge0` | 1522 | 125 | 4d | Python | Apache-2.0 |
| `amirh00sain/SpiderPanel` | 1179 | 4319 | 25d | Python | — |
| `FireRedTeam/FireRedAudio` | 1164 | 15 | 21d | Python | Apache-2.0 |
| `anthropics/fermats-last-theorem` | 1133 | 96 | 8d | Lean | Apache-2.0 |
| `kajisho5/ffmpeg-skill` | 1014 | 76 | 9d | Python | MIT |

### Generic-name pattern breakdown

Of 103 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 24 |
| `agent` | 22 |
| `awesome` | 15 |
| `skills` | 10 |
| `codex` | 9 |
| `claude` | 5 |
| `prompt` | 3 |
| `gpt` | 3 |
| `toolkit` | 3 |
| `starter` | 3 |
| `llm` | 2 |
| `cookbook` | 1 |
| `demo` | 1 |
| `agents` | 1 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 522 (52.2%)
- Repos with at least one topic: 478 (47.8%)

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
