# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-30 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 77 | 7.7% |
| 訊號完整 | 915 | 91.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Harlihm/Your-Self-Improving-AI-Brain` | 754 | 1 | 22d | **6** | desc:empty, license:none, low-forks:0.001, topics:none |
| 2 | `kanavtwtgg/birds.cafe` | 740 | 3 | 8d | **6** | desc:empty, license:none, low-forks:0.004, topics:none |
| 3 | `zhongerxin/Cowart` | 3473 | 273 | 11d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 645 | 206 | 1d | **5** | desc:empty, overnight-surge:645/day, generic-name:Codex-5.5-codex-instruct-5.5, topics:none |
| 5 | `jmmy9609-design/gpt-pp` | 402 | 204 | 20d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 6 | `world-action-models/awesome-world-action-models` | 300 | 7 | 12d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 7 | `chaseai-yt/grill-me-codex` | 324 | 34 | 24d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 8 | `levy-street/world-of-claudecraft` | 1379 | 418 | 19d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `zhengdian1/InterleaveThinker` | 210 | 5 | 18d | **4** | desc:empty, license:none, topics:none |
| 10 | `inbrainfun/inbrain` | 303 | 191 | 19d | **4** | desc:empty, license:none, topics:none |
| 11 | `SakanaAI/fugu` | 631 | 79 | 12d | **4** | desc:empty, license:none, topics:none |
| 12 | `InsiderX-Pro/SE-Bridge-TTS` | 303 | 1 | 20d | **4** | desc:empty, license:none, topics:none |
| 13 | `secret-tools/secret-tool` | 1060 | 1 | 21d | **4** | license:none, low-forks:0.001, topics:none |
| 14 | `byJoey/cfnew-deployer` | 305 | 192 | 7d | **4** | desc:empty, license:none, topics:none |
| 15 | `iebb/mithka` | 307 | 8 | 7d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 61 | 6.1% |
| description <20 chars | 8 | 0.8% |
| no license | 158 | 15.8% |
| high-attention no-desc (stars>1k + empty desc) | 2 | 0.2% |
| low fork ratio (stars>500 + fsr<0.02) | 14 | 1.4% |
| overnight surge (>300 spd + <7 days) | 6 | 0.6% |
| generic-AI-buzzword name | 95 | 9.5% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Unknown | 3 |
| JavaScript | 2 |
| Python | 2 |
| TypeScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 0 | 0 | 4 | 0.0% |
| 5000-9999 | 5 | 0 | 2 | 3 | 0.0% |
| 1000-4999 | 49 | 2 | 7 | 40 | 4.1% |
| 500-999 | 87 | 3 | 14 | 70 | 3.4% |
| 100-499 | 855 | 3 | 54 | 798 | 0.4% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `zhongerxin/Cowart` | 3473 | 273 | 11d | JavaScript | — |
| `levy-street/world-of-claudecraft` | 1379 | 418 | 19d | TypeScript | MIT |

### Generic-name pattern breakdown

Of 95 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `toolkit` | 19 |
| `skills` | 17 |
| `agent` | 16 |
| `skill` | 13 |
| `codex` | 9 |
| `awesome` | 5 |
| `claude` | 5 |
| `gpt` | 3 |
| `demo` | 2 |
| `agents` | 2 |
| `starter` | 1 |
| `vibe` | 1 |
| `copilot` | 1 |
| `llm` | 1 |

### Topics coverage

- Repos with **zero topics**: 797 (79.7%)
- Repos with at least one topic: 203 (20.3%)

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
