# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-06 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 158 | 15.8% |
| 訊號完整 | 824 | 82.4% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `bashalarmistalt/decimen-optical-transfer` | 4760 | 581 | 6d | **6** | desc:empty, high-attention-no-desc, overnight-surge:793/day, topics:none |
| 2 | `osama-fawad/Pekingman` | 1088 | 62 | 29d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `x4gKing/Marzban-Panel` | 1386 | 2686 | 24d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `mikiarlo3/awesome-growth-hacking-skills` | 520 | 3 | 1d | **6** | license:none, low-forks:0.006, overnight-surge:520/day, generic-name:awesome-growth-hacking-skills, topics:none |
| 5 | `x4gKing/3x-ui-Upgrade` | 1323 | 2927 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `x4gKing/Marzban-Node` | 1218 | 2450 | 24d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `TobiasLee/Rebuttal-Skill` | 446 | 19 | 22d | **5** | desc:empty, license:none, generic-name:Rebuttal-Skill, topics:none |
| 8 | `withmarbleapp/os-taxonomy` | 3881 | 679 | 28d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `ZzzLc0405/photo-abstract-editorial` | 540 | 26 | 1d | **5** | desc:empty, license:none, overnight-surge:540/day, topics:none |
| 10 | `h9-tec/Awesome_ai_learning` | 269 | 39 | 20d | **5** | desc:empty, license:none, generic-name:Awesome_ai_learning, topics:none |
| 11 | `margelo/ai-chat-demo` | 124 | 10 | 1d | **5** | desc:empty, license:none, generic-name:ai-chat-demo, topics:none |
| 12 | `LanceZPF/awesome-papers-awesome` | 538 | 1 | 21d | **5** | license:none, low-forks:0.002, generic-name:awesome-papers-awesome, topics:none |
| 13 | `slvDev/esp32-ai` | 3613 | 465 | 13d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `Subhan-code/Amicro--Micro-transitions-` | 1378 | 57 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `andrewyng/openworker` | 13214 | 1779 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 128 | 12.8% |
| description <20 chars | 43 | 4.3% |
| no license | 293 | 29.3% |
| high-attention no-desc (stars>1k + empty desc) | 10 | 1.0% |
| low fork ratio (stars>500 + fsr<0.02) | 11 | 1.1% |
| overnight surge (>300 spd + <7 days) | 19 | 1.9% |
| generic-AI-buzzword name | 135 | 13.5% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 4 |
| TypeScript | 3 |
| Unknown | 3 |
| HTML | 2 |
| Dockerfile | 2 |
| Shell | 1 |
| JavaScript | 1 |
| Rust | 1 |
| CSS | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 1 | 1 | 2 | 25.0% |
| 5000-9999 | 7 | 0 | 1 | 6 | 0.0% |
| 1000-4999 | 63 | 9 | 3 | 51 | 14.3% |
| 500-999 | 109 | 3 | 18 | 88 | 2.8% |
| 100-499 | 817 | 5 | 135 | 677 | 0.6% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 13214 | 1779 | 16d | Python | MIT |
| `bashalarmistalt/decimen-optical-transfer` | 4760 | 581 | 6d | TypeScript | MIT |
| `withmarbleapp/os-taxonomy` | 3881 | 679 | 28d | JavaScript | ODbL-1.0 |
| `slvDev/esp32-ai` | 3613 | 465 | 13d | Python | MIT |
| `CluvexStudio/Aether` | 1736 | 116 | 22d | Rust | AGPL-3.0 |
| `x4gKing/Marzban-Panel` | 1386 | 2686 | 24d | Dockerfile | — |
| `Subhan-code/Amicro--Micro-transitions-` | 1378 | 57 | 25d | TypeScript | MIT |
| `x4gKing/3x-ui-Upgrade` | 1323 | 2927 | 28d | HTML | — |
| `x4gKing/Marzban-Node` | 1218 | 2450 | 24d | Dockerfile | — |
| `osama-fawad/Pekingman` | 1088 | 62 | 29d | HTML | — |

### Generic-name pattern breakdown

Of 135 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 24 |
| `codex` | 23 |
| `skills` | 20 |
| `skill` | 16 |
| `awesome` | 14 |
| `claude` | 9 |
| `agents` | 6 |
| `gpt` | 4 |
| `prompt` | 4 |
| `template` | 4 |
| `demo` | 3 |
| `vibe` | 3 |
| `llm` | 3 |
| `copilot` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 555 (55.5%)
- Repos with at least one topic: 445 (44.5%)

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
