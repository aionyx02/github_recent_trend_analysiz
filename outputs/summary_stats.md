# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 674.1 | 295.0 | 42722 |
| forks | 91.7 | 31.0 | 4046 |
| open_issues | 13.2 | 2.0 | 2055 |
| stars_per_day | 55.9 | 20.7 | 1929 |
| age_days | 17.2 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `eternity4719/HowToLiveBetter` | 42722 | 3368 | HTML | Web |
| `NandhaKishorM/laya` | 30862 | 2719 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 22065 | 1586 | Python | AI/ML |
| `Niko1221/Strata` | 12879 | 1084 | C++ | AI/ML |
| `jaredpalmer/kev` | 8479 | 559 | Python | Other |
| `robbietilton/Compositor` | 8113 | 812 | Swift | Mobile |
| `cdyforever/how-to-live-better` | 7643 | 514 | HTML | Web |
| `zai-org/ZCode` | 7428 | 2264 | TypeScript | AI/ML |
| `tamaratran/fast-jev-compaction` | 7408 | 501 | TypeScript | AI/ML |
| `jev-chat/jev-chat-jarvis` | 7355 | 1224 | Kotlin | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `NandhaKishorM/laya` | 1928.9 | 30862 | 16d | AI/ML |
| `eternity4719/HowToLiveBetter` | 1582.3 | 42722 | 27d | Web |
| `Niko1221/Strata` | 1287.9 | 12879 | 10d | AI/ML |
| `kargulstudio/sales-crm` | 1274.0 | 1274 | 1d | Other |
| `browser-use/jev-ultrafast` | 1225.8 | 22065 | 18d | AI/ML |
| `KKKKhazix/AIHOT` | 989.3 | 5936 | 6d | AI/ML |
| `rehan-remade/universal-modder` | 897.0 | 3588 | 4d | AI/ML |
| `CopilotKit/OpenDots` | 694.4 | 3472 | 5d | AI/ML |
| `QingYunA/answer-me-with-html` | 689.5 | 1379 | 2d | AI/ML |
| `facebookincubator/muse-gadget-sdk` | 672.5 | 1345 | 2d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 409 | 486 | 276 | 69 | 41.0 | 18.1 |
| AI/ML | 368 | 820 | 334 | 107 | 73.5 | 9.8 |
| Mobile | 74 | 672 | 258 | 123 | 55.7 | 14.0 |
| Web | 65 | 1208 | 270 | 126 | 72.1 | 6.5 |
| CLI/Tooling | 21 | 373 | 237 | 46 | 30.3 | 5.0 |
| Data | 18 | 539 | 300 | 142 | 47.0 | 9.9 |
| Finance/Trading | 14 | 835 | 312 | 100 | 51.1 | 5.5 |
| Game | 13 | 563 | 388 | 55 | 50.8 | 21.9 |
| Security | 11 | 463 | 315 | 107 | 23.5 | 3.5 |
| DevOps | 7 | 510 | 436 | 24 | 29.1 | 3.9 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.629 |         0.093 |      0.008 |
| forks       |   0.629 |   1     |         0.111 |      0.04  |
| open_issues |   0.093 |   0.111 |         1     |      0.034 |
| age_days    |   0.008 |   0.04  |         0.034 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.613 |         0.324 |     -0.022 |
| forks       |   0.613 |   1     |         0.321 |     -0.06  |
| open_issues |   0.324 |   0.321 |         1     |     -0.056 |
| age_days    |  -0.022 |  -0.06  |        -0.056 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 70 |
| `ai-agents` | 57 |
| `llm` | 55 |
| `codex` | 53 |
| `jev` | 41 |
| `macos` | 41 |
| `agent-skills` | 36 |
| `developer-tools` | 32 |
| `python` | 30 |
| `awesome-list` | 30 |
| `mcp` | 28 |
| `windows` | 28 |
| `typescript` | 26 |
| `rust` | 26 |
| `awesome` | 25 |
| `ai` | 24 |
| `typesafe` | 20 |
| `ai-agent` | 19 |
| `android` | 18 |
| `swift` | 18 |
