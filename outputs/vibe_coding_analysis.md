# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-17 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 23 | 2.3% |
| 待檢視 | 131 | 13.1% |
| 訊號完整 | 846 | 84.6% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Mantitup-Org/vista` | 1825 | 18 | 12d | **8** | desc:empty, license:none, high-attention-no-desc, low-forks:0.010, topics:none |
| 2 | `rizqinrr/viserys-agent` | 662 | 2 | 4d | **7** | desc:empty, license:none, low-forks:0.003, generic-name:viserys-agent, topics:none |
| 3 | `FireRedTeam/FireRedAudio` | 1600 | 16 | 25d | **7** | desc:empty, high-attention-no-desc, low-forks:0.010, topics:none |
| 4 | `kajisho5/ffmpeg-skill` | 1083 | 81 | 13d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 5 | `amirh00sain/SpiderPanel` | 1280 | 4718 | 29d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `HEJustinSun/my-girlfriend-jingtian-latex` | 4213 | 640 | 20d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `capncodes69/9r-bulk-add` | 647 | 8 | 26d | **6** | desc:empty, license:none, low-forks:0.012, topics:none |
| 8 | `Faizpi/bank-sampah` | 646 | 1 | 5d | **6** | desc:empty, license:none, low-forks:0.002, topics:none |
| 9 | `rizqinrr/cv` | 641 | 0 | 28d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 10 | `sitimas9/ghsibudi` | 639 | 0 | 27d | **5** | desc:short, license:none, low-forks:0.000, topics:none |
| 11 | `zjwzcx/Awesome-Astra-Embodied-AI` | 811 | 16 | 4d | **5** | license:none, low-forks:0.020, generic-name:Awesome-Astra-Embodied-AI, topics:none |
| 12 | `charlie-chann/ai-agent-langgraph-main` | 120 | 7 | 5d | **5** | desc:empty, license:none, generic-name:ai-agent-langgraph-main, topics:none |
| 13 | `ai-sucks-butt/ai-sucks-butt` | 2372 | 0 | 2d | **5** | license:none, low-forks:0.000, overnight-surge:1186/day, topics:none |
| 14 | `lyt2003-yt/swarm-agent` | 191 | 0 | 26d | **5** | desc:empty, license:none, generic-name:swarm-agent, topics:none |
| 15 | `capncodes69/myfreebuff` | 654 | 3 | 12d | **5** | desc:empty, low-forks:0.005, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 126 | 12.6% |
| description <20 chars | 26 | 2.6% |
| no license | 291 | 29.1% |
| high-attention no-desc (stars>1k + empty desc) | 8 | 0.8% |
| low fork ratio (stars>500 + fsr<0.02) | 23 | 2.3% |
| overnight surge (>300 spd + <7 days) | 8 | 0.8% |
| generic-AI-buzzword name | 109 | 10.9% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 12 |
| JavaScript | 3 |
| Rust | 2 |
| TypeScript | 1 |
| TeX | 1 |
| PHP | 1 |
| Unknown | 1 |
| PowerShell | 1 |
| Lean | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| 5000-9999 | 7 | 0 | 0 | 7 | 0.0% |
| 1000-4999 | 79 | 9 | 1 | 69 | 11.4% |
| 500-999 | 115 | 9 | 16 | 90 | 7.8% |
| 100-499 | 799 | 5 | 114 | 680 | 0.6% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `HEJustinSun/my-girlfriend-jingtian-latex` | 4213 | 640 | 20d | TeX | — |
| `tobi/walgit` | 2522 | 148 | 24d | Rust | MIT |
| `Edge0-AI/Edge0` | 1864 | 156 | 8d | Python | Apache-2.0 |
| `Mantitup-Org/vista` | 1825 | 18 | 12d | TypeScript | — |
| `FireRedTeam/FireRedAudio` | 1600 | 16 | 25d | Python | Apache-2.0 |
| `amirh00sain/SpiderPanel` | 1280 | 4718 | 29d | Python | — |
| `anthropics/fermats-last-theorem` | 1189 | 102 | 12d | Lean | Apache-2.0 |
| `kajisho5/ffmpeg-skill` | 1083 | 81 | 13d | Python | MIT |

### Generic-name pattern breakdown

Of 109 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 23 |
| `agent` | 22 |
| `awesome` | 18 |
| `skills` | 9 |
| `gpt` | 7 |
| `claude` | 7 |
| `codex` | 7 |
| `llm` | 3 |
| `toolkit` | 3 |
| `cookbook` | 2 |
| `starter` | 2 |
| `prompt` | 2 |
| `agents` | 1 |
| `copilot` | 1 |
| `demo` | 1 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 552 (55.2%)
- Repos with at least one topic: 448 (44.8%)

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
