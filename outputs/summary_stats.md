# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 580.5 | 264.0 | 27348 |
| forks | 87.0 | 28.0 | 3453 |
| open_issues | 10.1 | 1.0 | 2003 |
| stars_per_day | 55.8 | 20.1 | 3039 |
| age_days | 16.2 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `NandhaKishorM/laya` | 27348 | 2385 | Python | AI/ML |
| `eternity4719/HowToLiveBetter` | 23839 | 1782 | HTML | Web |
| `browser-use/jev-ultrafast` | 21028 | 1450 | Python | AI/ML |
| `lnkiai/m3e-canvas` | 8390 | 887 | TypeScript | Web |
| `jaredpalmer/kev` | 7575 | 465 | Python | Other |
| `tamaratran/fast-jev-compaction` | 7074 | 443 | TypeScript | AI/ML |
| `rakanki911/DLSS5-Swapper` | 7035 | 365 | JavaScript | Game |
| `zai-org/ZCode` | 7009 | 2121 | TypeScript | AI/ML |
| `jev-chat/jev-chat-jarvis` | 6873 | 1173 | Kotlin | AI/ML |
| `Human-Agent-Society/reef` | 6870 | 632 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `NandhaKishorM/laya` | 3038.7 | 27348 | 9d | AI/ML |
| `browser-use/jev-ultrafast` | 1911.6 | 21028 | 11d | AI/ML |
| `eternity4719/HowToLiveBetter` | 1192.0 | 23839 | 20d | Web |
| `dzhng/jevgrep` | 1146.0 | 1146 | 1d | AI/ML |
| `jev-chat/jev-chat-jarvis` | 1145.5 | 6873 | 6d | AI/ML |
| `zai-org/ZCode` | 1001.3 | 7009 | 7d | AI/ML |
| `mizorewww/laya-mlx` | 817.9 | 6543 | 8d | AI/ML |
| `jaredpalmer/kev` | 757.5 | 7575 | 10d | Other |
| `tamaratran/fast-jev-compaction` | 707.4 | 7074 | 10d | AI/ML |
| `feitangyuan/onetake` | 651.0 | 651 | 1d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 411 | 432 | 234 | 81 | 38.0 | 14.5 |
| AI/ML | 376 | 704 | 300 | 94 | 75.7 | 7.6 |
| Web | 65 | 982 | 248 | 90 | 70.9 | 4.1 |
| Mobile | 64 | 510 | 241 | 106 | 47.4 | 6.8 |
| CLI/Tooling | 18 | 309 | 216 | 34 | 42.6 | 3.0 |
| Finance/Trading | 17 | 615 | 257 | 70 | 61.8 | 5.6 |
| Data | 15 | 483 | 277 | 157 | 44.9 | 10.0 |
| DevOps | 12 | 321 | 158 | 23 | 31.1 | 2.8 |
| Game | 12 | 946 | 302 | 67 | 77.0 | 19.3 |
| Security | 10 | 331 | 276 | 72 | 25.1 | 3.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.51  |         0.09  |     -0.016 |
| forks       |   0.51  |   1     |         0.08  |      0.017 |
| open_issues |   0.09  |   0.08  |         1     |      0.027 |
| age_days    |  -0.016 |   0.017 |         0.027 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.574 |         0.285 |     -0.03  |
| forks       |   0.574 |   1     |         0.318 |     -0.08  |
| open_issues |   0.285 |   0.318 |         1     |      0.031 |
| age_days    |  -0.03  |  -0.08  |         0.031 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 58 |
| `ai-agents` | 56 |
| `claude-code` | 53 |
| `codex` | 47 |
| `jev` | 37 |
| `macos` | 37 |
| `developer-tools` | 33 |
| `awesome-list` | 31 |
| `python` | 30 |
| `agent-skills` | 29 |
| `mcp` | 28 |
| `awesome` | 26 |
| `ai` | 25 |
| `typescript` | 25 |
| `windows` | 22 |
| `rust` | 19 |
| `typesafe` | 19 |
| `ai-agent` | 18 |
| `swift` | 17 |
| `react` | 16 |
