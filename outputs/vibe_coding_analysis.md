# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-27 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 99 | 9.9% |
| 訊號完整 | 882 | 88.2% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `BeSwanGlobal/BeSwanGlobal` | 516 | 0 | 24d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 2 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 2032 | 500 | 28d | **6** | desc:empty, high-attention-no-desc, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 3 | `x4gKing/X4G` | 6829 | 12527 | 22d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `andrewyng/openworker` | 7635 | 1025 | 6d | **6** | desc:empty, high-attention-no-desc, overnight-surge:1272/day, topics:none |
| 5 | `x4gKing/PasarGuard` | 1171 | 2268 | 21d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `x4gKing/PasarGuard-Node` | 1060 | 2080 | 20d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `x4gKing/Marzban-Node` | 1016 | 2036 | 14d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 8 | `x4gKing/3x-ui-Upgrade` | 1219 | 2584 | 18d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 9 | `x4gKing/3x-ui` | 1559 | 3095 | 22d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 10 | `x4gKing/Marzban-Panel` | 1177 | 2250 | 14d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 11 | `slvDev/esp32-ai` | 1560 | 160 | 3d | **6** | desc:empty, high-attention-no-desc, overnight-surge:520/day, topics:none |
| 12 | `h9-tec/Awesome_ai_learning` | 245 | 36 | 10d | **5** | desc:empty, license:none, generic-name:Awesome_ai_learning, topics:none |
| 13 | `JimLiu/science-skills` | 219 | 53 | 25d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |
| 14 | `ion-design/ditto.site` | 1118 | 146 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `CluvexStudio/Aether` | 1563 | 102 | 12d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 89 | 8.9% |
| description <20 chars | 19 | 1.9% |
| no license | 519 | 51.9% |
| high-attention no-desc (stars>1k + empty desc) | 15 | 1.5% |
| low fork ratio (stars>500 + fsr<0.02) | 15 | 1.5% |
| overnight surge (>300 spd + <7 days) | 6 | 0.6% |
| generic-AI-buzzword name | 122 | 12.2% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| Dockerfile | 5 |
| Unknown | 3 |
| HTML | 2 |
| TypeScript | 2 |
| Rust | 1 |
| JavaScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 1 | 2 | 0.0% |
| 5000-9999 | 6 | 2 | 1 | 3 | 33.3% |
| 1000-4999 | 63 | 12 | 5 | 46 | 19.0% |
| 500-999 | 101 | 2 | 18 | 81 | 2.0% |
| 100-499 | 827 | 3 | 74 | 750 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 7635 | 1025 | 6d | Python | MIT |
| `x4gKing/X4G` | 6829 | 12527 | 22d | Python | — |
| `withmarbleapp/os-taxonomy` | 3691 | 639 | 18d | JavaScript | ODbL-1.0 |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 2032 | 500 | 28d | Python | MIT |
| `CluvexStudio/Aether` | 1563 | 102 | 12d | Rust | AGPL-3.0 |
| `slvDev/esp32-ai` | 1560 | 160 | 3d | Python | MIT |
| `x4gKing/3x-ui` | 1559 | 3095 | 22d | Dockerfile | — |
| `buchidonggua/dg-ai-notes` | 1332 | 96 | 21d | MDX | MIT |
| `x4gKing/3x-ui-Upgrade` | 1219 | 2584 | 18d | HTML | — |
| `x4gKing/Marzban-Panel` | 1177 | 2250 | 14d | Dockerfile | — |
| `x4gKing/PasarGuard` | 1171 | 2268 | 21d | Dockerfile | — |
| `ion-design/ditto.site` | 1118 | 146 | 27d | TypeScript | MIT |
| `x4gKing/PasarGuard-Node` | 1060 | 2080 | 20d | Dockerfile | — |
| `Subhan-code/Amicro--Micro-transitions-` | 1046 | 42 | 15d | TypeScript | MIT |
| `x4gKing/Marzban-Node` | 1016 | 2036 | 14d | Dockerfile | — |

### Generic-name pattern breakdown

Of 122 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 20 |
| `skills` | 19 |
| `codex` | 16 |
| `claude` | 16 |
| `skill` | 15 |
| `awesome` | 9 |
| `prompt` | 6 |
| `agents` | 4 |
| `llm` | 4 |
| `template` | 3 |
| `gpt` | 2 |
| `starter` | 2 |
| `copilot` | 2 |
| `vibe` | 2 |
| `toolkit` | 2 |

### Topics coverage

- Repos with **zero topics**: 381 (38.1%)
- Repos with at least one topic: 619 (61.9%)

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
