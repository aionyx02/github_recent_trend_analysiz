# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-21 | Sample size: 1000 repos (with topics signal)_

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
| 1 | `anomalyco/rift` | 626 | 12 | 20d | **6** | desc:empty, license:none, low-forks:0.019, topics:none |
| 2 | `levy-street/world-of-claudecraft` | 1056 | 299 | 10d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 3 | `deermiya/visio-skill` | 117 | 9 | 25d | **5** | desc:empty, license:none, generic-name:visio-skill, topics:none |
| 4 | `jiaran-king/Re-Zero---Starting-LLM-` | 206 | 7 | 24d | **5** | desc:empty, license:none, generic-name:Re-Zero---Starting-LLM-, topics:none |
| 5 | `chaseai-yt/grill-me-codex` | 252 | 32 | 15d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 6 | `gakiyukr/Codex_team_auto` | 105 | 53 | 3d | **5** | desc:empty, license:none, generic-name:Codex_team_auto, topics:none |
| 7 | `qqfly1to19/awesome_proofreading_auto` | 145 | 24 | 29d | **5** | desc:empty, license:none, generic-name:awesome_proofreading_auto, topics:none |
| 8 | `zhongerxin/cowart` | 657 | 61 | 2d | **5** | desc:empty, license:none, overnight-surge:328/day, topics:none |
| 9 | `jmmy9609-design/gpt-pp` | 396 | 204 | 11d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 10 | `world-action-models/awesome-world-action-models` | 202 | 2 | 3d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 11 | `Regert888/gpt-outlook-register` | 105 | 41 | 12d | **5** | desc:empty, license:none, generic-name:gpt-outlook-register, topics:none |
| 12 | `pzr2508/RL_for_Game` | 121 | 2 | 6d | **4** | desc:empty, license:none, topics:none |
| 13 | `vorpus/performativeUI` | 750 | 21 | 13d | **4** | desc:empty, license:none, topics:none |
| 14 | `Moh4696/websites-100-audit` | 234 | 48 | 22d | **4** | desc:empty, license:none, topics:none |
| 15 | `wechat-miniprogram/ai-mode-demo` | 230 | 35 | 15d | **4** | desc:empty, generic-name:ai-mode-demo, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 134 | 13.4% |
| description <20 chars | 24 | 2.4% |
| no license | 349 | 34.9% |
| high-attention no-desc (stars>1k + empty desc) | 1 | 0.1% |
| low fork ratio (stars>500 + fsr<0.02) | 13 | 1.3% |
| overnight surge (>300 spd + <7 days) | 5 | 0.5% |
| generic-AI-buzzword name | 150 | 15.0% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| Unknown | 2 |
| Rust | 1 |
| TypeScript | 1 |
| JavaScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 4 | 0 | 0 | 4 | 0.0% |
| 1000-4999 | 45 | 1 | 4 | 40 | 2.2% |
| 500-999 | 95 | 2 | 20 | 73 | 2.1% |
| 100-499 | 849 | 8 | 146 | 695 | 0.9% |
| <100 | 4 | 0 | 0 | 4 | 0.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `levy-street/world-of-claudecraft` | 1056 | 299 | 10d | TypeScript | MIT |

### Generic-name pattern breakdown

Of 150 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 30 |
| `skill` | 29 |
| `skills` | 25 |
| `awesome` | 16 |
| `claude` | 14 |
| `codex` | 11 |
| `llm` | 5 |
| `gpt` | 5 |
| `vibe` | 3 |
| `demo` | 2 |
| `prompt` | 2 |
| `toolkit` | 2 |
| `agents` | 2 |
| `template` | 1 |
| `cookbook` | 1 |
| `copilot` | 1 |
| `starter` | 1 |

### Topics coverage

- Repos with **zero topics**: 616 (61.6%)
- Repos with at least one topic: 384 (38.4%)

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
