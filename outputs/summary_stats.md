# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 429.6 | 187.0 | 17309 |
| forks | 74.9 | 14.0 | 10400 |
| open_issues | 4.0 | 0.0 | 1204 |
| stars_per_day | 42.3 | 11.4 | 5770 |
| age_days | 17.5 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 17309 | 3170 | Rust | AI/ML |
| `JustVugg/colibri` | 15803 | 1421 | C | Game |
| `baidu/Unlimited-OCR` | 14405 | 1221 | Python | Other |
| `langchain-ai/openwiki` | 12197 | 840 | TypeScript | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 9144 | 968 | JavaScript | AI/ML |
| `deepseek-ai/DeepSpec` | 6687 | 613 | Python | Other |
| `x4gKing/X4G` | 5663 | 10400 | Python | Other |
| `Yu9191/wloc` | 5429 | 1038 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 4910 | 1027 | TypeScript | AI/ML |
| `zhongerxin/Cowart` | 4775 | 363 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `xai-org/grok-build` | 5769.7 | 17309 | 3d | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 4572.0 | 9144 | 2d | AI/ML |
| `JustVugg/colibri` | 987.7 | 15803 | 16d | Game |
| `tandpfun/wardrobe` | 938.0 | 938 | 1d | AI/ML |
| `baidu/Unlimited-OCR` | 496.7 | 14405 | 29d | Other |
| `langchain-ai/openwiki` | 487.9 | 12197 | 25d | AI/ML |
| `PengZhang64/circuit-framework` | 479.0 | 479 | 1d | AI/ML |
| `pablostanley/yoinks` | 476.0 | 476 | 1d | CLI/Tooling |
| `x4gKing/X4G` | 435.6 | 5663 | 13d | Other |
| `nethical6/conversation-steganography` | 395.0 | 395 | 1d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 387 | 478 | 209 | 62 | 60.6 | 3.0 |
| Web | 225 | 192 | 151 | 21 | 13.6 | 0.8 |
| Other | 224 | 583 | 278 | 144 | 44.2 | 9.9 |
| Data | 33 | 229 | 151 | 9 | 11.6 | 1.0 |
| Finance/Trading | 30 | 231 | 186 | 266 | 32.0 | 0.3 |
| Mobile | 29 | 407 | 193 | 39 | 39.2 | 5.4 |
| CLI/Tooling | 24 | 482 | 195 | 33 | 52.7 | 2.1 |
| Security | 19 | 469 | 211 | 98 | 37.2 | 1.3 |
| Game | 17 | 1226 | 271 | 108 | 78.2 | 7.6 |
| DevOps | 12 | 252 | 152 | 7 | 14.1 | 1.5 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.451 |         0.107 |     -0.012 |
| forks       |   0.451 |   1     |         0.033 |     -0.058 |
| open_issues |   0.107 |   0.033 |         1     |      0.01  |
| age_days    |  -0.012 |  -0.058 |         0.01  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.812 |         0.585 |     -0.032 |
| forks       |   0.812 |   1     |         0.581 |     -0.082 |
| open_issues |   0.585 |   0.581 |         1     |      0.044 |
| age_days    |  -0.032 |  -0.082 |         0.044 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 74 |
| `ai-agents` | 65 |
| `claude-code` | 65 |
| `claude` | 56 |
| `ai` | 54 |
| `python` | 53 |
| `codex` | 45 |
| `claude-opus` | 44 |
| `manga` | 44 |
| `typescript` | 43 |
| `manga-downloader` | 43 |
| `cli` | 35 |
| `anthropic` | 35 |
| `developer-tools` | 34 |
| `mcp` | 32 |
| `macos` | 30 |
| `android` | 27 |
| `rust` | 26 |
| `hentai` | 26 |
| `open-source` | 23 |
