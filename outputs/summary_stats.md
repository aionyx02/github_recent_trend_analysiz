# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 493.1 | 183.0 | 79647 |
| forks | 83.9 | 11.0 | 6755 |
| open_issues | 5.8 | 0.0 | 1193 |
| stars_per_day | 40.7 | 13.8 | 2950 |
| age_days | 14.9 | 11.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `DietrichGebert/ponytail` | 79647 | 4279 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 13876 | 1151 | Python | Other |
| `XiaomiMiMo/MiMo-Code` | 11735 | 1160 | TypeScript | AI/ML |
| `langchain-ai/openwiki` | 10211 | 679 | TypeScript | AI/ML |
| `shadcn/improve` | 7581 | 316 | Unknown | Other |
| `omnigent-ai/omnigent` | 6950 | 938 | Python | AI/ML |
| `deepseek-ai/DeepSpec` | 6512 | 581 | Python | Other |
| `zhongerxin/Cowart` | 4279 | 330 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 4245 | 909 | TypeScript | AI/ML |
| `makerspet/oomwoo` | 4030 | 188 | Python | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 2949.9 | 79647 | 27d | AI/ML |
| `withmarbleapp/os-taxonomy` | 1771.0 | 1771 | 1d | Other |
| `x4gKing/X4G` | 711.8 | 3559 | 5d | Other |
| `baidu/Unlimited-OCR` | 660.8 | 13876 | 21d | Other |
| `Robbyant/lingbot-world-v2` | 656.0 | 656 | 1d | Other |
| `Robbyant/lingbot-video` | 615.0 | 615 | 1d | Other |
| `elder-plinius/T3MP3ST` | 606.4 | 4245 | 7d | AI/ML |
| `langchain-ai/openwiki` | 600.6 | 10211 | 17d | AI/ML |
| `Shpigford/knockoff` | 536.0 | 1608 | 3d | Other |
| `deepseek-ai/DeepSpec` | 500.9 | 6512 | 13d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 397 | 664 | 209 | 98 | 43.8 | 7.2 |
| Web | 230 | 176 | 151 | 4 | 15.6 | 0.4 |
| Other | 217 | 594 | 282 | 119 | 67.6 | 10.8 |
| Data | 36 | 247 | 152 | 10 | 18.5 | 1.6 |
| Mobile | 26 | 600 | 266 | 41 | 53.7 | 7.9 |
| CLI/Tooling | 23 | 580 | 269 | 43 | 47.3 | 2.5 |
| Finance/Trading | 23 | 228 | 152 | 583 | 27.0 | 0.4 |
| DevOps | 19 | 285 | 197 | 11 | 20.0 | 2.1 |
| Security | 17 | 470 | 203 | 104 | 29.2 | 4.5 |
| Game | 12 | 320 | 200 | 23 | 34.9 | 3.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.437 |         0.15  |      0.106 |
| forks       |   0.437 |   1     |         0.104 |      0.016 |
| open_issues |   0.15  |   0.104 |         1     |      0.08  |
| age_days    |   0.106 |   0.016 |         0.08  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.768 |         0.587 |      0.344 |
| forks       |   0.768 |   1     |         0.604 |      0.357 |
| open_issues |   0.587 |   0.604 |         1     |      0.283 |
| age_days    |   0.344 |   0.357 |         0.283 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 65 |
| `claude` | 59 |
| `ai-agents` | 58 |
| `llm` | 57 |
| `ai` | 52 |
| `claude-opus` | 48 |
| `manga` | 47 |
| `manga-downloader` | 47 |
| `python` | 44 |
| `anthropic` | 37 |
| `codex` | 36 |
| `typescript` | 34 |
| `developer-tools` | 33 |
| `open-source` | 33 |
| `cli` | 30 |
| `macos` | 30 |
| `mcp` | 29 |
| `ai-agent` | 27 |
| `hentai` | 27 |
| `manga-reader` | 26 |
