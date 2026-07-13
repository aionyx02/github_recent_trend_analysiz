# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 378.3 | 173.0 | 14139 |
| forks | 87.0 | 11.0 | 9220 |
| open_issues | 3.9 | 0.0 | 1188 |
| stars_per_day | 31.5 | 10.9 | 707 |
| age_days | 15.6 | 14.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `baidu/Unlimited-OCR` | 14139 | 1188 | Python | Other |
| `langchain-ai/openwiki` | 10830 | 741 | TypeScript | AI/ML |
| `JustVugg/colibri` | 7775 | 632 | C | Game |
| `deepseek-ai/DeepSpec` | 6605 | 592 | Python | Other |
| `x4gKing/X4G` | 4907 | 9220 | Python | Other |
| `elder-plinius/T3MP3ST` | 4573 | 971 | TypeScript | AI/ML |
| `zhongerxin/Cowart` | 4480 | 342 | JavaScript | Other |
| `Yu9191/wloc` | 4345 | 795 | JavaScript | Other |
| `bikini/exploitarium` | 3890 | 1119 | Python | Security |
| `baairon/torlink` | 3524 | 234 | TypeScript | CLI/Tooling |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `JustVugg/colibri` | 706.8 | 7775 | 11d | Game |
| `withmarbleapp/os-taxonomy` | 704.0 | 2816 | 4d | Other |
| `mereyabdenbekuly-ctrl/clodex-ide` | 691.0 | 691 | 1d | Security |
| `x4gKing/X4G` | 613.4 | 4907 | 8d | Other |
| `baidu/Unlimited-OCR` | 589.1 | 14139 | 24d | Other |
| `langchain-ai/openwiki` | 541.5 | 10830 | 20d | AI/ML |
| `elder-plinius/T3MP3ST` | 457.3 | 4573 | 10d | AI/ML |
| `deepseek-ai/DeepSpec` | 412.8 | 6605 | 16d | Other |
| `MDX-Tom/gpt-5.6-instruct` | 382.0 | 382 | 1d | AI/ML |
| `Shpigford/knockoff` | 306.2 | 1837 | 6d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 400 | 390 | 198 | 91 | 31.6 | 3.3 |
| Web | 236 | 177 | 151 | 16 | 14.3 | 0.5 |
| Other | 209 | 572 | 287 | 140 | 47.5 | 10.0 |
| Data | 34 | 253 | 151 | 11 | 15.6 | 1.5 |
| Finance/Trading | 23 | 215 | 152 | 547 | 21.6 | 0.3 |
| Mobile | 22 | 498 | 266 | 41 | 41.7 | 6.0 |
| Security | 20 | 433 | 194 | 87 | 62.4 | 3.5 |
| CLI/Tooling | 19 | 553 | 269 | 40 | 38.6 | 1.0 |
| DevOps | 19 | 299 | 180 | 11 | 29.5 | 2.1 |
| Game | 18 | 661 | 210 | 50 | 59.6 | 4.9 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.306 |         0.129 |      0.084 |
| forks       |   0.306 |   1     |         0.024 |     -0.065 |
| open_issues |   0.129 |   0.024 |         1     |      0.02  |
| age_days    |   0.084 |  -0.065 |         0.02  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.724 |         0.573 |      0.203 |
| forks       |   0.724 |   1     |         0.579 |      0.164 |
| open_issues |   0.573 |   0.579 |         1     |      0.19  |
| age_days    |   0.203 |   0.164 |         0.19  |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 69 |
| `llm` | 62 |
| `ai-agents` | 60 |
| `claude` | 58 |
| `ai` | 49 |
| `python` | 48 |
| `claude-opus` | 48 |
| `manga` | 47 |
| `manga-downloader` | 47 |
| `codex` | 43 |
| `typescript` | 38 |
| `anthropic` | 37 |
| `developer-tools` | 36 |
| `cli` | 33 |
| `mcp` | 33 |
| `open-source` | 28 |
| `ai-agent` | 27 |
| `hentai` | 27 |
| `manga-reader` | 26 |
| `macos` | 25 |
