# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 547.0 | 196.5 | 79158 |
| forks | 52.8 | 0.0 | 10335 |
| open_issues | 7.6 | 0.0 | 2113 |
| stars_per_day | 131.9 | 190.0 | 4132 |
| age_days | 9.0 | 1.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 79158 | 10335 | Python | AI/ML |
| `DietrichGebert/ponytail` | 66109 | 3401 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 11831 | 925 | Python | Other |
| `XiaomiMiMo/MiMo-Code` | 11028 | 1066 | TypeScript | AI/ML |
| `unicity-astrid/book` | 7543 | 31 | Perl | Security |
| `unicity-astrid/handbook` | 7491 | 42 | Unknown | Other |
| `shadcn/improve` | 6401 | 264 | Unknown | Other |
| `zgwl/chinese-buy-us-stock-guide` | 5402 | 806 | Unknown | Other |
| `omnigent-ai/omnigent` | 5382 | 688 | Python | AI/ML |
| `XxHuberrr/Mineradio` | 4894 | 369 | HTML | Web |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 4131.8 | 66109 | 16d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 2827.1 | 79158 | 28d | AI/ML |
| `deepseek-ai/DeepSpec` | 1403.0 | 2806 | 2d | Other |
| `baidu/Unlimited-OCR` | 1183.1 | 11831 | 10d | Other |
| `Krishnagangwal/CS-Fundamentals` | 667.0 | 667 | 1d | Data |
| `XiaomiMiMo/MiMo-Code` | 612.7 | 11028 | 18d | AI/ML |
| `bozhouDev/codex-orange-book` | 465.4 | 2327 | 5d | AI/ML |
| `downclash/clash` | 367.0 | 367 | 1d | Other |
| `shadcn/improve` | 355.6 | 6401 | 18d | Other |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 347.0 | 347 | 1d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 655 | 301 | 191 | 16 | 162.1 | 1.3 |
| AI/ML | 215 | 1280 | 348 | 136 | 76.7 | 18.0 |
| Web | 28 | 849 | 399 | 71 | 40.8 | 84.1 |
| CLI/Tooling | 25 | 392 | 297 | 25 | 89.7 | 5.3 |
| Mobile | 19 | 622 | 317 | 64 | 39.9 | 10.9 |
| Game | 17 | 219 | 190 | 3 | 151.3 | 0.6 |
| Security | 14 | 1026 | 282 | 115 | 71.0 | 2.4 |
| Data | 11 | 570 | 484 | 122 | 91.7 | 6.4 |
| Finance/Trading | 11 | 295 | 298 | 557 | 37.9 | 0.1 |
| DevOps | 5 | 364 | 331 | 24 | 25.7 | 11.6 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.871 |         0.475 |      0.12  |
| forks       |   0.871 |   1     |         0.55  |      0.143 |
| open_issues |   0.475 |   0.55  |         1     |      0.12  |
| age_days    |   0.12  |   0.143 |         0.12  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.841 |         0.637 |      0.796 |
| forks       |   0.841 |   1     |         0.702 |      0.838 |
| open_issues |   0.637 |   0.702 |         1     |      0.644 |
| age_days    |   0.796 |   0.838 |         0.644 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 35 |
| `ai-agents` | 32 |
| `ai` | 30 |
| `llm` | 29 |
| `codex` | 26 |
| `ai-agent` | 20 |
| `claude` | 17 |
| `macos` | 17 |
| `cli` | 14 |
| `typescript` | 14 |
| `python` | 13 |
| `agent-skills` | 12 |
| `developer-tools` | 12 |
| `prompt-engineering` | 12 |
| `mcp` | 11 |
| `skills` | 11 |
| `react` | 10 |
| `open-source` | 10 |
| `local-first` | 10 |
| `agent` | 9 |
