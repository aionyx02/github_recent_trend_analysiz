# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 476.2 | 216.0 | 52524 |
| forks | 155.8 | 21.0 | 8115 |
| open_issues | 10.6 | 1.0 | 4579 |
| stars_per_day | 35.3 | 15.9 | 1945 |
| age_days | 17.3 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `nexu-io/open-design` | 52524 | 5973 | TypeScript | AI/ML |
| `antirez/ds4` | 11906 | 1017 | C | Game |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6532 | 5050 | C++ | Other |
| `BigPizzaV3/CodexPlusPlus` | 6039 | 399 | Rust | AI/ML |
| `nexu-io/html-anything` | 5025 | 503 | HTML | AI/ML |
| `V4bel/dirtyfrag` | 4766 | 760 | C | Other |
| `vercel-labs/zerolang` | 4532 | 288 | C | AI/ML |
| `denuitt1/mhr-cfw` | 4226 | 425 | Python | Other |
| `darrylmorley/whatcable` | 4056 | 108 | Swift | Mobile |
| `vercel-labs/zero-native` | 4001 | 158 | Zig | Web |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `nexu-io/open-design` | 1945.3 | 52524 | 27d | AI/ML |
| `joeseesun/wechat-radar` | 1137.0 | 1137 | 1d | Other |
| `antirez/ds4` | 626.6 | 11906 | 19d | Game |
| `perplexityai/bumblebee` | 546.2 | 2731 | 5d | Other |
| `FULU-Foundation/OrcaSlicer-bambulab` | 466.6 | 6532 | 14d | Other |
| `thananon/9arm-skills` | 458.8 | 2294 | 5d | CLI/Tooling |
| `vercel-labs/zerolang` | 453.2 | 4532 | 10d | AI/ML |
| `FoundZiGu/GuJumpgate` | 440.5 | 2643 | 6d | Other |
| `nexu-io/html-anything` | 358.9 | 5025 | 14d | AI/ML |
| `BigPizzaV3/CodexPlusPlus` | 317.8 | 6039 | 19d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 395 | 590 | 223 | 96 | 36.6 | 6.5 |
| Other | 380 | 381 | 206 | 123 | 33.7 | 17.8 |
| Web | 52 | 382 | 183 | 101 | 25.0 | 4.3 |
| Mobile | 47 | 375 | 196 | 23 | 25.2 | 5.3 |
| CLI/Tooling | 31 | 445 | 239 | 122 | 38.1 | 4.0 |
| Finance/Trading | 30 | 262 | 243 | 1831 | 54.6 | 0.5 |
| Game | 23 | 803 | 215 | 61 | 61.0 | 7.7 |
| Security | 22 | 450 | 214 | 130 | 29.2 | 7.8 |
| Data | 10 | 740 | 332 | 98 | 49.7 | 18.9 |
| DevOps | 10 | 337 | 204 | 96 | 16.7 | 8.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.359 |         0.087 |      0.074 |
| forks       |   0.359 |   1     |         0.054 |     -0.095 |
| open_issues |   0.087 |   0.054 |         1     |     -0.031 |
| age_days    |   0.074 |  -0.095 |        -0.031 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.549 |         0.306 |      0.094 |
| forks       |   0.549 |   1     |         0.245 |      0.102 |
| open_issues |   0.306 |   0.245 |         1     |      0.093 |
| age_days    |   0.094 |   0.102 |         0.093 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 58 |
| `ai-agents` | 49 |
| `typescript` | 38 |
| `llm` | 36 |
| `ai` | 34 |
| `codex` | 32 |
| `claude` | 31 |
| `python` | 31 |
| `mcp` | 31 |
| `cli` | 27 |
| `open-source` | 26 |
| `macos` | 22 |
| `rust` | 22 |
| `skills` | 20 |
| `ai-agent` | 20 |
| `trading-bot` | 20 |
| `agent` | 19 |
| `anthropic` | 18 |
| `developer-tools` | 18 |
| `openai` | 16 |
