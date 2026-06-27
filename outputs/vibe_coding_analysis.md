# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-27 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 9 | 0.9% |
| 待檢視 | 178 | 17.8% |
| 訊號完整 | 813 | 81.3% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Michaelliv/pi-dynamic-workflows` | 1004 | 56 | 29d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `kanavtwtgg/birds.cafe` | 736 | 2 | 5d | **6** | desc:empty, license:none, low-forks:0.003, topics:none |
| 3 | `zhongerxin/Cowart` | 3100 | 240 | 8d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `chaseai-yt/grill-me-codex` | 284 | 33 | 21d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 5 | `jmmy9609-design/gpt-pp` | 403 | 205 | 17d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 6 | `Regert888/gpt-outlook-register` | 117 | 44 | 18d | **5** | desc:empty, license:none, generic-name:gpt-outlook-register, topics:none |
| 7 | `gakiyukr/Codex_team_auto` | 108 | 53 | 9d | **5** | desc:empty, license:none, generic-name:Codex_team_auto, topics:none |
| 8 | `levy-street/world-of-claudecraft` | 1319 | 395 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `world-action-models/awesome-world-action-models` | 293 | 6 | 9d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 10 | `Iwancof/HackRFOneSegTuner` | 106 | 9 | 7d | **4** | desc:empty, license:none, topics:none |
| 11 | `ivorpad/mercadona-cli` | 108 | 13 | 1d | **4** | desc:empty, license:none, topics:none |
| 12 | `inbrainfun/inbrain` | 303 | 191 | 16d | **4** | desc:empty, license:none, topics:none |
| 13 | `ConiferKit/sage` | 299 | 12 | 25d | **4** | desc:empty, license:none, topics:none |
| 14 | `PMTraderAdam/pm-adam-trader` | 297 | 1 | 2d | **4** | desc:empty, license:none, topics:none |
| 15 | `itssosunny/im-not-strange-ai` | 125 | 22 | 6d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 136 | 13.6% |
| description <20 chars | 20 | 2.0% |
| no license | 350 | 35.0% |
| high-attention no-desc (stars>1k + empty desc) | 3 | 0.3% |
| low fork ratio (stars>500 + fsr<0.02) | 13 | 1.3% |
| overnight surge (>300 spd + <7 days) | 2 | 0.2% |
| generic-AI-buzzword name | 160 | 16.0% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 3 |
| TypeScript | 2 |
| JavaScript | 2 |
| Unknown | 2 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 0 | 0 | 4 | 0.0% |
| 5000-9999 | 6 | 0 | 3 | 3 | 0.0% |
| 1000-4999 | 46 | 3 | 5 | 38 | 6.5% |
| 500-999 | 91 | 1 | 16 | 74 | 1.1% |
| 100-499 | 821 | 5 | 145 | 671 | 0.6% |
| <100 | 32 | 0 | 9 | 23 | 0.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `zhongerxin/Cowart` | 3100 | 240 | 8d | JavaScript | — |
| `levy-street/world-of-claudecraft` | 1319 | 395 | 16d | TypeScript | MIT |
| `Michaelliv/pi-dynamic-workflows` | 1004 | 56 | 29d | TypeScript | — |

### Generic-name pattern breakdown

Of 160 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 34 |
| `agent` | 32 |
| `skills` | 28 |
| `codex` | 13 |
| `claude` | 13 |
| `awesome` | 12 |
| `gpt` | 7 |
| `agents` | 4 |
| `demo` | 3 |
| `llm` | 3 |
| `vibe` | 3 |
| `prompt` | 2 |
| `toolkit` | 2 |
| `template` | 2 |
| `starter` | 1 |
| `copilot` | 1 |

### Topics coverage

- Repos with **zero topics**: 608 (60.8%)
- Repos with at least one topic: 392 (39.2%)

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
