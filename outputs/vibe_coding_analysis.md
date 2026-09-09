# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-09 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 8 | 0.8% |
| 待檢視 | 118 | 11.8% |
| 訊號完整 | 874 | 87.4% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `amirh00sain/SpiderPanel` | 1222 | 4125 | 21d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 2 | `almendili/skills` | 380 | 28 | 23d | **5** | desc:empty, license:none, generic-name:skills, topics:none |
| 3 | `yczz/oc-english` | 855 | 15 | 7d | **5** | desc:short, license:none, low-forks:0.018, topics:none |
| 4 | `MiniMax-AI/awesome-minimax-h3-integration` | 309 | 24 | 26d | **5** | desc:empty, license:none, generic-name:awesome-minimax-h3-integration, topics:none |
| 5 | `guithepc/mentor-prompt` | 133 | 0 | 23d | **5** | desc:empty, license:none, generic-name:mentor-prompt, topics:none |
| 6 | `jtydhr88/screenwriting-skills` | 396 | 46 | 2d | **5** | desc:empty, license:none, generic-name:screenwriting-skills, topics:none |
| 7 | `tobi/walgit` | 2459 | 140 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `gvzdv/claudish-to-english` | 2556 | 120 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `rrzu/deepseek-harness-desktop` | 141 | 0 | 19d | **4** | desc:empty, license:none, topics:none |
| 10 | `solari-sdk/solari-cookbook` | 157 | 459 | 21d | **4** | desc:empty, generic-name:solari-cookbook, topics:none |
| 11 | `AlloxOrg/allox-os` | 316 | 2 | 27d | **4** | desc:empty, license:none, topics:none |
| 12 | `ericzakariasson/scandinavian-design` | 380 | 18 | 27d | **4** | desc:empty, license:none, topics:none |
| 13 | `x4gpanell/3x-ui` | 319 | 964 | 24d | **4** | desc:empty, license:none, topics:none |
| 14 | `wanonewan/wanwan` | 307 | 1843 | 24d | **4** | desc:empty, license:none, topics:none |
| 15 | `MiniMax-AI/MiniMax-Music3` | 836 | 78 | 28d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 99 | 9.9% |
| description <20 chars | 19 | 1.9% |
| no license | 264 | 26.4% |
| high-attention no-desc (stars>1k + empty desc) | 3 | 0.3% |
| low fork ratio (stars>500 + fsr<0.02) | 11 | 1.1% |
| overnight surge (>300 spd + <7 days) | 13 | 1.3% |
| generic-AI-buzzword name | 113 | 11.3% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 3 |
| Python | 1 |
| TypeScript | 1 |
| JavaScript | 1 |
| Rust | 1 |
| Shell | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 0 | 0 | 4 | 0.0% |
| 5000-9999 | 6 | 0 | 0 | 6 | 0.0% |
| 1000-4999 | 87 | 3 | 2 | 82 | 3.4% |
| 500-999 | 129 | 1 | 19 | 109 | 0.8% |
| 100-499 | 774 | 4 | 97 | 673 | 0.5% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `gvzdv/claudish-to-english` | 2556 | 120 | 29d | Shell | MIT |
| `tobi/walgit` | 2459 | 140 | 16d | Rust | MIT |
| `amirh00sain/SpiderPanel` | 1222 | 4125 | 21d | Python | — |

### Generic-name pattern breakdown

Of 113 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 26 |
| `skill` | 25 |
| `awesome` | 16 |
| `skills` | 14 |
| `codex` | 8 |
| `claude` | 4 |
| `toolkit` | 4 |
| `prompt` | 3 |
| `agents` | 2 |
| `starter` | 2 |
| `template` | 2 |
| `llm` | 2 |
| `vibe` | 2 |
| `cookbook` | 1 |
| `gpt` | 1 |
| `demo` | 1 |

### Topics coverage

- Repos with **zero topics**: 493 (49.3%)
- Repos with at least one topic: 507 (50.7%)

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
