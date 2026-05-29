# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 422.3 | 228.0 | 12409 |
| forks | 150.6 | 20.0 | 6863 |
| open_issues | 4.9 | 1.0 | 201 |
| stars_per_day | 39.0 | 17.9 | 1050 |
| age_days | 16.4 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `antirez/ds4` | 12409 | 1057 | C | Game |
| `BigPizzaV3/CodexPlusPlus` | 8132 | 538 | Rust | AI/ML |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6628 | 5082 | C++ | Other |
| `nexu-io/html-anything` | 5343 | 532 | HTML | AI/ML |
| `V4bel/dirtyfrag` | 4787 | 766 | C | Other |
| `darrylmorley/whatcable` | 4749 | 148 | Swift | Mobile |
| `vercel-labs/zerolang` | 4679 | 300 | C | AI/ML |
| `vercel-labs/zero-native` | 4027 | 161 | Zig | Web |
| `theori-io/copy-fail-CVE-2026-31431` | 3916 | 871 | Python | Security |
| `perplexityai/bumblebee` | 3846 | 330 | Go | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `op7418/guizang-social-card-skill` | 1050.0 | 1050 | 1d | AI/ML |
| `antirez/ds4` | 564.0 | 12409 | 22d | Game |
| `perplexityai/bumblebee` | 480.8 | 3846 | 8d | Other |
| `helloianneo/ian-xiaohei-illustrations` | 465.0 | 465 | 1d | AI/ML |
| `withkynam/vibecode-pro-max-kit` | 442.0 | 442 | 1d | AI/ML |
| `alfiyahkamilah1239298/WallpaperDownloader-26` | 399.0 | 399 | 1d | Game |
| `FULU-Foundation/OrcaSlicer-bambulab` | 389.9 | 6628 | 17d | Other |
| `BigPizzaV3/CodexPlusPlus` | 369.6 | 8132 | 22d | AI/ML |
| `vercel-labs/zerolang` | 359.9 | 4679 | 13d | AI/ML |
| `FoundZiGu/GuJumpgate` | 334.7 | 3012 | 9d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 396 | 353 | 211 | 85 | 35.2 | 4.0 |
| AI/ML | 375 | 488 | 243 | 102 | 41.5 | 5.6 |
| Web | 48 | 379 | 208 | 109 | 30.1 | 4.5 |
| Mobile | 35 | 456 | 274 | 27 | 29.6 | 3.7 |
| CLI/Tooling | 33 | 402 | 253 | 112 | 36.1 | 4.5 |
| Game | 33 | 611 | 207 | 44 | 69.2 | 5.8 |
| Finance/Trading | 30 | 293 | 265 | 2076 | 46.3 | 0.8 |
| Security | 26 | 414 | 206 | 109 | 36.8 | 6.8 |
| Data | 14 | 638 | 216 | 77 | 40.0 | 14.9 |
| DevOps | 10 | 360 | 230 | 102 | 63.9 | 8.5 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.153 |         0.566 |      0.123 |
| forks       |   0.153 |   1     |         0.047 |     -0.06  |
| open_issues |   0.566 |   0.047 |         1     |      0.088 |
| age_days    |   0.123 |  -0.06  |         0.088 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.516 |         0.301 |      0.141 |
| forks       |   0.516 |   1     |         0.275 |      0.243 |
| open_issues |   0.301 |   0.275 |         1     |      0.131 |
| age_days    |   0.141 |   0.243 |         0.131 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 56 |
| `ai-agents` | 45 |
| `typescript` | 43 |
| `llm` | 36 |
| `ai` | 31 |
| `python` | 30 |
| `mcp` | 30 |
| `codex` | 30 |
| `claude` | 28 |
| `cli` | 28 |
| `open-source` | 25 |
| `rust` | 20 |
| `ai-agent` | 20 |
| `agent` | 19 |
| `skills` | 19 |
| `anthropic` | 19 |
| `macos` | 18 |
| `trading-bot` | 18 |
| `cursor` | 17 |
| `openai` | 17 |
