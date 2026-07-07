# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-07-07 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 14 | 1.4% |
| 待檢視 | 71 | 7.1% |
| 訊號完整 | 915 | 91.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1563 | 439 | 8d | **6** | desc:empty, high-attention-no-desc, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 2 | `Harlihm/Your-Self-Improving-AI-Brain` | 868 | 1 | 29d | **6** | desc:empty, license:none, low-forks:0.001, topics:none |
| 3 | `zhongerxin/Cowart` | 4026 | 320 | 18d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `kanavtwtgg/birds.cafe` | 538 | 2 | 15d | **6** | desc:empty, license:none, low-forks:0.004, topics:none |
| 5 | `huang-sir1/radiology-skills` | 578 | 10 | 18d | **6** | desc:empty, low-forks:0.017, generic-name:radiology-skills, topics:none |
| 6 | `deepreinforce-ai/Ornith-1` | 1353 | 126 | 15d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `jd-opensource/JoyAI-VL-Interaction` | 1141 | 101 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `Regert888/gpt-outlook-register` | 182 | 65 | 28d | **5** | desc:empty, license:none, generic-name:gpt-outlook-register, topics:none |
| 9 | `jmmy9609-design/gpt-pp` | 403 | 204 | 27d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 10 | `world-action-models/awesome-world-action-models` | 312 | 7 | 19d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 11 | `terrense/LLM_path_for_begginers` | 314 | 8 | 14d | **5** | desc:empty, license:none, generic-name:LLM_path_for_begginers, topics:none |
| 12 | `levy-street/world-of-claudecraft` | 1516 | 472 | 26d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `google-research/tabfm` | 1451 | 131 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `JimLiu/science-skills` | 202 | 51 | 5d | **5** | desc:empty, license:none, generic-name:science-skills, topics:none |
| 15 | `ZeKaiNie/universal-examprep-skill` | 242 | 12 | 12d | **4** | desc:empty, generic-name:universal-examprep-skill, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 63 | 6.3% |
| description <20 chars | 11 | 1.1% |
| no license | 601 | 60.1% |
| high-attention no-desc (stars>1k + empty desc) | 6 | 0.6% |
| low fork ratio (stars>500 + fsr<0.02) | 13 | 1.3% |
| overnight surge (>300 spd + <7 days) | 8 | 0.8% |
| generic-AI-buzzword name | 193 | 19.3% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| Unknown | 4 |
| JavaScript | 2 |
| TypeScript | 1 |
| HTML | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 5 | 0 | 0 | 5 | 0.0% |
| 1000-4999 | 48 | 6 | 4 | 38 | 12.5% |
| 500-999 | 95 | 3 | 15 | 77 | 3.2% |
| 100-499 | 849 | 5 | 52 | 792 | 0.6% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `zhongerxin/Cowart` | 4026 | 320 | 18d | JavaScript | — |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 1563 | 439 | 8d | Python | MIT |
| `levy-street/world-of-claudecraft` | 1516 | 472 | 26d | TypeScript | MIT |
| `google-research/tabfm` | 1451 | 131 | 20d | Python | Apache-2.0 |
| `deepreinforce-ai/Ornith-1` | 1353 | 126 | 15d | Unknown | MIT |
| `jd-opensource/JoyAI-VL-Interaction` | 1141 | 101 | 25d | Python | Apache-2.0 |

### Generic-name pattern breakdown

Of 193 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `toolkit` | 87 |
| `skills` | 21 |
| `skill` | 21 |
| `agent` | 19 |
| `codex` | 10 |
| `awesome` | 10 |
| `claude` | 10 |
| `gpt` | 3 |
| `copilot` | 3 |
| `llm` | 2 |
| `demo` | 2 |
| `agents` | 2 |
| `starter` | 1 |
| `prompt` | 1 |
| `vibe` | 1 |

### Topics coverage

- Repos with **zero topics**: 333 (33.3%)
- Repos with at least one topic: 667 (66.7%)

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
