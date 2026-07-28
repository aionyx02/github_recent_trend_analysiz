# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 453.4 | 195.5 | 23132 |
| forks | 89.0 | 14.0 | 12647 |
| open_issues | 4.6 | 0.0 | 954 |
| stars_per_day | 35.5 | 10.7 | 2646 |
| age_days | 21.4 | 24.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 23132 | 4370 | Rust | AI/ML |
| `JustVugg/colibri` | 20312 | 2042 | C | Game |
| `Fei-Away/Codex-Dream-Skin` | 12516 | 1253 | JavaScript | AI/ML |
| `andrewyng/openworker` | 9481 | 1225 | Python | Other |
| `unicity-aos/aos-ce` | 7634 | 12 | Rust | AI/ML |
| `img2threejs/img2threejs` | 7250 | 555 | Python | AI/ML |
| `x4gKing/X4G` | 6910 | 12647 | Python | Other |
| `oso95/scroll-world` | 5559 | 640 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 5268 | 1089 | TypeScript | AI/ML |
| `withmarbleapp/os-taxonomy` | 3704 | 642 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `MoonshotAI/Kimi-K3` | 2646.0 | 2646 | 1d | Other |
| `xai-org/grok-build` | 1779.4 | 23132 | 13d | AI/ML |
| `andrewyng/openworker` | 1354.4 | 9481 | 7d | Other |
| `Fei-Away/Codex-Dream-Skin` | 1043.0 | 12516 | 12d | AI/ML |
| `JustVugg/colibri` | 781.2 | 20312 | 26d | Game |
| `img2threejs/img2threejs` | 604.2 | 7250 | 12d | AI/ML |
| `0xwilliamortiz/openclaude-improved` | 577.0 | 577 | 1d | AI/ML |
| `mshumer/Claude-of-Duty` | 550.5 | 1101 | 2d | Other |
| `unicity-aos/aos-ce` | 508.9 | 7634 | 15d | AI/ML |
| `slvDev/esp32-ai` | 467.5 | 1870 | 4d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 386 | 548 | 225 | 64 | 41.9 | 4.3 |
| Web | 231 | 206 | 151 | 21 | 9.9 | 0.8 |
| Other | 213 | 578 | 268 | 186 | 59.1 | 10.6 |
| Mobile | 31 | 432 | 244 | 42 | 27.7 | 6.0 |
| Finance/Trading | 30 | 226 | 176 | 459 | 16.5 | 1.2 |
| Data | 30 | 253 | 151 | 14 | 12.1 | 0.4 |
| CLI/Tooling | 24 | 387 | 233 | 29 | 32.8 | 2.1 |
| Security | 23 | 255 | 184 | 48 | 29.2 | 4.2 |
| DevOps | 18 | 205 | 163 | 12 | 11.7 | 0.9 |
| Game | 14 | 1758 | 272 | 163 | 75.4 | 8.4 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.45  |         0.139 |     -0.115 |
| forks       |   0.45  |   1     |         0.044 |     -0.051 |
| open_issues |   0.139 |   0.044 |         1     |     -0.04  |
| age_days    |  -0.115 |  -0.051 |        -0.04  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.829 |         0.594 |     -0.634 |
| forks       |   0.829 |   1     |         0.575 |     -0.654 |
| open_issues |   0.594 |   0.575 |         1     |     -0.416 |
| age_days    |  -0.634 |  -0.654 |        -0.416 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 73 |
| `llm` | 70 |
| `python` | 65 |
| `ai-agents` | 59 |
| `claude` | 55 |
| `codex` | 52 |
| `claude-opus` | 47 |
| `typescript` | 45 |
| `manga-downloader` | 43 |
| `ai` | 42 |
| `manga` | 42 |
| `developer-tools` | 35 |
| `anthropic` | 35 |
| `cli` | 34 |
| `windows` | 32 |
| `mcp` | 31 |
| `macos` | 30 |
| `ai-agent` | 27 |
| `local-first` | 27 |
| `android` | 26 |
