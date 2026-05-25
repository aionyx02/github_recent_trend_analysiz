# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 481.2 | 227.0 | 51422 |
| forks | 175.3 | 21.0 | 8074 |
| open_issues | 9.5 | 1.0 | 3742 |
| stars_per_day | 41.3 | 16.9 | 1978 |
| age_days | 16.7 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `nexu-io/open-design` | 51422 | 5878 | TypeScript | AI/ML |
| `antirez/ds4` | 11711 | 995 | C | Game |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6471 | 5017 | C++ | Other |
| `freestylefly/awesome-gpt-image-2` | 6408 | 861 | JavaScript | AI/ML |
| `BigPizzaV3/CodexPlusPlus` | 5246 | 341 | Rust | Other |
| `nexu-io/html-anything` | 4830 | 497 | HTML | AI/ML |
| `V4bel/dirtyfrag` | 4753 | 758 | C | Other |
| `vercel-labs/zerolang` | 4470 | 280 | C | AI/ML |
| `denuitt1/mhr-cfw` | 4038 | 399 | Python | Other |
| `darrylmorley/whatcable` | 4018 | 107 | Swift | Mobile |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `nexu-io/open-design` | 1977.8 | 51422 | 26d | AI/ML |
| `antirez/ds4` | 650.6 | 11711 | 18d | Game |
| `perplexityai/bumblebee` | 558.2 | 2233 | 4d | Other |
| `thananon/9arm-skills` | 502.2 | 2009 | 4d | CLI/Tooling |
| `FULU-Foundation/OrcaSlicer-bambulab` | 497.8 | 6471 | 13d | Other |
| `vercel-labs/zerolang` | 496.7 | 4470 | 9d | AI/ML |
| `FoundZiGu/GuJumpgate` | 476.4 | 2382 | 5d | Other |
| `nexu-io/html-anything` | 371.5 | 4830 | 13d | AI/ML |
| `bonus-2026/casino-bonus` | 357.0 | 357 | 1d | Other |
| `open-gsd/get-shit-done-redux` | 302.0 | 604 | 2d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 420 | 398 | 220 | 211 | 43.5 | 15.0 |
| AI/ML | 365 | 597 | 234 | 102 | 40.3 | 5.4 |
| Web | 74 | 344 | 198 | 479 | 26.7 | 3.2 |
| Mobile | 41 | 408 | 218 | 23 | 26.8 | 6.9 |
| CLI/Tooling | 30 | 438 | 238 | 120 | 41.6 | 3.8 |
| Game | 26 | 768 | 268 | 117 | 86.6 | 6.4 |
| Security | 21 | 468 | 259 | 134 | 40.7 | 8.4 |
| DevOps | 12 | 315 | 216 | 232 | 21.2 | 7.6 |
| Data | 11 | 678 | 327 | 85 | 62.4 | 16.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.345 |         0.1   |      0.068 |
| forks       |   0.345 |   1     |         0.059 |     -0.102 |
| open_issues |   0.1   |   0.059 |         1     |     -0.027 |
| age_days    |   0.068 |  -0.102 |        -0.027 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.412 |         0.292 |      0.03  |
| forks       |   0.412 |   1     |         0.253 |      0.114 |
| open_issues |   0.292 |   0.253 |         1     |      0.135 |
| age_days    |   0.03  |   0.114 |         0.135 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 56 |
| `ai-agents` | 46 |
| `typescript` | 40 |
| `llm` | 33 |
| `mcp` | 30 |
| `claude` | 29 |
| `python` | 29 |
| `ai` | 29 |
| `codex` | 29 |
| `open-source` | 26 |
| `cli` | 25 |
| `bot` | 23 |
| `macos` | 21 |
| `rust` | 20 |
| `nodejs` | 19 |
| `trading-bot` | 19 |
| `skills` | 18 |
| `agent` | 18 |
| `ai-agent` | 18 |
| `polymarket` | 18 |
