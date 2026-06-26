# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-26 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 10 | 1.0% |
| 待檢視 | 178 | 17.8% |
| 訊號完整 | 812 | 81.2% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `zhongerxin/Cowart` | 3012 | 231 | 7d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `Michaelliv/pi-dynamic-workflows` | 1004 | 57 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `kanavtwtgg/birds.cafe` | 784 | 2 | 4d | **6** | desc:empty, license:none, low-forks:0.003, topics:none |
| 4 | `Regert888/gpt-outlook-register` | 113 | 44 | 17d | **5** | desc:empty, license:none, generic-name:gpt-outlook-register, topics:none |
| 5 | `world-action-models/awesome-world-action-models` | 292 | 6 | 8d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 6 | `chaseai-yt/grill-me-codex` | 278 | 33 | 20d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 7 | `gakiyukr/Codex_team_auto` | 107 | 53 | 8d | **5** | desc:empty, license:none, generic-name:Codex_team_auto, topics:none |
| 8 | `jmmy9609-design/gpt-pp` | 402 | 206 | 16d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 9 | `jiaran-king/Re-Zero---Starting-LLM-` | 221 | 8 | 29d | **5** | desc:empty, license:none, generic-name:Re-Zero---Starting-LLM-, topics:none |
| 10 | `levy-street/world-of-claudecraft` | 1285 | 384 | 15d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `bozhouDev/codex-orange-book` | 2062 | 211 | 2d | **4** | license:none, overnight-surge:1031/day, generic-name:codex-orange-book, topics:none |
| 12 | `J-jaeyoung/bad-epoll` | 144 | 12 | 1d | **4** | desc:empty, license:none, topics:none |
| 13 | `cauenapier/TownSquare` | 172 | 6 | 19d | **4** | desc:empty, license:none, topics:none |
| 14 | `byJoey/cfnew-deployer` | 190 | 137 | 3d | **4** | desc:empty, license:none, topics:none |
| 15 | `Phoenixx1202/Spectrum-Library` | 139 | 4 | 19d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 133 | 13.3% |
| description <20 chars | 21 | 2.1% |
| no license | 345 | 34.5% |
| high-attention no-desc (stars>1k + empty desc) | 3 | 0.3% |
| low fork ratio (stars>500 + fsr<0.02) | 13 | 1.3% |
| overnight surge (>300 spd + <7 days) | 3 | 0.3% |
| generic-AI-buzzword name | 158 | 15.8% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 4 |
| JavaScript | 2 |
| TypeScript | 2 |
| Unknown | 2 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 7 | 0 | 3 | 4 | 0.0% |
| 1000-4999 | 49 | 3 | 5 | 41 | 6.1% |
| 500-999 | 96 | 1 | 16 | 79 | 1.0% |
| 100-499 | 828 | 6 | 151 | 671 | 0.7% |
| <100 | 17 | 0 | 3 | 14 | 0.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `zhongerxin/Cowart` | 3012 | 231 | 7d | JavaScript | — |
| `levy-street/world-of-claudecraft` | 1285 | 384 | 15d | TypeScript | MIT |
| `Michaelliv/pi-dynamic-workflows` | 1004 | 57 | 28d | TypeScript | — |

### Generic-name pattern breakdown

Of 158 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 32 |
| `agent` | 30 |
| `skills` | 27 |
| `claude` | 14 |
| `codex` | 13 |
| `awesome` | 12 |
| `gpt` | 7 |
| `llm` | 4 |
| `vibe` | 4 |
| `agents` | 4 |
| `demo` | 3 |
| `prompt` | 2 |
| `toolkit` | 2 |
| `template` | 2 |
| `starter` | 1 |
| `copilot` | 1 |

### Topics coverage

- Repos with **zero topics**: 603 (60.3%)
- Repos with at least one topic: 397 (39.7%)

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
