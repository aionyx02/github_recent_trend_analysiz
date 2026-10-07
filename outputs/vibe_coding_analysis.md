# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-10-07 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 130 | 13.0% |
| 訊號完整 | 853 | 85.3% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `openai/math` | 7275 | 683 | 1d | **6** | desc:empty, high-attention-no-desc, overnight-surge:7275/day, topics:none |
| 2 | `Vodiwalker/vodiwalker_panel` | 1206 | 3212 | 26d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `kargulstudio/sales-crm` | 1617 | 342 | 2d | **6** | desc:empty, high-attention-no-desc, overnight-surge:808/day, topics:none |
| 4 | `ArasTey/lunel` | 1037 | 2465 | 27d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `deillusion/Aha-Engine` | 533 | 4 | 26d | **6** | desc:empty, license:none, low-forks:0.008, topics:none |
| 6 | `nex-agi/Nex-N2.5` | 1119 | 30 | 29d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 7 | `google-research/rrsi` | 1291 | 123 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `vinnylarouge/jevlike` | 1351 | 119 | 20d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `Lumid-Off/AirCard-Windows` | 1297 | 103 | 18d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 10 | `fsiaonma/elpis` | 557 | 5 | 7d | **5** | desc:short, license:none, low-forks:0.009, topics:none |
| 11 | `wy51ai/floorplan-3d` | 1468 | 298 | 7d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `cloudflare/forge` | 1066 | 42 | 15d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `storytold/effectcraft` | 1240 | 487 | 5d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `deadinside28/bloodborne_pc` | 1449 | 130 | 5d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `imexlovery/video-report-agent` | 183 | 12 | 28d | **5** | desc:empty, license:none, generic-name:video-report-agent, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 113 | 11.3% |
| description <20 chars | 13 | 1.3% |
| no license | 270 | 27.0% |
| high-attention no-desc (stars>1k + empty desc) | 14 | 1.4% |
| low fork ratio (stars>500 + fsr<0.02) | 23 | 2.3% |
| overnight surge (>300 spd + <7 days) | 11 | 1.1% |
| generic-AI-buzzword name | 108 | 10.8% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| TypeScript | 4 |
| Rust | 2 |
| Lean | 1 |
| JavaScript | 1 |
| Unknown | 1 |
| HTML | 1 |
| C++ | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 6 | 0 | 0 | 6 | 0.0% |
| 5000-9999 | 11 | 1 | 0 | 10 | 9.1% |
| 1000-4999 | 116 | 13 | 7 | 96 | 11.2% |
| 500-999 | 171 | 2 | 24 | 145 | 1.2% |
| 100-499 | 696 | 1 | 99 | 596 | 0.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `openai/math` | 7275 | 683 | 1d | Lean | Apache-2.0 |
| `Contrastive-LM/CLM` | 2903 | 252 | 13d | Python | Apache-2.0 |
| `kargulstudio/sales-crm` | 1617 | 342 | 2d | TypeScript | MIT |
| `wy51ai/floorplan-3d` | 1468 | 298 | 7d | HTML | MIT |
| `deadinside28/bloodborne_pc` | 1449 | 130 | 5d | C++ | GPL-2.0 |
| `vinnylarouge/jevlike` | 1351 | 119 | 20d | Python | MIT |
| `Lumid-Off/AirCard-Windows` | 1297 | 103 | 18d | Rust | MIT |
| `google-research/rrsi` | 1291 | 123 | 20d | Python | Apache-2.0 |
| `storytold/effectcraft` | 1240 | 487 | 5d | Rust | Apache-2.0 |
| `Vodiwalker/vodiwalker_panel` | 1206 | 3212 | 26d | Python | — |
| `nex-agi/Nex-N2.5` | 1119 | 30 | 29d | Unknown | — |
| `reladraw/reladraw` | 1086 | 25 | 29d | TypeScript | Apache-2.0 |
| `cloudflare/forge` | 1066 | 42 | 15d | TypeScript | Apache-2.0 |
| `ArasTey/lunel` | 1037 | 2465 | 27d | Python | — |

### Generic-name pattern breakdown

Of 108 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 31 |
| `skill` | 21 |
| `agent` | 19 |
| `skills` | 8 |
| `codex` | 6 |
| `gpt` | 5 |
| `claude` | 5 |
| `llm` | 4 |
| `cookbook` | 2 |
| `demo` | 2 |
| `vibe` | 2 |
| `prompt` | 1 |
| `agents` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 557 (55.7%)
- Repos with at least one topic: 443 (44.3%)

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
