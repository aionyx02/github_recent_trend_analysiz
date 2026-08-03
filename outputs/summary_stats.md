# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 477.9 | 204.0 | 23974 |
| forks | 121.9 | 22.0 | 13515 |
| open_issues | 5.2 | 1.0 | 433 |
| stars_per_day | 42.9 | 13.4 | 2054 |
| age_days | 17.9 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 23974 | 4544 | Rust | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 13039 | 1297 | JavaScript | AI/ML |
| `andrewyng/openworker` | 12280 | 1660 | Python | Other |
| `img2threejs/img2threejs` | 9268 | 701 | Python | AI/ML |
| `unicity-aos/aos-ce` | 8574 | 17 | Rust | AI/ML |
| `openai/codex-security` | 8294 | 560 | TypeScript | AI/ML |
| `yc-software/qm` | 8217 | 861 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 7952 | 582 | Unknown | Other |
| `x4gKing/X4G` | 7376 | 13515 | Python | Other |
| `oso95/scroll-world` | 7199 | 803 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `yc-software/qm` | 2054.2 | 8217 | 4d | AI/ML |
| `bashalarmistalt/decimen-optical-transfer` | 1334.7 | 4004 | 3d | Other |
| `MoonshotAI/Kimi-K3` | 1325.3 | 7952 | 6d | Other |
| `xai-org/grok-build` | 1261.8 | 23974 | 19d | AI/ML |
| `trycompai/crm` | 1052.5 | 2105 | 2d | Other |
| `andrewyng/openworker` | 944.6 | 12280 | 13d | Other |
| `DannyMac180/sol-advisor` | 830.0 | 830 | 1d | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 724.4 | 13039 | 18d | AI/ML |
| `xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer` | 629.3 | 1888 | 3d | Other |
| `WilonityDev/WilonityLoader` | 609.5 | 1219 | 2d | Game |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 412 | 585 | 216 | 116 | 46.8 | 6.3 |
| Other | 345 | 465 | 194 | 144 | 45.8 | 4.7 |
| Web | 76 | 317 | 183 | 83 | 33.8 | 3.4 |
| Mobile | 41 | 386 | 195 | 28 | 33.3 | 4.6 |
| CLI/Tooling | 34 | 351 | 220 | 34 | 36.7 | 3.0 |
| Security | 29 | 284 | 191 | 70 | 18.2 | 10.3 |
| Game | 19 | 330 | 220 | 22 | 69.8 | 2.6 |
| Finance/Trading | 18 | 180 | 140 | 688 | 11.3 | 0.4 |
| DevOps | 15 | 251 | 230 | 22 | 15.7 | 2.1 |
| Data | 11 | 283 | 218 | 34 | 31.3 | 2.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.426 |         0.352 |     -0.002 |
| forks       |   0.426 |   1     |         0.092 |      0.092 |
| open_issues |   0.352 |   0.092 |         1     |     -0.017 |
| age_days    |  -0.002 |   0.092 |        -0.017 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.513 |         0.411 |      0.035 |
| forks       |   0.513 |   1     |         0.267 |      0.012 |
| open_issues |   0.411 |   0.267 |         1     |      0.064 |
| age_days    |   0.035 |   0.012 |         0.064 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 78 |
| `ai-agents` | 71 |
| `codex` | 71 |
| `llm` | 70 |
| `ai` | 53 |
| `developer-tools` | 46 |
| `claude` | 42 |
| `typescript` | 41 |
| `python` | 39 |
| `local-first` | 36 |
| `cli` | 32 |
| `agent-skills` | 32 |
| `mcp` | 32 |
| `windows` | 30 |
| `macos` | 29 |
| `rust` | 29 |
| `react` | 28 |
| `ai-agent` | 25 |
| `desktop-app` | 25 |
| `open-source` | 22 |
