# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 489.1 | 179.0 | 78524 |
| forks | 80.1 | 11.0 | 5317 |
| open_issues | 5.8 | 0.0 | 1194 |
| stars_per_day | 40.3 | 15.1 | 3020 |
| age_days | 14.7 | 11.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `DietrichGebert/ponytail` | 78524 | 4200 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 13762 | 1139 | Python | Other |
| `XiaomiMiMo/MiMo-Code` | 11677 | 1147 | TypeScript | AI/ML |
| `langchain-ai/openwiki` | 9933 | 662 | TypeScript | AI/ML |
| `shadcn/improve` | 7533 | 314 | Unknown | Other |
| `omnigent-ai/omnigent` | 6845 | 915 | Python | AI/ML |
| `cobusgreyling/loop-engineering` | 6759 | 864 | JavaScript | AI/ML |
| `deepseek-ai/DeepSpec` | 6485 | 576 | Python | Other |
| `zhongerxin/Cowart` | 4206 | 326 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 3997 | 857 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 3020.2 | 78524 | 26d | AI/ML |
| `withmarbleapp/os-taxonomy` | 855.0 | 855 | 1d | Other |
| `Shpigford/knockoff` | 730.0 | 1460 | 2d | Other |
| `x4gKing/X4G` | 692.0 | 2768 | 4d | Other |
| `baidu/Unlimited-OCR` | 688.1 | 13762 | 20d | Other |
| `elder-plinius/T3MP3ST` | 666.2 | 3997 | 6d | AI/ML |
| `langchain-ai/openwiki` | 620.8 | 9933 | 16d | AI/ML |
| `deepseek-ai/DeepSpec` | 540.4 | 6485 | 12d | Other |
| `Robbyant/lingbot-video` | 443.0 | 443 | 1d | Other |
| `Robbyant/lingbot-world-v2` | 420.0 | 420 | 1d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 403 | 661 | 204 | 90 | 44.7 | 7.2 |
| Web | 231 | 179 | 151 | 4 | 17.2 | 0.4 |
| Other | 209 | 582 | 276 | 112 | 63.6 | 11.0 |
| Data | 37 | 242 | 151 | 10 | 19.9 | 1.5 |
| Mobile | 26 | 582 | 264 | 40 | 49.9 | 7.9 |
| Finance/Trading | 23 | 220 | 154 | 625 | 22.3 | 0.4 |
| CLI/Tooling | 22 | 586 | 280 | 45 | 54.4 | 3.0 |
| DevOps | 20 | 282 | 177 | 12 | 21.0 | 5.2 |
| Security | 16 | 572 | 216 | 146 | 32.9 | 5.5 |
| Game | 13 | 221 | 193 | 17 | 23.3 | 3.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.455 |         0.166 |      0.102 |
| forks       |   0.455 |   1     |         0.113 |      0.041 |
| open_issues |   0.166 |   0.113 |         1     |      0.073 |
| age_days    |   0.102 |   0.041 |         0.073 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.768 |         0.562 |      0.356 |
| forks       |   0.768 |   1     |         0.595 |      0.399 |
| open_issues |   0.562 |   0.595 |         1     |      0.302 |
| age_days    |   0.356 |   0.399 |         0.302 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 68 |
| `ai-agents` | 62 |
| `llm` | 62 |
| `claude` | 57 |
| `ai` | 53 |
| `manga` | 47 |
| `manga-downloader` | 47 |
| `claude-opus` | 47 |
| `python` | 46 |
| `anthropic` | 39 |
| `typescript` | 36 |
| `codex` | 35 |
| `developer-tools` | 34 |
| `open-source` | 34 |
| `mcp` | 31 |
| `cli` | 30 |
| `macos` | 30 |
| `ai-agent` | 28 |
| `hentai` | 27 |
| `manga-reader` | 26 |
