# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 429.0 | 193.0 | 21081 |
| forks | 80.8 | 14.0 | 11059 |
| open_issues | 4.0 | 0.0 | 1192 |
| stars_per_day | 34.8 | 11.4 | 3514 |
| age_days | 18.8 | 22.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 21081 | 3900 | Rust | AI/ML |
| `JustVugg/colibri` | 17166 | 1589 | C | Game |
| `langchain-ai/openwiki` | 12692 | 881 | TypeScript | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 11330 | 1152 | JavaScript | AI/ML |
| `deepseek-ai/DeepSpec` | 6714 | 621 | Python | Other |
| `x4gKing/X4G` | 6026 | 11059 | Python | Other |
| `Yu9191/wloc` | 5885 | 1162 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 5052 | 1038 | TypeScript | AI/ML |
| `oso95/scroll-world` | 4528 | 529 | JavaScript | Other |
| `unicity-aos/aos-ce` | 4289 | 3 | Rust | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `xai-org/grok-build` | 3513.5 | 21081 | 6d | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 2266.0 | 11330 | 5d | AI/ML |
| `JustVugg/colibri` | 903.5 | 17166 | 19d | Game |
| `unicity-aos/aos-ce` | 536.1 | 4289 | 8d | AI/ML |
| `lopopolo/harness-engineering` | 477.0 | 954 | 2d | AI/ML |
| `langchain-ai/openwiki` | 453.3 | 12692 | 28d | AI/ML |
| `x4gKing/X4G` | 376.6 | 6026 | 16d | Other |
| `Blaizzy/nativ` | 358.0 | 358 | 1d | AI/ML |
| `oso95/scroll-world` | 323.4 | 4528 | 14d | Other |
| `tandpfun/wardrobe` | 309.0 | 1236 | 4d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 387 | 502 | 219 | 58 | 48.7 | 3.2 |
| Other | 229 | 516 | 269 | 146 | 37.4 | 9.7 |
| Web | 221 | 195 | 151 | 18 | 11.5 | 0.9 |
| Finance/Trading | 29 | 236 | 205 | 486 | 16.5 | 0.3 |
| CLI/Tooling | 28 | 478 | 214 | 43 | 38.0 | 2.4 |
| Data | 28 | 240 | 151 | 10 | 10.8 | 0.5 |
| Mobile | 28 | 441 | 260 | 43 | 33.3 | 5.2 |
| Security | 20 | 466 | 198 | 99 | 34.2 | 1.6 |
| Game | 17 | 1326 | 280 | 118 | 72.6 | 7.5 |
| DevOps | 13 | 185 | 153 | 6 | 12.1 | 0.5 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.447 |         0.108 |     -0.058 |
| forks       |   0.447 |   1     |         0.03  |     -0.068 |
| open_issues |   0.108 |   0.03  |         1     |      0.009 |
| age_days    |  -0.058 |  -0.068 |         0.009 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.813 |         0.59  |     -0.189 |
| forks       |   0.813 |   1     |         0.582 |     -0.213 |
| open_issues |   0.59  |   0.582 |         1     |     -0.045 |
| age_days    |  -0.189 |  -0.213 |        -0.045 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 66 |
| `claude-code` | 64 |
| `ai-agents` | 60 |
| `python` | 60 |
| `claude` | 53 |
| `typescript` | 47 |
| `codex` | 47 |
| `ai` | 44 |
| `manga-downloader` | 43 |
| `manga` | 43 |
| `claude-opus` | 43 |
| `cli` | 34 |
| `mcp` | 32 |
| `anthropic` | 32 |
| `macos` | 30 |
| `developer-tools` | 30 |
| `local-first` | 27 |
| `android` | 27 |
| `rust` | 26 |
| `ai-agent` | 25 |
