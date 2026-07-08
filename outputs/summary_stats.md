# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 476.9 | 175.5 | 77307 |
| forks | 64.2 | 10.0 | 4126 |
| open_issues | 6.0 | 0.0 | 1192 |
| stars_per_day | 39.0 | 16.8 | 3092 |
| age_days | 14.4 | 11.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `DietrichGebert/ponytail` | 77307 | 4126 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 13666 | 1125 | Python | Other |
| `XiaomiMiMo/MiMo-Code` | 11609 | 1138 | TypeScript | AI/ML |
| `langchain-ai/openwiki` | 9428 | 614 | TypeScript | AI/ML |
| `shadcn/improve` | 7465 | 313 | Unknown | Other |
| `omnigent-ai/omnigent` | 6694 | 892 | Python | AI/ML |
| `cobusgreyling/loop-engineering` | 6508 | 831 | JavaScript | AI/ML |
| `deepseek-ai/DeepSpec` | 6428 | 565 | Python | Other |
| `zhongerxin/Cowart` | 4116 | 325 | JavaScript | Other |
| `makerspet/oomwoo` | 3913 | 180 | Python | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 3092.3 | 77307 | 25d | AI/ML |
| `Shpigford/knockoff` | 1161.0 | 1161 | 1d | Other |
| `baidu/Unlimited-OCR` | 719.3 | 13666 | 19d | Other |
| `elder-plinius/T3MP3ST` | 704.8 | 3524 | 5d | AI/ML |
| `langchain-ai/openwiki` | 628.5 | 9428 | 15d | AI/ML |
| `deepseek-ai/DeepSpec` | 584.4 | 6428 | 11d | Other |
| `MaximeRivest/riddle` | 554.0 | 1108 | 2d | Other |
| `ammaarreshi/Generals-Mac-iOS-iPad` | 438.0 | 1314 | 3d | Mobile |
| `XiaomiMiMo/MiMo-Code` | 430.0 | 11609 | 27d | AI/ML |
| `Robbyant/lingbot-vision` | 409.0 | 409 | 1d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 400 | 658 | 207 | 79 | 44.3 | 7.4 |
| Web | 243 | 177 | 151 | 4 | 19.0 | 0.3 |
| Other | 204 | 562 | 271 | 87 | 56.7 | 11.3 |
| Data | 37 | 240 | 151 | 10 | 21.6 | 1.5 |
| Mobile | 27 | 502 | 252 | 35 | 49.7 | 10.8 |
| CLI/Tooling | 23 | 555 | 260 | 43 | 61.1 | 3.3 |
| Finance/Trading | 21 | 186 | 152 | 428 | 19.4 | 0.1 |
| DevOps | 19 | 285 | 190 | 11 | 20.4 | 5.0 |
| Security | 16 | 566 | 216 | 145 | 34.7 | 5.6 |
| Game | 10 | 224 | 192 | 14 | 22.8 | 2.5 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.581 |         0.194 |      0.099 |
| forks       |   0.581 |   1     |         0.166 |      0.072 |
| open_issues |   0.194 |   0.166 |         1     |      0.074 |
| age_days    |   0.099 |   0.072 |         0.074 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.776 |         0.579 |      0.437 |
| forks       |   0.776 |   1     |         0.604 |      0.459 |
| open_issues |   0.579 |   0.604 |         1     |      0.337 |
| age_days    |   0.437 |   0.459 |         0.337 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 67 |
| `llm` | 65 |
| `ai-agents` | 62 |
| `claude` | 58 |
| `ai` | 54 |
| `claude-opus` | 48 |
| `python` | 47 |
| `manga` | 47 |
| `manga-downloader` | 47 |
| `anthropic` | 39 |
| `typescript` | 38 |
| `open-source` | 36 |
| `cli` | 35 |
| `developer-tools` | 34 |
| `codex` | 34 |
| `macos` | 32 |
| `mcp` | 31 |
| `ai-agent` | 28 |
| `video-download-tool` | 28 |
| `hentai` | 28 |
