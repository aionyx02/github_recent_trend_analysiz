# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-10-06 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 127 | 12.7% |
| 訊號完整 | 858 | 85.8% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `deillusion/Aha-Engine` | 513 | 4 | 25d | **6** | desc:empty, license:none, low-forks:0.008, topics:none |
| 2 | `nex-agi/Nex-N2.5` | 1054 | 25 | 28d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `ArasTey/lunel` | 1034 | 2452 | 26d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `kargulstudio/sales-crm` | 1547 | 323 | 1d | **6** | desc:empty, high-attention-no-desc, overnight-surge:1547/day, topics:none |
| 5 | `Vodiwalker/vodiwalker_panel` | 1182 | 3157 | 25d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `Contrastive-LM/CLM` | 2873 | 249 | 12d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `fsiaonma/elpis` | 552 | 4 | 6d | **5** | desc:short, license:none, low-forks:0.007, topics:none |
| 8 | `wy51ai/floorplan-3d` | 1435 | 294 | 6d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `cloudflare/forge` | 1054 | 41 | 14d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `google-research/rrsi` | 1272 | 122 | 19d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `reladraw/reladraw` | 1078 | 25 | 28d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `Lumid-Off/AirCard-Windows` | 1275 | 102 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `vinnylarouge/jevlike` | 1347 | 118 | 19d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `YXBwbWFya2V0/AppMarket` | 341 | 163 | 1d | **5** | desc:empty, license:none, overnight-surge:341/day, topics:none |
| 15 | `imexlovery/video-report-agent` | 173 | 12 | 27d | **5** | desc:empty, license:none, generic-name:video-report-agent, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 111 | 11.1% |
| description <20 chars | 16 | 1.6% |
| no license | 291 | 29.1% |
| high-attention no-desc (stars>1k + empty desc) | 11 | 1.1% |
| low fork ratio (stars>500 + fsr<0.02) | 18 | 1.8% |
| overnight surge (>300 spd + <7 days) | 30 | 3.0% |
| generic-AI-buzzword name | 108 | 10.8% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| TypeScript | 4 |
| JavaScript | 1 |
| Unknown | 1 |
| HTML | 1 |
| Rust | 1 |
| Kotlin | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 0 | 0 | 4 | 0.0% |
| 5000-9999 | 11 | 0 | 0 | 11 | 0.0% |
| 1000-4999 | 110 | 11 | 8 | 91 | 10.0% |
| 500-999 | 166 | 2 | 21 | 143 | 1.2% |
| 100-499 | 709 | 2 | 98 | 609 | 0.3% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `Contrastive-LM/CLM` | 2873 | 249 | 12d | Python | Apache-2.0 |
| `kargulstudio/sales-crm` | 1547 | 323 | 1d | TypeScript | MIT |
| `wy51ai/floorplan-3d` | 1435 | 294 | 6d | HTML | MIT |
| `vinnylarouge/jevlike` | 1347 | 118 | 19d | Python | MIT |
| `Lumid-Off/AirCard-Windows` | 1275 | 102 | 17d | Rust | MIT |
| `google-research/rrsi` | 1272 | 122 | 19d | Python | Apache-2.0 |
| `Vodiwalker/vodiwalker_panel` | 1182 | 3157 | 25d | Python | — |
| `reladraw/reladraw` | 1078 | 25 | 28d | TypeScript | Apache-2.0 |
| `nex-agi/Nex-N2.5` | 1054 | 25 | 28d | Unknown | — |
| `cloudflare/forge` | 1054 | 41 | 14d | TypeScript | Apache-2.0 |
| `ArasTey/lunel` | 1034 | 2452 | 26d | Python | — |

### Generic-name pattern breakdown

Of 108 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 32 |
| `agent` | 20 |
| `skill` | 19 |
| `skills` | 9 |
| `codex` | 7 |
| `gpt` | 5 |
| `claude` | 4 |
| `llm` | 4 |
| `cookbook` | 2 |
| `vibe` | 2 |
| `prompt` | 1 |
| `demo` | 1 |
| `playground` | 1 |
| `agents` | 1 |

### Topics coverage

- Repos with **zero topics**: 537 (53.7%)
- Repos with at least one topic: 463 (46.3%)

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
