# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 574.3 | 257.0 | 25218 |
| forks | 84.6 | 28.0 | 3270 |
| open_issues | 10.9 | 1.0 | 2017 |
| stars_per_day | 57.5 | 20.6 | 3603 |
| age_days | 16.1 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `NandhaKishorM/laya` | 25218 | 2189 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 20392 | 1392 | Python | AI/ML |
| `eternity4719/HowToLiveBetter` | 17070 | 1178 | HTML | Web |
| `lnkiai/m3e-canvas` | 8259 | 865 | TypeScript | Web |
| `jaredpalmer/kev` | 7121 | 421 | Python | Other |
| `tamaratran/fast-jev-compaction` | 6905 | 419 | TypeScript | AI/ML |
| `zai-org/ZCode` | 6810 | 2048 | TypeScript | AI/ML |
| `rakanki911/DLSS5-Swapper` | 6775 | 355 | JavaScript | Game |
| `XiaoDuoYa/codex-with-chatgpt` | 6684 | 603 | TypeScript | AI/ML |
| `jev-chat/jev-chat-jarvis` | 6605 | 1140 | Kotlin | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `NandhaKishorM/laya` | 3602.6 | 25218 | 7d | AI/ML |
| `browser-use/jev-ultrafast` | 2265.8 | 20392 | 9d | AI/ML |
| `jev-chat/jev-chat-jarvis` | 1651.2 | 6605 | 4d | AI/ML |
| `zai-org/ZCode` | 1362.0 | 6810 | 5d | AI/ML |
| `tobi/disktree` | 1100.0 | 1100 | 1d | Other |
| `mizorewww/laya-mlx` | 1065.0 | 6390 | 6d | AI/ML |
| `eternity4719/HowToLiveBetter` | 948.3 | 17070 | 18d | Web |
| `jaredpalmer/kev` | 890.1 | 7121 | 8d | Other |
| `tamaratran/fast-jev-compaction` | 863.1 | 6905 | 8d | AI/ML |
| `Contrastive-LM/CLM` | 693.0 | 1386 | 2d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 411 | 449 | 239 | 80 | 41.2 | 16.6 |
| AI/ML | 375 | 700 | 292 | 91 | 77.6 | 7.1 |
| Web | 66 | 822 | 258 | 80 | 62.5 | 4.1 |
| Mobile | 60 | 529 | 242 | 103 | 48.7 | 10.3 |
| CLI/Tooling | 21 | 275 | 212 | 25 | 34.8 | 1.6 |
| Finance/Trading | 18 | 598 | 246 | 72 | 73.8 | 3.9 |
| Data | 16 | 461 | 269 | 148 | 51.6 | 8.7 |
| DevOps | 12 | 286 | 188 | 25 | 35.2 | 3.2 |
| Game | 11 | 959 | 239 | 60 | 68.2 | 15.5 |
| Security | 10 | 320 | 251 | 71 | 29.5 | 3.3 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.498 |         0.1   |     -0.009 |
| forks       |   0.498 |   1     |         0.085 |      0.001 |
| open_issues |   0.1   |   0.085 |         1     |      0.02  |
| age_days    |  -0.009 |   0.001 |         0.02  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.575 |         0.308 |      0.012 |
| forks       |   0.575 |   1     |         0.334 |     -0.057 |
| open_issues |   0.308 |   0.334 |         1     |      0.026 |
| age_days    |   0.012 |  -0.057 |         0.026 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 59 |
| `ai-agents` | 55 |
| `claude-code` | 53 |
| `codex` | 44 |
| `macos` | 40 |
| `jev` | 37 |
| `developer-tools` | 34 |
| `mcp` | 31 |
| `python` | 29 |
| `agent-skills` | 28 |
| `awesome-list` | 28 |
| `ai` | 25 |
| `typescript` | 25 |
| `awesome` | 25 |
| `windows` | 24 |
| `rust` | 22 |
| `ai-agent` | 20 |
| `swift` | 19 |
| `typesafe` | 19 |
| `open-source` | 18 |
