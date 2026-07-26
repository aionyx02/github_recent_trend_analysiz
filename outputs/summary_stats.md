# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 435.2 | 196.5 | 22597 |
| forks | 87.0 | 14.0 | 12363 |
| open_issues | 4.1 | 0.0 | 952 |
| stars_per_day | 32.7 | 10.7 | 2054 |
| age_days | 20.7 | 23.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 22597 | 4265 | Rust | AI/ML |
| `JustVugg/colibri` | 19234 | 1915 | C | Game |
| `Fei-Away/Codex-Dream-Skin` | 12318 | 1238 | JavaScript | AI/ML |
| `unicity-aos/aos-ce` | 7324 | 12 | Rust | AI/ML |
| `deepseek-ai/DeepSpec` | 6769 | 629 | Python | Other |
| `x4gKing/X4G` | 6730 | 12363 | Python | Other |
| `andrewyng/openworker` | 5595 | 754 | Python | Other |
| `oso95/scroll-world` | 5263 | 610 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 5200 | 1080 | TypeScript | AI/ML |
| `img2threejs/img2threejs` | 5049 | 381 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `xai-org/grok-build` | 2054.3 | 22597 | 11d | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 1231.8 | 12318 | 10d | AI/ML |
| `andrewyng/openworker` | 1119.0 | 5595 | 5d | Other |
| `JustVugg/colibri` | 801.4 | 19234 | 24d | Game |
| `mikiarlo3/ai-copywriter` | 703.0 | 703 | 1d | AI/ML |
| `unicity-aos/aos-ce` | 563.4 | 7324 | 13d | AI/ML |
| `img2threejs/img2threejs` | 504.9 | 5049 | 10d | AI/ML |
| `slvDev/esp32-ai` | 494.5 | 989 | 2d | Other |
| `melloworchid8rr6g/TG-Polymarket-bot` | 390.0 | 390 | 1d | Finance/Trading |
| `mikehasa/agentacct` | 341.0 | 341 | 1d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 386 | 522 | 219 | 62 | 41.0 | 3.7 |
| Other | 227 | 532 | 252 | 162 | 43.2 | 9.2 |
| Web | 224 | 203 | 151 | 19 | 10.7 | 0.8 |
| Data | 31 | 235 | 151 | 9 | 12.4 | 0.6 |
| Finance/Trading | 30 | 230 | 204 | 538 | 32.7 | 1.2 |
| Mobile | 27 | 434 | 228 | 45 | 30.5 | 5.5 |
| CLI/Tooling | 26 | 388 | 232 | 40 | 30.4 | 3.0 |
| Security | 19 | 269 | 193 | 52 | 23.8 | 1.1 |
| Game | 16 | 1506 | 270 | 138 | 67.3 | 7.6 |
| DevOps | 14 | 186 | 156 | 9 | 12.4 | 0.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.442 |         0.095 |     -0.106 |
| forks       |   0.442 |   1     |         0.031 |     -0.048 |
| open_issues |   0.095 |   0.031 |         1     |     -0.032 |
| age_days    |  -0.106 |  -0.048 |        -0.032 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.805 |         0.589 |     -0.503 |
| forks       |   0.805 |   1     |         0.574 |     -0.5   |
| open_issues |   0.589 |   0.574 |         1     |     -0.308 |
| age_days    |  -0.503 |  -0.5   |        -0.308 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 70 |
| `llm` | 65 |
| `python` | 61 |
| `ai-agents` | 58 |
| `codex` | 52 |
| `claude` | 52 |
| `ai` | 45 |
| `typescript` | 45 |
| `manga-downloader` | 44 |
| `claude-opus` | 43 |
| `manga` | 42 |
| `mcp` | 36 |
| `developer-tools` | 35 |
| `cli` | 34 |
| `macos` | 30 |
| `anthropic` | 30 |
| `windows` | 28 |
| `local-first` | 26 |
| `rust` | 26 |
| `android` | 26 |
