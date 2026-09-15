# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-15 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 128 | 12.8% |
| 訊號完整 | 851 | 85.1% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Mantitup-Org/vista` | 1513 | 17 | 10d | **8** | desc:empty, license:none, high-attention-no-desc, low-forks:0.011, topics:none |
| 2 | `rizqinrr/viserys-agent` | 651 | 2 | 2d | **8** | desc:empty, license:none, low-forks:0.003, overnight-surge:326/day, generic-name:viserys-agent, topics:none |
| 3 | `FireRedTeam/FireRedAudio` | 1384 | 15 | 23d | **7** | desc:empty, high-attention-no-desc, low-forks:0.011, topics:none |
| 4 | `zjwzcx/Awesome-Astra-Embodied-AI` | 644 | 12 | 2d | **6** | license:none, low-forks:0.019, overnight-surge:322/day, generic-name:Awesome-Astra-Embodied-AI, topics:none |
| 5 | `Faizpi/bank-sampah` | 646 | 1 | 3d | **6** | desc:empty, license:none, low-forks:0.002, topics:none |
| 6 | `amirh00sain/SpiderPanel` | 1245 | 4554 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `kajisho5/ffmpeg-skill` | 1060 | 78 | 11d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 8 | `capncodes69/9r-bulk-add` | 647 | 1 | 24d | **6** | desc:empty, license:none, low-forks:0.002, topics:none |
| 9 | `rizqinrr/cv` | 641 | 0 | 26d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 10 | `capncodes69/myfreebuff` | 653 | 3 | 10d | **5** | desc:empty, low-forks:0.005, topics:none |
| 11 | `inclusionAI/Choruz` | 712 | 9 | 12d | **5** | desc:empty, low-forks:0.013, topics:none |
| 12 | `decioriolepartition/qgkknlvf` | 756 | 0 | 16d | **5** | desc:empty, license:none, low-forks:0.000 |
| 13 | `yczz/oc-english` | 838 | 15 | 13d | **5** | desc:short, license:none, low-forks:0.018, topics:none |
| 14 | `sitimas9/ghsibudi` | 639 | 0 | 25d | **5** | desc:short, license:none, low-forks:0.000, topics:none |
| 15 | `tobi/walgit` | 2504 | 148 | 22d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 124 | 12.4% |
| description <20 chars | 23 | 2.3% |
| no license | 283 | 28.3% |
| high-attention no-desc (stars>1k + empty desc) | 7 | 0.7% |
| low fork ratio (stars>500 + fsr<0.02) | 25 | 2.5% |
| overnight surge (>300 spd + <7 days) | 8 | 0.8% |
| generic-AI-buzzword name | 104 | 10.4% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 7 |
| TypeScript | 3 |
| JavaScript | 3 |
| Unknown | 3 |
| Rust | 2 |
| PHP | 1 |
| PowerShell | 1 |
| Lean | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| 5000-9999 | 4 | 0 | 0 | 4 | 0.0% |
| 1000-4999 | 81 | 7 | 1 | 73 | 8.6% |
| 500-999 | 117 | 11 | 15 | 91 | 9.4% |
| 100-499 | 798 | 3 | 112 | 683 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `tobi/walgit` | 2504 | 148 | 22d | Rust | MIT |
| `Edge0-AI/Edge0` | 1731 | 141 | 6d | Python | Apache-2.0 |
| `Mantitup-Org/vista` | 1513 | 17 | 10d | TypeScript | — |
| `FireRedTeam/FireRedAudio` | 1384 | 15 | 23d | Python | Apache-2.0 |
| `amirh00sain/SpiderPanel` | 1245 | 4554 | 27d | Python | — |
| `anthropics/fermats-last-theorem` | 1171 | 99 | 10d | Lean | Apache-2.0 |
| `kajisho5/ffmpeg-skill` | 1060 | 78 | 11d | Python | MIT |

### Generic-name pattern breakdown

Of 104 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 24 |
| `agent` | 21 |
| `awesome` | 14 |
| `skills` | 9 |
| `codex` | 8 |
| `gpt` | 5 |
| `claude` | 5 |
| `prompt` | 4 |
| `toolkit` | 3 |
| `llm` | 3 |
| `starter` | 3 |
| `cookbook` | 1 |
| `demo` | 1 |
| `agents` | 1 |
| `copilot` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 556 (55.6%)
- Repos with at least one topic: 444 (44.4%)

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
