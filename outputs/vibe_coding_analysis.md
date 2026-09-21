# 公開 Metadata 完整度分析 (Metadata Completeness Risk Score)

_Generated: 2026-09-21 | Sample size: 1000 repos (with topics signal)_

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
| 待檢視 | 140 | 14.0% |
| 訊號完整 | 843 | 84.3% |

### Top 15 highest-scoring repos

| Rank | Repo | Stars | Forks | Age | Score | Reasons |
|---:|---|---:|---:|---:|---:|---|
| 1 | `Mantitup-Org/vista` | 2377 | 36 | 16d | **8** | desc:empty, license:none, high-attention-no-desc, low-forks:0.015, topics:none |
| 2 | `FireRedTeam/FireRedAudio` | 2002 | 18 | 29d | **7** | desc:empty, high-attention-no-desc, low-forks:0.009, topics:none |
| 3 | `FjordWorkerShanty/Microsoft-Activation-Script` | 1586 | 0 | 22d | **7** | desc:empty, license:none, high-attention-no-desc, low-forks:0.000 |
| 4 | `NandhaKishorM/laya` | 7492 | 637 | 2d | **6** | desc:empty, high-attention-no-desc, overnight-surge:3746/day, topics:none |
| 5 | `HEJustinSun/my-girlfriend-jingtian-latex` | 4206 | 636 | 24d | **6** | desc:empty, license:none, high-attention-no-desc, topics:none |
| 6 | `kajisho5/ffmpeg-skill` | 1335 | 99 | 17d | **6** | desc:empty, high-attention-no-desc, generic-name:ffmpeg-skill, topics:none |
| 7 | `Faizpi/bank-sampah` | 647 | 1 | 9d | **6** | desc:empty, license:none, low-forks:0.002, topics:none |
| 8 | `azerioid/azerioid-stack-manager` | 516 | 1 | 19d | **6** | desc:empty, license:none, low-forks:0.002, topics:none |
| 9 | `rizqinrr/viserys-agent` | 693 | 10 | 8d | **6** | desc:empty, low-forks:0.014, generic-name:viserys-agent, topics:none |
| 10 | `cheng-haha/GPT-Policy` | 241 | 4 | 10d | **5** | desc:empty, license:none, generic-name:GPT-Policy, topics:none |
| 11 | `Edge0-AI/Edge0` | 2035 | 178 | 12d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 12 | `anthropics/fermats-last-theorem` | 1207 | 103 | 16d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 13 | `vinnylarouge/jevlike` | 1144 | 99 | 4d | **5** | desc:empty, high-attention-no-desc, topics:none |
| 14 | `inclusionAI/Choruz` | 779 | 9 | 18d | **5** | desc:empty, low-forks:0.012, topics:none |
| 15 | `v-modal/awesome-jev-tools` | 605 | 8 | 1d | **5** | license:none, low-forks:0.013, overnight-surge:605/day, generic-name:awesome-jev-tools |

### Signal frequency (independent of tier)

| Signal | Count | % |
|---|---:|---:|
| description empty | 124 | 12.4% |
| description <20 chars | 24 | 2.4% |
| no license | 295 | 29.5% |
| high-attention no-desc (stars>1k + empty desc) | 10 | 1.0% |
| low fork ratio (stars>500 + fsr<0.02) | 21 | 2.1% |
| overnight surge (>300 spd + <7 days) | 23 | 2.3% |
| generic-AI-buzzword name | 112 | 11.2% |

### 低資訊密度 tier — by primary language

| Language | Repos in 低資訊密度 tier |
|---|---:|
| Python | 6 |
| Unknown | 2 |
| PHP | 2 |
| Rust | 2 |
| TypeScript | 1 |
| TeX | 1 |
| JavaScript | 1 |
| Lean | 1 |
| PowerShell | 1 |

### 低資訊密度 concentration by stars bucket

Where in the popularity distribution does the low-metadata cohort cluster?

| Stars bucket | Total | 低資訊密度 | 待檢視 | 訊號完整 | 低資訊密度 % |
|---|---:|---:|---:|---:|---:|
| ≥10000 | 2 | 0 | 1 | 1 | 0.0% |
| 5000-9999 | 6 | 1 | 0 | 5 | 16.7% |
| 1000-4999 | 88 | 9 | 3 | 76 | 10.2% |
| 500-999 | 133 | 6 | 23 | 104 | 4.5% |
| 100-499 | 771 | 1 | 113 | 657 | 0.1% |

### High-attention no-description zoom (stars > 1000 + empty description)

These are the most visible high-attention low-metadata artifacts —
high stars with zero description text.

| Repo | Stars | Forks | Age | Language | License |
|---|---:|---:|---:|---|---|
| `NandhaKishorM/laya` | 7492 | 637 | 2d | Python | Apache-2.0 |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 4206 | 636 | 24d | TeX | — |
| `tobi/walgit` | 2541 | 155 | 28d | Rust | MIT |
| `Mantitup-Org/vista` | 2377 | 36 | 16d | TypeScript | — |
| `Edge0-AI/Edge0` | 2035 | 178 | 12d | Python | Apache-2.0 |
| `FireRedTeam/FireRedAudio` | 2002 | 18 | 29d | Python | Apache-2.0 |
| `FjordWorkerShanty/Microsoft-Activation-Script` | 1586 | 0 | 22d | Unknown | — |
| `kajisho5/ffmpeg-skill` | 1335 | 99 | 17d | Python | MIT |
| `anthropics/fermats-last-theorem` | 1207 | 103 | 16d | Lean | Apache-2.0 |
| `vinnylarouge/jevlike` | 1144 | 99 | 4d | Python | MIT |

### Generic-name pattern breakdown

Of 112 repos with a generic-AI-buzzword token in the name, the token distribution is:

| Token | Repos |
|---|---:|
| `skill` | 27 |
| `awesome` | 22 |
| `agent` | 20 |
| `skills` | 10 |
| `gpt` | 8 |
| `codex` | 7 |
| `claude` | 6 |
| `toolkit` | 2 |
| `agents` | 2 |
| `prompt` | 2 |
| `llm` | 2 |
| `demo` | 1 |
| `vibe` | 1 |
| `starter` | 1 |
| `cookbook` | 1 |

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
