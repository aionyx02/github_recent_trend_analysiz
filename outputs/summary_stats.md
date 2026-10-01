# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 630.9 | 287.5 | 32979 |
| forks | 93.6 | 29.0 | 3795 |
| open_issues | 10.8 | 1.0 | 2043 |
| stars_per_day | 60.8 | 21.1 | 2464 |
| age_days | 16.5 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `eternity4719/HowToLiveBetter` | 32979 | 2509 | HTML | Web |
| `NandhaKishorM/laya` | 29570 | 2564 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 21637 | 1520 | Python | AI/ML |
| `lnkiai/m3e-canvas` | 8526 | 898 | TypeScript | Web |
| `jaredpalmer/kev` | 8135 | 518 | Python | Other |
| `tamaratran/fast-jev-compaction` | 7282 | 475 | TypeScript | AI/ML |
| `zai-org/ZCode` | 7271 | 2207 | TypeScript | AI/ML |
| `jev-chat/jev-chat-jarvis` | 7207 | 1214 | Kotlin | AI/ML |
| `robbietilton/Compositor` | 6741 | 690 | Swift | Mobile |
| `mizorewww/laya-mlx` | 6673 | 532 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `NandhaKishorM/laya` | 2464.2 | 29570 | 12d | AI/ML |
| `KKKKhazix/AIHOT` | 2184.5 | 4369 | 2d | AI/ML |
| `feder-cr/dots` | 2110.0 | 2110 | 1d | AI/ML |
| `browser-use/jev-ultrafast` | 1545.5 | 21637 | 14d | AI/ML |
| `eternity4719/HowToLiveBetter` | 1433.9 | 32979 | 23d | Web |
| `rehan-remade/universal-modder` | 1254.0 | 1254 | 1d | AI/ML |
| `wy51ai/floorplan-3d` | 1089.0 | 1089 | 1d | Web |
| `jev-chat/jev-chat-jarvis` | 800.8 | 7207 | 9d | AI/ML |
| `nanaism/yomiyasu` | 797.0 | 797 | 1d | AI/ML |
| `zai-org/ZCode` | 727.1 | 7271 | 10d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 421 | 465 | 258 | 82 | 43.8 | 14.4 |
| AI/ML | 362 | 776 | 333 | 105 | 83.9 | 8.4 |
| Mobile | 67 | 557 | 251 | 112 | 44.0 | 8.5 |
| Web | 66 | 1157 | 258 | 108 | 84.1 | 7.0 |
| CLI/Tooling | 19 | 344 | 227 | 41 | 38.3 | 3.6 |
| Finance/Trading | 17 | 677 | 280 | 81 | 55.7 | 5.0 |
| Data | 16 | 500 | 282 | 152 | 35.5 | 10.5 |
| Game | 12 | 488 | 388 | 53 | 52.6 | 19.8 |
| DevOps | 10 | 382 | 176 | 29 | 28.1 | 2.8 |
| Security | 10 | 475 | 352 | 109 | 31.2 | 4.3 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.534 |         0.085 |     -0.006 |
| forks       |   0.534 |   1     |         0.078 |      0.045 |
| open_issues |   0.085 |   0.078 |         1     |      0.022 |
| age_days    |  -0.006 |   0.045 |         0.022 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.606 |         0.273 |     -0.02  |
| forks       |   0.606 |   1     |         0.325 |     -0.046 |
| open_issues |   0.273 |   0.325 |         1     |     -0.01  |
| age_days    |  -0.02  |  -0.046 |        -0.01  |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 54 |
| `ai-agents` | 52 |
| `llm` | 51 |
| `codex` | 45 |
| `jev` | 38 |
| `macos` | 37 |
| `developer-tools` | 31 |
| `awesome-list` | 30 |
| `mcp` | 28 |
| `typescript` | 28 |
| `agent-skills` | 28 |
| `python` | 26 |
| `awesome` | 25 |
| `windows` | 24 |
| `ai` | 23 |
| `rust` | 20 |
| `typesafe` | 19 |
| `react` | 17 |
| `android` | 17 |
| `open-source` | 17 |
