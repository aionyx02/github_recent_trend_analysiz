# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-02 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 9 | 0.9% |
| 待檢視 | 103 | 10.3% |
| 訊號完整 | 888 | 88.8% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1071 | 331 | 3d | **7** | desc:empty, high-attention-no-desc, overnight-surge:357/day, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 2 | `zhongerxin/Cowart` | 3639 | 284 | 13d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `Harlihm/Your-Self-Improving-AI-Brain` | 863 | 1 | 24d | **6** | desc:empty, license:none, low-forks:0.001, topics:none |
| 4 | `kanavtwtgg/birds.cafe` | 703 | 2 | 10d | **6** | desc:empty, license:none, low-forks:0.003, topics:none |
| 5 | `world-action-models/awesome-world-action-models` | 306 | 7 | 14d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 6 | `jmmy9609-design/gpt-pp` | 402 | 204 | 22d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 7 | `chaseai-yt/grill-me-codex` | 339 | 36 | 26d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 8 | `terrense/LLM_path_for_begginers` | 213 | 6 | 9d | **5** | desc:empty, license:none, generic-name:LLM_path_for_begginers, topics:none |
| 9 | `levy-street/world-of-claudecraft` | 1407 | 432 | 21d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `Kulaxyz/self-learning-skills` | 809 | 10 | 3d | **4** | low-forks:0.012, generic-name:self-learning-skills, topics:none |
| 11 | `ZeKaiNie/universal-examprep-skill` | 215 | 11 | 7d | **4** | desc:empty, generic-name:universal-examprep-skill, topics:none |
| 12 | `xiejhhhhhh/Draftpaper_loop` | 203 | 8 | 29d | **4** | desc:empty, license:none, topics:none |
| 13 | `insanekrishnna/polymatch` | 919 | 2 | 24d | **4** | license:none, low-forks:0.002, topics:none |
| 14 | `Neph0s/Agentopia` | 153 | 19 | 26d | **4** | desc:empty, license:none, topics:none |
| 15 | `downclash/clash` | 343 | 0 | 4d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 85 | 8.5% |
| description <20 chars | 10 | 1.0% |
| no license | 326 | 32.6% |
| high-attention no-desc (stars>1k + empty desc) | 3 | 0.3% |
| low fork ratio (stars>500 + fsr<0.02) | 17 | 1.7% |
| overnight surge (>300 spd + <7 days) | 6 | 0.6% |
| generic-AI-buzzword name | 117 | 11.7% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 4 |
| Python | 2 |
| JavaScript | 2 |
| TypeScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 6 | 0 | 2 | 4 | 0.0% |
| 1000-4999 | 48 | 3 | 5 | 40 | 6.2% |
| 500-999 | 86 | 2 | 15 | 69 | 2.3% |
| 100-499 | 857 | 4 | 81 | 772 | 0.5% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `zhongerxin/Cowart` | 3639 | 284 | 13d | JavaScript | — |
| `levy-street/world-of-claudecraft` | 1407 | 432 | 21d | TypeScript | MIT |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1071 | 331 | 3d | Python | MIT |

### Generic-name pattern breakdown

Of 117 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `agent` | 21 |
| `skill` | 20 |
| `skills` | 17 |
| `codex` | 14 |
| `claude` | 14 |
| `awesome` | 11 |
| `gpt` | 3 |
| `demo` | 3 |
| `agents` | 3 |
| `llm` | 2 |
| `starter` | 2 |
| `playground` | 1 |
| `prompt` | 1 |
| `test` | 1 |
| `toolkit` | 1 |
| `template` | 1 |
| `vibe` | 1 |
| `copilot` | 1 |

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
