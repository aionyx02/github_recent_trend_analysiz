# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-03 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 100 | 10.0% |
| 訊號完整 | 889 | 88.9% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Harlihm/Your-Self-Improving-AI-Brain` | 973 | 1 | 25d | **6** | desc:empty, license:none, low-forks:0.001, topics:none |
| 2 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1168 | 349 | 4d | **6** | desc:empty, high-attention-no-desc, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 3 | `kanavtwtgg/birds.cafe` | 703 | 2 | 11d | **6** | desc:empty, license:none, low-forks:0.003, topics:none |
| 4 | `zhongerxin/Cowart` | 3707 | 286 | 14d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `terrense/LLM_path_for_begginers` | 243 | 6 | 10d | **5** | desc:empty, license:none, generic-name:LLM_path_for_begginers, topics:none |
| 6 | `deepreinforce-ai/Ornith-1` | 1044 | 99 | 11d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `jmmy9609-design/gpt-pp` | 402 | 204 | 23d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 8 | `chaseai-yt/grill-me-codex` | 343 | 37 | 27d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 9 | `JimLiu/science-skills` | 171 | 44 | 1d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |
| 10 | `world-action-models/awesome-world-action-models` | 306 | 7 | 15d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 11 | `levy-street/world-of-claudecraft` | 1423 | 439 | 22d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `opengram-server/opengram` | 206 | 21 | 28d | **4** | desc:empty, license:none, topics:none |
| 13 | `Pengbinghui/pipeline-math` | 201 | 14 | 6d | **4** | desc:empty, license:none, topics:none |
| 14 | `secret-tools/secret-tool` | 1200 | 2 | 24d | **4** | license:none, low-forks:0.002, topics:none |
| 15 | `SakanaAI/fugu` | 701 | 81 | 15d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 84 | 8.4% |
| description <20 chars | 11 | 1.1% |
| no license | 353 | 35.3% |
| high-attention no-desc (stars>1k + empty desc) | 4 | 0.4% |
| low fork ratio (stars>500 + fsr<0.02) | 16 | 1.6% |
| overnight surge (>300 spd + <7 days) | 5 | 0.5% |
| generic-AI-buzzword name | 122 | 12.2% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 5 |
| Python | 2 |
| JavaScript | 2 |
| HTML | 1 |
| TypeScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 6 | 0 | 2 | 4 | 0.0% |
| 1000-4999 | 49 | 4 | 6 | 39 | 8.2% |
| 500-999 | 84 | 2 | 15 | 67 | 2.4% |
| 100-499 | 858 | 5 | 77 | 776 | 0.6% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `zhongerxin/Cowart` | 3707 | 286 | 14d | JavaScript | — |
| `levy-street/world-of-claudecraft` | 1423 | 439 | 22d | TypeScript | MIT |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1168 | 349 | 4d | Python | MIT |
| `deepreinforce-ai/Ornith-1` | 1044 | 99 | 11d | Unknown | MIT |

### Generic-name pattern breakdown

Of 122 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 21 |
| `skill` | 20 |
| `skills` | 18 |
| `claude` | 17 |
| `codex` | 13 |
| `awesome` | 11 |
| `llm` | 3 |
| `gpt` | 3 |
| `demo` | 3 |
| `toolkit` | 2 |
| `starter` | 2 |
| `copilot` | 2 |
| `agents` | 2 |
| `prompt` | 1 |
| `playground` | 1 |
| `test` | 1 |
| `template` | 1 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 575 (57.5%)
- Repos with at least one topic: 425 (42.5%)

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
