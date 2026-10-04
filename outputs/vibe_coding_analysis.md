# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-10-04 | Sample size: 1000 repos (with topics signal)_

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
| 1 | `Mantitup-Org/vista` | 2366 | 47 | 29d | **8** | desc:empty, license:none, high-attention-no-desc, low-forks:0.020, topics:none |
| 2 | `wy51ai/floorplan-3d` | 1372 | 283 | 4d | **6** | desc:empty, high-attention-no-desc, overnight-surge:343/day, topics:none |
| 3 | `Vodiwalker/vodiwalker_panel` | 1140 | 3028 | 23d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `ArasTey/lunel` | 1016 | 2421 | 24d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `imexlovery/video-report-agent` | 161 | 12 | 25d | **5** | desc:empty, license:none, generic-name:video-report-agent, topics:none |
| 6 | `cloudflare/forge` | 1002 | 38 | 12d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `anthropics/fermats-last-theorem` | 1250 | 106 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `google-research/rrsi` | 1232 | 119 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `fsiaonma/elpis` | 546 | 4 | 4d | **5** | desc:short, license:none, low-forks:0.007, topics:none |
| 10 | `Lumid-Off/AirCard-Windows` | 1219 | 91 | 15d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `vinnylarouge/jevlike` | 1341 | 117 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `Taichu-AI/ZDTaichu5.0-9B` | 3124 | 551 | 29d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `reladraw/reladraw` | 1048 | 23 | 26d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `Edge0-AI/Edge0` | 2858 | 333 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `Contrastive-LM/CLM` | 2785 | 239 | 10d | **5** | desc:empty, high-attention-no-desc, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 113 | 11.3% |
| description <20 chars | 17 | 1.7% |
| no license | 303 | 30.3% |
| high-attention no-desc (stars>1k + empty desc) | 13 | 1.3% |
| low fork ratio (stars>500 + fsr<0.02) | 20 | 2.0% |
| overnight surge (>300 spd + <7 days) | 39 | 3.9% |
| generic-AI-buzzword name | 110 | 11.0% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 8 |
| TypeScript | 4 |
| HTML | 1 |
| Lean | 1 |
| Rust | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 10 | 0 | 0 | 10 | 0.0% |
| 1000-4999 | 105 | 13 | 4 | 88 | 12.4% |
| 500-999 | 162 | 1 | 26 | 135 | 0.6% |
| 100-499 | 720 | 1 | 97 | 622 | 0.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `Taichu-AI/ZDTaichu5.0-9B` | 3124 | 551 | 29d | Python | Apache-2.0 |
| `Edge0-AI/Edge0` | 2858 | 333 | 25d | Python | Apache-2.0 |
| `Contrastive-LM/CLM` | 2785 | 239 | 10d | Python | Apache-2.0 |
| `Mantitup-Org/vista` | 2366 | 47 | 29d | TypeScript | — |
| `wy51ai/floorplan-3d` | 1372 | 283 | 4d | HTML | MIT |
| `vinnylarouge/jevlike` | 1341 | 117 | 17d | Python | MIT |
| `anthropics/fermats-last-theorem` | 1250 | 106 | 29d | Lean | Apache-2.0 |
| `google-research/rrsi` | 1232 | 119 | 17d | Python | Apache-2.0 |
| `Lumid-Off/AirCard-Windows` | 1219 | 91 | 15d | Rust | MIT |
| `Vodiwalker/vodiwalker_panel` | 1140 | 3028 | 23d | Python | — |
| `reladraw/reladraw` | 1048 | 23 | 26d | TypeScript | Apache-2.0 |
| `ArasTey/lunel` | 1016 | 2421 | 24d | Python | — |
| `cloudflare/forge` | 1002 | 38 | 12d | TypeScript | Apache-2.0 |

### Generic-name pattern breakdown

Of 110 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 32 |
| `agent` | 20 |
| `skill` | 20 |
| `skills` | 10 |
| `codex` | 8 |
| `gpt` | 5 |
| `claude` | 4 |
| `llm` | 3 |
| `vibe` | 2 |
| `toolkit` | 1 |
| `prompt` | 1 |
| `demo` | 1 |
| `agents` | 1 |
| `cookbook` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 541 (54.1%)
- Repos with at least one topic: 459 (45.9%)

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
