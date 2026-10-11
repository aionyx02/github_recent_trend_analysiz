# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-10-11 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 125 | 12.5% |
| 訊號完整 | 861 | 86.1% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `openai/math` | 13900 | 1545 | 4d | **6** | desc:empty, high-attention-no-desc, overnight-surge:3475/day, topics:none |
| 2 | `wangmingxuan666/Tiersense` | 1319 | 218 | 16d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 3 | `storytold/effectcraft` | 4862 | 2297 | 9d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 4 | `deadinside28/bloodborne_pc` | 2403 | 366 | 9d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 5 | `cloudflare/forge` | 1110 | 45 | 19d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 6 | `google-research/rrsi` | 1445 | 140 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 7 | `kargulstudio/sales-crm` | 1694 | 372 | 6d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 8 | `Contrastive-LM/CLM` | 2971 | 256 | 17d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 9 | `fsiaonma/elpis` | 578 | 5 | 11d | **5** | desc:short, license:none, low-forks:0.009, topics:none |
| 10 | `wy51ai/floorplan-3d` | 2144 | 404 | 11d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `Lumid-Off/AirCard-Windows` | 1342 | 108 | 22d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `vinnylarouge/jevlike` | 1350 | 117 | 24d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `storytold/designcraft` | 2761 | 1701 | 9d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `Spearmintai/mintocode` | 659 | 11 | 10d | **5** | desc:empty, low-forks:0.017, topics:none |
| 15 | `nanocle/Charakuru` | 491 | 41 | 4d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 95 | 9.5% |
| description <20 chars | 13 | 1.3% |
| no license | 281 | 28.1% |
| high-attention no-desc (stars>1k + empty desc) | 12 | 1.2% |
| low fork ratio (stars>500 + fsr<0.02) | 27 | 2.7% |
| overnight surge (>300 spd + <7 days) | 51 | 5.1% |
| generic-AI-buzzword name | 100 | 10.0% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 4 |
| Rust | 3 |
| TypeScript | 3 |
| Lean | 1 |
| Unknown | 1 |
| C++ | 1 |
| HTML | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 7 | 1 | 0 | 6 | 14.3% |
| 5000-9999 | 15 | 0 | 0 | 15 | 0.0% |
| 1000-4999 | 130 | 11 | 9 | 110 | 8.5% |
| 500-999 | 187 | 2 | 32 | 153 | 1.1% |
| 100-499 | 661 | 0 | 84 | 577 | 0.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `openai/math` | 13900 | 1545 | 4d | Lean | Apache-2.0 |
| `storytold/effectcraft` | 4862 | 2297 | 9d | Rust | Apache-2.0 |
| `Contrastive-LM/CLM` | 2971 | 256 | 17d | Python | Apache-2.0 |
| `storytold/designcraft` | 2761 | 1701 | 9d | Rust | Apache-2.0 |
| `deadinside28/bloodborne_pc` | 2403 | 366 | 9d | C++ | GPL-2.0 |
| `wy51ai/floorplan-3d` | 2144 | 404 | 11d | HTML | MIT |
| `kargulstudio/sales-crm` | 1694 | 372 | 6d | TypeScript | MIT |
| `google-research/rrsi` | 1445 | 140 | 24d | Python | Apache-2.0 |
| `vinnylarouge/jevlike` | 1350 | 117 | 24d | Python | MIT |
| `Lumid-Off/AirCard-Windows` | 1342 | 108 | 22d | Rust | MIT |
| `wangmingxuan666/Tiersense` | 1319 | 218 | 16d | Unknown | — |
| `cloudflare/forge` | 1110 | 45 | 19d | TypeScript | Apache-2.0 |

### Generic-name pattern breakdown

Of 100 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 27 |
| `agent` | 17 |
| `skill` | 17 |
| `skills` | 11 |
| `claude` | 9 |
| `codex` | 5 |
| `llm` | 3 |
| `gpt` | 2 |
| `cookbook` | 2 |
| `vibe` | 2 |
| `demo` | 2 |
| `toolkit` | 1 |
| `prompt` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 521 (52.1%)
- Repos with at least one topic: 479 (47.9%)

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
