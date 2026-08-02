# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 469.5 | 200.0 | 23825 |
| forks | 120.7 | 22.0 | 13328 |
| open_issues | 5.1 | 1.0 | 350 |
| stars_per_day | 41.1 | 13.1 | 1854 |
| age_days | 18.0 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 23825 | 4526 | Rust | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 12954 | 1294 | JavaScript | AI/ML |
| `andrewyng/openworker` | 11717 | 1581 | Python | Other |
| `img2threejs/img2threejs` | 8991 | 686 | Python | AI/ML |
| `unicity-aos/aos-ce` | 8575 | 17 | Rust | AI/ML |
| `openai/codex-security` | 8037 | 537 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 7847 | 565 | Unknown | Other |
| `x4gKing/X4G` | 7273 | 13328 | Python | Other |
| `oso95/scroll-world` | 6922 | 786 | JavaScript | Other |
| `yc-software/qm` | 5563 | 576 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `yc-software/qm` | 1854.3 | 5563 | 3d | AI/ML |
| `bashalarmistalt/decimen-optical-transfer` | 1602.0 | 3204 | 2d | Other |
| `MoonshotAI/Kimi-K3` | 1569.4 | 7847 | 5d | Other |
| `xai-org/grok-build` | 1323.6 | 23825 | 18d | AI/ML |
| `trycompai/crm` | 1060.0 | 1060 | 1d | Other |
| `andrewyng/openworker` | 976.4 | 11717 | 12d | Other |
| `Fei-Away/Codex-Dream-Skin` | 762.0 | 12954 | 17d | AI/ML |
| `xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer` | 631.0 | 1262 | 2d | Other |
| `WilonityDev/WilonityLoader` | 532.0 | 532 | 1d | Game |
| `img2threejs/img2threejs` | 528.9 | 8991 | 17d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 407 | 578 | 212 | 119 | 42.8 | 5.7 |
| Other | 345 | 458 | 191 | 140 | 48.0 | 5.1 |
| Web | 72 | 338 | 195 | 89 | 25.0 | 4.0 |
| Mobile | 46 | 362 | 191 | 27 | 31.0 | 5.5 |
| CLI/Tooling | 33 | 365 | 221 | 34 | 37.6 | 2.6 |
| Security | 30 | 277 | 192 | 66 | 18.7 | 8.2 |
| Game | 20 | 254 | 198 | 18 | 63.5 | 2.4 |
| Finance/Trading | 17 | 180 | 140 | 721 | 11.0 | 0.4 |
| Data | 16 | 221 | 131 | 22 | 25.4 | 1.7 |
| DevOps | 14 | 244 | 230 | 21 | 15.6 | 1.5 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.424 |         0.35  |     -0.002 |
| forks       |   0.424 |   1     |         0.089 |      0.077 |
| open_issues |   0.35  |   0.089 |         1     |     -0.018 |
| age_days    |  -0.002 |   0.077 |        -0.018 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.508 |         0.404 |      0.025 |
| forks       |   0.508 |   1     |         0.27  |     -0.036 |
| open_issues |   0.404 |   0.27  |         1     |      0.041 |
| age_days    |   0.025 |  -0.036 |         0.041 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 80 |
| `codex` | 73 |
| `ai-agents` | 69 |
| `llm` | 68 |
| `ai` | 49 |
| `developer-tools` | 46 |
| `claude` | 44 |
| `typescript` | 41 |
| `python` | 38 |
| `local-first` | 35 |
| `mcp` | 34 |
| `cli` | 32 |
| `windows` | 32 |
| `agent-skills` | 31 |
| `macos` | 30 |
| `ai-agent` | 29 |
| `rust` | 28 |
| `desktop-app` | 27 |
| `react` | 25 |
| `agent` | 24 |
