# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 467.8 | 218.0 | 54436 |
| forks | 163.1 | 19.0 | 6841 |
| open_issues | 5.3 | 1.0 | 348 |
| stars_per_day | 37.0 | 18.0 | 1877 |
| age_days | 16.4 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `nexu-io/open-design` | 54436 | 6166 | TypeScript | AI/ML |
| `antirez/ds4` | 12265 | 1042 | C | Game |
| `BigPizzaV3/CodexPlusPlus` | 7557 | 498 | Rust | AI/ML |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6605 | 5078 | C++ | Other |
| `nexu-io/html-anything` | 5262 | 527 | HTML | AI/ML |
| `V4bel/dirtyfrag` | 4782 | 765 | C | Other |
| `vercel-labs/zerolang` | 4628 | 295 | C | AI/ML |
| `darrylmorley/whatcable` | 4604 | 137 | Swift | Mobile |
| `vercel-labs/zero-native` | 4020 | 160 | Zig | Web |
| `theori-io/copy-fail-CVE-2026-31431` | 3912 | 869 | Python | Security |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `nexu-io/open-design` | 1877.1 | 54436 | 29d | AI/ML |
| `antirez/ds4` | 584.0 | 12265 | 21d | Game |
| `perplexityai/bumblebee` | 526.4 | 3685 | 7d | Other |
| `op7418/guizang-social-card-skill` | 526.0 | 526 | 1d | AI/ML |
| `FULU-Foundation/OrcaSlicer-bambulab` | 412.8 | 6605 | 16d | Other |
| `vercel-labs/zerolang` | 385.7 | 4628 | 12d | AI/ML |
| `BigPizzaV3/CodexPlusPlus` | 359.9 | 7557 | 21d | AI/ML |
| `FoundZiGu/GuJumpgate` | 358.5 | 2868 | 8d | Other |
| `thananon/9arm-skills` | 352.3 | 2466 | 7d | CLI/Tooling |
| `nexu-io/html-anything` | 328.9 | 5262 | 16d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 392 | 338 | 200 | 103 | 33.7 | 3.9 |
| AI/ML | 376 | 620 | 240 | 117 | 40.3 | 7.0 |
| Web | 49 | 368 | 201 | 106 | 26.6 | 4.4 |
| Mobile | 41 | 428 | 223 | 25 | 28.2 | 4.3 |
| Game | 33 | 624 | 205 | 45 | 56.7 | 6.3 |
| CLI/Tooling | 32 | 486 | 251 | 129 | 39.6 | 3.9 |
| Finance/Trading | 29 | 288 | 261 | 2138 | 52.3 | 0.8 |
| Security | 26 | 409 | 216 | 110 | 29.3 | 6.8 |
| Data | 14 | 613 | 198 | 74 | 41.8 | 14.9 |
| DevOps | 8 | 382 | 338 | 121 | 20.5 | 10.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.316 |         0.7   |      0.092 |
| forks       |   0.316 |   1     |         0.188 |     -0.065 |
| open_issues |   0.7   |   0.188 |         1     |      0.111 |
| age_days    |   0.092 |  -0.065 |         0.111 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.565 |         0.305 |      0.176 |
| forks       |   0.565 |   1     |         0.297 |      0.26  |
| open_issues |   0.305 |   0.297 |         1     |      0.146 |
| age_days    |   0.176 |   0.26  |         0.146 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 54 |
| `ai-agents` | 46 |
| `typescript` | 41 |
| `llm` | 34 |
| `ai` | 31 |
| `python` | 30 |
| `mcp` | 30 |
| `claude` | 29 |
| `cli` | 28 |
| `codex` | 28 |
| `open-source` | 25 |
| `rust` | 20 |
| `ai-agent` | 20 |
| `macos` | 19 |
| `anthropic` | 19 |
| `agent` | 18 |
| `skills` | 18 |
| `developer-tools` | 18 |
| `openai` | 17 |
| `trading-bot` | 17 |
