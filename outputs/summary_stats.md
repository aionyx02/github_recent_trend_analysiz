# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 619.8 | 284.5 | 31439 |
| forks | 91.2 | 29.0 | 3748 |
| open_issues | 10.0 | 1.0 | 2040 |
| stars_per_day | 59.4 | 20.7 | 3858 |
| age_days | 16.3 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `eternity4719/HowToLiveBetter` | 31439 | 2353 | HTML | Web |
| `NandhaKishorM/laya` | 28953 | 2527 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 21500 | 1497 | Python | AI/ML |
| `lnkiai/m3e-canvas` | 8484 | 895 | TypeScript | Web |
| `jaredpalmer/kev` | 8003 | 506 | Python | Other |
| `Human-Agent-Society/reef` | 7348 | 686 | Python | AI/ML |
| `zai-org/ZCode` | 7231 | 2194 | TypeScript | AI/ML |
| `tamaratran/fast-jev-compaction` | 7225 | 463 | TypeScript | AI/ML |
| `jev-chat/jev-chat-jarvis` | 7169 | 1212 | Kotlin | AI/ML |
| `mizorewww/laya-mlx` | 6644 | 522 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `KKKKhazix/AIHOT` | 3858.0 | 3858 | 1d | AI/ML |
| `NandhaKishorM/laya` | 2632.1 | 28953 | 11d | AI/ML |
| `browser-use/jev-ultrafast` | 1653.8 | 21500 | 13d | AI/ML |
| `eternity4719/HowToLiveBetter` | 1429.0 | 31439 | 22d | Web |
| `firelex/jeff` | 1148.0 | 1148 | 1d | Other |
| `feder-cr/dots` | 1026.0 | 1026 | 1d | AI/ML |
| `jev-chat/jev-chat-jarvis` | 896.1 | 7169 | 8d | AI/ML |
| `zai-org/ZCode` | 803.4 | 7231 | 9d | AI/ML |
| `wy51ai/floorplan-3d` | 801.0 | 801 | 1d | Web |
| `jaredpalmer/kev` | 666.9 | 8003 | 12d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 411 | 455 | 262 | 82 | 43.0 | 13.6 |
| AI/ML | 370 | 760 | 327 | 100 | 79.8 | 7.8 |
| Web | 73 | 1064 | 251 | 94 | 78.2 | 6.0 |
| Mobile | 65 | 549 | 253 | 112 | 47.2 | 8.3 |
| Finance/Trading | 18 | 631 | 270 | 75 | 58.8 | 4.0 |
| CLI/Tooling | 16 | 367 | 260 | 39 | 31.8 | 3.9 |
| Data | 16 | 482 | 278 | 149 | 36.8 | 9.9 |
| Game | 12 | 465 | 344 | 51 | 58.6 | 18.3 |
| Security | 10 | 449 | 346 | 103 | 31.5 | 4.3 |
| DevOps | 9 | 395 | 176 | 30 | 32.9 | 3.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.53  |         0.079 |      0.002 |
| forks       |   0.53  |   1     |         0.072 |      0.041 |
| open_issues |   0.079 |   0.072 |         1     |      0.03  |
| age_days    |   0.002 |   0.041 |         0.03  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.608 |         0.304 |      0.022 |
| forks       |   0.608 |   1     |         0.342 |     -0.024 |
| open_issues |   0.304 |   0.342 |         1     |      0.039 |
| age_days    |   0.022 |  -0.024 |         0.039 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 54 |
| `llm` | 53 |
| `claude-code` | 51 |
| `codex` | 42 |
| `jev` | 38 |
| `macos` | 36 |
| `developer-tools` | 31 |
| `awesome-list` | 30 |
| `python` | 28 |
| `mcp` | 28 |
| `typescript` | 28 |
| `agent-skills` | 27 |
| `awesome` | 25 |
| `ai` | 24 |
| `windows` | 23 |
| `apimart` | 20 |
| `rust` | 19 |
| `typesafe` | 19 |
| `ai-agent` | 17 |
| `android` | 16 |
