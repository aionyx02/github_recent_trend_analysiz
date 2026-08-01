# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-01 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 17 | 1.7% |
| 待檢視 | 155 | 15.5% |
| 訊號完整 | 828 | 82.8% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `x4gKing/X4G` | 7194 | 13182 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `bashalarmistalt/decimen-optical-transfer` | 2473 | 296 | 1d | **6** | desc:empty, high-attention-no-desc, overnight-surge:2473/day, topics:none |
| 3 | `x4gKing/PasarGuard` | 1339 | 2596 | 26d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `x4gKing/3x-ui` | 2060 | 4094 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `x4gKing/Marzban-Panel` | 1269 | 2437 | 19d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `x4gKing/PasarGuard-Node` | 1219 | 2396 | 25d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `x4gKing/3x-ui-Upgrade` | 1279 | 2791 | 23d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 8 | `x4gKing/Marzban-Node` | 1100 | 2215 | 19d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 9 | `that-company/dat-skill` | 179 | 0 | 12d | **5** | desc:empty, license:none, generic-name:dat-skill, topics:none |
| 10 | `Subhan-code/Amicro--Micro-transitions-` | 1323 | 53 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `h9-tec/Awesome_ai_learning` | 254 | 37 | 15d | **5** | desc:empty, license:none, generic-name:Awesome_ai_learning, topics:none |
| 12 | `withmarbleapp/os-taxonomy` | 3761 | 648 | 23d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `CluvexStudio/Aether` | 1658 | 111 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `Packets/tew` | 340 | 56 | 1d | **5** | desc:empty, license:none, overnight-surge:340/day, topics:none |
| 15 | `slvDev/esp32-ai` | 2650 | 326 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 121 | 12.1% |
| description <20 chars | 35 | 3.5% |
| no license | 275 | 27.5% |
| high-attention no-desc (stars>1k + empty desc) | 14 | 1.4% |
| low fork ratio (stars>500 + fsr<0.02) | 13 | 1.3% |
| overnight surge (>300 spd + <7 days) | 9 | 0.9% |
| generic-AI-buzzword name | 133 | 13.3% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Dockerfile | 5 |
| Python | 4 |
| Unknown | 3 |
| TypeScript | 2 |
| HTML | 1 |
| JavaScript | 1 |
| Rust | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 1 | 1 | 1 | 33.3% |
| 5000-9999 | 7 | 1 | 2 | 4 | 14.3% |
| 1000-4999 | 71 | 11 | 6 | 54 | 15.5% |
| 500-999 | 108 | 0 | 19 | 89 | 0.0% |
| 100-499 | 811 | 4 | 127 | 680 | 0.5% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 11421 | 1536 | 11d | Python | MIT |
| `x4gKing/X4G` | 7194 | 13182 | 27d | Python | — |
| `withmarbleapp/os-taxonomy` | 3761 | 648 | 23d | JavaScript | ODbL-1.0 |
| `slvDev/esp32-ai` | 2650 | 326 | 8d | Python | MIT |
| `bashalarmistalt/decimen-optical-transfer` | 2473 | 296 | 1d | TypeScript | MIT |
| `x4gKing/3x-ui` | 2060 | 4094 | 27d | Dockerfile | — |
| `buchidonggua/dg-ai-notes` | 1658 | 130 | 26d | MDX | MIT |
| `CluvexStudio/Aether` | 1658 | 111 | 17d | Rust | AGPL-3.0 |
| `x4gKing/PasarGuard` | 1339 | 2596 | 26d | Dockerfile | — |
| `Subhan-code/Amicro--Micro-transitions-` | 1323 | 53 | 20d | TypeScript | MIT |
| `x4gKing/3x-ui-Upgrade` | 1279 | 2791 | 23d | HTML | — |
| `x4gKing/Marzban-Panel` | 1269 | 2437 | 19d | Dockerfile | — |
| `x4gKing/PasarGuard-Node` | 1219 | 2396 | 25d | Dockerfile | — |
| `x4gKing/Marzban-Node` | 1100 | 2215 | 19d | Dockerfile | — |

### Generic-name pattern breakdown

Of 133 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `codex` | 23 |
| `agent` | 23 |
| `skills` | 22 |
| `skill` | 18 |
| `awesome` | 11 |
| `claude` | 8 |
| `agents` | 7 |
| `prompt` | 6 |
| `llm` | 4 |
| `gpt` | 3 |
| `vibe` | 2 |
| `toolkit` | 2 |
| `copilot` | 1 |
| `playground` | 1 |
| `demo` | 1 |
| `template` | 1 |

### Topics coverage

- Repos with **zero topics**: 550 (55.0%)
- Repos with at least one topic: 450 (45.0%)

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
