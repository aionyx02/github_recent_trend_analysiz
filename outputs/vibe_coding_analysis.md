# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-08 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 21 | 2.1% |
| 待檢視 | 147 | 14.7% |
| 訊號完整 | 832 | 83.2% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `ZzzLc0405/photo-abstract-editorial` | 1540 | 79 | 3d | **7** | desc:empty, license:none, high-attention-no-desc, overnight-surge:513/day, topics:none |
| 2 | `snekxs/openmouse` | 1032 | 67 | 11d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `x4gKing/Marzban-Panel` | 1432 | 2784 | 26d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `MiniMax-AI/MiniMax-H3` | 1181 | 62 | 8d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `chuspeeism/dashi-taskboard` | 1241 | 183 | 14d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `x4gKing/Marzban-Node` | 1268 | 2542 | 26d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `X-EraAI/ActPhysCause-Challenge` | 507 | 0 | 22d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 8 | `Zeejay0/gathered-scenes-zine-skill` | 1042 | 56 | 6d | **6** | desc:empty, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 9 | `Subhan-code/Amicro--Micro-transitions-` | 1390 | 57 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `andrewyng/openworker` | 13659 | 1844 | 18d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `that-company/dat-skill` | 179 | 0 | 19d | **5** | desc:empty, license:none, generic-name:dat-skill, topics:none |
| 12 | `CluvexStudio/Aether` | 1762 | 120 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `margelo/ai-chat-demo` | 154 | 12 | 3d | **5** | desc:empty, license:none, generic-name:ai-chat-demo, topics:none |
| 14 | `h9-tec/Awesome_ai_learning` | 273 | 39 | 22d | **5** | desc:empty, license:none, generic-name:Awesome_ai_learning, topics:none |
| 15 | `bashalarmistalt/decimen-optical-transfer` | 5189 | 634 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 124 | 12.4% |
| description <20 chars | 43 | 4.3% |
| no license | 290 | 29.0% |
| high-attention no-desc (stars>1k + empty desc) | 12 | 1.2% |
| low fork ratio (stars>500 + fsr<0.02) | 11 | 1.1% |
| overnight surge (>300 spd + <7 days) | 8 | 0.8% |
| generic-AI-buzzword name | 130 | 13.0% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 5 |
| Python | 5 |
| TypeScript | 4 |
| Dockerfile | 2 |
| JavaScript | 1 |
| Rust | 1 |
| Shell | 1 |
| HTML | 1 |
| CSS | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 1 | 1 | 4 | 16.7% |
| 5000-9999 | 6 | 1 | 1 | 4 | 16.7% |
| 1000-4999 | 70 | 10 | 4 | 56 | 14.3% |
| 500-999 | 100 | 3 | 16 | 81 | 3.0% |
| 100-499 | 818 | 6 | 125 | 687 | 0.7% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 13659 | 1844 | 18d | Python | MIT |
| `bashalarmistalt/decimen-optical-transfer` | 5189 | 634 | 8d | TypeScript | MIT |
| `slvDev/esp32-ai` | 3763 | 483 | 15d | Python | MIT |
| `CluvexStudio/Aether` | 1762 | 120 | 24d | Rust | AGPL-3.0 |
| `ZzzLc0405/photo-abstract-editorial` | 1540 | 79 | 3d | Unknown | — |
| `x4gKing/Marzban-Panel` | 1432 | 2784 | 26d | Dockerfile | — |
| `Subhan-code/Amicro--Micro-transitions-` | 1390 | 57 | 27d | TypeScript | MIT |
| `x4gKing/Marzban-Node` | 1268 | 2542 | 26d | Dockerfile | — |
| `chuspeeism/dashi-taskboard` | 1241 | 183 | 14d | JavaScript | — |
| `MiniMax-AI/MiniMax-H3` | 1181 | 62 | 8d | Python | — |
| `Zeejay0/gathered-scenes-zine-skill` | 1042 | 56 | 6d | Unknown | MIT |
| `snekxs/openmouse` | 1032 | 67 | 11d | TypeScript | — |

### Generic-name pattern breakdown

Of 130 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 22 |
| `codex` | 21 |
| `skills` | 20 |
| `skill` | 18 |
| `awesome` | 14 |
| `claude` | 10 |
| `agents` | 5 |
| `gpt` | 4 |
| `template` | 3 |
| `prompt` | 3 |
| `llm` | 3 |
| `demo` | 2 |
| `vibe` | 2 |
| `copilot` | 1 |
| `starter` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 570 (57.0%)
- Repos with at least one topic: 430 (43.0%)

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
