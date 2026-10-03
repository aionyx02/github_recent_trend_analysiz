# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 636.7 | 283.5 | 36396 |
| forks | 94.4 | 29.0 | 3894 |
| open_issues | 11.8 | 2.0 | 2046 |
| stars_per_day | 53.4 | 20.6 | 2166 |
| age_days | 16.9 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `eternity4719/HowToLiveBetter` | 36396 | 2841 | HTML | Web |
| `NandhaKishorM/laya` | 30325 | 2643 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 21853 | 1553 | Python | AI/ML |
| `jaredpalmer/kev` | 8343 | 542 | Python | Other |
| `Niko1221/Strata` | 7393 | 649 | C++ | AI/ML |
| `zai-org/ZCode` | 7356 | 2242 | TypeScript | AI/ML |
| `tamaratran/fast-jev-compaction` | 7345 | 483 | TypeScript | AI/ML |
| `jev-chat/jev-chat-jarvis` | 7280 | 1220 | Kotlin | AI/ML |
| `robbietilton/Compositor` | 7139 | 723 | Swift | Mobile |
| `mizorewww/laya-mlx` | 6728 | 536 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `NandhaKishorM/laya` | 2166.1 | 30325 | 14d | AI/ML |
| `eternity4719/HowToLiveBetter` | 1455.8 | 36396 | 25d | Web |
| `browser-use/jev-ultrafast` | 1365.8 | 21853 | 16d | AI/ML |
| `KKKKhazix/AIHOT` | 1276.8 | 5107 | 4d | AI/ML |
| `rehan-remade/universal-modder` | 1178.5 | 2357 | 2d | AI/ML |
| `Niko1221/Strata` | 924.1 | 7393 | 8d | AI/ML |
| `feder-cr/dots` | 855.3 | 2566 | 3d | AI/ML |
| `jev-chat/jev-chat-jarvis` | 661.8 | 7280 | 11d | AI/ML |
| `nanaism/yomiyasu` | 624.0 | 1248 | 2d | AI/ML |
| `Louis-CFM/coucou` | 622.8 | 3114 | 5d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 407 | 486 | 267 | 83 | 37.3 | 16.4 |
| AI/ML | 365 | 778 | 323 | 106 | 73.3 | 8.6 |
| Mobile | 74 | 573 | 250 | 109 | 45.2 | 9.9 |
| Web | 67 | 1034 | 244 | 105 | 67.5 | 7.0 |
| Data | 20 | 490 | 290 | 127 | 57.0 | 10.4 |
| CLI/Tooling | 19 | 352 | 233 | 41 | 29.4 | 4.7 |
| Finance/Trading | 16 | 723 | 272 | 84 | 50.7 | 7.1 |
| Game | 11 | 569 | 365 | 60 | 50.4 | 25.1 |
| Security | 11 | 467 | 313 | 102 | 26.9 | 4.5 |
| DevOps | 10 | 388 | 186 | 30 | 24.3 | 3.6 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.547 |         0.075 |      0     |
| forks       |   0.547 |   1     |         0.078 |      0.06  |
| open_issues |   0.075 |   0.078 |         1     |      0.028 |
| age_days    |   0     |   0.06  |         0.028 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.604 |         0.298 |     -0.008 |
| forks       |   0.604 |   1     |         0.303 |     -0.043 |
| open_issues |   0.298 |   0.303 |         1     |     -0.027 |
| age_days    |  -0.008 |  -0.043 |        -0.027 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 60 |
| `llm` | 56 |
| `ai-agents` | 52 |
| `codex` | 48 |
| `macos` | 41 |
| `jev` | 40 |
| `awesome-list` | 30 |
| `developer-tools` | 30 |
| `agent-skills` | 30 |
| `python` | 28 |
| `mcp` | 26 |
| `typescript` | 26 |
| `windows` | 26 |
| `ai` | 25 |
| `awesome` | 24 |
| `rust` | 22 |
| `typesafe` | 19 |
| `android` | 18 |
| `open-source` | 17 |
| `swift` | 17 |
