# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 418.8 | 191.0 | 20460 |
| forks | 78.1 | 14.0 | 10854 |
| open_issues | 3.9 | 0.0 | 1194 |
| stars_per_day | 35.2 | 11.1 | 4092 |
| age_days | 18.4 | 21.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 20460 | 3731 | Rust | AI/ML |
| `JustVugg/colibri` | 16611 | 1518 | C | Game |
| `langchain-ai/openwiki` | 12547 | 864 | TypeScript | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 10844 | 1110 | JavaScript | AI/ML |
| `deepseek-ai/DeepSpec` | 6701 | 618 | Python | Other |
| `x4gKing/X4G` | 5907 | 10854 | Python | Other |
| `Yu9191/wloc` | 5803 | 1139 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 5016 | 1039 | TypeScript | AI/ML |
| `oso95/scroll-world` | 4025 | 502 | JavaScript | Other |
| `bikini/exploitarium` | 3975 | 1139 | Python | Security |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `xai-org/grok-build` | 4092.0 | 20460 | 5d | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 2711.0 | 10844 | 4d | AI/ML |
| `JustVugg/colibri` | 922.8 | 16611 | 18d | Game |
| `lopopolo/harness-engineering` | 621.0 | 621 | 1d | AI/ML |
| `langchain-ai/openwiki` | 464.7 | 12547 | 27d | AI/ML |
| `xiejunjie524/handdraw-story-video` | 424.0 | 424 | 1d | Other |
| `nethical6/conversation-steganography` | 418.0 | 836 | 2d | Other |
| `x4gKing/X4G` | 393.8 | 5907 | 15d | Other |
| `tandpfun/wardrobe` | 392.0 | 1176 | 3d | AI/ML |
| `oso95/scroll-world` | 309.6 | 4025 | 13d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 382 | 489 | 214 | 57 | 48.7 | 3.0 |
| Web | 228 | 192 | 151 | 23 | 12.3 | 0.8 |
| Other | 223 | 513 | 271 | 145 | 38.5 | 9.7 |
| Mobile | 31 | 418 | 263 | 41 | 34.5 | 5.5 |
| Finance/Trading | 30 | 236 | 212 | 396 | 19.1 | 0.3 |
| Data | 29 | 237 | 151 | 10 | 11.1 | 0.5 |
| CLI/Tooling | 27 | 490 | 210 | 44 | 42.7 | 2.2 |
| Security | 20 | 462 | 204 | 98 | 38.0 | 1.6 |
| Game | 17 | 1289 | 277 | 116 | 72.4 | 8.9 |
| DevOps | 13 | 181 | 153 | 6 | 13.1 | 0.4 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.456 |         0.109 |     -0.061 |
| forks       |   0.456 |   1     |         0.031 |     -0.075 |
| open_issues |   0.109 |   0.031 |         1     |      0.008 |
| age_days    |  -0.061 |  -0.075 |         0.008 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.813 |         0.583 |     -0.152 |
| forks       |   0.813 |   1     |         0.58  |     -0.178 |
| open_issues |   0.583 |   0.58  |         1     |     -0.022 |
| age_days    |  -0.152 |  -0.178 |        -0.022 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 69 |
| `claude-code` | 62 |
| `ai-agents` | 59 |
| `python` | 57 |
| `claude` | 52 |
| `ai` | 45 |
| `codex` | 44 |
| `claude-opus` | 44 |
| `typescript` | 43 |
| `manga-downloader` | 43 |
| `manga` | 43 |
| `cli` | 35 |
| `anthropic` | 34 |
| `mcp` | 32 |
| `macos` | 30 |
| `developer-tools` | 30 |
| `android` | 27 |
| `local-first` | 26 |
| `rust` | 26 |
| `windows` | 24 |
