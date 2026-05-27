# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 478.8 | 225.5 | 53356 |
| forks | 163.8 | 20.0 | 8111 |
| open_issues | 5.8 | 1.0 | 349 |
| stars_per_day | 37.1 | 18.0 | 1906 |
| age_days | 16.7 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `nexu-io/open-design` | 53356 | 6055 | TypeScript | AI/ML |
| `antirez/ds4` | 12049 | 1026 | C | Game |
| `BigPizzaV3/CodexPlusPlus` | 6779 | 444 | Rust | AI/ML |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6568 | 5067 | C++ | Other |
| `nexu-io/html-anything` | 5170 | 515 | HTML | AI/ML |
| `V4bel/dirtyfrag` | 4773 | 763 | C | Other |
| `vercel-labs/zerolang` | 4574 | 291 | C | AI/ML |
| `darrylmorley/whatcable` | 4311 | 124 | Swift | Mobile |
| `denuitt1/mhr-cfw` | 4266 | 431 | Python | Other |
| `vercel-labs/zero-native` | 4010 | 160 | Zig | Web |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `nexu-io/open-design` | 1905.6 | 53356 | 28d | AI/ML |
| `antirez/ds4` | 602.5 | 12049 | 20d | Game |
| `perplexityai/bumblebee` | 556.3 | 3338 | 6d | Other |
| `FULU-Foundation/OrcaSlicer-bambulab` | 437.9 | 6568 | 15d | Other |
| `vercel-labs/zerolang` | 415.8 | 4574 | 11d | AI/ML |
| `thananon/9arm-skills` | 398.0 | 2388 | 6d | CLI/Tooling |
| `FoundZiGu/GuJumpgate` | 394.9 | 2764 | 7d | Other |
| `nexu-io/html-anything` | 344.7 | 5170 | 15d | AI/ML |
| `BigPizzaV3/CodexPlusPlus` | 338.9 | 6779 | 20d | AI/ML |
| `open-gsd/get-shit-done-redux` | 301.2 | 1205 | 4d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 399 | 372 | 211 | 117 | 34.0 | 5.1 |
| AI/ML | 371 | 618 | 238 | 113 | 38.5 | 6.8 |
| Web | 45 | 383 | 205 | 114 | 25.0 | 4.6 |
| Mobile | 40 | 431 | 232 | 24 | 28.2 | 6.3 |
| Finance/Trading | 32 | 278 | 258 | 1832 | 68.2 | 0.5 |
| Game | 32 | 629 | 198 | 46 | 58.2 | 5.8 |
| CLI/Tooling | 31 | 487 | 246 | 130 | 37.7 | 4.0 |
| Security | 27 | 401 | 215 | 106 | 34.9 | 6.5 |
| Data | 14 | 585 | 180 | 71 | 44.0 | 14.2 |
| DevOps | 9 | 374 | 245 | 107 | 21.8 | 9.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.336 |         0.663 |      0.091 |
| forks       |   0.336 |   1     |         0.316 |     -0.061 |
| open_issues |   0.663 |   0.316 |         1     |      0.129 |
| age_days    |   0.091 |  -0.061 |         0.129 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.545 |         0.3   |      0.183 |
| forks       |   0.545 |   1     |         0.296 |      0.23  |
| open_issues |   0.3   |   0.296 |         1     |      0.157 |
| age_days    |   0.183 |   0.23  |         0.157 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 50 |
| `ai-agents` | 43 |
| `typescript` | 41 |
| `ai` | 32 |
| `llm` | 32 |
| `python` | 30 |
| `mcp` | 30 |
| `claude` | 29 |
| `cli` | 28 |
| `open-source` | 27 |
| `codex` | 26 |
| `macos` | 21 |
| `rust` | 21 |
| `trading-bot` | 19 |
| `agent` | 18 |
| `skills` | 17 |
| `anthropic` | 17 |
| `openai` | 16 |
| `windows` | 15 |
| `ai-agent` | 15 |
