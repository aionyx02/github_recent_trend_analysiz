# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-06-28 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 177 | 17.7% |
| 訊號完整 | 815 | 81.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `kanavtwtgg/birds.cafe` | 736 | 2 | 6d | **6** | desc:empty, license:none, low-forks:0.003, topics:none |
| 2 | `zhongerxin/Cowart` | 3195 | 245 | 9d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `jmmy9609-design/gpt-pp` | 403 | 205 | 18d | **5** | desc:empty, license:none, generic-name:gpt-pp, topics:none |
| 4 | `world-action-models/awesome-world-action-models` | 293 | 6 | 10d | **5** | desc:empty, license:none, generic-name:awesome-world-action-models, topics:none |
| 5 | `gakiyukr/Codex_team_auto` | 108 | 53 | 10d | **5** | desc:empty, license:none, generic-name:Codex_team_auto, topics:none |
| 6 | `Regert888/gpt-outlook-register` | 118 | 44 | 19d | **5** | desc:empty, license:none, generic-name:gpt-outlook-register, topics:none |
| 7 | `chaseai-yt/grill-me-codex` | 292 | 33 | 22d | **5** | desc:empty, license:none, generic-name:grill-me-codex, topics:none |
| 8 | `levy-street/world-of-claudecraft` | 1350 | 403 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `Iwancof/HackRFOneSegTuner` | 107 | 9 | 8d | **4** | desc:empty, license:none, topics:none |
| 10 | `Neph0s/Agentopia` | 135 | 18 | 22d | **4** | desc:empty, license:none, topics:none |
| 11 | `cclank/tokei` | 149 | 20 | 23d | **4** | desc:empty, license:none, topics:none |
| 12 | `viitor-ai/viitor-voice-nar` | 144 | 30 | 18d | **4** | desc:empty, license:none, topics:none |
| 13 | `Phoenixx1202/Spectrum-Library` | 141 | 4 | 21d | **4** | desc:empty, license:none, topics:none |
| 14 | `xiejhhhhhh/Draftpaper_loop` | 153 | 6 | 25d | **4** | desc:empty, license:none, topics:none |
| 15 | `J-jaeyoung/bad-epoll` | 161 | 13 | 3d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 136 | 13.6% |
| description <20 chars | 21 | 2.1% |
| no license | 343 | 34.3% |
| high-attention no-desc (stars>1k + empty desc) | 2 | 0.2% |
| low fork ratio (stars>500 + fsr<0.02) | 15 | 1.5% |
| overnight surge (>300 spd + <7 days) | 6 | 0.6% |
| generic-AI-buzzword name | 159 | 15.9% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 3 |
| JavaScript | 2 |
| Unknown | 2 |
| TypeScript | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 0 | 0 | 4 | 0.0% |
| 5000-9999 | 6 | 0 | 3 | 3 | 0.0% |
| 1000-4999 | 46 | 2 | 6 | 38 | 4.3% |
| 500-999 | 88 | 1 | 15 | 72 | 1.1% |
| 100-499 | 821 | 5 | 146 | 670 | 0.6% |
| <100 | 35 | 0 | 7 | 28 | 0.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `zhongerxin/Cowart` | 3195 | 245 | 9d | JavaScript | — |
| `levy-street/world-of-claudecraft` | 1350 | 403 | 17d | TypeScript | MIT |

### Generic-name pattern breakdown

Of 159 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 34 |
| `agent` | 33 |
| `skills` | 30 |
| `awesome` | 13 |
| `codex` | 13 |
| `claude` | 12 |
| `gpt` | 6 |
| `demo` | 3 |
| `llm` | 3 |
| `agents` | 3 |
| `vibe` | 3 |
| `toolkit` | 2 |
| `prompt` | 1 |
| `template` | 1 |
| `starter` | 1 |
| `copilot` | 1 |

### Topics coverage

- Repos with **zero topics**: 594 (59.4%)
- Repos with at least one topic: 406 (40.6%)

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
