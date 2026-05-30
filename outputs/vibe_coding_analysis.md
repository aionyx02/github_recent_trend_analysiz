# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-05-30 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 19 | 1.9% |
| 待檢視 | 115 | 11.5% |
| 訊號完整 | 866 | 86.6% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2534 | 353 | 9d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:9arm-skills, topics:none |
| 2 | `ywnd1144/Gopay_plus_automatic` | 1221 | 620 | 17d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `Ch1rpy2613/Mirrai` | 863 | 11 | 24d | **6** | desc:empty, license:none, low-forks:0.013, topics:none |
| 4 | `V4bel/dirtyfrag` | 4788 | 768 | 22d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `wrongly-cuddly-obsession/NTSB_FOIA_MU5735` | 1080 | 365 | 29d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `limin112/wechat-publish-template` | 158 | 18 | 11d | **5** | desc:empty, license:none, generic-name:wechat-publish-template, topics:none |
| 7 | `energypantry/agent-browser-runtime` | 125 | 37 | 12d | **5** | desc:empty, license:none, generic-name:agent-browser-runtime, topics:none |
| 8 | `Tong89/smartNode` | 1971 | 168 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `FULU-Foundation/OrcaSlicer-bambulab` | 6655 | 5091 | 18d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `Blueemi/codex-eu-patcher` | 129 | 9 | 23d | **5** | desc:empty, license:none, generic-name:codex-eu-patcher, topics:none |
| 11 | `PrismML-Eng/Bonsai-Image-Demo` | 172 | 23 | 24d | **5** | desc:empty, license:none, generic-name:Bonsai-Image-Demo, topics:none |
| 12 | `Michaelliv/pi-dynamic-workflows` | 469 | 19 | 1d | **5** | desc:empty, license:none, overnight-surge:469/day, topics:none |
| 13 | `foyzulkarim/claude-lens` | 220 | 29 | 29d | **5** | desc:empty, license:none, generic-name:claude-lens, topics:none |
| 14 | `mit-han-lab/kernel-design-agents` | 336 | 25 | 17d | **5** | desc:empty, license:none, generic-name:kernel-design-agents, topics:none |
| 15 | `cat9999aaa/thinshell` | 520 | 9 | 15d | **5** | desc:short, license:none, low-forks:0.017, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 109 | 10.9% |
| description <20 chars | 23 | 2.3% |
| no license | 370 | 37.0% |
| high-attention no-desc (stars>1k + empty desc) | 8 | 0.8% |
| low fork ratio (stars>500 + fsr<0.02) | 8 | 0.8% |
| overnight surge (>300 spd + <7 days) | 8 | 0.8% |
| generic-AI-buzzword name | 122 | 12.2% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| JavaScript | 5 |
| Python | 3 |
| Unknown | 3 |
| TypeScript | 2 |
| HTML | 2 |
| Shell | 1 |
| C | 1 |
| C++ | 1 |
| PowerShell | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 1 | 0 | 0 | 1 | 0.0% |
| 5000-9999 | 3 | 1 | 0 | 2 | 33.3% |
| 1000-4999 | 60 | 7 | 1 | 52 | 11.7% |
| 500-999 | 112 | 2 | 13 | 97 | 1.8% |
| 100-499 | 824 | 9 | 101 | 714 | 1.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `FULU-Foundation/OrcaSlicer-bambulab` | 6655 | 5091 | 18d | C++ | AGPL-3.0 |
| `V4bel/dirtyfrag` | 4788 | 768 | 22d | C | — |
| `FoundZiGu/GuJumpgate` | 3074 | 810 | 10d | JavaScript | MIT |
| `thananon/9arm-skills` | 2534 | 353 | 9d | Shell | — |
| `Tong89/smartNode` | 1971 | 168 | 8d | Python | MIT |
| `ywnd1144/Gopay_plus_automatic` | 1221 | 620 | 17d | Python | — |
| `wrongly-cuddly-obsession/NTSB_FOIA_MU5735` | 1080 | 365 | 29d | Unknown | — |
| `gtxx3600/GPTSession2CPAandSub2API` | 1027 | 281 | 21d | JavaScript | MIT |

### Generic-name pattern breakdown

Of 122 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 29 |
| `claude` | 20 |
| `skill` | 18 |
| `skills` | 14 |
| `codex` | 13 |
| `agents` | 6 |
| `awesome` | 6 |
| `prompt` | 4 |
| `gpt` | 3 |
| `template` | 2 |
| `demo` | 2 |
| `llm` | 2 |
| `toolkit` | 2 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 534 (53.4%)
- Repos with at least one topic: 466 (46.6%)

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
