# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 569.9 | 255.5 | 26276 |
| forks | 84.2 | 26.0 | 3280 |
| open_issues | 10.3 | 1.0 | 2017 |
| stars_per_day | 55.6 | 20.2 | 3284 |
| age_days | 16.1 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `NandhaKishorM/laya` | 26276 | 2287 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 20685 | 1421 | Python | AI/ML |
| `eternity4719/HowToLiveBetter` | 19539 | 1379 | HTML | Web |
| `lnkiai/m3e-canvas` | 8322 | 871 | TypeScript | Web |
| `jaredpalmer/kev` | 7327 | 441 | Python | Other |
| `tamaratran/fast-jev-compaction` | 6991 | 433 | TypeScript | AI/ML |
| `rakanki911/DLSS5-Swapper` | 6903 | 361 | JavaScript | Game |
| `zai-org/ZCode` | 6866 | 2069 | TypeScript | AI/ML |
| `jev-chat/jev-chat-jarvis` | 6741 | 1161 | Kotlin | AI/ML |
| `XiaoDuoYa/codex-with-chatgpt` | 6736 | 619 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `NandhaKishorM/laya` | 3284.5 | 26276 | 8d | AI/ML |
| `browser-use/jev-ultrafast` | 2068.5 | 20685 | 10d | AI/ML |
| `jev-chat/jev-chat-jarvis` | 1348.2 | 6741 | 5d | AI/ML |
| `zai-org/ZCode` | 1144.3 | 6866 | 6d | AI/ML |
| `eternity4719/HowToLiveBetter` | 1028.4 | 19539 | 19d | Web |
| `mizorewww/laya-mlx` | 920.9 | 6446 | 7d | AI/ML |
| `jaredpalmer/kev` | 814.1 | 7327 | 9d | Other |
| `tamaratran/fast-jev-compaction` | 776.8 | 6991 | 9d | AI/ML |
| `tobi/disktree` | 721.0 | 1442 | 2d | Other |
| `supermemoryai/company-brain` | 606.0 | 606 | 1d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 407 | 421 | 233 | 78 | 39.9 | 15.3 |
| AI/ML | 384 | 700 | 286 | 91 | 72.7 | 7.3 |
| Mobile | 64 | 490 | 230 | 98 | 45.9 | 7.9 |
| Web | 60 | 947 | 254 | 89 | 67.4 | 4.8 |
| Finance/Trading | 19 | 608 | 250 | 68 | 72.8 | 4.6 |
| CLI/Tooling | 18 | 295 | 214 | 31 | 44.3 | 1.6 |
| Data | 15 | 471 | 277 | 155 | 48.9 | 10.3 |
| Game | 12 | 915 | 257 | 64 | 74.4 | 15.5 |
| DevOps | 11 | 310 | 158 | 24 | 33.3 | 2.7 |
| Security | 10 | 326 | 272 | 72 | 27.1 | 3.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.5   |         0.097 |     -0.014 |
| forks       |   0.5   |   1     |         0.081 |      0.008 |
| open_issues |   0.097 |   0.081 |         1     |      0.019 |
| age_days    |  -0.014 |   0.008 |         0.019 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.571 |         0.263 |     -0.023 |
| forks       |   0.571 |   1     |         0.309 |     -0.085 |
| open_issues |   0.263 |   0.309 |         1     |      0.032 |
| age_days    |  -0.023 |  -0.085 |         0.032 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 59 |
| `ai-agents` | 58 |
| `claude-code` | 56 |
| `codex` | 48 |
| `macos` | 39 |
| `jev` | 38 |
| `developer-tools` | 34 |
| `mcp` | 32 |
| `python` | 31 |
| `awesome-list` | 29 |
| `agent-skills` | 28 |
| `ai` | 26 |
| `awesome` | 26 |
| `typescript` | 25 |
| `windows` | 23 |
| `rust` | 21 |
| `ai-agent` | 19 |
| `typesafe` | 19 |
| `swift` | 18 |
| `react` | 16 |
