# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-28 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 106 | 10.6% |
| 訊號完整 | 875 | 87.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `slvDev/esp32-ai` | 1870 | 195 | 4d | **6** | desc:empty, high-attention-no-desc, overnight-surge:468/day, topics:none |
| 2 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 2033 | 501 | 29d | **6** | desc:empty, high-attention-no-desc, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 3 | `x4gKing/3x-ui` | 1703 | 3383 | 23d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `x4gKing/3x-ui-Upgrade` | 1239 | 2634 | 19d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `x4gKing/Marzban-Panel` | 1195 | 2283 | 15d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `x4gKing/Marzban-Node` | 1030 | 2068 | 15d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `x4gKing/PasarGuard` | 1228 | 2372 | 22d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 8 | `x4gKing/PasarGuard-Node` | 1121 | 2178 | 21d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 9 | `x4gKing/X4G` | 6910 | 12647 | 23d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 10 | `BeSwanGlobal/BeSwanGlobal` | 516 | 0 | 25d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 11 | `Subhan-code/Amicro--Micro-transitions-` | 1183 | 48 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `ion-design/ditto.site` | 1144 | 148 | 28d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `JimLiu/science-skills` | 219 | 53 | 26d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |
| 14 | `Ssupercoder/Salary-Negotiation-Skill` | 536 | 8 | 29d | **5** | license:none, low-forks:0.015, generic-name:Salary-Negotiation-Skill, topics:none |
| 15 | `andrewyng/openworker` | 9481 | 1225 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 90 | 9.0% |
| description <20 chars | 18 | 1.8% |
| no license | 516 | 51.6% |
| high-attention no-desc (stars>1k + empty desc) | 15 | 1.5% |
| low fork ratio (stars>500 + fsr<0.02) | 14 | 1.4% |
| overnight surge (>300 spd + <7 days) | 7 | 0.7% |
| generic-AI-buzzword name | 128 | 12.8% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| Dockerfile | 5 |
| Unknown | 3 |
| HTML | 2 |
| TypeScript | 2 |
| JavaScript | 1 |
| Rust | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 1 | 2 | 0.0% |
| 5000-9999 | 6 | 2 | 1 | 3 | 33.3% |
| 1000-4999 | 66 | 12 | 7 | 47 | 18.2% |
| 500-999 | 104 | 2 | 19 | 83 | 1.9% |
| 100-499 | 821 | 3 | 78 | 740 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 9481 | 1225 | 7d | Python | MIT |
| `x4gKing/X4G` | 6910 | 12647 | 23d | Python | — |
| `withmarbleapp/os-taxonomy` | 3704 | 642 | 19d | JavaScript | ODbL-1.0 |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 2033 | 501 | 29d | Python | MIT |
| `slvDev/esp32-ai` | 1870 | 195 | 4d | Python | MIT |
| `x4gKing/3x-ui` | 1703 | 3383 | 23d | Dockerfile | — |
| `CluvexStudio/Aether` | 1574 | 102 | 13d | Rust | AGPL-3.0 |
| `buchidonggua/dg-ai-notes` | 1465 | 110 | 22d | MDX | MIT |
| `x4gKing/3x-ui-Upgrade` | 1239 | 2634 | 19d | HTML | — |
| `x4gKing/PasarGuard` | 1228 | 2372 | 22d | Dockerfile | — |
| `x4gKing/Marzban-Panel` | 1195 | 2283 | 15d | Dockerfile | — |
| `Subhan-code/Amicro--Micro-transitions-` | 1183 | 48 | 16d | TypeScript | MIT |
| `ion-design/ditto.site` | 1144 | 148 | 28d | TypeScript | MIT |
| `x4gKing/PasarGuard-Node` | 1121 | 2178 | 21d | Dockerfile | — |
| `x4gKing/Marzban-Node` | 1030 | 2068 | 15d | Dockerfile | — |

### Generic-name pattern breakdown

Of 128 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 21 |
| `claude` | 19 |
| `skills` | 18 |
| `codex` | 17 |
| `skill` | 13 |
| `awesome` | 9 |
| `prompt` | 6 |
| `llm` | 5 |
| `agents` | 4 |
| `starter` | 3 |
| `template` | 3 |
| `playground` | 2 |
| `gpt` | 2 |
| `vibe` | 2 |
| `copilot` | 2 |
| `toolkit` | 2 |

### Topics coverage

- Repos with **zero topics**: 395 (39.5%)
- Repos with at least one topic: 605 (60.5%)

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
