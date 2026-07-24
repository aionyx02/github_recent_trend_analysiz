# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-24 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 12 | 1.2% |
| 待檢視 | 106 | 10.6% |
| 訊號完整 | 882 | 88.2% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `x4gKing/3x-ui` | 1373 | 2655 | 19d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `x4gKing/X4G` | 6531 | 12002 | 19d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `x4gKing/3x-ui-Upgrade` | 1176 | 2490 | 15d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 2013 | 497 | 25d | **6** | desc:empty, high-attention-no-desc, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 5 | `andrewyng/openworker` | 2235 | 303 | 3d | **6** | desc:empty, high-attention-no-desc, overnight-surge:745/day, topics:none |
| 6 | `x4gKing/Marzban-Panel` | 1097 | 2097 | 11d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `h9-tec/Awesome_ai_learning` | 236 | 33 | 7d | **5** | desc:empty, license:none, generic-name:Awesome_ai_learning, topics:none |
| 8 | `TobiasLee/Rebuttal-Skill` | 380 | 14 | 9d | **5** | desc:empty, license:none, generic-name:Rebuttal-Skill, topics:none |
| 9 | `nyblnet/bento` | 1234 | 70 | 6d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `withmarbleapp/os-taxonomy` | 3634 | 629 | 15d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `JimLiu/science-skills` | 216 | 52 | 22d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |
| 12 | `CluvexStudio/Aether` | 1488 | 94 | 9d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `J-jaeyoung/bad-epoll` | 498 | 45 | 29d | **4** | desc:empty, license:none, topics:none |
| 14 | `gnipbao/codex-whiteboard-video-skill` | 195 | 42 | 27d | **4** | desc:empty, generic-name:codex-whiteboard-video-skill, topics:none |
| 15 | `Kulaxyz/token-diet` | 508 | 4 | 20d | **4** | license:none, low-forks:0.008, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 91 | 9.1% |
| description <20 chars | 20 | 2.0% |
| no license | 499 | 49.9% |
| high-attention no-desc (stars>1k + empty desc) | 10 | 1.0% |
| low fork ratio (stars>500 + fsr<0.02) | 13 | 1.3% |
| overnight surge (>300 spd + <7 days) | 4 | 0.4% |
| generic-AI-buzzword name | 130 | 13.0% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 3 |
| Dockerfile | 2 |
| HTML | 2 |
| Unknown | 2 |
| TypeScript | 1 |
| JavaScript | 1 |
| Rust | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 1 | 2 | 0.0% |
| 5000-9999 | 6 | 1 | 1 | 4 | 16.7% |
| 1000-4999 | 58 | 8 | 4 | 46 | 13.8% |
| 500-999 | 106 | 0 | 24 | 82 | 0.0% |
| 100-499 | 827 | 3 | 76 | 748 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `x4gKing/X4G` | 6531 | 12002 | 19d | Python | — |
| `withmarbleapp/os-taxonomy` | 3634 | 629 | 15d | JavaScript | ODbL-1.0 |
| `andrewyng/openworker` | 2235 | 303 | 3d | Python | MIT |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 2013 | 497 | 25d | Python | MIT |
| `CluvexStudio/Aether` | 1488 | 94 | 9d | Rust | AGPL-3.0 |
| `x4gKing/3x-ui` | 1373 | 2655 | 19d | Dockerfile | — |
| `nyblnet/bento` | 1234 | 70 | 6d | TypeScript | MIT |
| `x4gKing/3x-ui-Upgrade` | 1176 | 2490 | 15d | HTML | — |
| `buchidonggua/dg-ai-notes` | 1139 | 79 | 18d | MDX | MIT |
| `x4gKing/Marzban-Panel` | 1097 | 2097 | 11d | Dockerfile | — |

### Generic-name pattern breakdown

Of 130 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 21 |
| `skills` | 20 |
| `codex` | 17 |
| `skill` | 17 |
| `claude` | 17 |
| `awesome` | 11 |
| `prompt` | 6 |
| `llm` | 4 |
| `starter` | 4 |
| `template` | 3 |
| `agents` | 2 |
| `copilot` | 2 |
| `toolkit` | 2 |
| `gpt` | 2 |
| `vibe` | 2 |

### Topics coverage

- Repos with **zero topics**: 389 (38.9%)
- Repos with at least one topic: 611 (61.1%)

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
