# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 528.2 | 252.0 | 17350 |
| forks | 84.8 | 25.0 | 3647 |
| open_issues | 11.4 | 1.0 | 2561 |
| stars_per_day | 67.1 | 19.2 | 6123 |
| age_days | 16.3 | 16.5 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `browser-use/jev-ultrafast` | 17350 | 1098 | Python | AI/ML |
| `NandhaKishorM/laya` | 13795 | 1118 | Python | Other |
| `eternity4719/HowToLiveBetter` | 12035 | 809 | HTML | Web |
| `lnkiai/m3e-canvas` | 7978 | 835 | TypeScript | Web |
| `sapientinc/PRAXIST` | 6646 | 735 | Python | Other |
| `rakanki911/DLSS5-Swapper` | 6276 | 330 | JavaScript | Game |
| `tamaratran/fast-jev-compaction` | 6175 | 346 | TypeScript | AI/ML |
| `zai-org/ZCode` | 6123 | 1770 | TypeScript | AI/ML |
| `XiaoDuoYa/codex-with-chatgpt` | 5883 | 555 | TypeScript | AI/ML |
| `Albert-Weasker/niubigeo` | 4828 | 274 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `zai-org/ZCode` | 6123.0 | 6123 | 1d | AI/ML |
| `NandhaKishorM/laya` | 4598.3 | 13795 | 3d | Other |
| `browser-use/jev-ultrafast` | 3470.0 | 17350 | 5d | AI/ML |
| `jev-chat/jev-chat-jarvis` | 2860.0 | 2860 | 1d | AI/ML |
| `mizorewww/laya-mlx` | 2403.5 | 4807 | 2d | AI/ML |
| `tamaratran/fast-jev-compaction` | 1543.8 | 6175 | 4d | AI/ML |
| `robbietilton/Compositor` | 933.2 | 4666 | 5d | Mobile |
| `eternity4719/HowToLiveBetter` | 859.6 | 12035 | 14d | Web |
| `jaredpalmer/kev` | 753.0 | 3012 | 4d | Other |
| `TheoLeeCJ/SemIf` | 711.0 | 3555 | 5d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 410 | 483 | 243 | 92 | 54.5 | 19.2 |
| AI/ML | 377 | 569 | 272 | 81 | 87.5 | 6.3 |
| Mobile | 63 | 472 | 237 | 75 | 52.8 | 7.0 |
| Web | 52 | 850 | 257 | 85 | 58.1 | 4.2 |
| Data | 20 | 431 | 331 | 122 | 75.1 | 8.8 |
| Finance/Trading | 19 | 447 | 236 | 105 | 86.9 | 3.5 |
| CLI/Tooling | 18 | 433 | 250 | 34 | 39.3 | 4.1 |
| DevOps | 14 | 217 | 162 | 22 | 14.5 | 4.1 |
| Security | 14 | 321 | 291 | 80 | 46.8 | 2.4 |
| Game | 13 | 707 | 186 | 79 | 60.2 | 9.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.424 |         0.054 |     -0.024 |
| forks       |   0.424 |   1     |         0.048 |      0.009 |
| open_issues |   0.054 |   0.048 |         1     |     -0.009 |
| age_days    |  -0.024 |   0.009 |        -0.009 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.54  |         0.298 |      0.026 |
| forks       |   0.54  |   1     |         0.319 |      0.012 |
| open_issues |   0.298 |   0.319 |         1     |      0.015 |
| age_days    |   0.026 |   0.012 |         0.015 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 54 |
| `ai-agents` | 52 |
| `llm` | 50 |
| `codex` | 48 |
| `python` | 34 |
| `ai-agent` | 32 |
| `developer-tools` | 32 |
| `macos` | 31 |
| `typescript` | 31 |
| `agent-skills` | 29 |
| `mcp` | 28 |
| `ai` | 27 |
| `awesome-list` | 22 |
| `windows` | 21 |
| `jev` | 21 |
| `react` | 20 |
| `rust` | 20 |
| `awesome` | 20 |
| `open-source` | 19 |
| `self-hosted` | 19 |
