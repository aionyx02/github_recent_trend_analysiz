# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 571.7 | 262.5 | 23914 |
| forks | 85.4 | 29.0 | 3258 |
| open_issues | 10.7 | 1.0 | 2007 |
| stars_per_day | 64.0 | 22.0 | 3986 |
| age_days | 15.8 | 16.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `NandhaKishorM/laya` | 23914 | 2056 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 20020 | 1353 | Python | AI/ML |
| `eternity4719/HowToLiveBetter` | 15247 | 1035 | HTML | Web |
| `lnkiai/m3e-canvas` | 8202 | 861 | TypeScript | Web |
| `jaredpalmer/kev` | 6869 | 402 | Python | Other |
| `tamaratran/fast-jev-compaction` | 6781 | 405 | TypeScript | AI/ML |
| `sapientinc/PRAXIST` | 6770 | 785 | Python | Other |
| `zai-org/ZCode` | 6749 | 2020 | TypeScript | AI/ML |
| `rakanki911/DLSS5-Swapper` | 6652 | 350 | JavaScript | Game |
| `XiaoDuoYa/codex-with-chatgpt` | 6640 | 601 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `NandhaKishorM/laya` | 3985.7 | 23914 | 6d | AI/ML |
| `browser-use/jev-ultrafast` | 2502.5 | 20020 | 8d | AI/ML |
| `jev-chat/jev-chat-jarvis` | 2147.7 | 6443 | 3d | AI/ML |
| `zai-org/ZCode` | 1687.2 | 6749 | 4d | AI/ML |
| `mizorewww/laya-mlx` | 1258.2 | 6291 | 5d | AI/ML |
| `Contrastive-LM/CLM` | 1041.0 | 1041 | 1d | Other |
| `jaredpalmer/kev` | 981.3 | 6869 | 7d | Other |
| `tamaratran/fast-jev-compaction` | 968.7 | 6781 | 7d | AI/ML |
| `mikehasa/golive-skill` | 923.0 | 923 | 1d | AI/ML |
| `eternity4719/HowToLiveBetter` | 896.9 | 15247 | 17d | Web |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 402 | 467 | 246 | 84 | 44.8 | 16.5 |
| AI/ML | 383 | 683 | 294 | 90 | 86.8 | 7.0 |
| Web | 61 | 820 | 266 | 81 | 64.6 | 4.2 |
| Mobile | 60 | 514 | 248 | 102 | 54.3 | 9.7 |
| CLI/Tooling | 23 | 273 | 223 | 29 | 67.3 | 1.5 |
| Finance/Trading | 20 | 547 | 246 | 65 | 65.5 | 3.0 |
| Data | 18 | 431 | 266 | 135 | 52.8 | 8.6 |
| DevOps | 12 | 278 | 187 | 25 | 44.6 | 3.1 |
| Game | 11 | 935 | 214 | 58 | 77.1 | 17.0 |
| Security | 10 | 314 | 232 | 71 | 32.6 | 3.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.496 |         0.088 |     -0.006 |
| forks       |   0.496 |   1     |         0.079 |      0.004 |
| open_issues |   0.088 |   0.079 |         1     |      0.017 |
| age_days    |  -0.006 |   0.004 |         0.017 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.556 |         0.304 |      0.054 |
| forks       |   0.556 |   1     |         0.327 |     -0.028 |
| open_issues |   0.304 |   0.327 |         1     |      0.048 |
| age_days    |   0.054 |  -0.028 |         0.048 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 59 |
| `claude-code` | 55 |
| `ai-agents` | 51 |
| `codex` | 45 |
| `macos` | 41 |
| `developer-tools` | 37 |
| `jev` | 34 |
| `mcp` | 31 |
| `rust` | 29 |
| `python` | 28 |
| `agent-skills` | 28 |
| `awesome-list` | 28 |
| `ai` | 27 |
| `typescript` | 26 |
| `awesome` | 26 |
| `windows` | 24 |
| `ai-agent` | 21 |
| `open-source` | 19 |
| `swift` | 19 |
| `typesafe` | 18 |
