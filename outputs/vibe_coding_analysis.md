# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-19 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 18 | 1.8% |
| 待檢視 | 139 | 13.9% |
| 訊號完整 | 843 | 84.3% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Mantitup-Org/vista` | 2002 | 24 | 14d | **8** | desc:empty, license:none, high-attention-no-desc, low-forks:0.012, topics:none |
| 2 | `rizqinrr/viserys-agent` | 665 | 3 | 6d | **7** | desc:empty, license:none, low-forks:0.005, generic-name:viserys-agent, topics:none |
| 3 | `FireRedTeam/FireRedAudio` | 1819 | 17 | 27d | **7** | desc:empty, high-attention-no-desc, low-forks:0.009, topics:none |
| 4 | `FjordWorkerShanty/Microsoft-Activation-Script` | 1759 | 0 | 20d | **7** | desc:empty, license:none, high-attention-no-desc, low-forks:0.000 |
| 5 | `kajisho5/ffmpeg-skill` | 1199 | 88 | 15d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 6 | `HEJustinSun/my-girlfriend-jingtian-latex` | 4212 | 638 | 22d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `Faizpi/bank-sampah` | 646 | 1 | 7d | **6** | desc:empty, license:none, low-forks:0.002, topics:none |
| 8 | `capncodes69/9r-bulk-add` | 647 | 8 | 28d | **6** | desc:empty, license:none, low-forks:0.012, topics:none |
| 9 | `anthropics/fermats-last-theorem` | 1196 | 102 | 14d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `Edge0-AI/Edge0` | 1982 | 167 | 10d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `tobi/walgit` | 2530 | 153 | 26d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `sitimas9/ghsibudi` | 639 | 0 | 29d | **5** | desc:short, license:none, low-forks:0.000, topics:none |
| 13 | `charlie-chann/ai-agent-langgraph-main` | 120 | 7 | 7d | **5** | desc:empty, license:none, generic-name:ai-agent-langgraph-main, topics:none |
| 14 | `cheng-haha/GPT-Policy` | 213 | 3 | 8d | **5** | desc:empty, license:none, generic-name:GPT-Policy, topics:none |
| 15 | `capncodes69/myfreebuff` | 649 | 3 | 14d | **5** | desc:empty, low-forks:0.005, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 127 | 12.7% |
| description <20 chars | 26 | 2.6% |
| no license | 292 | 29.2% |
| high-attention no-desc (stars>1k + empty desc) | 8 | 0.8% |
| low fork ratio (stars>500 + fsr<0.02) | 21 | 2.1% |
| overnight surge (>300 spd + <7 days) | 14 | 1.4% |
| generic-AI-buzzword name | 108 | 10.8% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 8 |
| Unknown | 2 |
| Rust | 2 |
| TypeScript | 1 |
| JavaScript | 1 |
| TeX | 1 |
| PHP | 1 |
| Lean | 1 |
| PowerShell | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| 5000-9999 | 7 | 0 | 1 | 6 | 0.0% |
| 1000-4999 | 77 | 8 | 2 | 67 | 10.4% |
| 500-999 | 126 | 7 | 18 | 101 | 5.6% |
| 100-499 | 790 | 3 | 118 | 669 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `HEJustinSun/my-girlfriend-jingtian-latex` | 4212 | 638 | 22d | TeX | — |
| `tobi/walgit` | 2530 | 153 | 26d | Rust | MIT |
| `Mantitup-Org/vista` | 2002 | 24 | 14d | TypeScript | — |
| `Edge0-AI/Edge0` | 1982 | 167 | 10d | Python | Apache-2.0 |
| `FireRedTeam/FireRedAudio` | 1819 | 17 | 27d | Python | Apache-2.0 |
| `FjordWorkerShanty/Microsoft-Activation-Script` | 1759 | 0 | 20d | Unknown | — |
| `kajisho5/ffmpeg-skill` | 1199 | 88 | 15d | Python | MIT |
| `anthropics/fermats-last-theorem` | 1196 | 102 | 14d | Lean | Apache-2.0 |

### Generic-name pattern breakdown

Of 108 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 21 |
| `skill` | 21 |
| `awesome` | 21 |
| `skills` | 10 |
| `gpt` | 8 |
| `claude` | 7 |
| `codex` | 7 |
| `toolkit` | 2 |
| `prompt` | 2 |
| `starter` | 2 |
| `agents` | 2 |
| `vibe` | 1 |
| `demo` | 1 |
| `copilot` | 1 |
| `llm` | 1 |
| `cookbook` | 1 |

### Topics coverage

- Repos with **zero topics**: 562 (56.2%)
- Repos with at least one topic: 438 (43.8%)

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
