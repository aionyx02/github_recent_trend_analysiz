# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-02 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 20 | 2.0% |
| 待檢視 | 148 | 14.8% |
| 訊號完整 | 832 | 83.2% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `x4gKing/X4G` | 7273 | 13328 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `osama-fawad/Pekingman` | 1012 | 53 | 25d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `x4gKing/3x-ui-Upgrade` | 1290 | 2822 | 24d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `trycompai/crm` | 1060 | 131 | 1d | **6** | desc:empty, high-attention-no-desc, overnight-surge:1060/day, topics:none |
| 5 | `x4gKing/Marzban-Panel` | 1295 | 2475 | 20d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `x4gKing/PasarGuard-Node` | 1241 | 2426 | 26d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `x4gKing/3x-ui` | 2103 | 4202 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 8 | `x4gKing/Marzban-Node` | 1131 | 2253 | 20d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 9 | `x4gKing/PasarGuard` | 1364 | 2631 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 10 | `bashalarmistalt/decimen-optical-transfer` | 3204 | 375 | 2d | **6** | desc:empty, high-attention-no-desc, overnight-surge:1602/day, topics:none |
| 11 | `TobiasLee/Rebuttal-Skill` | 445 | 18 | 18d | **5** | desc:empty, license:none, generic-name:Rebuttal-Skill, topics:none |
| 12 | `h9-tec/Awesome_ai_learning` | 257 | 38 | 16d | **5** | desc:empty, license:none, generic-name:Awesome_ai_learning, topics:none |
| 13 | `Packets/tew` | 341 | 69 | 1d | **5** | desc:empty, license:none, overnight-surge:341/day, topics:none |
| 14 | `CluvexStudio/Aether` | 1673 | 113 | 18d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `withmarbleapp/os-taxonomy` | 3783 | 649 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 120 | 12.0% |
| description <20 chars | 36 | 3.6% |
| no license | 276 | 27.6% |
| high-attention no-desc (stars>1k + empty desc) | 16 | 1.6% |
| low fork ratio (stars>500 + fsr<0.02) | 12 | 1.2% |
| overnight surge (>300 spd + <7 days) | 12 | 1.2% |
| generic-AI-buzzword name | 133 | 13.3% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Dockerfile | 5 |
| Python | 4 |
| TypeScript | 4 |
| Unknown | 3 |
| HTML | 2 |
| Rust | 1 |
| JavaScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 1 | 1 | 1 | 33.3% |
| 5000-9999 | 7 | 1 | 2 | 4 | 14.3% |
| 1000-4999 | 72 | 13 | 5 | 54 | 18.1% |
| 500-999 | 102 | 0 | 16 | 86 | 0.0% |
| 100-499 | 816 | 5 | 124 | 687 | 0.6% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 11717 | 1581 | 12d | Python | MIT |
| `x4gKing/X4G` | 7273 | 13328 | 28d | Python | — |
| `withmarbleapp/os-taxonomy` | 3783 | 649 | 24d | JavaScript | ODbL-1.0 |
| `bashalarmistalt/decimen-optical-transfer` | 3204 | 375 | 2d | TypeScript | MIT |
| `slvDev/esp32-ai` | 2752 | 342 | 9d | Python | MIT |
| `x4gKing/3x-ui` | 2103 | 4202 | 28d | Dockerfile | — |
| `buchidonggua/dg-ai-notes` | 1678 | 133 | 27d | MDX | MIT |
| `CluvexStudio/Aether` | 1673 | 113 | 18d | Rust | AGPL-3.0 |
| `x4gKing/PasarGuard` | 1364 | 2631 | 27d | Dockerfile | — |
| `Subhan-code/Amicro--Micro-transitions-` | 1338 | 53 | 21d | TypeScript | MIT |
| `x4gKing/Marzban-Panel` | 1295 | 2475 | 20d | Dockerfile | — |
| `x4gKing/3x-ui-Upgrade` | 1290 | 2822 | 24d | HTML | — |
| `x4gKing/PasarGuard-Node` | 1241 | 2426 | 26d | Dockerfile | — |
| `x4gKing/Marzban-Node` | 1131 | 2253 | 20d | Dockerfile | — |
| `trycompai/crm` | 1060 | 131 | 1d | TypeScript | MIT |
| `osama-fawad/Pekingman` | 1012 | 53 | 25d | HTML | — |

### Generic-name pattern breakdown

Of 133 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `codex` | 24 |
| `agent` | 23 |
| `skills` | 20 |
| `skill` | 19 |
| `awesome` | 12 |
| `claude` | 9 |
| `agents` | 6 |
| `prompt` | 4 |
| `llm` | 4 |
| `vibe` | 3 |
| `gpt` | 3 |
| `toolkit` | 2 |
| `copilot` | 1 |
| `demo` | 1 |
| `playground` | 1 |
| `template` | 1 |

### Topics coverage

- Repos with **zero topics**: 545 (54.5%)
- Repos with at least one topic: 455 (45.5%)

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
