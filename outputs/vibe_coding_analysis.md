# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-19 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 170 | 17.0% |
| 訊號完整 | 819 | 81.9% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `thananon/9arm-skills` | 2837 | 381 | 29d | **7** | desc:empty, license:none, high-attention-no-desc, generic-name:9arm-skills, topics:none |
| 2 | `anomalyco/rift` | 621 | 12 | 18d | **6** | desc:empty, license:none, low-forks:0.019, topics:none |
| 3 | `world-action-models/awesome-world-action-models` | 174 | 2 | 1d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 4 | `Tong89/smartNode` | 1984 | 174 | 28d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 5 | `qqfly1to19/awesome_proofreading_auto` | 143 | 24 | 27d | **5** | desc:empty, license:none, generic-name:awesome_proofreading_auto, topics:none |
| 6 | `jiaran-king/Re-Zero---Starting-LLM-` | 202 | 7 | 22d | **5** | desc:empty, license:none, generic-name:Re-Zero---Starting-LLM-, topics:none |
| 7 | `jmmy9609-design/gpt-pp` | 397 | 204 | 9d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 8 | `chaseai-yt/grill-me-codex` | 242 | 31 | 13d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 9 | `THUYRan/Legal-Skills-Chinese` | 291 | 41 | 29d | **5** | desc:empty, license:none, generic-name:Legal-Skills-Chinese, topics:none |
| 10 | `levy-street/world-of-claudecraft` | 1023 | 288 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `deermiya/visio-skill` | 117 | 9 | 23d | **5** | desc:empty, license:none, generic-name:visio-skill, topics:none |
| 12 | `riyagoelrs/tiktok-scraper` | 150 | 15 | 23d | **4** | desc:empty, license:none, topics:none |
| 13 | `chaitin/agent-compose` | 149 | 13 | 12d | **4** | desc:empty, generic-name:agent-compose, topics:none |
| 14 | `johnmiddleton12/wearable` | 279 | 137 | 20d | **4** | desc:empty, license:none, topics:none |
| 15 | `inbrainfun/inbrain` | 304 | 190 | 8d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 140 | 14.0% |
| description <20 chars | 22 | 2.2% |
| no license | 394 | 39.4% |
| high-attention no-desc (stars>1k + empty desc) | 3 | 0.3% |
| low fork ratio (stars>500 + fsr<0.02) | 8 | 0.8% |
| overnight surge (>300 spd + <7 days) | 5 | 0.5% |
| generic-AI-buzzword name | 151 | 15.1% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 5 |
| Unknown | 3 |
| Shell | 1 |
| Rust | 1 |
| TypeScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 2 | 0 | 0 | 2 | 0.0% |
| 5000-9999 | 5 | 0 | 0 | 5 | 0.0% |
| 1000-4999 | 49 | 3 | 3 | 43 | 6.1% |
| 500-999 | 96 | 1 | 18 | 77 | 1.0% |
| 100-499 | 848 | 7 | 149 | 692 | 0.8% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `thananon/9arm-skills` | 2837 | 381 | 29d | Shell | — |
| `Tong89/smartNode` | 1984 | 174 | 28d | Python | MIT |
| `levy-street/world-of-claudecraft` | 1023 | 288 | 8d | TypeScript | MIT |

### Generic-name pattern breakdown

Of 151 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 29 |
| `skill` | 28 |
| `skills` | 24 |
| `awesome` | 17 |
| `claude` | 15 |
| `codex` | 12 |
| `llm` | 5 |
| `gpt` | 4 |
| `vibe` | 4 |
| `toolkit` | 3 |
| `demo` | 2 |
| `prompt` | 2 |
| `agents` | 2 |
| `template` | 1 |
| `cookbook` | 1 |
| `copilot` | 1 |
| `starter` | 1 |

### Topics coverage

- Repos with **zero topics**: 586 (58.6%)
- Repos with at least one topic: 414 (41.4%)

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
