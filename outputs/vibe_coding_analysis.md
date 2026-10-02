# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-10-02 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 15 | 1.5% |
| 待檢視 | 120 | 12.0% |
| 訊號完整 | 865 | 86.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Mantitup-Org/vista` | 2378 | 47 | 27d | **8** | desc:empty, license:none, high-attention-no-desc, low-forks:0.020, topics:none |
| 2 | `reladraw/reladraw` | 1012 | 19 | 24d | **7** | desc:empty, high-attention-no-desc, low-forks:0.019, topics:none |
| 3 | `wy51ai/floorplan-3d` | 1255 | 260 | 2d | **6** | desc:empty, high-attention-no-desc, overnight-surge:628/day, topics:none |
| 4 | `kajisho5/ffmpeg-skill` | 1452 | 119 | 28d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 5 | `Vodiwalker/vodiwalker_panel` | 1072 | 2852 | 21d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `Contrastive-LM/CLM` | 2716 | 238 | 8d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `Taichu-AI/ZDTaichu5.0-9B` | 2837 | 551 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `Lumid-Off/AirCard-Windows` | 1152 | 85 | 13d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `imexlovery/video-report-agent` | 152 | 10 | 23d | **5** | desc:empty, license:none, generic-name:video-report-agent, topics:none |
| 10 | `inclusionAI/Choruz` | 912 | 9 | 29d | **5** | desc:empty, low-forks:0.010, topics:none |
| 11 | `google-research/rrsi` | 1182 | 107 | 15d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `Edge0-AI/Edge0` | 2326 | 211 | 23d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `LinkMouseIndex/SteamSharedAccount-AllGame` | 691 | 0 | 23d | **5** | desc:empty, license:none, low-forks:0.000 |
| 14 | `vinnylarouge/jevlike` | 1339 | 116 | 15d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `anthropics/fermats-last-theorem` | 1247 | 106 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 110 | 11.0% |
| description <20 chars | 17 | 1.7% |
| no license | 278 | 27.8% |
| high-attention no-desc (stars>1k + empty desc) | 12 | 1.2% |
| low fork ratio (stars>500 + fsr<0.02) | 17 | 1.7% |
| overnight surge (>300 spd + <7 days) | 16 | 1.6% |
| generic-AI-buzzword name | 117 | 11.7% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 8 |
| TypeScript | 2 |
| Rust | 2 |
| HTML | 1 |
| Unknown | 1 |
| Lean | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 10 | 0 | 0 | 10 | 0.0% |
| 1000-4999 | 106 | 12 | 3 | 91 | 11.3% |
| 500-999 | 155 | 2 | 23 | 130 | 1.3% |
| 100-499 | 726 | 1 | 94 | 631 | 0.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `Taichu-AI/ZDTaichu5.0-9B` | 2837 | 551 | 27d | Python | Apache-2.0 |
| `Contrastive-LM/CLM` | 2716 | 238 | 8d | Python | Apache-2.0 |
| `Mantitup-Org/vista` | 2378 | 47 | 27d | TypeScript | — |
| `Edge0-AI/Edge0` | 2326 | 211 | 23d | Python | Apache-2.0 |
| `kajisho5/ffmpeg-skill` | 1452 | 119 | 28d | Python | MIT |
| `vinnylarouge/jevlike` | 1339 | 116 | 15d | Python | MIT |
| `wy51ai/floorplan-3d` | 1255 | 260 | 2d | HTML | MIT |
| `anthropics/fermats-last-theorem` | 1247 | 106 | 27d | Lean | Apache-2.0 |
| `google-research/rrsi` | 1182 | 107 | 15d | Python | Apache-2.0 |
| `Lumid-Off/AirCard-Windows` | 1152 | 85 | 13d | Rust | MIT |
| `Vodiwalker/vodiwalker_panel` | 1072 | 2852 | 21d | Python | — |
| `reladraw/reladraw` | 1012 | 19 | 24d | TypeScript | Apache-2.0 |

### Generic-name pattern breakdown

Of 117 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 33 |
| `skill` | 24 |
| `agent` | 21 |
| `skills` | 10 |
| `codex` | 7 |
| `claude` | 5 |
| `gpt` | 5 |
| `llm` | 5 |
| `toolkit` | 1 |
| `vibe` | 1 |
| `prompt` | 1 |
| `demo` | 1 |
| `agents` | 1 |
| `cookbook` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 572 (57.2%)
- Repos with at least one topic: 428 (42.8%)

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
