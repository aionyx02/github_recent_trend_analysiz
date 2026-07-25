# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 427.9 | 190.0 | 22407 |
| forks | 84.3 | 12.0 | 12193 |
| open_issues | 3.8 | 0.0 | 954 |
| stars_per_day | 32.0 | 10.4 | 2241 |
| age_days | 20.4 | 23.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 22407 | 4233 | Rust | AI/ML |
| `JustVugg/colibri` | 18750 | 1837 | C | Game |
| `Fei-Away/Codex-Dream-Skin` | 12262 | 1231 | JavaScript | AI/ML |
| `unicity-aos/aos-ce` | 7186 | 10 | Rust | AI/ML |
| `deepseek-ai/DeepSpec` | 6765 | 628 | Python | Other |
| `x4gKing/X4G` | 6625 | 12193 | Python | Other |
| `elder-plinius/T3MP3ST` | 5171 | 1071 | TypeScript | AI/ML |
| `oso95/scroll-world` | 5147 | 595 | JavaScript | Other |
| `img2threejs/img2threejs` | 4265 | 317 | Python | AI/ML |
| `baairon/torlink` | 3818 | 251 | TypeScript | CLI/Tooling |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `xai-org/grok-build` | 2240.7 | 22407 | 10d | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 1362.4 | 12262 | 9d | AI/ML |
| `andrewyng/openworker` | 936.0 | 3744 | 4d | Other |
| `JustVugg/colibri` | 815.2 | 18750 | 23d | Game |
| `unicity-aos/aos-ce` | 598.8 | 7186 | 12d | AI/ML |
| `slvDev/esp32-ai` | 538.0 | 538 | 1d | Other |
| `img2threejs/img2threejs` | 473.9 | 4265 | 9d | AI/ML |
| `lopopolo/harness-engineering` | 389.3 | 2336 | 6d | AI/ML |
| `x4gKing/X4G` | 331.2 | 6625 | 20d | Other |
| `Jakubantalik/thinking-orbs` | 314.7 | 944 | 3d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 387 | 506 | 213 | 61 | 40.9 | 3.2 |
| Web | 227 | 200 | 151 | 18 | 10.3 | 0.8 |
| Other | 221 | 522 | 252 | 157 | 40.1 | 8.8 |
| Data | 30 | 231 | 151 | 9 | 11.7 | 0.3 |
| Finance/Trading | 30 | 231 | 204 | 530 | 27.1 | 1.0 |
| Mobile | 29 | 429 | 266 | 44 | 32.2 | 5.3 |
| CLI/Tooling | 26 | 533 | 264 | 51 | 41.4 | 3.1 |
| Security | 19 | 266 | 191 | 52 | 26.6 | 0.8 |
| Game | 17 | 1393 | 253 | 125 | 65.7 | 8.0 |
| DevOps | 14 | 186 | 156 | 5 | 9.4 | 0.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.44  |         0.091 |     -0.112 |
| forks       |   0.44  |   1     |         0.029 |     -0.058 |
| open_issues |   0.091 |   0.029 |         1     |     -0.019 |
| age_days    |  -0.112 |  -0.058 |        -0.019 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.809 |         0.589 |     -0.484 |
| forks       |   0.809 |   1     |         0.585 |     -0.482 |
| open_issues |   0.589 |   0.585 |         1     |     -0.288 |
| age_days    |  -0.484 |  -0.482 |        -0.288 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 69 |
| `llm` | 66 |
| `python` | 63 |
| `ai-agents` | 58 |
| `claude` | 56 |
| `codex` | 51 |
| `claude-opus` | 47 |
| `typescript` | 45 |
| `manga-downloader` | 44 |
| `manga` | 43 |
| `ai` | 42 |
| `mcp` | 35 |
| `cli` | 33 |
| `developer-tools` | 33 |
| `anthropic` | 33 |
| `macos` | 31 |
| `windows` | 28 |
| `local-first` | 26 |
| `rust` | 26 |
| `hentai` | 26 |
