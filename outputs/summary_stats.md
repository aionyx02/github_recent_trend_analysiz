# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 456.3 | 197.0 | 23338 |
| forks | 135.0 | 21.0 | 12756 |
| open_issues | 5.8 | 1.0 | 954 |
| stars_per_day | 39.2 | 12.7 | 3758 |
| age_days | 17.5 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 23338 | 4428 | Rust | AI/ML |
| `JustVugg/colibri` | 20748 | 2112 | C | Game |
| `Fei-Away/Codex-Dream-Skin` | 12647 | 1261 | JavaScript | AI/ML |
| `andrewyng/openworker` | 10273 | 1340 | Python | Other |
| `img2threejs/img2threejs` | 7864 | 598 | Python | AI/ML |
| `unicity-aos/aos-ce` | 7753 | 14 | Rust | AI/ML |
| `x4gKing/X4G` | 6968 | 12756 | Python | Other |
| `oso95/scroll-world` | 5649 | 649 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 5282 | 1092 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 3758 | 314 | Unknown | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `MoonshotAI/Kimi-K3` | 3758.0 | 3758 | 1d | Other |
| `xai-org/grok-build` | 1667.0 | 23338 | 14d | AI/ML |
| `andrewyng/openworker` | 1284.1 | 10273 | 8d | Other |
| `Fei-Away/Codex-Dream-Skin` | 972.8 | 12647 | 13d | AI/ML |
| `JustVugg/colibri` | 768.4 | 20748 | 27d | Game |
| `mshumer/Claude-of-Duty` | 671.7 | 2015 | 3d | Other |
| `img2threejs/img2threejs` | 604.9 | 7864 | 13d | AI/ML |
| `unicity-aos/aos-ce` | 484.6 | 7753 | 16d | AI/ML |
| `0xwilliamortiz/ponytail-improved` | 475.0 | 475 | 1d | AI/ML |
| `slvDev/esp32-ai` | 428.4 | 2142 | 5d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 409 | 536 | 215 | 118 | 42.4 | 5.2 |
| Other | 347 | 413 | 177 | 131 | 44.8 | 7.8 |
| Web | 71 | 331 | 195 | 90 | 20.9 | 4.3 |
| Mobile | 48 | 341 | 170 | 31 | 27.9 | 5.4 |
| CLI/Tooling | 29 | 338 | 209 | 27 | 30.2 | 2.5 |
| Finance/Trading | 27 | 218 | 194 | 1046 | 16.4 | 1.3 |
| Security | 26 | 260 | 184 | 51 | 26.3 | 3.9 |
| Game | 20 | 1301 | 225 | 120 | 54.7 | 7.0 |
| DevOps | 14 | 219 | 192 | 21 | 16.4 | 1.6 |
| Data | 9 | 248 | 159 | 29 | 21.8 | 1.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.387 |         0.154 |      0.012 |
| forks       |   0.387 |   1     |         0.028 |      0.039 |
| open_issues |   0.154 |   0.028 |         1     |      0.035 |
| age_days    |   0.012 |   0.039 |         0.035 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.506 |         0.334 |      0.06  |
| forks       |   0.506 |   1     |         0.197 |     -0.024 |
| open_issues |   0.334 |   0.197 |         1     |      0.05  |
| age_days    |   0.06  |  -0.024 |         0.05  |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 70 |
| `ai-agents` | 66 |
| `codex` | 66 |
| `llm` | 62 |
| `claude` | 44 |
| `python` | 41 |
| `ai` | 40 |
| `typescript` | 38 |
| `developer-tools` | 36 |
| `cli` | 34 |
| `mcp` | 34 |
| `local-first` | 34 |
| `agent-skills` | 31 |
| `macos` | 30 |
| `windows` | 29 |
| `rust` | 28 |
| `ai-agent` | 26 |
| `desktop-app` | 23 |
| `react` | 21 |
| `agent` | 20 |
