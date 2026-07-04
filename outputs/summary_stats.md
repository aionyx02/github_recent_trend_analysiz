# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 458.7 | 174.0 | 73336 |
| forks | 48.9 | 9.0 | 3831 |
| open_issues | 4.6 | 0.0 | 711 |
| stars_per_day | 39.5 | 30.2 | 3492 |
| age_days | 13.3 | 11.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `DietrichGebert/ponytail` | 73336 | 3831 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 13205 | 1071 | Python | Other |
| `XiaomiMiMo/MiMo-Code` | 11384 | 1115 | TypeScript | AI/ML |
| `unicity-astrid/book` | 7533 | 31 | Perl | Security |
| `unicity-astrid/handbook` | 7481 | 42 | Unknown | Other |
| `shadcn/improve` | 6791 | 272 | Unknown | Other |
| `omnigent-ai/omnigent` | 6185 | 809 | Python | AI/ML |
| `deepseek-ai/DeepSpec` | 6097 | 515 | Python | Other |
| `cobusgreyling/loop-engineering` | 5472 | 712 | JavaScript | AI/ML |
| `diffusionstudio/lottie` | 4443 | 237 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 3492.2 | 73336 | 21d | AI/ML |
| `baidu/Unlimited-OCR` | 880.3 | 13205 | 15d | Other |
| `deepseek-ai/DeepSpec` | 871.0 | 6097 | 7d | Other |
| `xuchonglang/investing-for-beginners` | 559.0 | 559 | 1d | Other |
| `XiaomiMiMo/MiMo-Code` | 495.0 | 11384 | 23d | AI/ML |
| `uzairansaruzi/hermex` | 474.0 | 474 | 1d | AI/ML |
| `jamesob/local-llm` | 457.0 | 457 | 1d | CLI/Tooling |
| `mekos2772/ios-location-spoofer` | 424.3 | 1273 | 3d | Mobile |
| `jmerelnyc/Talos` | 421.0 | 421 | 1d | AI/ML |
| `asz798838958/FrciblyK12` | 391.0 | 391 | 1d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 381 | 620 | 201 | 73 | 44.4 | 7.2 |
| Web | 245 | 177 | 151 | 5 | 30.3 | 0.2 |
| Other | 214 | 537 | 238 | 55 | 42.7 | 5.4 |
| Data | 38 | 296 | 151 | 36 | 36.3 | 2.2 |
| CLI/Tooling | 24 | 483 | 236 | 38 | 55.9 | 5.7 |
| Mobile | 24 | 524 | 249 | 32 | 43.3 | 7.8 |
| DevOps | 20 | 232 | 162 | 9 | 21.9 | 3.8 |
| Security | 20 | 860 | 214 | 122 | 51.9 | 4.8 |
| Finance/Trading | 19 | 199 | 151 | 124 | 27.3 | 0.2 |
| Game | 15 | 223 | 179 | 8 | 17.3 | 1.4 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.671 |         0.301 |      0.089 |
| forks       |   0.671 |   1     |         0.314 |      0.106 |
| open_issues |   0.301 |   0.314 |         1     |      0.127 |
| age_days    |   0.089 |   0.106 |         0.127 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.773 |         0.554 |      0.586 |
| forks       |   0.773 |   1     |         0.617 |      0.638 |
| open_issues |   0.554 |   0.617 |         1     |      0.483 |
| age_days    |   0.586 |   0.638 |         0.483 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 63 |
| `llm` | 55 |
| `claude` | 54 |
| `ai-agents` | 52 |
| `ai` | 51 |
| `claude-opus` | 49 |
| `manga-downloader` | 47 |
| `manga` | 46 |
| `python` | 45 |
| `anthropic` | 39 |
| `codex` | 35 |
| `typescript` | 34 |
| `open-source` | 33 |
| `macos` | 30 |
| `developer-tools` | 29 |
| `cli` | 29 |
| `android` | 29 |
| `video-download-tool` | 28 |
| `hentai` | 28 |
| `manga-reader` | 25 |
