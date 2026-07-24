# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 437.4 | 197.0 | 22209 |
| forks | 87.2 | 13.0 | 12002 |
| open_issues | 3.8 | 0.0 | 945 |
| stars_per_day | 33.6 | 11.0 | 2468 |
| age_days | 19.9 | 23.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 22209 | 4194 | Rust | AI/ML |
| `JustVugg/colibri` | 18414 | 1787 | C | Game |
| `Fei-Away/Codex-Dream-Skin` | 12158 | 1219 | JavaScript | AI/ML |
| `unicity-aos/aos-ce` | 7034 | 9 | Rust | AI/ML |
| `deepseek-ai/DeepSpec` | 6759 | 626 | Python | Other |
| `x4gKing/X4G` | 6531 | 12002 | Python | Other |
| `Yu9191/wloc` | 6225 | 1237 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 5138 | 1063 | TypeScript | AI/ML |
| `oso95/scroll-world` | 5027 | 580 | JavaScript | Other |
| `baairon/torlink` | 3802 | 251 | TypeScript | CLI/Tooling |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `xai-org/grok-build` | 2467.7 | 22209 | 9d | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 1519.8 | 12158 | 8d | AI/ML |
| `JustVugg/colibri` | 837.0 | 18414 | 22d | Game |
| `andrewyng/openworker` | 745.0 | 2235 | 3d | Other |
| `unicity-aos/aos-ce` | 639.5 | 7034 | 11d | AI/ML |
| `lopopolo/harness-engineering` | 459.0 | 2295 | 5d | AI/ML |
| `Jakubantalik/thinking-orbs` | 434.5 | 869 | 2d | AI/ML |
| `hoainho/img2threejs` | 429.8 | 3438 | 8d | AI/ML |
| `berabuddies/redis-poc` | 351.0 | 351 | 1d | Other |
| `x4gKing/X4G` | 343.7 | 6531 | 19d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 384 | 517 | 226 | 62 | 44.4 | 3.1 |
| Web | 225 | 202 | 152 | 19 | 10.8 | 0.9 |
| Other | 223 | 544 | 257 | 158 | 41.2 | 9.0 |
| Mobile | 31 | 406 | 221 | 41 | 35.3 | 4.9 |
| Finance/Trading | 30 | 241 | 220 | 596 | 21.0 | 1.2 |
| Data | 29 | 225 | 151 | 8 | 9.1 | 0.3 |
| CLI/Tooling | 27 | 512 | 226 | 48 | 39.5 | 3.0 |
| Security | 20 | 292 | 194 | 55 | 29.8 | 0.7 |
| Game | 16 | 1444 | 268 | 128 | 72.6 | 7.8 |
| DevOps | 15 | 185 | 153 | 6 | 9.7 | 0.5 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.44  |         0.089 |     -0.09  |
| forks       |   0.44  |   1     |         0.029 |     -0.047 |
| open_issues |   0.089 |   0.029 |         1     |     -0.005 |
| age_days    |  -0.09  |  -0.047 |        -0.005 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.81  |         0.6   |     -0.387 |
| forks       |   0.81  |   1     |         0.585 |     -0.386 |
| open_issues |   0.6   |   0.585 |         1     |     -0.213 |
| age_days    |  -0.387 |  -0.386 |        -0.213 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 65 |
| `llm` | 64 |
| `ai-agents` | 62 |
| `python` | 61 |
| `claude` | 55 |
| `codex` | 52 |
| `typescript` | 48 |
| `manga-downloader` | 44 |
| `manga` | 43 |
| `claude-opus` | 43 |
| `ai` | 42 |
| `mcp` | 35 |
| `cli` | 34 |
| `developer-tools` | 32 |
| `macos` | 31 |
| `anthropic` | 31 |
| `local-first` | 27 |
| `agent-skills` | 26 |
| `windows` | 26 |
| `rust` | 26 |
