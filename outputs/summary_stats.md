# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 413.3 | 190.0 | 19451 |
| forks | 76.7 | 14.0 | 10628 |
| open_issues | 3.9 | 0.0 | 1194 |
| stars_per_day | 38.1 | 11.3 | 4863 |
| age_days | 17.9 | 20.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 19451 | 3499 | Rust | AI/ML |
| `JustVugg/colibri` | 16216 | 1470 | C | Game |
| `langchain-ai/openwiki` | 12355 | 852 | TypeScript | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 9974 | 1036 | JavaScript | AI/ML |
| `deepseek-ai/DeepSpec` | 6694 | 614 | Python | Other |
| `x4gKing/X4G` | 5770 | 10628 | Python | Other |
| `Yu9191/wloc` | 5657 | 1096 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 4961 | 1035 | TypeScript | AI/ML |
| `bikini/exploitarium` | 3966 | 1139 | Python | Security |
| `baairon/torlink` | 3680 | 245 | TypeScript | CLI/Tooling |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `xai-org/grok-build` | 4862.8 | 19451 | 4d | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 3324.7 | 9974 | 3d | AI/ML |
| `JustVugg/colibri` | 953.9 | 16216 | 17d | Game |
| `nethical6/conversation-steganography` | 742.0 | 742 | 1d | Other |
| `tandpfun/wardrobe` | 542.0 | 1084 | 2d | AI/ML |
| `langchain-ai/openwiki` | 475.2 | 12355 | 26d | AI/ML |
| `x4gKing/X4G` | 412.1 | 5770 | 14d | Other |
| `withmarbleapp/os-taxonomy` | 328.7 | 3287 | 10d | Other |
| `lopopolo/harness-engineering` | 327.0 | 327 | 1d | AI/ML |
| `CluvexStudio/Aether` | 318.0 | 1272 | 4d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 388 | 479 | 210 | 62 | 52.3 | 3.0 |
| Web | 227 | 194 | 151 | 22 | 13.5 | 0.8 |
| Other | 221 | 503 | 269 | 148 | 41.1 | 9.6 |
| Mobile | 30 | 413 | 254 | 41 | 40.1 | 5.3 |
| Data | 30 | 233 | 151 | 10 | 11.5 | 0.4 |
| Finance/Trading | 30 | 227 | 193 | 278 | 22.7 | 0.3 |
| CLI/Tooling | 26 | 488 | 206 | 44 | 41.6 | 2.1 |
| Security | 19 | 469 | 212 | 102 | 46.2 | 1.5 |
| Game | 17 | 1258 | 272 | 112 | 75.1 | 7.9 |
| DevOps | 12 | 254 | 152 | 7 | 13.4 | 0.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.455 |         0.108 |     -0.055 |
| forks       |   0.455 |   1     |         0.031 |     -0.069 |
| open_issues |   0.108 |   0.031 |         1     |      0.008 |
| age_days    |  -0.055 |  -0.069 |         0.008 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.806 |         0.586 |     -0.1   |
| forks       |   0.806 |   1     |         0.576 |     -0.138 |
| open_issues |   0.586 |   0.576 |         1     |      0.016 |
| age_days    |  -0.1   |  -0.138 |         0.016 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 72 |
| `claude-code` | 66 |
| `ai-agents` | 65 |
| `claude` | 56 |
| `python` | 54 |
| `ai` | 52 |
| `codex` | 45 |
| `claude-opus` | 44 |
| `manga` | 44 |
| `manga-downloader` | 43 |
| `typescript` | 42 |
| `anthropic` | 35 |
| `cli` | 34 |
| `developer-tools` | 32 |
| `mcp` | 31 |
| `macos` | 29 |
| `android` | 27 |
| `hentai` | 26 |
| `rust` | 25 |
| `open-source` | 23 |
