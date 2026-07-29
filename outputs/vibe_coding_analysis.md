# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-29 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 156 | 15.6% |
| 訊號完整 | 825 | 82.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `x4gKing/X4G` | 6968 | 12756 | 24d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `x4gKing/3x-ui-Upgrade` | 1245 | 2674 | 20d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `x4gKing/Marzban-Panel` | 1211 | 2314 | 16d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `slvDev/esp32-ai` | 2142 | 237 | 5d | **6** | desc:empty, high-attention-no-desc, overnight-surge:428/day, topics:none |
| 5 | `x4gKing/3x-ui` | 1804 | 3591 | 24d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `x4gKing/Marzban-Node` | 1048 | 2099 | 16d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `BeSwanGlobal/BeSwanGlobal` | 516 | 0 | 26d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 8 | `x4gKing/PasarGuard` | 1261 | 2435 | 23d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 9 | `x4gKing/PasarGuard-Node` | 1153 | 2244 | 22d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 10 | `h9-tec/Awesome_ai_learning` | 248 | 36 | 12d | **5** | desc:empty, license:none, generic-name:Awesome_ai_learning, topics:none |
| 11 | `dimmas893/monorepo-nest-next-starter` | 220 | 216 | 3d | **5** | desc:empty, license:none, generic-name:monorepo-nest-next-starter, topics:none |
| 12 | `withmarbleapp/os-taxonomy` | 3716 | 644 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `Subhan-code/Amicro--Micro-transitions-` | 1257 | 47 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `CluvexStudio/Aether` | 1585 | 104 | 14d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `andrewyng/openworker` | 10273 | 1340 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 125 | 12.5% |
| description <20 chars | 37 | 3.7% |
| no license | 302 | 30.2% |
| high-attention no-desc (stars>1k + empty desc) | 14 | 1.4% |
| low fork ratio (stars>500 + fsr<0.02) | 13 | 1.3% |
| overnight surge (>300 spd + <7 days) | 7 | 0.7% |
| generic-AI-buzzword name | 138 | 13.8% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Dockerfile | 5 |
| Python | 4 |
| Unknown | 3 |
| TypeScript | 3 |
| HTML | 2 |
| JavaScript | 1 |
| Rust | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 1 | 1 | 2 | 25.0% |
| 5000-9999 | 5 | 1 | 1 | 3 | 20.0% |
| 1000-4999 | 70 | 11 | 9 | 50 | 15.7% |
| 500-999 | 102 | 1 | 17 | 84 | 1.0% |
| 100-499 | 819 | 5 | 128 | 686 | 0.6% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 10273 | 1340 | 8d | Python | MIT |
| `x4gKing/X4G` | 6968 | 12756 | 24d | Python | — |
| `withmarbleapp/os-taxonomy` | 3716 | 644 | 20d | JavaScript | ODbL-1.0 |
| `slvDev/esp32-ai` | 2142 | 237 | 5d | Python | MIT |
| `x4gKing/3x-ui` | 1804 | 3591 | 24d | Dockerfile | — |
| `CluvexStudio/Aether` | 1585 | 104 | 14d | Rust | AGPL-3.0 |
| `buchidonggua/dg-ai-notes` | 1545 | 115 | 23d | MDX | MIT |
| `x4gKing/PasarGuard` | 1261 | 2435 | 23d | Dockerfile | — |
| `Subhan-code/Amicro--Micro-transitions-` | 1257 | 47 | 17d | TypeScript | MIT |
| `x4gKing/3x-ui-Upgrade` | 1245 | 2674 | 20d | HTML | — |
| `x4gKing/Marzban-Panel` | 1211 | 2314 | 16d | Dockerfile | — |
| `ion-design/ditto.site` | 1180 | 154 | 29d | TypeScript | MIT |
| `x4gKing/PasarGuard-Node` | 1153 | 2244 | 22d | Dockerfile | — |
| `x4gKing/Marzban-Node` | 1048 | 2099 | 16d | Dockerfile | — |

### Generic-name pattern breakdown

Of 138 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skills` | 22 |
| `codex` | 22 |
| `agent` | 22 |
| `skill` | 18 |
| `claude` | 14 |
| `awesome` | 13 |
| `agents` | 6 |
| `prompt` | 6 |
| `llm` | 4 |
| `toolkit` | 3 |
| `gpt` | 3 |
| `vibe` | 2 |
| `starter` | 1 |
| `playground` | 1 |
| `template` | 1 |

### Topics coverage

- Repos with **zero topics**: 553 (55.3%)
- Repos with at least one topic: 447 (44.7%)

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
