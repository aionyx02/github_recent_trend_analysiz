# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-08-09 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 142 | 14.2% |
| 訊號完整 | 837 | 83.7% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `ZzzLc0405/photo-abstract-editorial` | 1809 | 90 | 4d | **7** | desc:empty, license:none, high-attention-no-desc, overnight-surge:452/day, topics:none |
| 2 | `Zeejay0/gathered-scenes-zine-skill` | 1503 | 73 | 7d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:gathered-scenes-zine-skill, topics:none |
| 3 | `MiniMax-AI/MiniMax-H3` | 2065 | 127 | 9d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `yuhuangerdi/InduSecAgent` | 568 | 10 | 5d | **6** | desc:empty, license:none, low-forks:0.018, topics:none |
| 5 | `X-EraAI/ActPhysCause-Challenge` | 546 | 0 | 23d | **6** | desc:empty, license:none, low-forks:0.000, topics:none |
| 6 | `chuspeeism/dashi-taskboard` | 1272 | 190 | 15d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `x4gKing/Marzban-Node` | 1287 | 2583 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 8 | `OpenMouse-Project/openmouse` | 1092 | 70 | 12d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 9 | `x4gKing/Marzban-Panel` | 1453 | 2828 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 10 | `bashalarmistalt/decimen-optical-transfer` | 5375 | 649 | 9d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `CluvexStudio/Aether` | 1772 | 120 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `TobiasLee/Rebuttal-Skill` | 451 | 20 | 25d | **5** | desc:empty, license:none, generic-name:Rebuttal-Skill, topics:none |
| 13 | `margelo/ai-chat-demo` | 158 | 13 | 4d | **5** | desc:empty, license:none, generic-name:ai-chat-demo, topics:none |
| 14 | `Subhan-code/Amicro--Micro-transitions-` | 1454 | 59 | 28d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `andrewyng/openworker` | 13849 | 1882 | 19d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 120 | 12.0% |
| description <20 chars | 81 | 8.1% |
| no license | 340 | 34.0% |
| high-attention no-desc (stars>1k + empty desc) | 12 | 1.2% |
| low fork ratio (stars>500 + fsr<0.02) | 15 | 1.5% |
| overnight surge (>300 spd + <7 days) | 8 | 0.8% |
| generic-AI-buzzword name | 128 | 12.8% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| Unknown | 5 |
| TypeScript | 4 |
| Dockerfile | 2 |
| Vue | 1 |
| JavaScript | 1 |
| Rust | 1 |
| Shell | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 1 | 1 | 4 | 16.7% |
| 5000-9999 | 7 | 1 | 1 | 5 | 14.3% |
| 1000-4999 | 72 | 10 | 3 | 59 | 13.9% |
| 500-999 | 101 | 4 | 18 | 79 | 4.0% |
| 100-499 | 814 | 5 | 119 | 690 | 0.6% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `andrewyng/openworker` | 13849 | 1882 | 19d | Python | MIT |
| `bashalarmistalt/decimen-optical-transfer` | 5375 | 649 | 9d | TypeScript | MIT |
| `slvDev/esp32-ai` | 3810 | 490 | 16d | Python | MIT |
| `MiniMax-AI/MiniMax-H3` | 2065 | 127 | 9d | Python | — |
| `ZzzLc0405/photo-abstract-editorial` | 1809 | 90 | 4d | Unknown | — |
| `CluvexStudio/Aether` | 1772 | 120 | 25d | Rust | AGPL-3.0 |
| `Zeejay0/gathered-scenes-zine-skill` | 1503 | 73 | 7d | Unknown | — |
| `Subhan-code/Amicro--Micro-transitions-` | 1454 | 59 | 28d | TypeScript | MIT |
| `x4gKing/Marzban-Panel` | 1453 | 2828 | 27d | Dockerfile | — |
| `x4gKing/Marzban-Node` | 1287 | 2583 | 27d | Dockerfile | — |
| `chuspeeism/dashi-taskboard` | 1272 | 190 | 15d | JavaScript | — |
| `OpenMouse-Project/openmouse` | 1092 | 70 | 12d | TypeScript | — |

### Generic-name pattern breakdown

Of 128 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 23 |
| `skills` | 20 |
| `codex` | 20 |
| `skill` | 15 |
| `awesome` | 13 |
| `claude` | 9 |
| `toolkit` | 6 |
| `agents` | 5 |
| `gpt` | 3 |
| `prompt` | 3 |
| `template` | 3 |
| `demo` | 2 |
| `llm` | 2 |
| `copilot` | 1 |
| `playground` | 1 |
| `starter` | 1 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 538 (53.8%)
- Repos with at least one topic: 462 (46.2%)

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
