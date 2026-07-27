# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 440.8 | 192.5 | 22892 |
| forks | 85.5 | 12.0 | 12527 |
| open_issues | 4.2 | 0.0 | 954 |
| stars_per_day | 33.3 | 10.6 | 1908 |
| age_days | 19.3 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 22892 | 4316 | Rust | AI/ML |
| `JustVugg/colibri` | 19834 | 1991 | C | Game |
| `Fei-Away/Codex-Dream-Skin` | 12414 | 1252 | JavaScript | AI/ML |
| `andrewyng/openworker` | 7635 | 1025 | Python | Other |
| `unicity-aos/aos-ce` | 7533 | 12 | Rust | AI/ML |
| `x4gKing/X4G` | 6829 | 12527 | Python | Other |
| `img2threejs/img2threejs` | 6418 | 490 | Python | AI/ML |
| `oso95/scroll-world` | 5414 | 625 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 5243 | 1085 | TypeScript | AI/ML |
| `withmarbleapp/os-taxonomy` | 3691 | 639 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `xai-org/grok-build` | 1907.7 | 22892 | 12d | AI/ML |
| `andrewyng/openworker` | 1272.5 | 7635 | 6d | Other |
| `Fei-Away/Codex-Dream-Skin` | 1128.5 | 12414 | 11d | AI/ML |
| `mshumer/Claude-of-Duty` | 825.0 | 825 | 1d | Other |
| `JustVugg/colibri` | 793.4 | 19834 | 25d | Game |
| `img2threejs/img2threejs` | 583.5 | 6418 | 11d | AI/ML |
| `unicity-aos/aos-ce` | 538.1 | 7533 | 14d | AI/ML |
| `slvDev/esp32-ai` | 520.0 | 1560 | 3d | Other |
| `VictorTaelin/OptMem` | 478.0 | 478 | 1d | AI/ML |
| `mikiarlo3/ai-copywriter` | 440.0 | 880 | 2d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 382 | 536 | 220 | 63 | 41.7 | 4.1 |
| Other | 304 | 434 | 203 | 124 | 35.9 | 6.9 |
| Web | 118 | 252 | 153 | 36 | 14.2 | 1.6 |
| Mobile | 43 | 344 | 193 | 29 | 23.1 | 3.8 |
| Security | 34 | 225 | 176 | 30 | 18.2 | 0.6 |
| Finance/Trading | 32 | 227 | 186 | 416 | 20.2 | 1.2 |
| CLI/Tooling | 29 | 357 | 206 | 34 | 30.9 | 2.0 |
| Game | 26 | 996 | 174 | 85 | 43.7 | 4.0 |
| Data | 20 | 303 | 164 | 20 | 18.1 | 1.1 |
| DevOps | 12 | 201 | 186 | 13 | 13.5 | 1.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.452 |         0.111 |     -0.066 |
| forks       |   0.452 |   1     |         0.037 |     -0.018 |
| open_issues |   0.111 |   0.037 |         1     |     -0.007 |
| age_days    |  -0.066 |  -0.018 |        -0.007 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.762 |         0.558 |     -0.335 |
| forks       |   0.762 |   1     |         0.583 |     -0.292 |
| open_issues |   0.558 |   0.583 |         1     |     -0.153 |
| age_days    |  -0.335 |  -0.292 |        -0.153 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 64 |
| `claude-code` | 59 |
| `ai-agents` | 54 |
| `codex` | 49 |
| `claude` | 49 |
| `python` | 44 |
| `ai` | 42 |
| `typescript` | 39 |
| `mcp` | 32 |
| `ai-agent` | 30 |
| `developer-tools` | 27 |
| `local-first` | 27 |
| `windows` | 27 |
| `cli` | 25 |
| `macos` | 25 |
| `manga-downloader` | 25 |
| `anthropic` | 24 |
| `agent-skills` | 23 |
| `claude-opus` | 23 |
| `manga` | 23 |
