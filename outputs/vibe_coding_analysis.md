# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-30 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 121 | 12.1% |
| 訊號完整 | 865 | 86.5% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Mantitup-Org/vista` | 2390 | 47 | 25d | **8** | desc:empty, license:none, high-attention-no-desc, low-forks:0.020, topics:none |
| 2 | `Contrastive-LM/CLM` | 2572 | 223 | 6d | **6** | desc:empty, high-attention-no-desc, overnight-surge:429/day, topics:none |
| 3 | `NxcoreAI/NxMem` | 1091 | 107 | 19d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 4 | `Vodiwalker/vodiwalker_panel` | 1003 | 2623 | 19d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 5 | `kajisho5/ffmpeg-skill` | 1437 | 117 | 26d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 6 | `azerioid/azerioid-stack-manager` | 721 | 4 | 28d | **6** | desc:empty, license:none, low-forks:0.006, topics:none |
| 7 | `wy51ai/floorplan-3d` | 801 | 183 | 1d | **5** | desc:empty, license:none, overnight-surge:801/day, topics:none |
| 8 | `inclusionAI/Choruz` | 890 | 9 | 27d | **5** | desc:empty, low-forks:0.010, topics:none |
| 9 | `reladraw/reladraw` | 981 | 17 | 22d | **5** | desc:empty, low-forks:0.017, topics:none |
| 10 | `Taichu-AI/ZDTaichu5.0-9B` | 1935 | 359 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 11 | `Lumid-Off/AirCard-Windows` | 1060 | 74 | 11d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `anthropics/fermats-last-theorem` | 1243 | 106 | 25d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `vinnylarouge/jevlike` | 1335 | 118 | 13d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `Edge0-AI/Edge0` | 2142 | 192 | 21d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 15 | `leoliu0/ratex` | 172 | 3 | 13d | **4** | desc:empty, license:none, topics:none |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 110 | 11.0% |
| description <20 chars | 21 | 2.1% |
| no license | 299 | 29.9% |
| high-attention no-desc (stars>1k + empty desc) | 10 | 1.0% |
| low fork ratio (stars>500 + fsr<0.02) | 19 | 1.9% |
| overnight surge (>300 spd + <7 days) | 17 | 1.7% |
| generic-AI-buzzword name | 119 | 11.9% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| TypeScript | 3 |
| Rust | 2 |
| PHP | 1 |
| HTML | 1 |
| Lean | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 3 | 0 | 0 | 3 | 0.0% |
| 5000-9999 | 10 | 0 | 0 | 10 | 0.0% |
| 1000-4999 | 92 | 10 | 3 | 79 | 10.9% |
| 500-999 | 159 | 4 | 24 | 131 | 2.5% |
| 100-499 | 736 | 0 | 94 | 642 | 0.0% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `Contrastive-LM/CLM` | 2572 | 223 | 6d | Python | Apache-2.0 |
| `Mantitup-Org/vista` | 2390 | 47 | 25d | TypeScript | — |
| `Edge0-AI/Edge0` | 2142 | 192 | 21d | Python | Apache-2.0 |
| `Taichu-AI/ZDTaichu5.0-9B` | 1935 | 359 | 25d | Python | Apache-2.0 |
| `kajisho5/ffmpeg-skill` | 1437 | 117 | 26d | Python | MIT |
| `vinnylarouge/jevlike` | 1335 | 118 | 13d | Python | MIT |
| `anthropics/fermats-last-theorem` | 1243 | 106 | 25d | Lean | Apache-2.0 |
| `NxcoreAI/NxMem` | 1091 | 107 | 19d | TypeScript | — |
| `Lumid-Off/AirCard-Windows` | 1060 | 74 | 11d | Rust | MIT |
| `Vodiwalker/vodiwalker_panel` | 1003 | 2623 | 19d | Python | — |

### Generic-name pattern breakdown

Of 119 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `awesome` | 34 |
| `skill` | 22 |
| `agent` | 20 |
| `skills` | 10 |
| `codex` | 7 |
| `gpt` | 6 |
| `claude` | 6 |
| `llm` | 5 |
| `agents` | 2 |
| `prompt` | 2 |
| `toolkit` | 1 |
| `vibe` | 1 |
| `demo` | 1 |
| `cookbook` | 1 |
| `playground` | 1 |

### Topics coverage

- Repos with **zero topics**: 565 (56.5%)
- Repos with at least one topic: 435 (43.5%)

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
