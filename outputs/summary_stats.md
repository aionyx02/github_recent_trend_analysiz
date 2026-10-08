# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 721.3 | 299.5 | 31631 |
| forks | 99.4 | 31.5 | 3276 |
| open_issues | 14.4 | 2.0 | 1764 |
| stars_per_day | 77.0 | 22.1 | 11384 |
| age_days | 16.7 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `NandhaKishorM/laya` | 31631 | 2798 | Python | AI/ML |
| `storytold/photocraft` | 22483 | 2931 | Rust | Other |
| `browser-use/jev-ultrafast` | 22351 | 1623 | Python | AI/ML |
| `Niko1221/Strata` | 17970 | 1592 | C++ | AI/ML |
| `robbietilton/Compositor` | 12686 | 1143 | Swift | Mobile |
| `openai/math` | 11384 | 1160 | Lean | Other |
| `cdyforever/how-to-live-better` | 9997 | 701 | HTML | Web |
| `jaredpalmer/kev` | 8714 | 571 | Python | Other |
| `zai-org/ZCode` | 7534 | 2296 | TypeScript | AI/ML |
| `tamaratran/fast-jev-compaction` | 7503 | 517 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `openai/math` | 11384.0 | 11384 | 1d | Other |
| `storytold/photocraft` | 3211.9 | 22483 | 7d | Other |
| `alchaincyf/huashu-art-motion` | 2262.0 | 2262 | 1d | Other |
| `NandhaKishorM/laya` | 1664.8 | 31631 | 19d | AI/ML |
| `Niko1221/Strata` | 1382.3 | 17970 | 13d | AI/ML |
| `browser-use/jev-ultrafast` | 1064.3 | 22351 | 21d | AI/ML |
| `alejandrobujan/tendedero` | 853.0 | 853 | 1d | Mobile |
| `rehan-remade/universal-modder` | 775.3 | 5427 | 7d | AI/ML |
| `LoreanXavier/pt-pc` | 769.0 | 769 | 1d | Game |
| `KKKKhazix/AIHOT` | 740.9 | 6668 | 9d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 400 | 590 | 281 | 92 | 94.4 | 20.2 |
| AI/ML | 369 | 905 | 342 | 117 | 70.9 | 10.3 |
| Mobile | 73 | 856 | 293 | 85 | 63.3 | 17.4 |
| Web | 69 | 542 | 249 | 80 | 56.9 | 6.2 |
| CLI/Tooling | 23 | 411 | 225 | 51 | 33.8 | 5.2 |
| Finance/Trading | 18 | 706 | 242 | 94 | 45.9 | 6.0 |
| Data | 17 | 745 | 315 | 160 | 64.8 | 11.2 |
| Game | 17 | 555 | 231 | 51 | 85.2 | 20.9 |
| DevOps | 7 | 418 | 221 | 34 | 24.1 | 3.7 |
| Security | 7 | 604 | 465 | 158 | 28.7 | 5.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.688 |         0.203 |     -0.027 |
| forks       |   0.688 |   1     |         0.18  |     -0.016 |
| open_issues |   0.203 |   0.18  |         1     |     -0.009 |
| age_days    |  -0.027 |  -0.016 |        -0.009 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.617 |         0.304 |      0.016 |
| forks       |   0.617 |   1     |         0.316 |     -0.034 |
| open_issues |   0.304 |   0.316 |         1     |     -0.073 |
| age_days    |   0.016 |  -0.034 |        -0.073 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 77 |
| `ai-agents` | 61 |
| `llm` | 58 |
| `codex` | 57 |
| `macos` | 47 |
| `jev` | 46 |
| `agent-skills` | 38 |
| `developer-tools` | 33 |
| `typescript` | 32 |
| `rust` | 31 |
| `mcp` | 29 |
| `awesome-list` | 29 |
| `python` | 28 |
| `ai` | 28 |
| `windows` | 26 |
| `ai-agent` | 24 |
| `cli` | 23 |
| `awesome` | 23 |
| `open-source` | 22 |
| `typesafe` | 21 |
