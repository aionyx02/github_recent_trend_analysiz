# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 486.4 | 231.5 | 51684 |
| forks | 178.5 | 21.0 | 8078 |
| open_issues | 9.8 | 1.0 | 3892 |
| stars_per_day | 42.5 | 17.3 | 1988 |
| age_days | 16.6 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `nexu-io/open-design` | 51684 | 5910 | TypeScript | AI/ML |
| `antirez/ds4` | 11766 | 1000 | C | Game |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6479 | 5025 | C++ | Other |
| `freestylefly/awesome-gpt-image-2` | 6453 | 864 | JavaScript | AI/ML |
| `BigPizzaV3/CodexPlusPlus` | 5484 | 357 | Rust | AI/ML |
| `nexu-io/html-anything` | 4889 | 498 | HTML | AI/ML |
| `V4bel/dirtyfrag` | 4758 | 758 | C | Other |
| `vercel-labs/zerolang` | 4482 | 283 | C | AI/ML |
| `denuitt1/mhr-cfw` | 4056 | 400 | Python | Other |
| `darrylmorley/whatcable` | 4024 | 107 | Swift | Mobile |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `nexu-io/open-design` | 1987.8 | 51684 | 26d | AI/ML |
| `antirez/ds4` | 653.7 | 11766 | 18d | Game |
| `perplexityai/bumblebee` | 585.2 | 2341 | 4d | Other |
| `thananon/9arm-skills` | 512.0 | 2048 | 4d | CLI/Tooling |
| `FULU-Foundation/OrcaSlicer-bambulab` | 498.4 | 6479 | 13d | Other |
| `vercel-labs/zerolang` | 498.0 | 4482 | 9d | AI/ML |
| `FoundZiGu/GuJumpgate` | 491.6 | 2458 | 5d | Other |
| `nexu-io/html-anything` | 376.1 | 4889 | 13d | AI/ML |
| `bonus-2026/casino-bonus` | 357.0 | 357 | 1d | Finance/Trading |
| `open-gsd/get-shit-done-redux` | 344.0 | 688 | 2d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 390 | 608 | 234 | 107 | 42.0 | 6.2 |
| Other | 374 | 396 | 230 | 110 | 42.2 | 16.2 |
| Web | 51 | 393 | 215 | 105 | 28.2 | 4.2 |
| Finance/Trading | 45 | 223 | 196 | 1774 | 53.7 | 0.7 |
| Mobile | 41 | 411 | 221 | 23 | 27.2 | 7.0 |
| CLI/Tooling | 30 | 442 | 240 | 120 | 42.1 | 3.9 |
| Game | 25 | 795 | 279 | 56 | 92.9 | 6.8 |
| Security | 22 | 455 | 252 | 129 | 40.4 | 7.9 |
| Data | 11 | 688 | 331 | 86 | 63.1 | 17.0 |
| DevOps | 11 | 325 | 214 | 89 | 16.6 | 7.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.34  |         0.104 |      0.069 |
| forks       |   0.34  |   1     |         0.059 |     -0.104 |
| open_issues |   0.104 |   0.059 |         1     |     -0.026 |
| age_days    |   0.069 |  -0.104 |        -0.026 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.411 |         0.287 |      0.029 |
| forks       |   0.411 |   1     |         0.244 |      0.115 |
| open_issues |   0.287 |   0.244 |         1     |      0.135 |
| age_days    |   0.029 |   0.115 |         0.135 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 55 |
| `ai-agents` | 46 |
| `typescript` | 41 |
| `llm` | 34 |
| `claude` | 31 |
| `ai` | 30 |
| `mcp` | 30 |
| `python` | 29 |
| `codex` | 28 |
| `open-source` | 26 |
| `cli` | 25 |
| `bot` | 23 |
| `macos` | 21 |
| `rust` | 21 |
| `trading-bot` | 19 |
| `ai-agent` | 19 |
| `nodejs` | 19 |
| `trading` | 18 |
| `polymarket` | 18 |
| `agent` | 18 |
