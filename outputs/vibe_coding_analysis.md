# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-12 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 166 | 16.6% |
| 訊號完整 | 818 | 81.8% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2758 | 376 | 22d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:9arm-skills, topics:none |
| 2 | `google-antigravity/antigravity-cli` | 1038 | 68 | 29d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `OpenNSWM-Lab/FAROS` | 1026 | 171 | 29d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `XiaomiMiMo/MiMo-Code` | 5645 | 448 | 1d | **6** | desc:empty, high-attention-no-desc, overnight-surge:5645/day, topics:none |
| 5 | `anomalyco/rift` | 566 | 11 | 11d | **6** | desc:empty, license:none, low-forks:0.019, topics:none |
| 6 | `THUYRan/Legal-Skills-Chinese` | 246 | 35 | 22d | **5** | desc:empty, license:none, generic-name:Legal-Skills-Chinese, topics:none |
| 7 | `rosemarycox5334-debug/PA_Agent` | 130 | 63 | 23d | **5** | desc:empty, license:none, generic-name:PA_Agent, topics:none |
| 8 | `qqfly1to19/awesome_proofreading_auto` | 136 | 24 | 20d | **5** | desc:empty, license:none, generic-name:awesome_proofreading_auto, topics:none |
| 9 | `deermiya/visio-skill` | 103 | 8 | 16d | **5** | desc:empty, license:none, generic-name:visio-skill, topics:none |
| 10 | `jiaran-king/Re-Zero---Starting-LLM-` | 174 | 5 | 15d | **5** | desc:empty, license:none, generic-name:Re-Zero---Starting-LLM-, topics:none |
| 11 | `chaseai-yt/grill-me-codex` | 184 | 25 | 6d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 12 | `jmmy9609-design/gpt-pp` | 364 | 197 | 2d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 13 | `FoundZiGu/GuJumpgate` | 3821 | 986 | 23d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `Tong89/smartNode` | 1990 | 176 | 21d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `limin112/wechat-publish-template` | 231 | 27 | 24d | **5** | desc:empty, license:none, generic-name:wechat-publish-template, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 138 | 13.8% |
| description <20 chars | 27 | 2.7% |
| no license | 374 | 37.4% |
| high-attention no-desc (stars>1k + empty desc) | 6 | 0.6% |
| low fork ratio (stars>500 + fsr<0.02) | 9 | 0.9% |
| overnight surge (>300 spd + <7 days) | 6 | 0.6% |
| generic-AI-buzzword name | 133 | 13.3% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 8 |
| Unknown | 3 |
| Shell | 1 |
| TypeScript | 1 |
| Rust | 1 |
| JavaScript | 1 |
| HTML | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 1 | 0 | 0 | 1 | 0.0% |
| 5000-9999 | 4 | 1 | 1 | 2 | 25.0% |
| 1000-4999 | 59 | 5 | 5 | 49 | 8.5% |
| 500-999 | 87 | 1 | 13 | 73 | 1.1% |
| 100-499 | 849 | 9 | 147 | 693 | 1.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `XiaomiMiMo/MiMo-Code` | 5645 | 448 | 1d | TypeScript | MIT |
| `FoundZiGu/GuJumpgate` | 3821 | 986 | 23d | JavaScript | MIT |
| `thananon/9arm-skills` | 2758 | 376 | 22d | Shell | — |
| `Tong89/smartNode` | 1990 | 176 | 21d | Python | MIT |
| `google-antigravity/antigravity-cli` | 1038 | 68 | 29d | Unknown | — |
| `OpenNSWM-Lab/FAROS` | 1026 | 171 | 29d | Python | — |

### Generic-name pattern breakdown

Of 133 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 29 |
| `skill` | 26 |
| `skills` | 21 |
| `awesome` | 13 |
| `claude` | 13 |
| `codex` | 12 |
| `llm` | 3 |
| `gpt` | 3 |
| `template` | 3 |
| `vibe` | 3 |
| `toolkit` | 2 |
| `agents` | 2 |
| `demo` | 1 |
| `cookbook` | 1 |
| `starter` | 1 |

### Topics coverage

- Repos with **zero topics**: 626 (62.6%)
- Repos with at least one topic: 374 (37.4%)

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
