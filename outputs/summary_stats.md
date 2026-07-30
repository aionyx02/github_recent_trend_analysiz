# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 469.1 | 198.0 | 23473 |
| forks | 120.6 | 21.0 | 12888 |
| open_issues | 5.0 | 1.0 | 317 |
| stars_per_day | 39.6 | 12.7 | 3482 |
| age_days | 17.7 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 23473 | 4462 | Rust | AI/ML |
| `JustVugg/colibri` | 21073 | 2167 | C | Game |
| `Fei-Away/Codex-Dream-Skin` | 12731 | 1271 | JavaScript | AI/ML |
| `andrewyng/openworker` | 10801 | 1428 | Python | Other |
| `img2threejs/img2threejs` | 8348 | 638 | Python | AI/ML |
| `unicity-aos/aos-ce` | 8022 | 14 | Rust | AI/ML |
| `x4gKing/X4G` | 7050 | 12888 | Python | Other |
| `MoonshotAI/Kimi-K3` | 6963 | 467 | Unknown | Other |
| `oso95/scroll-world` | 5892 | 692 | JavaScript | Other |
| `openai/codex-security` | 5481 | 357 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `MoonshotAI/Kimi-K3` | 3481.5 | 6963 | 2d | Other |
| `xai-org/grok-build` | 1564.9 | 23473 | 15d | AI/ML |
| `andrewyng/openworker` | 1200.1 | 10801 | 9d | Other |
| `Fei-Away/Codex-Dream-Skin` | 909.4 | 12731 | 14d | AI/ML |
| `JustVugg/colibri` | 752.6 | 21073 | 28d | Game |
| `xikhar/persona` | 604.0 | 604 | 1d | Other |
| `img2threejs/img2threejs` | 596.3 | 8348 | 14d | AI/ML |
| `mshumer/Claude-of-Duty` | 575.8 | 2303 | 4d | Other |
| `0xwilliamortiz/ponytail-improved` | 555.0 | 555 | 1d | AI/ML |
| `talivia-group/talivia` | 482.0 | 482 | 1d | Data |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 406 | 552 | 222 | 121 | 41.3 | 5.6 |
| Other | 348 | 432 | 182 | 130 | 45.7 | 4.9 |
| Web | 71 | 333 | 202 | 93 | 24.0 | 4.3 |
| Mobile | 47 | 360 | 175 | 33 | 29.2 | 5.4 |
| CLI/Tooling | 31 | 338 | 206 | 27 | 29.7 | 3.1 |
| Security | 29 | 257 | 182 | 54 | 22.2 | 4.2 |
| Game | 19 | 1375 | 225 | 130 | 55.6 | 7.5 |
| Finance/Trading | 18 | 183 | 140 | 698 | 13.8 | 2.1 |
| DevOps | 16 | 215 | 185 | 19 | 15.9 | 1.2 |
| Data | 15 | 229 | 131 | 21 | 48.1 | 1.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.434 |         0.332 |      0.011 |
| forks       |   0.434 |   1     |         0.09  |      0.043 |
| open_issues |   0.332 |   0.09  |         1     |     -0.012 |
| age_days    |   0.011 |   0.043 |        -0.012 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.519 |         0.362 |      0.035 |
| forks       |   0.519 |   1     |         0.245 |     -0.018 |
| open_issues |   0.362 |   0.245 |         1     |      0.026 |
| age_days    |   0.035 |  -0.018 |         0.026 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 72 |
| `ai-agents` | 70 |
| `codex` | 68 |
| `llm` | 66 |
| `ai` | 45 |
| `claude` | 44 |
| `python` | 42 |
| `developer-tools` | 42 |
| `typescript` | 39 |
| `local-first` | 39 |
| `cli` | 36 |
| `mcp` | 35 |
| `agent-skills` | 31 |
| `macos` | 31 |
| `windows` | 30 |
| `rust` | 29 |
| `ai-agent` | 27 |
| `desktop-app` | 25 |
| `react` | 23 |
| `agent` | 22 |
