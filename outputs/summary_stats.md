# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 483.1 | 232.0 | 72262 |
| forks | 54.5 | 8.0 | 3750 |
| open_issues | 8.3 | 0.0 | 3874 |
| stars_per_day | 85.5 | 37.8 | 3613 |
| age_days | 11.9 | 10.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `DietrichGebert/ponytail` | 72262 | 3750 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 13103 | 1059 | Python | Other |
| `XiaomiMiMo/MiMo-Code` | 11324 | 1107 | TypeScript | AI/ML |
| `unicity-astrid/book` | 7533 | 31 | Perl | Security |
| `unicity-astrid/handbook` | 7481 | 42 | Unknown | Other |
| `shadcn/improve` | 6619 | 271 | Unknown | Other |
| `omnigent-ai/omnigent` | 6102 | 791 | Python | AI/ML |
| `deepseek-ai/DeepSpec` | 5922 | 491 | Python | Other |
| `cobusgreyling/loop-engineering` | 5100 | 640 | JavaScript | AI/ML |
| `diffusionstudio/lottie` | 4391 | 233 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 3613.1 | 72262 | 20d | AI/ML |
| `deepseek-ai/DeepSpec` | 987.0 | 5922 | 6d | Other |
| `baidu/Unlimited-OCR` | 935.9 | 13103 | 14d | Other |
| `mekos2772/ios-location-spoofer` | 601.5 | 1203 | 2d | Mobile |
| `XiaomiMiMo/MiMo-Code` | 514.7 | 11324 | 22d | AI/ML |
| `bikini/exploitarium` | 391.9 | 3527 | 9d | Security |
| `TianhangZhuzth/Fundamental-Ava` | 379.0 | 758 | 2d | AI/ML |
| `baairon/torlink` | 378.6 | 2650 | 7d | CLI/Tooling |
| `Krishnagangwal/CS-Fundamentals` | 366.2 | 1465 | 4d | Data |
| `asz798838958/FrciblyK12` | 354.0 | 354 | 1d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 388 | 398 | 234 | 28 | 129.6 | 2.8 |
| AI/ML | 330 | 695 | 250 | 68 | 50.7 | 8.1 |
| Web | 109 | 241 | 151 | 15 | 42.4 | 36.2 |
| Data | 31 | 341 | 214 | 43 | 83.0 | 3.2 |
| Game | 31 | 240 | 233 | 4 | 148.8 | 0.5 |
| Finance/Trading | 27 | 263 | 234 | 511 | 45.5 | 0.1 |
| CLI/Tooling | 25 | 455 | 220 | 32 | 60.8 | 5.3 |
| Security | 24 | 853 | 246 | 113 | 72.6 | 4.2 |
| Mobile | 23 | 537 | 259 | 31 | 72.2 | 8.0 |
| DevOps | 12 | 291 | 206 | 14 | 43.0 | 5.3 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.574 |         0.066 |      0.086 |
| forks       |   0.574 |   1     |         0.107 |      0.103 |
| open_issues |   0.066 |   0.107 |         1     |      0.085 |
| age_days    |   0.086 |   0.103 |         0.085 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.567 |         0.394 |      0.251 |
| forks       |   0.567 |   1     |         0.607 |      0.685 |
| open_issues |   0.394 |   0.607 |         1     |      0.514 |
| age_days    |   0.251 |   0.685 |         0.514 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 53 |
| `ai` | 50 |
| `ai-agents` | 45 |
| `llm` | 43 |
| `claude` | 42 |
| `codex` | 34 |
| `python` | 30 |
| `claude-opus` | 29 |
| `typescript` | 28 |
| `anthropic` | 25 |
| `open-source` | 24 |
| `ai-agent` | 22 |
| `macos` | 22 |
| `developer-tools` | 20 |
| `cli` | 20 |
| `mcp` | 19 |
| `agent-skills` | 18 |
| `manga-downloader` | 17 |
| `prompt-engineering` | 16 |
| `react` | 15 |
