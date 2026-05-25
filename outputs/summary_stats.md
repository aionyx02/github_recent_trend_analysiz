# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 482.4 | 228.5 | 51484 |
| forks | 176.0 | 21.0 | 8073 |
| open_issues | 9.6 | 1.0 | 3778 |
| stars_per_day | 41.6 | 17.1 | 1980 |
| age_days | 16.7 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `nexu-io/open-design` | 51484 | 5885 | TypeScript | AI/ML |
| `antirez/ds4` | 11719 | 995 | C | Game |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6474 | 5020 | C++ | Other |
| `freestylefly/awesome-gpt-image-2` | 6422 | 862 | JavaScript | AI/ML |
| `BigPizzaV3/CodexPlusPlus` | 5328 | 346 | Rust | Other |
| `nexu-io/html-anything` | 4845 | 497 | HTML | AI/ML |
| `V4bel/dirtyfrag` | 4754 | 758 | C | Other |
| `vercel-labs/zerolang` | 4476 | 280 | C | AI/ML |
| `denuitt1/mhr-cfw` | 4041 | 399 | Python | Other |
| `darrylmorley/whatcable` | 4018 | 107 | Swift | Mobile |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `nexu-io/open-design` | 1980.2 | 51484 | 26d | AI/ML |
| `antirez/ds4` | 651.1 | 11719 | 18d | Game |
| `perplexityai/bumblebee` | 563.5 | 2254 | 4d | Other |
| `thananon/9arm-skills` | 505.2 | 2021 | 4d | CLI/Tooling |
| `FULU-Foundation/OrcaSlicer-bambulab` | 498.0 | 6474 | 13d | Other |
| `vercel-labs/zerolang` | 497.3 | 4476 | 9d | AI/ML |
| `FoundZiGu/GuJumpgate` | 478.8 | 2394 | 5d | Other |
| `nexu-io/html-anything` | 372.7 | 4845 | 13d | AI/ML |
| `bonus-2026/casino-bonus` | 357.0 | 357 | 1d | Other |
| `open-gsd/get-shit-done-redux` | 309.0 | 618 | 2d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 419 | 400 | 223 | 212 | 44.0 | 15.1 |
| AI/ML | 365 | 598 | 234 | 102 | 40.5 | 5.4 |
| Web | 75 | 341 | 194 | 475 | 26.5 | 3.1 |
| Mobile | 41 | 408 | 219 | 23 | 26.8 | 7.0 |
| CLI/Tooling | 30 | 439 | 238 | 120 | 41.7 | 3.8 |
| Game | 26 | 770 | 268 | 117 | 87.4 | 6.5 |
| Security | 21 | 468 | 263 | 134 | 41.0 | 8.4 |
| DevOps | 12 | 315 | 216 | 240 | 21.2 | 7.4 |
| Data | 11 | 681 | 328 | 85 | 62.6 | 16.5 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.344 |         0.1   |      0.068 |
| forks       |   0.344 |   1     |         0.059 |     -0.102 |
| open_issues |   0.1   |   0.059 |         1     |     -0.026 |
| age_days    |   0.068 |  -0.102 |        -0.026 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.415 |         0.291 |      0.03  |
| forks       |   0.415 |   1     |         0.251 |      0.114 |
| open_issues |   0.291 |   0.251 |         1     |      0.143 |
| age_days    |   0.03  |   0.114 |         0.143 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 55 |
| `ai-agents` | 46 |
| `typescript` | 40 |
| `llm` | 33 |
| `ai` | 30 |
| `claude` | 29 |
| `python` | 29 |
| `mcp` | 29 |
| `codex` | 28 |
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
