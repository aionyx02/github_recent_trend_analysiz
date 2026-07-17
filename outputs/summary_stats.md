# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 419.8 | 184.0 | 15186 |
| forks | 74.0 | 13.0 | 10526 |
| open_issues | 3.7 | 0.0 | 1198 |
| stars_per_day | 47.1 | 11.3 | 7480 |
| age_days | 17.1 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `JustVugg/colibri` | 15186 | 1333 | C | Game |
| `baidu/Unlimited-OCR` | 14366 | 1213 | Python | Other |
| `xai-org/grok-build` | 13921 | 2559 | Rust | AI/ML |
| `langchain-ai/openwiki` | 11997 | 825 | TypeScript | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 7480 | 818 | JavaScript | AI/ML |
| `deepseek-ai/DeepSpec` | 6680 | 607 | Python | Other |
| `x4gKing/X4G` | 5705 | 10526 | Python | Other |
| `Yu9191/wloc` | 5309 | 1001 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 4855 | 1016 | TypeScript | AI/ML |
| `zhongerxin/Cowart` | 4742 | 359 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `Fei-Away/Codex-Dream-Skin` | 7480.0 | 7480 | 1d | AI/ML |
| `xai-org/grok-build` | 6960.5 | 13921 | 2d | AI/ML |
| `JustVugg/colibri` | 1012.4 | 15186 | 15d | Game |
| `tandpfun/wardrobe` | 728.0 | 728 | 1d | AI/ML |
| `baidu/Unlimited-OCR` | 513.1 | 14366 | 28d | Other |
| `langchain-ai/openwiki` | 499.9 | 11997 | 24d | AI/ML |
| `CluvexStudio/Aether` | 487.0 | 974 | 2d | Other |
| `x4gKing/X4G` | 475.4 | 5705 | 12d | Other |
| `PengZhang64/circuit-framework` | 407.0 | 407 | 1d | AI/ML |
| `withmarbleapp/os-taxonomy` | 402.5 | 3220 | 8d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 385 | 463 | 209 | 61 | 71.4 | 2.7 |
| Web | 232 | 190 | 151 | 21 | 14.7 | 0.7 |
| Other | 221 | 581 | 280 | 151 | 46.2 | 9.9 |
| Data | 32 | 230 | 151 | 9 | 12.0 | 1.0 |
| Finance/Trading | 30 | 225 | 174 | 210 | 40.2 | 0.3 |
| Mobile | 26 | 426 | 236 | 42 | 37.1 | 5.6 |
| CLI/Tooling | 22 | 522 | 219 | 37 | 44.3 | 1.8 |
| Game | 19 | 1068 | 263 | 91 | 75.6 | 5.9 |
| Security | 19 | 466 | 210 | 97 | 46.5 | 1.2 |
| DevOps | 14 | 240 | 152 | 7 | 13.9 | 1.4 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.431 |         0.105 |     -0.009 |
| forks       |   0.431 |   1     |         0.031 |     -0.065 |
| open_issues |   0.105 |   0.031 |         1     |      0.01  |
| age_days    |  -0.009 |  -0.065 |         0.01  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.805 |         0.583 |     -0.002 |
| forks       |   0.805 |   1     |         0.588 |     -0.04  |
| open_issues |   0.583 |   0.588 |         1     |      0.085 |
| age_days    |  -0.002 |  -0.04  |         0.085 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 70 |
| `claude-code` | 66 |
| `ai-agents` | 63 |
| `claude` | 58 |
| `python` | 53 |
| `ai` | 51 |
| `claude-opus` | 48 |
| `manga` | 45 |
| `manga-downloader` | 45 |
| `typescript` | 44 |
| `codex` | 41 |
| `anthropic` | 38 |
| `cli` | 35 |
| `developer-tools` | 33 |
| `mcp` | 31 |
| `macos` | 29 |
| `hentai` | 27 |
| `rust` | 26 |
| `android` | 26 |
| `open-source` | 25 |
