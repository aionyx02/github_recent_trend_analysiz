# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-16 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 20 | 2.0% |
| 待檢視 | 129 | 12.9% |
| 訊號完整 | 851 | 85.1% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Mantitup-Org/vista` | 1769 | 17 | 11d | **8** | desc:empty, license:none, high-attention-no-desc, low-forks:0.010, topics:none |
| 2 | `rizqinrr/viserys-agent` | 653 | 2 | 3d | **7** | desc:empty, license:none, low-forks:0.003, generic-name:viserys-agent, topics:none |
| 3 | `FireRedTeam/FireRedAudio` | 1481 | 15 | 24d | **7** | desc:empty, high-attention-no-desc, low-forks:0.010, topics:none |
| 4 | `amirh00sain/SpiderPanel` | 1259 | 4638 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `kajisho5/ffmpeg-skill` | 1070 | 78 | 12d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 6 | `capncodes69/9r-bulk-add` | 647 | 1 | 25d | **6** | desc:empty, license:none, low-forks:0.002, topics:none |
| 7 | `Faizpi/bank-sampah` | 646 | 1 | 4d | **6** | desc:empty, license:none, low-forks:0.002, topics:none |
| 8 | `rizqinrr/cv` | 641 | 0 | 27d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 9 | `yczz/oc-english` | 823 | 15 | 14d | **5** | desc:short, license:none, low-forks:0.018, topics:none |
| 10 | `inclusionAI/Choruz` | 718 | 9 | 13d | **5** | desc:empty, low-forks:0.013, topics:none |
| 11 | `decioriolepartition/qgkknlvf` | 689 | 1 | 17d | **5** | desc:empty, license:none, low-forks:0.001 |
| 12 | `capncodes69/myfreebuff` | 653 | 3 | 11d | **5** | desc:empty, low-forks:0.005, topics:none |
| 13 | `sitimas9/ghsibudi` | 639 | 0 | 26d | **5** | desc:short, license:none, low-forks:0.000, topics:none |
| 14 | `lyt2003-yt/swarm-agent` | 182 | 0 | 25d | **5** | desc:empty, license:none, generic-name:swarm-agent, topics:none |
| 15 | `zjwzcx/Awesome-Astra-Embodied-AI` | 742 | 14 | 3d | **5** | license:none, low-forks:0.019, generic-name:Awesome-Astra-Embodied-AI, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 120 | 12.0% |
| description <20 chars | 26 | 2.6% |
| no license | 287 | 28.7% |
| high-attention no-desc (stars>1k + empty desc) | 7 | 0.7% |
| low fork ratio (stars>500 + fsr<0.02) | 26 | 2.6% |
| overnight surge (>300 spd + <7 days) | 5 | 0.5% |
| generic-AI-buzzword name | 105 | 10.5% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 9 |
| JavaScript | 3 |
| Rust | 2 |
| Unknown | 2 |
| TypeScript | 1 |
| PHP | 1 |
| PowerShell | 1 |
| Lean | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| 5000-9999 | 5 | 0 | 0 | 5 | 0.0% |
| 1000-4999 | 87 | 8 | 2 | 77 | 9.2% |
| 500-999 | 115 | 10 | 15 | 90 | 8.7% |
| 100-499 | 793 | 2 | 112 | 679 | 0.3% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `tobi/walgit` | 2515 | 148 | 23d | Rust | MIT |
| `Edge0-AI/Edge0` | 1777 | 146 | 7d | Python | Apache-2.0 |
| `Mantitup-Org/vista` | 1769 | 17 | 11d | TypeScript | — |
| `FireRedTeam/FireRedAudio` | 1481 | 15 | 24d | Python | Apache-2.0 |
| `amirh00sain/SpiderPanel` | 1259 | 4638 | 28d | Python | — |
| `anthropics/fermats-last-theorem` | 1182 | 102 | 11d | Lean | Apache-2.0 |
| `kajisho5/ffmpeg-skill` | 1070 | 78 | 12d | Python | MIT |

### Generic-name pattern breakdown

Of 105 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 25 |
| `agent` | 20 |
| `awesome` | 14 |
| `skills` | 9 |
| `codex` | 8 |
| `claude` | 7 |
| `gpt` | 6 |
| `prompt` | 3 |
| `toolkit` | 3 |
| `llm` | 3 |
| `starter` | 2 |
| `cookbook` | 1 |
| `agents` | 1 |
| `vibe` | 1 |
| `demo` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 560 (56.0%)
- Repos with at least one topic: 440 (44.0%)

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
