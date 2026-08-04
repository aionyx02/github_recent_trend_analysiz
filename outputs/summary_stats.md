# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 481.4 | 207.5 | 24075 |
| forks | 108.1 | 22.0 | 4563 |
| open_issues | 5.5 | 1.0 | 469 |
| stars_per_day | 42.7 | 13.3 | 2089 |
| age_days | 18.1 | 20.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 24075 | 4563 | Rust | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 13129 | 1300 | JavaScript | AI/ML |
| `andrewyng/openworker` | 12607 | 1698 | Python | Other |
| `yc-software/qm` | 10445 | 1109 | TypeScript | AI/ML |
| `img2threejs/img2threejs` | 9484 | 714 | Python | AI/ML |
| `unicity-aos/aos-ce` | 8574 | 17 | Rust | AI/ML |
| `openai/codex-security` | 8457 | 582 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 8013 | 598 | Unknown | Other |
| `oso95/scroll-world` | 7339 | 817 | JavaScript | Other |
| `drumih/turbo-fieldfare` | 4741 | 234 | Swift | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `yc-software/qm` | 2089.0 | 10445 | 5d | AI/ML |
| `trycompai/crm` | 1243.0 | 3729 | 3d | Other |
| `xai-org/grok-build` | 1203.8 | 24075 | 20d | AI/ML |
| `MoonshotAI/Kimi-K3` | 1144.7 | 8013 | 7d | Other |
| `bashalarmistalt/decimen-optical-transfer` | 1092.2 | 4369 | 4d | Other |
| `thebuggeddev/anatomy` | 912.0 | 912 | 1d | AI/ML |
| `andrewyng/openworker` | 900.5 | 12607 | 14d | Other |
| `FareedKhan-dev/kimi-k3-in-c` | 731.5 | 1463 | 2d | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 691.0 | 13129 | 19d | AI/ML |
| `imsai-sh/zhuzhiliao` | 634.5 | 1269 | 2d | Web |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 417 | 596 | 225 | 118 | 48.4 | 6.7 |
| Other | 338 | 460 | 194 | 101 | 43.8 | 4.9 |
| Web | 74 | 343 | 200 | 92 | 34.2 | 4.0 |
| Mobile | 43 | 319 | 185 | 23 | 33.2 | 4.4 |
| CLI/Tooling | 35 | 363 | 221 | 36 | 39.3 | 3.3 |
| Security | 30 | 292 | 181 | 68 | 18.2 | 11.8 |
| Finance/Trading | 18 | 198 | 140 | 698 | 13.0 | 0.4 |
| Game | 18 | 346 | 229 | 24 | 51.4 | 2.1 |
| DevOps | 15 | 251 | 236 | 26 | 15.8 | 2.7 |
| Data | 12 | 283 | 200 | 34 | 35.1 | 2.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.487 |         0.354 |     -0.014 |
| forks       |   0.487 |   1     |         0.12  |      0.084 |
| open_issues |   0.354 |   0.12  |         1     |     -0.017 |
| age_days    |  -0.014 |   0.084 |        -0.017 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.503 |         0.389 |      0.002 |
| forks       |   0.503 |   1     |         0.247 |      0.012 |
| open_issues |   0.389 |   0.247 |         1     |      0.045 |
| age_days    |   0.002 |   0.012 |         0.045 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 77 |
| `ai-agents` | 74 |
| `llm` | 72 |
| `codex` | 71 |
| `ai` | 56 |
| `developer-tools` | 46 |
| `typescript` | 44 |
| `claude` | 42 |
| `python` | 42 |
| `local-first` | 37 |
| `cli` | 33 |
| `agent-skills` | 33 |
| `mcp` | 32 |
| `react` | 29 |
| `macos` | 28 |
| `rust` | 28 |
| `windows` | 27 |
| `ai-agent` | 26 |
| `open-source` | 25 |
| `agent` | 25 |
