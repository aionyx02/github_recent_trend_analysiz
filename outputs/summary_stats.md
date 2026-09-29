# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 590.6 | 268.0 | 28166 |
| forks | 89.2 | 28.0 | 3636 |
| open_issues | 10.2 | 1.0 | 2030 |
| stars_per_day | 57.0 | 20.2 | 2817 |
| age_days | 16.1 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `NandhaKishorM/laya` | 28166 | 2455 | Python | AI/ML |
| `eternity4719/HowToLiveBetter` | 26512 | 2011 | HTML | Web |
| `browser-use/jev-ultrafast` | 21297 | 1480 | Python | AI/ML |
| `lnkiai/m3e-canvas` | 8439 | 891 | TypeScript | Web |
| `jaredpalmer/kev` | 7797 | 489 | Python | Other |
| `Human-Agent-Society/reef` | 7211 | 686 | Python | AI/ML |
| `tamaratran/fast-jev-compaction` | 7170 | 454 | TypeScript | AI/ML |
| `zai-org/ZCode` | 7137 | 2161 | TypeScript | AI/ML |
| `jev-chat/jev-chat-jarvis` | 7069 | 1200 | Kotlin | AI/ML |
| `mizorewww/laya-mlx` | 6612 | 518 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `NandhaKishorM/laya` | 2816.6 | 28166 | 10d | AI/ML |
| `KKKKhazix/AIHOT` | 2442.0 | 2442 | 1d | AI/ML |
| `browser-use/jev-ultrafast` | 1774.8 | 21297 | 12d | AI/ML |
| `eternity4719/HowToLiveBetter` | 1262.5 | 26512 | 21d | Web |
| `jev-chat/jev-chat-jarvis` | 1009.9 | 7069 | 7d | AI/ML |
| `zai-org/ZCode` | 892.1 | 7137 | 8d | AI/ML |
| `firelex/jeff` | 846.0 | 846 | 1d | Other |
| `yihui-dev/awesome-opus5-5-videos` | 845.0 | 845 | 1d | AI/ML |
| `dzhng/jevgrep` | 817.5 | 1635 | 2d | AI/ML |
| `mizorewww/laya-mlx` | 734.7 | 6612 | 9d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 401 | 444 | 245 | 84 | 39.7 | 14.5 |
| AI/ML | 375 | 723 | 309 | 96 | 77.1 | 7.9 |
| Web | 72 | 975 | 252 | 87 | 69.7 | 4.9 |
| Mobile | 67 | 511 | 243 | 105 | 46.3 | 6.9 |
| CLI/Tooling | 18 | 321 | 216 | 35 | 34.4 | 3.4 |
| Finance/Trading | 18 | 613 | 267 | 72 | 70.0 | 5.8 |
| Data | 17 | 453 | 275 | 148 | 45.5 | 8.9 |
| Game | 12 | 415 | 302 | 48 | 62.6 | 16.1 |
| DevOps | 10 | 360 | 158 | 26 | 32.6 | 3.3 |
| Security | 10 | 357 | 338 | 82 | 25.8 | 3.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.518 |         0.097 |     -0.006 |
| forks       |   0.518 |   1     |         0.086 |      0.03  |
| open_issues |   0.097 |   0.086 |         1     |      0.032 |
| age_days    |  -0.006 |   0.03  |         0.032 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.583 |         0.307 |      0.026 |
| forks       |   0.583 |   1     |         0.334 |     -0.052 |
| open_issues |   0.307 |   0.334 |         1     |      0.043 |
| age_days    |   0.026 |  -0.052 |         0.043 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 54 |
| `ai-agents` | 51 |
| `claude-code` | 48 |
| `codex` | 43 |
| `jev` | 38 |
| `macos` | 37 |
| `developer-tools` | 31 |
| `awesome-list` | 30 |
| `python` | 28 |
| `mcp` | 27 |
| `agent-skills` | 27 |
| `typescript` | 25 |
| `awesome` | 25 |
| `windows` | 23 |
| `ai` | 22 |
| `apimart` | 20 |
| `typesafe` | 19 |
| `rust` | 17 |
| `swift` | 17 |
| `ai-agent` | 17 |
