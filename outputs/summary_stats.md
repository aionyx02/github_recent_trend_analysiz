# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 468.4 | 176.5 | 80355 |
| forks | 90.1 | 12.0 | 7844 |
| open_issues | 4.8 | 0.0 | 1187 |
| stars_per_day | 36.7 | 12.7 | 2870 |
| age_days | 15.2 | 12.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `DietrichGebert/ponytail` | 80355 | 4333 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 13962 | 1167 | Python | Other |
| `langchain-ai/openwiki` | 10408 | 697 | TypeScript | AI/ML |
| `omnigent-ai/omnigent` | 7027 | 948 | Python | AI/ML |
| `deepseek-ai/DeepSpec` | 6533 | 585 | Python | Other |
| `elder-plinius/T3MP3ST` | 4364 | 929 | TypeScript | AI/ML |
| `zhongerxin/Cowart` | 4345 | 332 | JavaScript | Other |
| `x4gKing/X4G` | 4136 | 7844 | Python | Other |
| `bikini/exploitarium` | 3865 | 1109 | Python | Security |
| `Yu9191/wloc` | 3829 | 671 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 2869.8 | 80355 | 28d | AI/ML |
| `withmarbleapp/os-taxonomy` | 1122.5 | 2245 | 2d | Other |
| `x4gKing/X4G` | 689.3 | 4136 | 6d | Other |
| `baidu/Unlimited-OCR` | 634.6 | 13962 | 22d | Other |
| `langchain-ai/openwiki` | 578.2 | 10408 | 18d | AI/ML |
| `elder-plinius/T3MP3ST` | 545.5 | 4364 | 8d | AI/ML |
| `deepseek-ai/DeepSpec` | 466.6 | 6533 | 14d | Other |
| `Shpigford/knockoff` | 430.5 | 1722 | 4d | Other |
| `Robbyant/lingbot-world-v2` | 365.0 | 730 | 2d | Other |
| `Robbyant/lingbot-video` | 328.5 | 657 | 2d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 396 | 626 | 202 | 103 | 41.4 | 5.5 |
| Web | 234 | 177 | 151 | 10 | 15.8 | 0.4 |
| Other | 217 | 553 | 283 | 119 | 53.2 | 9.8 |
| Data | 36 | 248 | 152 | 10 | 17.2 | 1.6 |
| Mobile | 24 | 605 | 266 | 41 | 49.0 | 6.5 |
| Finance/Trading | 24 | 228 | 152 | 695 | 33.7 | 0.4 |
| CLI/Tooling | 21 | 551 | 284 | 44 | 43.9 | 0.9 |
| DevOps | 17 | 291 | 160 | 11 | 18.9 | 2.4 |
| Security | 17 | 476 | 203 | 104 | 27.8 | 4.6 |
| Game | 14 | 402 | 202 | 29 | 50.1 | 3.9 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.402 |         0.104 |      0.092 |
| forks       |   0.402 |   1     |         0.06  |     -0.013 |
| open_issues |   0.104 |   0.06  |         1     |      0.052 |
| age_days    |   0.092 |  -0.013 |         0.052 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.772 |         0.597 |      0.326 |
| forks       |   0.772 |   1     |         0.59  |      0.304 |
| open_issues |   0.597 |   0.59  |         1     |      0.257 |
| age_days    |   0.326 |   0.304 |         0.257 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 69 |
| `ai-agents` | 60 |
| `claude` | 58 |
| `llm` | 57 |
| `ai` | 49 |
| `claude-opus` | 48 |
| `python` | 47 |
| `manga` | 47 |
| `manga-downloader` | 47 |
| `codex` | 39 |
| `anthropic` | 36 |
| `typescript` | 35 |
| `developer-tools` | 34 |
| `open-source` | 34 |
| `mcp` | 31 |
| `cli` | 30 |
| `ai-agent` | 27 |
| `hentai` | 27 |
| `macos` | 26 |
| `manga-reader` | 26 |
