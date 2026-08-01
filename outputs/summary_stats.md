# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 470.2 | 205.0 | 23744 |
| forks | 120.6 | 22.0 | 13182 |
| open_issues | 5.1 | 1.0 | 333 |
| stars_per_day | 41.1 | 13.3 | 2473 |
| age_days | 18.0 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 23744 | 4510 | Rust | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 12912 | 1289 | JavaScript | AI/ML |
| `andrewyng/openworker` | 11421 | 1536 | Python | Other |
| `img2threejs/img2threejs` | 8839 | 672 | Python | AI/ML |
| `unicity-aos/aos-ce` | 8575 | 16 | Rust | AI/ML |
| `openai/codex-security` | 7874 | 518 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 7755 | 542 | Unknown | Other |
| `x4gKing/X4G` | 7194 | 13182 | Python | Other |
| `oso95/scroll-world` | 6271 | 740 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 5332 | 1106 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `bashalarmistalt/decimen-optical-transfer` | 2473.0 | 2473 | 1d | Other |
| `MoonshotAI/Kimi-K3` | 1938.8 | 7755 | 4d | Other |
| `yc-software/qm` | 1546.5 | 3093 | 2d | AI/ML |
| `xai-org/grok-build` | 1396.7 | 23744 | 17d | AI/ML |
| `andrewyng/openworker` | 1038.3 | 11421 | 11d | Other |
| `Fei-Away/Codex-Dream-Skin` | 807.0 | 12912 | 16d | AI/ML |
| `xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer` | 625.0 | 625 | 1d | Other |
| `img2threejs/img2threejs` | 552.4 | 8839 | 16d | AI/ML |
| `WilonityDev/WilonityLoader` | 532.0 | 532 | 1d | Game |
| `digimata/quill` | 489.9 | 3429 | 7d | Mobile |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 409 | 576 | 220 | 120 | 42.4 | 6.1 |
| Other | 347 | 457 | 193 | 138 | 48.5 | 4.8 |
| Web | 67 | 355 | 212 | 92 | 27.8 | 4.4 |
| Mobile | 46 | 356 | 190 | 26 | 29.9 | 5.9 |
| CLI/Tooling | 32 | 361 | 218 | 33 | 29.0 | 2.5 |
| Security | 30 | 268 | 188 | 63 | 19.3 | 7.0 |
| Game | 21 | 277 | 184 | 16 | 56.6 | 2.4 |
| Data | 17 | 245 | 132 | 25 | 32.7 | 1.1 |
| Finance/Trading | 17 | 181 | 140 | 721 | 11.8 | 0.4 |
| DevOps | 14 | 234 | 213 | 20 | 16.3 | 1.6 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.427 |         0.332 |     -0.005 |
| forks       |   0.427 |   1     |         0.085 |      0.064 |
| open_issues |   0.332 |   0.085 |         1     |     -0.01  |
| age_days    |  -0.005 |   0.064 |        -0.01  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.502 |         0.381 |      0.028 |
| forks       |   0.502 |   1     |         0.26  |     -0.028 |
| open_issues |   0.381 |   0.26  |         1     |      0.025 |
| age_days    |   0.028 |  -0.028 |         0.025 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 74 |
| `llm` | 70 |
| `ai-agents` | 68 |
| `codex` | 68 |
| `ai` | 50 |
| `claude` | 45 |
| `developer-tools` | 45 |
| `typescript` | 39 |
| `python` | 39 |
| `mcp` | 36 |
| `local-first` | 36 |
| `cli` | 34 |
| `macos` | 32 |
| `windows` | 30 |
| `rust` | 30 |
| `agent-skills` | 29 |
| `ai-agent` | 28 |
| `react` | 25 |
| `desktop-app` | 25 |
| `agent` | 24 |
