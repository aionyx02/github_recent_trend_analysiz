# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 658.9 | 301.0 | 38962 |
| forks | 96.5 | 30.0 | 3956 |
| open_issues | 12.0 | 2.0 | 2050 |
| stars_per_day | 67.7 | 23.6 | 2038 |
| age_days | 16.3 | 16.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `eternity4719/HowToLiveBetter` | 38962 | 3051 | HTML | Web |
| `NandhaKishorM/laya` | 30577 | 2680 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 21939 | 1565 | Python | AI/ML |
| `Niko1221/Strata` | 9228 | 836 | C++ | AI/ML |
| `jaredpalmer/kev` | 8407 | 551 | Python | Other |
| `robbietilton/Compositor` | 7464 | 759 | Swift | Mobile |
| `zai-org/ZCode` | 7387 | 2256 | TypeScript | AI/ML |
| `tamaratran/fast-jev-compaction` | 7368 | 486 | TypeScript | AI/ML |
| `jev-chat/jev-chat-jarvis` | 7318 | 1220 | Kotlin | AI/ML |
| `cdyforever/how-to-live-better` | 7085 | 481 | HTML | Web |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `NandhaKishorM/laya` | 2038.5 | 30577 | 15d | AI/ML |
| `eternity4719/HowToLiveBetter` | 1498.5 | 38962 | 26d | Web |
| `browser-use/jev-ultrafast` | 1290.5 | 21939 | 17d | AI/ML |
| `KKKKhazix/AIHOT` | 1125.6 | 5628 | 5d | AI/ML |
| `Niko1221/Strata` | 1025.3 | 9228 | 9d | AI/ML |
| `facebookincubator/muse-gadget-sdk` | 1019.0 | 1019 | 1d | Other |
| `rehan-remade/universal-modder` | 937.3 | 2812 | 3d | AI/ML |
| `QingYunA/answer-me-with-html` | 747.0 | 747 | 1d | AI/ML |
| `CopilotKit/OpenDots` | 729.8 | 2919 | 4d | AI/ML |
| `feder-cr/dots` | 647.0 | 2588 | 4d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 444 | 483 | 282 | 77 | 65.3 | 15.2 |
| AI/ML | 343 | 831 | 353 | 115 | 76.7 | 9.5 |
| Mobile | 69 | 616 | 257 | 119 | 45.9 | 10.9 |
| Web | 59 | 1219 | 266 | 127 | 79.3 | 7.5 |
| CLI/Tooling | 19 | 381 | 234 | 49 | 40.1 | 4.7 |
| Data | 19 | 529 | 294 | 136 | 61.9 | 12.1 |
| Finance/Trading | 16 | 737 | 274 | 89 | 57.4 | 6.8 |
| Security | 12 | 486 | 394 | 98 | 58.3 | 3.1 |
| Game | 11 | 598 | 372 | 61 | 74.8 | 24.6 |
| DevOps | 8 | 456 | 325 | 21 | 27.3 | 3.9 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.555 |         0.081 |      0.025 |
| forks       |   0.555 |   1     |         0.087 |      0.095 |
| open_issues |   0.081 |   0.087 |         1     |      0.042 |
| age_days    |   0.025 |   0.095 |         0.042 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.56  |         0.263 |      0.023 |
| forks       |   0.56  |   1     |         0.361 |      0.088 |
| open_issues |   0.263 |   0.361 |         1     |      0.046 |
| age_days    |   0.023 |   0.088 |         0.046 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 61 |
| `llm` | 55 |
| `ai-agents` | 50 |
| `codex` | 48 |
| `jev` | 39 |
| `macos` | 39 |
| `developer-tools` | 31 |
| `agent-skills` | 31 |
| `awesome-list` | 30 |
| `python` | 25 |
| `ai` | 25 |
| `typescript` | 25 |
| `mcp` | 24 |
| `windows` | 24 |
| `awesome` | 23 |
| `rust` | 20 |
| `typesafe` | 19 |
| `open-source` | 18 |
| `swift` | 18 |
| `ai-agent` | 17 |
