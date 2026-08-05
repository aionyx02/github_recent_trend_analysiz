# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-05 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 146 | 14.6% |
| 訊號完整 | 838 | 83.8% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `x4gKing/3x-ui-Upgrade` | 1311 | 2895 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `x4gKing/PasarGuard-Node` | 1301 | 2554 | 29d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `x4gKing/Marzban-Node` | 1204 | 2411 | 23d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `x4gKing/Marzban-Panel` | 1376 | 2642 | 23d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `bashalarmistalt/decimen-optical-transfer` | 4604 | 556 | 5d | **6** | desc:empty, high-attention-no-desc, overnight-surge:921/day, topics:none |
| 6 | `osama-fawad/Pekingman` | 1075 | 60 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `LanceZPF/awesome-papers-awesome` | 524 | 1 | 20d | **5** | license:none, low-forks:0.002, generic-name:awesome-papers-awesome, topics:none |
| 8 | `Subhan-code/Amicro--Micro-transitions-` | 1368 | 55 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `CluvexStudio/Aether` | 1722 | 116 | 21d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `TobiasLee/Rebuttal-Skill` | 445 | 19 | 21d | **5** | desc:empty, license:none, generic-name:Rebuttal-Skill, topics:none |
| 11 | `andrewyng/openworker` | 12947 | 1748 | 15d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `slvDev/esp32-ai` | 3485 | 444 | 12d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `that-company/dat-skill` | 179 | 0 | 16d | **5** | desc:empty, license:none, generic-name:dat-skill, topics:none |
| 14 | `withmarbleapp/os-taxonomy` | 3849 | 669 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `tonbistudio/buzz-skills` | 144 | 11 | 5d | **5** | desc:empty, license:none, generic-name:buzz-skills, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 115 | 11.5% |
| description <20 chars | 43 | 4.3% |
| no license | 278 | 27.8% |
| high-attention no-desc (stars>1k + empty desc) | 11 | 1.1% |
| low fork ratio (stars>500 + fsr<0.02) | 14 | 1.4% |
| overnight surge (>300 spd + <7 days) | 19 | 1.9% |
| generic-AI-buzzword name | 127 | 12.7% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| Dockerfile | 3 |
| HTML | 2 |
| TypeScript | 2 |
| Unknown | 2 |
| Rust | 1 |
| JavaScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 1 | 1 | 2 | 25.0% |
| 5000-9999 | 6 | 0 | 1 | 5 | 0.0% |
| 1000-4999 | 66 | 10 | 3 | 53 | 15.2% |
| 500-999 | 114 | 1 | 20 | 93 | 0.9% |
| 100-499 | 810 | 4 | 121 | 685 | 0.5% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 12947 | 1748 | 15d | Python | MIT |
| `bashalarmistalt/decimen-optical-transfer` | 4604 | 556 | 5d | TypeScript | MIT |
| `withmarbleapp/os-taxonomy` | 3849 | 669 | 27d | JavaScript | ODbL-1.0 |
| `slvDev/esp32-ai` | 3485 | 444 | 12d | Python | MIT |
| `CluvexStudio/Aether` | 1722 | 116 | 21d | Rust | AGPL-3.0 |
| `x4gKing/Marzban-Panel` | 1376 | 2642 | 23d | Dockerfile | — |
| `Subhan-code/Amicro--Micro-transitions-` | 1368 | 55 | 24d | TypeScript | MIT |
| `x4gKing/3x-ui-Upgrade` | 1311 | 2895 | 27d | HTML | — |
| `x4gKing/PasarGuard-Node` | 1301 | 2554 | 29d | Dockerfile | — |
| `x4gKing/Marzban-Node` | 1204 | 2411 | 23d | Dockerfile | — |
| `osama-fawad/Pekingman` | 1075 | 60 | 28d | HTML | — |

### Generic-name pattern breakdown

Of 127 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 23 |
| `codex` | 22 |
| `skills` | 18 |
| `skill` | 16 |
| `awesome` | 13 |
| `claude` | 8 |
| `agents` | 6 |
| `llm` | 4 |
| `prompt` | 4 |
| `template` | 4 |
| `gpt` | 3 |
| `vibe` | 2 |
| `demo` | 2 |
| `copilot` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 554 (55.4%)
- Repos with at least one topic: 446 (44.6%)

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
