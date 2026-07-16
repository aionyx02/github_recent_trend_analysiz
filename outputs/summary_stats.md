# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 408.0 | 182.0 | 14533 |
| forks | 68.0 | 12.0 | 10176 |
| open_issues | 4.0 | 0.0 | 1196 |
| stars_per_day | 42.8 | 11.3 | 7728 |
| age_days | 16.8 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `JustVugg/colibri` | 14533 | 1241 | C | Game |
| `baidu/Unlimited-OCR` | 14304 | 1207 | Python | Other |
| `langchain-ai/openwiki` | 11709 | 808 | TypeScript | AI/ML |
| `xai-org/grok-build` | 7728 | 1214 | Rust | AI/ML |
| `deepseek-ai/DeepSpec` | 6668 | 603 | Python | Other |
| `x4gKing/X4G` | 5517 | 10176 | Python | Other |
| `Yu9191/wloc` | 5037 | 957 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 4807 | 1009 | TypeScript | AI/ML |
| `zhongerxin/Cowart` | 4672 | 354 | JavaScript | Other |
| `bikini/exploitarium` | 3934 | 1137 | Python | Security |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `xai-org/grok-build` | 7728.0 | 7728 | 1d | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 2620.0 | 2620 | 1d | AI/ML |
| `JustVugg/colibri` | 1038.1 | 14533 | 14d | Game |
| `CluvexStudio/Aether` | 590.0 | 590 | 1d | Other |
| `baidu/Unlimited-OCR` | 529.8 | 14304 | 27d | Other |
| `littledivy/mimic` | 528.5 | 1057 | 2d | Other |
| `langchain-ai/openwiki` | 509.1 | 11709 | 23d | AI/ML |
| `x4gKing/X4G` | 501.5 | 5517 | 11d | Other |
| `withmarbleapp/os-taxonomy` | 450.9 | 3156 | 7d | Other |
| `MatinSenPai/Aether-GUI` | 413.0 | 413 | 1d | Web |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 380 | 439 | 206 | 55 | 57.8 | 3.5 |
| Web | 236 | 186 | 151 | 20 | 15.7 | 0.6 |
| Other | 225 | 573 | 275 | 148 | 50.1 | 9.6 |
| Data | 33 | 244 | 151 | 10 | 13.0 | 1.6 |
| Finance/Trading | 26 | 224 | 156 | 133 | 27.4 | 0.3 |
| Mobile | 25 | 419 | 234 | 42 | 41.7 | 5.7 |
| Security | 21 | 432 | 178 | 88 | 44.2 | 1.1 |
| CLI/Tooling | 20 | 552 | 250 | 39 | 49.9 | 1.6 |
| Game | 19 | 1026 | 262 | 83 | 77.4 | 5.5 |
| DevOps | 15 | 290 | 153 | 10 | 16.2 | 1.5 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.4   |         0.124 |      0.028 |
| forks       |   0.4   |   1     |         0.033 |     -0.063 |
| open_issues |   0.124 |   0.033 |         1     |      0.028 |
| age_days    |   0.028 |  -0.063 |         0.028 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.81  |         0.595 |      0.044 |
| forks       |   0.81  |   1     |         0.597 |      0.02  |
| open_issues |   0.595 |   0.597 |         1     |      0.115 |
| age_days    |   0.044 |   0.02  |         0.115 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 68 |
| `claude-code` | 66 |
| `ai-agents` | 64 |
| `claude` | 56 |
| `python` | 52 |
| `ai` | 51 |
| `claude-opus` | 48 |
| `manga` | 46 |
| `manga-downloader` | 46 |
| `typescript` | 43 |
| `codex` | 41 |
| `anthropic` | 38 |
| `cli` | 34 |
| `mcp` | 32 |
| `developer-tools` | 32 |
| `android` | 27 |
| `hentai` | 27 |
| `open-source` | 26 |
| `macos` | 26 |
| `manga-reader` | 26 |
