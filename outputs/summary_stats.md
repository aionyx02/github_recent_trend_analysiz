# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 643.5 | 290.5 | 34537 |
| forks | 94.7 | 30.0 | 3856 |
| open_issues | 11.1 | 2.0 | 2051 |
| stars_per_day | 58.3 | 21.3 | 2311 |
| age_days | 16.7 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `eternity4719/HowToLiveBetter` | 34537 | 2680 | HTML | Web |
| `NandhaKishorM/laya` | 30048 | 2614 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 21769 | 1544 | Python | AI/ML |
| `lnkiai/m3e-canvas` | 8563 | 902 | TypeScript | Web |
| `jaredpalmer/kev` | 8269 | 531 | Python | Other |
| `tamaratran/fast-jev-compaction` | 7322 | 480 | TypeScript | AI/ML |
| `zai-org/ZCode` | 7317 | 2229 | TypeScript | AI/ML |
| `jev-chat/jev-chat-jarvis` | 7248 | 1220 | Kotlin | AI/ML |
| `robbietilton/Compositor` | 6938 | 708 | Swift | Mobile |
| `mizorewww/laya-mlx` | 6703 | 535 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `NandhaKishorM/laya` | 2311.4 | 30048 | 13d | AI/ML |
| `rehan-remade/universal-modder` | 1803.0 | 1803 | 1d | AI/ML |
| `KKKKhazix/AIHOT` | 1632.3 | 4897 | 3d | AI/ML |
| `browser-use/jev-ultrafast` | 1451.3 | 21769 | 15d | AI/ML |
| `eternity4719/HowToLiveBetter` | 1439.0 | 34537 | 24d | Web |
| `feder-cr/dots` | 1210.0 | 2420 | 2d | AI/ML |
| `nanaism/yomiyasu` | 1126.0 | 1126 | 1d | AI/ML |
| `Niko1221/Strata` | 766.1 | 5363 | 7d | AI/ML |
| `jev-chat/jev-chat-jarvis` | 724.8 | 7248 | 10d | AI/ML |
| `Louis-CFM/coucou` | 680.0 | 2720 | 4d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 418 | 474 | 265 | 83 | 39.5 | 14.9 |
| AI/ML | 362 | 787 | 334 | 105 | 82.9 | 8.3 |
| Mobile | 69 | 576 | 252 | 113 | 44.8 | 9.6 |
| Web | 65 | 1210 | 261 | 114 | 74.7 | 7.4 |
| CLI/Tooling | 19 | 344 | 230 | 41 | 32.8 | 4.7 |
| Data | 18 | 491 | 284 | 138 | 67.0 | 10.8 |
| Finance/Trading | 17 | 703 | 280 | 84 | 52.3 | 6.1 |
| Game | 12 | 510 | 358 | 54 | 49.8 | 22.1 |
| DevOps | 10 | 385 | 182 | 30 | 26.0 | 3.4 |
| Security | 10 | 490 | 354 | 112 | 30.2 | 4.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.541 |         0.081 |      0.004 |
| forks       |   0.541 |   1     |         0.077 |      0.057 |
| open_issues |   0.081 |   0.077 |         1     |      0.026 |
| age_days    |   0.004 |   0.057 |         0.026 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.611 |         0.28  |     -0.001 |
| forks       |   0.611 |   1     |         0.304 |     -0.038 |
| open_issues |   0.28  |   0.304 |         1     |     -0.031 |
| age_days    |  -0.001 |  -0.038 |        -0.031 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 60 |
| `llm` | 54 |
| `ai-agents` | 54 |
| `codex` | 47 |
| `macos` | 39 |
| `jev` | 38 |
| `developer-tools` | 31 |
| `agent-skills` | 30 |
| `awesome-list` | 30 |
| `typescript` | 28 |
| `mcp` | 26 |
| `windows` | 26 |
| `python` | 25 |
| `awesome` | 24 |
| `ai` | 23 |
| `rust` | 22 |
| `typesafe` | 19 |
| `android` | 18 |
| `open-source` | 18 |
| `swift` | 17 |
