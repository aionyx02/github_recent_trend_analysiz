# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-22 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 11 | 1.1% |
| 待檢視 | 107 | 10.7% |
| 訊號完整 | 882 | 88.2% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `x4gKing/3x-ui` | 1230 | 2372 | 17d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `x4gKing/X4G` | 6283 | 11509 | 17d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1985 | 495 | 23d | **6** | desc:empty, high-attention-no-desc, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 4 | `x4gKing/3x-ui-Upgrade` | 1137 | 2391 | 13d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `x4gKing/Marzban-Panel` | 1043 | 1978 | 9d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `CluvexStudio/Aether` | 1452 | 88 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `TobiasLee/Rebuttal-Skill` | 328 | 13 | 7d | **5** | desc:empty, license:none, generic-name:Rebuttal-Skill, topics:none |
| 8 | `withmarbleapp/os-taxonomy` | 3554 | 608 | 13d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `JimLiu/science-skills` | 216 | 53 | 20d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |
| 10 | `h9-tec/Awesome_ai_learning` | 229 | 29 | 5d | **5** | desc:empty, license:none, generic-name:Awesome_ai_learning, topics:none |
| 11 | `Fei-Away/Codex-Dream-Skin` | 11684 | 1180 | 6d | **5** | desc:short, license:none, overnight-surge:1947/day, generic-name:Codex-Dream-Skin, topics:none |
| 12 | `Kulaxyz/token-diet` | 524 | 4 | 18d | **4** | license:none, low-forks:0.008, topics:none |
| 13 | `x4gKing/Marzban-Node` | 898 | 1786 | 9d | **4** | desc:empty, license:none, topics:none |
| 14 | `unicity-aos/aos-ce` | 6090 | 4 | 9d | **4** | license:none, low-forks:0.001, topics:none |
| 15 | `yusukebe/ax` | 554 | 11 | 15d | **4** | desc:short, low-forks:0.020, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 91 | 9.1% |
| description <20 chars | 19 | 1.9% |
| no license | 494 | 49.4% |
| high-attention no-desc (stars>1k + empty desc) | 7 | 0.7% |
| low fork ratio (stars>500 + fsr<0.02) | 12 | 1.2% |
| overnight surge (>300 spd + <7 days) | 5 | 0.5% |
| generic-AI-buzzword name | 137 | 13.7% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Dockerfile | 2 |
| Python | 2 |
| HTML | 2 |
| Unknown | 2 |
| JavaScript | 2 |
| Rust | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 1 | 0 | 3 | 25.0% |
| 5000-9999 | 5 | 1 | 1 | 3 | 20.0% |
| 1000-4999 | 49 | 6 | 4 | 39 | 12.2% |
| 500-999 | 108 | 0 | 24 | 84 | 0.0% |
| 100-499 | 834 | 3 | 78 | 753 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `x4gKing/X4G` | 6283 | 11509 | 17d | Python | — |
| `withmarbleapp/os-taxonomy` | 3554 | 608 | 13d | JavaScript | ODbL-1.0 |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1985 | 495 | 23d | Python | MIT |
| `CluvexStudio/Aether` | 1452 | 88 | 7d | Rust | AGPL-3.0 |
| `x4gKing/3x-ui` | 1230 | 2372 | 17d | Dockerfile | — |
| `x4gKing/3x-ui-Upgrade` | 1137 | 2391 | 13d | HTML | — |
| `x4gKing/Marzban-Panel` | 1043 | 1978 | 9d | Dockerfile | — |

### Generic-name pattern breakdown

Of 137 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 24 |
| `skills` | 22 |
| `codex` | 18 |
| `skill` | 18 |
| `claude` | 15 |
| `awesome` | 12 |
| `prompt` | 7 |
| `llm` | 4 |
| `agents` | 3 |
| `gpt` | 3 |
| `template` | 3 |
| `starter` | 3 |
| `toolkit` | 2 |
| `copilot` | 2 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 402 (40.2%)
- Repos with at least one topic: 598 (59.8%)

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
