# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-05-29 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 116 | 11.6% |
| 訊號完整 | 866 | 86.6% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2507 | 350 | 8d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:9arm-skills, topics:none |
| 2 | `V4bel/dirtyfrag` | 4787 | 766 | 21d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `wrongly-cuddly-obsession/NTSB_FOIA_MU5735` | 1080 | 365 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `Ch1rpy2613/Mirrai` | 846 | 11 | 23d | **6** | desc:empty, license:none, low-forks:0.013, topics:none |
| 5 | `ywnd1144/Gopay_plus_automatic` | 1191 | 615 | 16d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `FoundZiGu/GuJumpgate` | 3012 | 800 | 9d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `cat9999aaa/thinshell` | 520 | 9 | 14d | **5** | desc:short, license:none, low-forks:0.017, topics:none |
| 8 | `Blueemi/codex-eu-patcher` | 126 | 9 | 22d | **5** | desc:empty, license:none, generic-name:codex-eu-patcher, topics:none |
| 9 | `FULU-Foundation/OrcaSlicer-bambulab` | 6628 | 5082 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `Tong89/smartNode` | 1875 | 155 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `gtxx3600/GPTSession2CPAandSub2API` | 1017 | 273 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `mit-han-lab/kernel-design-agents` | 323 | 24 | 16d | **5** | desc:empty, license:none, generic-name:kernel-design-agents, topics:none |
| 13 | `limin112/wechat-publish-template` | 158 | 18 | 10d | **5** | desc:empty, license:none, generic-name:wechat-publish-template, topics:none |
| 14 | `UIengF/claude-codex-teamwork` | 145 | 8 | 18d | **5** | desc:empty, license:none, generic-name:claude-codex-teamwork, topics:none |
| 15 | `asuojun/claude-vision-skill` | 135 | 5 | 26d | **5** | desc:empty, license:none, generic-name:claude-vision-skill, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 110 | 11.0% |
| description <20 chars | 24 | 2.4% |
| no license | 371 | 37.1% |
| high-attention no-desc (stars>1k + empty desc) | 8 | 0.8% |
| low fork ratio (stars>500 + fsr<0.02) | 8 | 0.8% |
| overnight surge (>300 spd + <7 days) | 6 | 0.6% |
| generic-AI-buzzword name | 125 | 12.5% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| JavaScript | 5 |
| Unknown | 3 |
| Python | 3 |
| HTML | 2 |
| Shell | 1 |
| C | 1 |
| TypeScript | 1 |
| C++ | 1 |
| PowerShell | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 1 | 0 | 0 | 1 | 0.0% |
| 5000-9999 | 3 | 1 | 0 | 2 | 33.3% |
| 1000-4999 | 64 | 7 | 1 | 56 | 10.9% |
| 500-999 | 105 | 2 | 14 | 89 | 1.9% |
| 100-499 | 827 | 8 | 101 | 718 | 1.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `FULU-Foundation/OrcaSlicer-bambulab` | 6628 | 5082 | 17d | C++ | AGPL-3.0 |
| `V4bel/dirtyfrag` | 4787 | 766 | 21d | C | — |
| `FoundZiGu/GuJumpgate` | 3012 | 800 | 9d | JavaScript | MIT |
| `thananon/9arm-skills` | 2507 | 350 | 8d | Shell | — |
| `Tong89/smartNode` | 1875 | 155 | 7d | Python | MIT |
| `ywnd1144/Gopay_plus_automatic` | 1191 | 615 | 16d | Python | — |
| `wrongly-cuddly-obsession/NTSB_FOIA_MU5735` | 1080 | 365 | 28d | Unknown | — |
| `gtxx3600/GPTSession2CPAandSub2API` | 1017 | 273 | 20d | JavaScript | MIT |

### Generic-name pattern breakdown

Of 125 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 28 |
| `claude` | 19 |
| `skill` | 18 |
| `skills` | 15 |
| `codex` | 14 |
| `agents` | 7 |
| `awesome` | 7 |
| `prompt` | 4 |
| `gpt` | 3 |
| `template` | 2 |
| `demo` | 2 |
| `llm` | 2 |
| `toolkit` | 2 |
| `vibe` | 1 |
| `copilot` | 1 |

### Topics coverage

- Repos with **zero topics**: 535 (53.5%)
- Repos with at least one topic: 465 (46.5%)

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
