# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-10-01 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 17 | 1.7% |
| 待檢視 | 126 | 12.6% |
| 訊號完整 | 857 | 85.7% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Mantitup-Org/vista` | 2383 | 47 | 26d | **8** | desc:empty, license:none, high-attention-no-desc, low-forks:0.020, topics:none |
| 2 | `reladraw/reladraw` | 1002 | 19 | 23d | **7** | desc:empty, high-attention-no-desc, low-forks:0.019, topics:none |
| 3 | `wy51ai/floorplan-3d` | 1089 | 232 | 1d | **6** | desc:empty, high-attention-no-desc, overnight-surge:1089/day, topics:none |
| 4 | `kajisho5/ffmpeg-skill` | 1446 | 118 | 27d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 5 | `NxcoreAI/NxMem` | 1087 | 107 | 20d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `azerioid/azerioid-stack-manager` | 715 | 4 | 29d | **6** | desc:empty, license:none, low-forks:0.006, topics:none |
| 7 | `Vodiwalker/vodiwalker_panel` | 1039 | 2742 | 20d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 8 | `anthropics/fermats-last-theorem` | 1243 | 106 | 26d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `Contrastive-LM/CLM` | 2656 | 230 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `Taichu-AI/ZDTaichu5.0-9B` | 2517 | 549 | 26d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `Majorclujerk/Server-Raider` | 1846 | 191 | 9d | **5** | desc:empty, license:none, high-attention-no-desc |
| 12 | `inclusionAI/Choruz` | 903 | 9 | 28d | **5** | desc:empty, low-forks:0.010, topics:none |
| 13 | `imexlovery/video-report-agent` | 149 | 10 | 22d | **5** | desc:empty, license:none, generic-name:video-report-agent, topics:none |
| 14 | `Edge0-AI/Edge0` | 2157 | 195 | 22d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `google-research/rrsi` | 1105 | 96 | 14d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 117 | 11.7% |
| description <20 chars | 20 | 2.0% |
| no license | 288 | 28.8% |
| high-attention no-desc (stars>1k + empty desc) | 14 | 1.4% |
| low fork ratio (stars>500 + fsr<0.02) | 18 | 1.8% |
| overnight surge (>300 spd + <7 days) | 20 | 2.0% |
| generic-AI-buzzword name | 119 | 11.9% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 8 |
| TypeScript | 3 |
| Rust | 2 |
| HTML | 1 |
| PHP | 1 |
| Lean | 1 |
| Unknown | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 9 | 0 | 0 | 9 | 0.0% |
| 1000-4999 | 98 | 14 | 2 | 82 | 14.3% |
| 500-999 | 157 | 2 | 23 | 132 | 1.3% |
| 100-499 | 733 | 1 | 101 | 631 | 0.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `Contrastive-LM/CLM` | 2656 | 230 | 7d | Python | Apache-2.0 |
| `Taichu-AI/ZDTaichu5.0-9B` | 2517 | 549 | 26d | Python | Apache-2.0 |
| `Mantitup-Org/vista` | 2383 | 47 | 26d | TypeScript | — |
| `Edge0-AI/Edge0` | 2157 | 195 | 22d | Python | Apache-2.0 |
| `Majorclujerk/Server-Raider` | 1846 | 191 | 9d | Unknown | — |
| `kajisho5/ffmpeg-skill` | 1446 | 118 | 27d | Python | MIT |
| `vinnylarouge/jevlike` | 1338 | 118 | 14d | Python | MIT |
| `anthropics/fermats-last-theorem` | 1243 | 106 | 26d | Lean | Apache-2.0 |
| `Lumid-Off/AirCard-Windows` | 1107 | 82 | 12d | Rust | MIT |
| `google-research/rrsi` | 1105 | 96 | 14d | Python | Apache-2.0 |
| `wy51ai/floorplan-3d` | 1089 | 232 | 1d | HTML | MIT |
| `NxcoreAI/NxMem` | 1087 | 107 | 20d | TypeScript | — |
| `Vodiwalker/vodiwalker_panel` | 1039 | 2742 | 20d | Python | — |
| `reladraw/reladraw` | 1002 | 19 | 23d | TypeScript | Apache-2.0 |

### Generic-name pattern breakdown

Of 119 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 34 |
| `skill` | 23 |
| `agent` | 21 |
| `skills` | 10 |
| `codex` | 7 |
| `gpt` | 5 |
| `claude` | 5 |
| `llm` | 5 |
| `agents` | 2 |
| `prompt` | 2 |
| `toolkit` | 1 |
| `vibe` | 1 |
| `demo` | 1 |
| `cookbook` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 580 (58.0%)
- Repos with at least one topic: 420 (42.0%)

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
