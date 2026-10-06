# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 687.1 | 300.0 | 45590 |
| forks | 91.0 | 29.0 | 4146 |
| open_issues | 13.1 | 2.0 | 2045 |
| stars_per_day | 64.1 | 22.1 | 1830 |
| age_days | 16.7 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `eternity4719/HowToLiveBetter` | 45590 | 3629 | HTML | Web |
| `NandhaKishorM/laya` | 31109 | 2742 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 22164 | 1597 | Python | AI/ML |
| `Niko1221/Strata` | 15002 | 1267 | C++ | AI/ML |
| `robbietilton/Compositor` | 8674 | 860 | Swift | Mobile |
| `jaredpalmer/kev` | 8559 | 563 | Python | Other |
| `cdyforever/how-to-live-better` | 8222 | 562 | HTML | Web |
| `zai-org/ZCode` | 7461 | 2272 | TypeScript | AI/ML |
| `tamaratran/fast-jev-compaction` | 7435 | 508 | TypeScript | AI/ML |
| `jev-chat/jev-chat-jarvis` | 7382 | 1225 | Kotlin | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `NandhaKishorM/laya` | 1829.9 | 31109 | 17d | AI/ML |
| `eternity4719/HowToLiveBetter` | 1628.2 | 45590 | 28d | Web |
| `kargulstudio/sales-crm` | 1547.0 | 1547 | 1d | Other |
| `Niko1221/Strata` | 1363.8 | 15002 | 11d | AI/ML |
| `browser-use/jev-ultrafast` | 1166.5 | 22164 | 19d | AI/ML |
| `KKKKhazix/AIHOT` | 875.1 | 6126 | 7d | AI/ML |
| `rehan-remade/universal-modder` | 848.6 | 4243 | 5d | AI/ML |
| `CopilotKit/OpenDots` | 635.7 | 3814 | 6d | AI/ML |
| `rauchg/gdp-ts` | 627.0 | 627 | 1d | Other |
| `elstongun/leviathan` | 545.0 | 545 | 1d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 423 | 485 | 279 | 63 | 56.0 | 18.0 |
| AI/ML | 353 | 862 | 342 | 112 | 75.4 | 9.5 |
| Mobile | 72 | 748 | 272 | 131 | 58.8 | 13.7 |
| Web | 63 | 1229 | 258 | 126 | 75.8 | 6.0 |
| CLI/Tooling | 26 | 354 | 219 | 40 | 56.4 | 4.3 |
| Data | 18 | 527 | 315 | 140 | 74.0 | 10.3 |
| Finance/Trading | 16 | 761 | 277 | 97 | 52.8 | 5.5 |
| Game | 11 | 668 | 422 | 63 | 59.9 | 25.4 |
| Security | 11 | 476 | 338 | 112 | 23.1 | 3.8 |
| DevOps | 7 | 439 | 240 | 32 | 25.3 | 6.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.637 |         0.083 |      0.023 |
| forks       |   0.637 |   1     |         0.108 |      0.062 |
| open_issues |   0.083 |   0.108 |         1     |      0.054 |
| age_days    |   0.023 |   0.062 |         0.054 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.601 |         0.321 |     -0.012 |
| forks       |   0.601 |   1     |         0.346 |      0.026 |
| open_issues |   0.321 |   0.346 |         1     |      0.019 |
| age_days    |  -0.012 |   0.026 |         0.019 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 70 |
| `llm` | 56 |
| `ai-agents` | 55 |
| `codex` | 54 |
| `jev` | 42 |
| `macos` | 41 |
| `agent-skills` | 36 |
| `developer-tools` | 30 |
| `awesome-list` | 29 |
| `windows` | 28 |
| `python` | 27 |
| `typescript` | 27 |
| `rust` | 27 |
| `ai` | 25 |
| `mcp` | 25 |
| `awesome` | 24 |
| `typesafe` | 21 |
| `ai-agent` | 20 |
| `linux` | 19 |
| `claude` | 18 |
