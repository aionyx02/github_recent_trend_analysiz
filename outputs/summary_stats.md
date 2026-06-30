# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 548.3 | 194.0 | 79434 |
| forks | 50.1 | 0.0 | 10379 |
| open_issues | 8.0 | 0.0 | 2463 |
| stars_per_day | 132.3 | 189.0 | 4010 |
| age_days | 8.9 | 1.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 79434 | 10379 | Python | AI/ML |
| `DietrichGebert/ponytail` | 68168 | 3504 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 12276 | 967 | Python | Other |
| `XiaomiMiMo/MiMo-Code` | 11104 | 1078 | TypeScript | AI/ML |
| `unicity-astrid/book` | 7536 | 31 | Perl | Security |
| `unicity-astrid/handbook` | 7484 | 42 | Unknown | Other |
| `shadcn/improve` | 6441 | 267 | Unknown | Other |
| `omnigent-ai/omnigent` | 5569 | 710 | Python | AI/ML |
| `XxHuberrr/Mineradio` | 5474 | 413 | HTML | Web |
| `deepseek-ai/DeepSpec` | 4613 | 382 | Python | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 4009.9 | 68168 | 17d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 2739.1 | 79434 | 29d | AI/ML |
| `deepseek-ai/DeepSpec` | 1537.7 | 4613 | 3d | Other |
| `baidu/Unlimited-OCR` | 1116.0 | 12276 | 11d | Other |
| `Krishnagangwal/CS-Fundamentals` | 1070.0 | 1070 | 1d | Data |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 645.0 | 645 | 1d | Other |
| `XiaomiMiMo/MiMo-Code` | 584.4 | 11104 | 19d | AI/ML |
| `bozhouDev/codex-orange-book` | 401.3 | 2408 | 6d | AI/ML |
| `Yu9191/wloc` | 348.8 | 1744 | 5d | Other |
| `shadcn/improve` | 339.0 | 6441 | 19d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 652 | 298 | 190 | 15 | 163.4 | 1.4 |
| AI/ML | 219 | 1282 | 350 | 133 | 73.9 | 18.0 |
| Web | 27 | 774 | 380 | 73 | 38.0 | 100.7 |
| CLI/Tooling | 21 | 432 | 284 | 30 | 108.8 | 4.7 |
| Mobile | 20 | 634 | 312 | 62 | 41.5 | 9.9 |
| Game | 18 | 218 | 189 | 3 | 152.2 | 0.6 |
| Security | 14 | 1033 | 294 | 114 | 52.9 | 3.6 |
| Data | 12 | 579 | 432 | 116 | 118.5 | 4.4 |
| Finance/Trading | 11 | 303 | 320 | 367 | 40.2 | 0.0 |
| DevOps | 6 | 340 | 272 | 22 | 21.9 | 10.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.88  |         0.431 |      0.124 |
| forks       |   0.88  |   1     |         0.516 |      0.147 |
| open_issues |   0.431 |   0.516 |         1     |      0.123 |
| age_days    |   0.124 |   0.147 |         0.123 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.846 |         0.637 |      0.801 |
| forks       |   0.846 |   1     |         0.716 |      0.852 |
| open_issues |   0.637 |   0.716 |         1     |      0.666 |
| age_days    |   0.801 |   0.852 |         0.666 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 34 |
| `claude-code` | 34 |
| `ai` | 32 |
| `llm` | 28 |
| `codex` | 23 |
| `ai-agent` | 18 |
| `claude` | 17 |
| `macos` | 17 |
| `typescript` | 15 |
| `agent-skills` | 12 |
| `cli` | 12 |
| `python` | 12 |
| `prompt-engineering` | 11 |
| `mcp` | 11 |
| `developer-tools` | 10 |
| `react` | 10 |
| `skills` | 10 |
| `open-source` | 10 |
| `agent` | 9 |
| `swift` | 9 |
