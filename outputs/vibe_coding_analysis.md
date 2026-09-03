# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-03 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 7 | 0.7% |
| 待檢視 | 105 | 10.5% |
| 訊號完整 | 888 | 88.8% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `ZzzLc0405/photo-abstract-editorial` | 5307 | 332 | 29d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `amirh00sain/SpiderPanel` | 1054 | 3536 | 15d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `almendili/skills` | 377 | 28 | 17d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 4 | `MiniMax-AI/awesome-minimax-h3-integration` | 276 | 19 | 20d | **5** | desc:empty, license:none, generic-name:awesome-minimax-h3-integration, topics:none |
| 5 | `itnann/Data-Analysis-Agent` | 170 | 5 | 27d | **5** | desc:empty, license:none, generic-name:Data-Analysis-Agent, topics:none |
| 6 | `gvzdv/claudish-to-english` | 2497 | 118 | 23d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `tobi/walgit` | 2407 | 132 | 10d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `XinXie-Condex/DeepSeek-Harness-Desktop` | 173 | 5 | 18d | **4** | desc:empty, license:none, topics:none |
| 9 | `QIYUEKURONG/ai-learning-planner` | 211 | 1 | 23d | **4** | desc:empty, license:none, topics:none |
| 10 | `Tencent-Hunyuan/Hy4-preview` | 338 | 19 | 6d | **4** | desc:empty, license:none, topics:none |
| 11 | `sjc88661/multi-agent-discuss` | 212 | 24 | 19d | **4** | desc:empty, generic-name:multi-agent-discuss, topics:none |
| 12 | `mufengyuan6/CodeMason` | 219 | 0 | 16d | **4** | desc:empty, license:none, topics:none |
| 13 | `subsy/skill-cabinet` | 374 | 25 | 2d | **4** | desc:empty, generic-name:skill-cabinet, topics:none |
| 14 | `ericzakariasson/scandinavian-design` | 368 | 18 | 21d | **4** | desc:empty, license:none, topics:none |
| 15 | `ganjoor/ganjoor-data` | 226 | 44 | 19d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 75 | 7.5% |
| description <20 chars | 169 | 16.9% |
| no license | 426 | 42.6% |
| high-attention no-desc (stars>1k + empty desc) | 4 | 0.4% |
| low fork ratio (stars>500 + fsr<0.02) | 15 | 1.5% |
| overnight surge (>300 spd + <7 days) | 8 | 0.8% |
| generic-AI-buzzword name | 106 | 10.6% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 2 |
| Python | 2 |
| TypeScript | 1 |
| Shell | 1 |
| Rust | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 5 | 0 | 1 | 4 | 0.0% |
| 5000-9999 | 6 | 1 | 1 | 4 | 16.7% |
| 1000-4999 | 80 | 3 | 4 | 73 | 3.8% |
| 500-999 | 145 | 0 | 22 | 123 | 0.0% |
| 100-499 | 764 | 3 | 77 | 684 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `ZzzLc0405/photo-abstract-editorial` | 5307 | 332 | 29d | Unknown | — |
| `gvzdv/claudish-to-english` | 2497 | 118 | 23d | Shell | MIT |
| `tobi/walgit` | 2407 | 132 | 10d | Rust | MIT |
| `amirh00sain/SpiderPanel` | 1054 | 3536 | 15d | Python | — |

### Generic-name pattern breakdown

Of 106 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 18 |
| `agent` | 17 |
| `skills` | 15 |
| `awesome` | 15 |
| `codex` | 8 |
| `toolkit` | 7 |
| `claude` | 4 |
| `prompt` | 4 |
| `gpt` | 4 |
| `llm` | 3 |
| `agents` | 2 |
| `starter` | 2 |
| `template` | 2 |
| `vibe` | 2 |
| `playground` | 1 |
| `test` | 1 |
| `demo` | 1 |

### Topics coverage

- Repos with **zero topics**: 370 (37.0%)
- Repos with at least one topic: 630 (63.0%)

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
