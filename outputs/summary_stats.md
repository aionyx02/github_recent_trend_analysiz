# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 461.8 | 176.0 | 80944 |
| forks | 86.0 | 11.0 | 8626 |
| open_issues | 4.2 | 0.0 | 1186 |
| stars_per_day | 34.1 | 11.7 | 2791 |
| age_days | 15.5 | 13.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `DietrichGebert/ponytail` | 80944 | 4369 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 14042 | 1180 | Python | Other |
| `langchain-ai/openwiki` | 10631 | 721 | TypeScript | AI/ML |
| `deepseek-ai/DeepSpec` | 6553 | 588 | Python | Other |
| `x4gKing/X4G` | 4559 | 8626 | Python | Other |
| `JustVugg/colibri` | 4464 | 390 | C | Game |
| `elder-plinius/T3MP3ST` | 4461 | 952 | TypeScript | AI/ML |
| `zhongerxin/Cowart` | 4380 | 335 | JavaScript | Other |
| `Yu9191/wloc` | 3956 | 700 | JavaScript | Other |
| `bikini/exploitarium` | 3873 | 1113 | Python | Security |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 2791.2 | 80944 | 29d | AI/ML |
| `withmarbleapp/os-taxonomy` | 839.0 | 2517 | 3d | Other |
| `x4gKing/X4G` | 651.3 | 4559 | 7d | Other |
| `baidu/Unlimited-OCR` | 610.5 | 14042 | 23d | Other |
| `langchain-ai/openwiki` | 559.5 | 10631 | 19d | AI/ML |
| `elder-plinius/T3MP3ST` | 495.7 | 4461 | 9d | AI/ML |
| `JustVugg/colibri` | 446.4 | 4464 | 10d | Game |
| `deepseek-ai/DeepSpec` | 436.9 | 6553 | 15d | Other |
| `Shpigford/knockoff` | 357.4 | 1787 | 5d | Other |
| `Robbyant/lingbot-world-v2` | 281.3 | 844 | 3d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 399 | 604 | 199 | 100 | 38.4 | 4.0 |
| Web | 234 | 178 | 151 | 12 | 14.8 | 0.4 |
| Other | 212 | 564 | 286 | 127 | 49.3 | 9.9 |
| Data | 37 | 247 | 151 | 10 | 16.0 | 1.6 |
| Finance/Trading | 24 | 221 | 152 | 489 | 26.3 | 0.2 |
| Mobile | 22 | 598 | 267 | 43 | 46.5 | 6.8 |
| CLI/Tooling | 21 | 527 | 270 | 38 | 39.3 | 1.0 |
| DevOps | 18 | 286 | 161 | 11 | 21.1 | 2.1 |
| Security | 17 | 446 | 183 | 94 | 37.0 | 3.8 |
| Game | 16 | 496 | 204 | 40 | 50.7 | 4.4 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.41  |         0.081 |      0.092 |
| forks       |   0.41  |   1     |         0.039 |     -0.034 |
| open_issues |   0.081 |   0.039 |         1     |      0.031 |
| age_days    |   0.092 |  -0.034 |         0.031 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.756 |         0.574 |      0.27  |
| forks       |   0.756 |   1     |         0.587 |      0.253 |
| open_issues |   0.574 |   0.587 |         1     |      0.245 |
| age_days    |   0.27  |   0.253 |         0.245 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 68 |
| `llm` | 61 |
| `ai-agents` | 59 |
| `claude` | 59 |
| `ai` | 48 |
| `claude-opus` | 48 |
| `manga` | 47 |
| `manga-downloader` | 47 |
| `python` | 45 |
| `codex` | 38 |
| `typescript` | 36 |
| `anthropic` | 36 |
| `developer-tools` | 35 |
| `mcp` | 34 |
| `open-source` | 32 |
| `cli` | 30 |
| `ai-agent` | 27 |
| `hentai` | 27 |
| `macos` | 26 |
| `manga-reader` | 26 |
