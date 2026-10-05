# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-10-05 | Sample size: 1000 repos (with topics signal)_

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
| 低資訊密度 | 12 | 1.2% |
| 待檢視 | 133 | 13.3% |
| 訊號完整 | 855 | 85.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `kargulstudio/sales-crm` | 1274 | 253 | 1d | **7** | desc:empty, license:none, high-attention-no-desc, overnight-surge:1274/day, topics:none |
| 2 | `ArasTey/lunel` | 1028 | 2443 | 25d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `Vodiwalker/vodiwalker_panel` | 1161 | 3097 | 24d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `fsiaonma/elpis` | 550 | 4 | 5d | **5** | desc:short, license:none, low-forks:0.007, topics:none |
| 5 | `imexlovery/video-report-agent` | 167 | 12 | 26d | **5** | desc:empty, license:none, generic-name:video-report-agent, topics:none |
| 6 | `cloudflare/forge` | 1026 | 39 | 13d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `vinnylarouge/jevlike` | 1344 | 118 | 18d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `reladraw/reladraw` | 1067 | 24 | 27d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `wy51ai/floorplan-3d` | 1414 | 291 | 5d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `google-research/rrsi` | 1253 | 121 | 18d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `Lumid-Off/AirCard-Windows` | 1249 | 97 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `Contrastive-LM/CLM` | 2844 | 245 | 11d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `taeold/djev-run` | 577 | 37 | 14d | **4** | desc:empty, license:none, topics:none |
| 14 | `tristanbuckmaster/fluid_lean` | 269 | 19 | 26d | **4** | desc:empty, license:none, topics:none |
| 15 | `corvofeng/atv-core` | 228 | 14 | 8d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 113 | 11.3% |
| description <20 chars | 16 | 1.6% |
| no license | 275 | 27.5% |
| high-attention no-desc (stars>1k + empty desc) | 10 | 1.0% |
| low fork ratio (stars>500 + fsr<0.02) | 20 | 2.0% |
| overnight surge (>300 spd + <7 days) | 14 | 1.4% |
| generic-AI-buzzword name | 115 | 11.5% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| TypeScript | 4 |
| HTML | 1 |
| Rust | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 4 | 0 | 0 | 4 | 0.0% |
| 5000-9999 | 10 | 0 | 0 | 10 | 0.0% |
| 1000-4999 | 107 | 10 | 6 | 91 | 9.3% |
| 500-999 | 170 | 1 | 24 | 145 | 0.6% |
| 100-499 | 709 | 1 | 103 | 605 | 0.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `Contrastive-LM/CLM` | 2844 | 245 | 11d | Python | Apache-2.0 |
| `wy51ai/floorplan-3d` | 1414 | 291 | 5d | HTML | MIT |
| `vinnylarouge/jevlike` | 1344 | 118 | 18d | Python | MIT |
| `kargulstudio/sales-crm` | 1274 | 253 | 1d | TypeScript | — |
| `google-research/rrsi` | 1253 | 121 | 18d | Python | Apache-2.0 |
| `Lumid-Off/AirCard-Windows` | 1249 | 97 | 16d | Rust | MIT |
| `Vodiwalker/vodiwalker_panel` | 1161 | 3097 | 24d | Python | — |
| `reladraw/reladraw` | 1067 | 24 | 27d | TypeScript | Apache-2.0 |
| `ArasTey/lunel` | 1028 | 2443 | 25d | Python | — |
| `cloudflare/forge` | 1026 | 39 | 13d | TypeScript | Apache-2.0 |

### Generic-name pattern breakdown

Of 115 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 33 |
| `agent` | 21 |
| `skill` | 20 |
| `skills` | 10 |
| `codex` | 8 |
| `gpt` | 5 |
| `claude` | 5 |
| `llm` | 4 |
| `cookbook` | 2 |
| `vibe` | 2 |
| `toolkit` | 1 |
| `prompt` | 1 |
| `demo` | 1 |
| `agents` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 559 (55.9%)
- Repos with at least one topic: 441 (44.1%)

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
