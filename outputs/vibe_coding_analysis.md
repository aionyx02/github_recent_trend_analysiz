# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-31 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 16 | 1.6% |
| 待檢視 | 154 | 15.4% |
| 訊號完整 | 830 | 83.0% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `x4gKing/3x-ui-Upgrade` | 1269 | 2750 | 22d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `x4gKing/X4G` | 7131 | 13038 | 26d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `x4gKing/Marzban-Panel` | 1244 | 2399 | 18d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `x4gKing/PasarGuard-Node` | 1197 | 2343 | 24d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `x4gKing/Marzban-Node` | 1075 | 2175 | 18d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `x4gKing/PasarGuard` | 1311 | 2541 | 25d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `x4gKing/3x-ui` | 1990 | 3950 | 26d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 8 | `TobiasLee/Rebuttal-Skill` | 443 | 18 | 16d | **5** | desc:empty, license:none, generic-name:Rebuttal-Skill, topics:none |
| 9 | `h9-tec/Awesome_ai_learning` | 251 | 36 | 14d | **5** | desc:empty, license:none, generic-name:Awesome_ai_learning, topics:none |
| 10 | `CluvexStudio/Aether` | 1638 | 108 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `Subhan-code/Amicro--Micro-transitions-` | 1306 | 52 | 19d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `that-company/dat-skill` | 179 | 0 | 11d | **5** | desc:empty, license:none, generic-name:dat-skill, topics:none |
| 13 | `withmarbleapp/os-taxonomy` | 3738 | 646 | 22d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `slvDev/esp32-ai` | 2540 | 311 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `JimLiu/science-skills` | 218 | 53 | 29d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 121 | 12.1% |
| description <20 chars | 35 | 3.5% |
| no license | 285 | 28.5% |
| high-attention no-desc (stars>1k + empty desc) | 13 | 1.3% |
| low fork ratio (stars>500 + fsr<0.02) | 12 | 1.2% |
| overnight surge (>300 spd + <7 days) | 7 | 0.7% |
| generic-AI-buzzword name | 136 | 13.6% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Dockerfile | 5 |
| Python | 4 |
| HTML | 2 |
| Unknown | 2 |
| Rust | 1 |
| TypeScript | 1 |
| JavaScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 1 | 1 | 2 | 25.0% |
| 5000-9999 | 7 | 1 | 2 | 4 | 14.3% |
| 1000-4999 | 69 | 10 | 7 | 52 | 14.5% |
| 500-999 | 109 | 0 | 18 | 91 | 0.0% |
| 100-499 | 811 | 4 | 126 | 681 | 0.5% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 11149 | 1491 | 10d | Python | MIT |
| `x4gKing/X4G` | 7131 | 13038 | 26d | Python | — |
| `withmarbleapp/os-taxonomy` | 3738 | 646 | 22d | JavaScript | ODbL-1.0 |
| `slvDev/esp32-ai` | 2540 | 311 | 7d | Python | MIT |
| `x4gKing/3x-ui` | 1990 | 3950 | 26d | Dockerfile | — |
| `buchidonggua/dg-ai-notes` | 1641 | 130 | 25d | MDX | MIT |
| `CluvexStudio/Aether` | 1638 | 108 | 16d | Rust | AGPL-3.0 |
| `x4gKing/PasarGuard` | 1311 | 2541 | 25d | Dockerfile | — |
| `Subhan-code/Amicro--Micro-transitions-` | 1306 | 52 | 19d | TypeScript | MIT |
| `x4gKing/3x-ui-Upgrade` | 1269 | 2750 | 22d | HTML | — |
| `x4gKing/Marzban-Panel` | 1244 | 2399 | 18d | Dockerfile | — |
| `x4gKing/PasarGuard-Node` | 1197 | 2343 | 24d | Dockerfile | — |
| `x4gKing/Marzban-Node` | 1075 | 2175 | 18d | Dockerfile | — |

### Generic-name pattern breakdown

Of 136 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 25 |
| `codex` | 23 |
| `skills` | 22 |
| `skill` | 17 |
| `awesome` | 12 |
| `claude` | 9 |
| `agents` | 6 |
| `prompt` | 5 |
| `llm` | 4 |
| `toolkit` | 3 |
| `gpt` | 3 |
| `playground` | 2 |
| `vibe` | 2 |
| `copilot` | 1 |
| `demo` | 1 |
| `template` | 1 |

### Topics coverage

- Repos with **zero topics**: 552 (55.2%)
- Repos with at least one topic: 448 (44.8%)

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
