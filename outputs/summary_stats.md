# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 544.2 | 255.0 | 18813 |
| forks | 83.0 | 25.0 | 3232 |
| open_issues | 11.1 | 1.0 | 2611 |
| stars_per_day | 67.1 | 20.0 | 4947 |
| age_days | 16.1 | 16.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `NandhaKishorM/laya` | 18813 | 1603 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 18688 | 1220 | Python | AI/ML |
| `eternity4719/HowToLiveBetter` | 12760 | 856 | HTML | Web |
| `lnkiai/m3e-canvas` | 8050 | 842 | TypeScript | Web |
| `sapientinc/PRAXIST` | 6715 | 751 | Python | Other |
| `tamaratran/fast-jev-compaction` | 6462 | 371 | TypeScript | AI/ML |
| `zai-org/ZCode` | 6462 | 1908 | TypeScript | AI/ML |
| `XiaoDuoYa/codex-with-chatgpt` | 6446 | 583 | TypeScript | AI/ML |
| `rakanki911/DLSS5-Swapper` | 6424 | 341 | JavaScript | Game |
| `mizorewww/laya-mlx` | 5738 | 416 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `jev-chat/jev-chat-jarvis` | 4947.0 | 4947 | 1d | AI/ML |
| `NandhaKishorM/laya` | 4703.2 | 18813 | 4d | AI/ML |
| `zai-org/ZCode` | 3231.0 | 6462 | 2d | AI/ML |
| `browser-use/jev-ultrafast` | 3114.7 | 18688 | 6d | AI/ML |
| `mizorewww/laya-mlx` | 1912.7 | 5738 | 3d | AI/ML |
| `unreallabsai/unreal-agent` | 1422.0 | 1422 | 1d | AI/ML |
| `tamaratran/fast-jev-compaction` | 1292.4 | 6462 | 5d | AI/ML |
| `jaredpalmer/kev` | 1031.0 | 5155 | 5d | Other |
| `eternity4719/HowToLiveBetter` | 850.7 | 12760 | 15d | Web |
| `robbietilton/Compositor` | 845.7 | 5074 | 6d | Mobile |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 412 | 444 | 241 | 81 | 40.8 | 18.0 |
| AI/ML | 384 | 642 | 280 | 89 | 100.4 | 6.7 |
| Web | 58 | 797 | 251 | 79 | 60.2 | 4.1 |
| Mobile | 58 | 479 | 240 | 87 | 49.6 | 7.1 |
| CLI/Tooling | 19 | 440 | 244 | 35 | 37.0 | 3.7 |
| Data | 19 | 410 | 277 | 129 | 65.8 | 8.6 |
| Finance/Trading | 18 | 523 | 252 | 59 | 80.0 | 2.1 |
| DevOps | 13 | 241 | 211 | 22 | 40.2 | 3.6 |
| Game | 11 | 848 | 211 | 91 | 94.8 | 12.0 |
| Security | 8 | 336 | 276 | 84 | 49.4 | 3.6 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.466 |         0.064 |     -0.031 |
| forks       |   0.466 |   1     |         0.06  |     -0.01  |
| open_issues |   0.064 |   0.06  |         1     |     -0.004 |
| age_days    |  -0.031 |  -0.01  |        -0.004 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.563 |         0.297 |      0.016 |
| forks       |   0.563 |   1     |         0.332 |      0.008 |
| open_issues |   0.297 |   0.332 |         1     |      0.034 |
| age_days    |   0.016 |   0.008 |         0.034 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 53 |
| `claude-code` | 53 |
| `ai-agents` | 49 |
| `codex` | 48 |
| `developer-tools` | 32 |
| `python` | 31 |
| `macos` | 31 |
| `ai-agent` | 31 |
| `mcp` | 29 |
| `agent-skills` | 29 |
| `jev` | 27 |
| `ai` | 27 |
| `typescript` | 26 |
| `awesome-list` | 24 |
| `awesome` | 23 |
| `windows` | 21 |
| `rust` | 19 |
| `open-source` | 19 |
| `react` | 17 |
| `agent` | 16 |
