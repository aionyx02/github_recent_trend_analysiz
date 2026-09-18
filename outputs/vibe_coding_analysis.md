# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-18 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 138 | 13.8% |
| 訊號完整 | 842 | 84.2% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Mantitup-Org/vista` | 1897 | 20 | 13d | **8** | desc:empty, license:none, high-attention-no-desc, low-forks:0.011, topics:none |
| 2 | `rizqinrr/viserys-agent` | 663 | 3 | 5d | **7** | desc:empty, license:none, low-forks:0.005, generic-name:viserys-agent, topics:none |
| 3 | `FireRedTeam/FireRedAudio` | 1706 | 17 | 26d | **7** | desc:empty, high-attention-no-desc, low-forks:0.010, topics:none |
| 4 | `rizqinrr/cv` | 641 | 0 | 29d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 5 | `kajisho5/ffmpeg-skill` | 1097 | 80 | 14d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 6 | `capncodes69/9r-bulk-add` | 647 | 8 | 27d | **6** | desc:empty, license:none, low-forks:0.012, topics:none |
| 7 | `Faizpi/bank-sampah` | 646 | 1 | 6d | **6** | desc:empty, license:none, low-forks:0.002, topics:none |
| 8 | `HEJustinSun/my-girlfriend-jingtian-latex` | 4211 | 640 | 21d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 9 | `tobi/walgit` | 2526 | 152 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `inclusionAI/Choruz` | 747 | 9 | 15d | **5** | desc:empty, low-forks:0.012, topics:none |
| 11 | `sitimas9/ghsibudi` | 639 | 0 | 28d | **5** | desc:short, license:none, low-forks:0.000, topics:none |
| 12 | `LetMeHappyCode/auto-video-agent` | 220 | 7 | 10d | **5** | desc:empty, license:none, generic-name:auto-video-agent, topics:none |
| 13 | `cheng-haha/GPT-Policy` | 203 | 2 | 7d | **5** | desc:empty, license:none, generic-name:GPT-Policy, topics:none |
| 14 | `lyt2003-yt/swarm-agent` | 191 | 0 | 27d | **5** | desc:empty, license:none, generic-name:swarm-agent, topics:none |
| 15 | `turkiyeyapayzekaakademisi/llm-rag-memory-ai-agents` | 122 | 1 | 29d | **5** | desc:empty, license:none, generic-name:llm-rag-memory-ai-agents, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 131 | 13.1% |
| description <20 chars | 27 | 2.7% |
| no license | 294 | 29.4% |
| high-attention no-desc (stars>1k + empty desc) | 7 | 0.7% |
| low fork ratio (stars>500 + fsr<0.02) | 22 | 2.2% |
| overnight surge (>300 spd + <7 days) | 11 | 1.1% |
| generic-AI-buzzword name | 109 | 10.9% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 10 |
| JavaScript | 2 |
| Rust | 2 |
| TypeScript | 1 |
| PHP | 1 |
| TeX | 1 |
| Unknown | 1 |
| PowerShell | 1 |
| Lean | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| 5000-9999 | 6 | 0 | 0 | 6 | 0.0% |
| 1000-4999 | 77 | 7 | 2 | 68 | 9.1% |
| 500-999 | 125 | 8 | 19 | 98 | 6.4% |
| 100-499 | 792 | 5 | 117 | 670 | 0.6% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `HEJustinSun/my-girlfriend-jingtian-latex` | 4211 | 640 | 21d | TeX | — |
| `tobi/walgit` | 2526 | 152 | 25d | Rust | MIT |
| `Edge0-AI/Edge0` | 1951 | 162 | 9d | Python | Apache-2.0 |
| `Mantitup-Org/vista` | 1897 | 20 | 13d | TypeScript | — |
| `FireRedTeam/FireRedAudio` | 1706 | 17 | 26d | Python | Apache-2.0 |
| `anthropics/fermats-last-theorem` | 1196 | 102 | 13d | Lean | Apache-2.0 |
| `kajisho5/ffmpeg-skill` | 1097 | 80 | 14d | Python | MIT |

### Generic-name pattern breakdown

Of 109 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 22 |
| `skill` | 20 |
| `awesome` | 20 |
| `skills` | 11 |
| `gpt` | 8 |
| `claude` | 7 |
| `codex` | 7 |
| `toolkit` | 3 |
| `llm` | 2 |
| `prompt` | 2 |
| `starter` | 2 |
| `copilot` | 1 |
| `vibe` | 1 |
| `demo` | 1 |
| `agents` | 1 |
| `cookbook` | 1 |

### Topics coverage

- Repos with **zero topics**: 551 (55.1%)
- Repos with at least one topic: 449 (44.9%)

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
