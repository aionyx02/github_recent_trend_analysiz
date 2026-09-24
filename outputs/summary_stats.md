# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 559.5 | 258.0 | 21930 |
| forks | 84.7 | 27.5 | 3243 |
| open_issues | 10.5 | 1.0 | 1957 |
| stars_per_day | 65.7 | 21.1 | 4386 |
| age_days | 15.8 | 16.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `NandhaKishorM/laya` | 21930 | 1876 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 19494 | 1296 | Python | AI/ML |
| `eternity4719/HowToLiveBetter` | 13652 | 921 | HTML | Web |
| `lnkiai/m3e-canvas` | 8129 | 854 | TypeScript | Web |
| `sapientinc/PRAXIST` | 6747 | 768 | Python | Other |
| `tamaratran/fast-jev-compaction` | 6662 | 389 | TypeScript | AI/ML |
| `zai-org/ZCode` | 6656 | 1987 | TypeScript | AI/ML |
| `XiaoDuoYa/codex-with-chatgpt` | 6589 | 596 | TypeScript | AI/ML |
| `jaredpalmer/kev` | 6536 | 356 | Python | Other |
| `rakanki911/DLSS5-Swapper` | 6530 | 345 | JavaScript | Game |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `NandhaKishorM/laya` | 4386.0 | 21930 | 5d | AI/ML |
| `jev-chat/jev-chat-jarvis` | 2800.5 | 5601 | 2d | AI/ML |
| `browser-use/jev-ultrafast` | 2784.9 | 19494 | 7d | AI/ML |
| `zai-org/ZCode` | 2218.7 | 6656 | 3d | AI/ML |
| `mizorewww/laya-mlx` | 1531.5 | 6126 | 4d | AI/ML |
| `tamaratran/fast-jev-compaction` | 1110.3 | 6662 | 6d | AI/ML |
| `jaredpalmer/kev` | 1089.3 | 6536 | 6d | Other |
| `unreallabsai/unreal-agent` | 916.5 | 1833 | 2d | AI/ML |
| `eternity4719/HowToLiveBetter` | 853.2 | 13652 | 16d | Web |
| `robbietilton/Compositor` | 762.6 | 5338 | 7d | Mobile |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 408 | 452 | 244 | 83 | 42.8 | 16.2 |
| AI/ML | 382 | 667 | 292 | 90 | 92.0 | 6.9 |
| Mobile | 60 | 498 | 242 | 95 | 54.0 | 8.3 |
| Web | 56 | 830 | 258 | 76 | 63.0 | 4.2 |
| CLI/Tooling | 25 | 393 | 222 | 38 | 70.5 | 3.1 |
| Data | 19 | 423 | 277 | 132 | 55.9 | 8.9 |
| Finance/Trading | 19 | 548 | 250 | 61 | 80.0 | 2.9 |
| DevOps | 12 | 265 | 188 | 24 | 65.8 | 3.2 |
| Game | 10 | 962 | 286 | 109 | 87.7 | 13.2 |
| Security | 9 | 321 | 247 | 77 | 38.9 | 3.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.481 |         0.088 |     -0.019 |
| forks       |   0.481 |   1     |         0.076 |      0     |
| open_issues |   0.088 |   0.076 |         1     |      0.009 |
| age_days    |  -0.019 |   0     |         0.009 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.557 |         0.304 |      0.027 |
| forks       |   0.557 |   1     |         0.334 |     -0.017 |
| open_issues |   0.304 |   0.334 |         1     |      0.039 |
| age_days    |   0.027 |  -0.017 |         0.039 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 59 |
| `claude-code` | 54 |
| `ai-agents` | 51 |
| `codex` | 47 |
| `macos` | 39 |
| `developer-tools` | 37 |
| `jev` | 30 |
| `mcp` | 30 |
| `rust` | 29 |
| `agent-skills` | 29 |
| `python` | 28 |
| `ai` | 28 |
| `typescript` | 28 |
| `ai-agent` | 26 |
| `awesome-list` | 26 |
| `awesome` | 24 |
| `windows` | 23 |
| `open-source` | 19 |
| `swift` | 19 |
| `agent` | 17 |
