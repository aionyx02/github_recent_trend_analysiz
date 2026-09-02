# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 812.8 | 318.0 | 208970 |
| forks | 88.9 | 17.0 | 24377 |
| open_issues | 5.6 | 1.0 | 304 |
| stars_per_day | 51.3 | 15.8 | 10998 |
| age_days | 20.2 | 22.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 208970 | 24377 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 22930 | 1125 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 19980 | 2305 | Python | AI/ML |
| `firecrawl/anydoc` | 19949 | 1200 | Rust | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 14172 | 2497 | Python | Other |
| `pathwaycom/arc-task-gen` | 10027 | 65 | Python | Other |
| `yjh051108/dsh-routing-suite` | 7026 | 145 | JavaScript | Other |
| `sapientinc/PRAXIST` | 6751 | 557 | Python | Other |
| `zhu1090093659/dsh-web` | 6711 | 440 | TypeScript | Web |
| `arvids-unavailable/openGym` | 6589 | 1092 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 10998.4 | 208970 | 19d | Other |
| `sapientinc/PRAXIST` | 1350.2 | 6751 | 5d | Other |
| `anywhere-labs/dsh-desktop` | 1206.8 | 22930 | 19d | Other |
| `guillaumemeyer/watermarks-remover` | 951.4 | 19980 | 21d | AI/ML |
| `GangTailorUpgrade/undress-service` | 886.0 | 886 | 1d | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 745.9 | 14172 | 19d | Other |
| `firecrawl/anydoc` | 687.9 | 19949 | 29d | Other |
| `XiaoDuoYa/codex-with-chatgpt` | 556.8 | 2227 | 4d | AI/ML |
| `2akouwu/codex-cli-portable-setup-kit` | 493.0 | 493 | 1d | AI/ML |
| `MengTo/threeui` | 450.8 | 4959 | 11d | Web |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 489 | 1047 | 320 | 113 | 61.5 | 5.3 |
| AI/ML | 317 | 619 | 326 | 70 | 44.3 | 6.0 |
| Web | 57 | 720 | 308 | 92 | 47.9 | 3.5 |
| Mobile | 45 | 484 | 302 | 39 | 30.7 | 9.9 |
| Data | 28 | 327 | 290 | 22 | 20.1 | 3.6 |
| CLI/Tooling | 23 | 649 | 413 | 67 | 39.3 | 11.1 |
| Security | 15 | 399 | 356 | 69 | 22.7 | 1.2 |
| Game | 12 | 474 | 267 | 31 | 60.8 | 7.2 |
| Finance/Trading | 7 | 342 | 193 | 99 | 52.6 | 2.1 |
| DevOps | 7 | 504 | 241 | 75 | 25.5 | 3.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.969 |         0.115 |     -0.007 |
| forks       |   0.969 |   1     |         0.088 |     -0.029 |
| open_issues |   0.115 |   0.088 |         1     |     -0.04  |
| age_days    |  -0.007 |  -0.029 |        -0.04  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.408 |         0.258 |     -0.01  |
| forks       |   0.408 |   1     |         0.588 |     -0.376 |
| open_issues |   0.258 |   0.588 |         1     |     -0.246 |
| age_days    |  -0.01  |  -0.376 |        -0.246 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 82 |
| `deepseek-harness` | 76 |
| `ai-agents` | 61 |
| `dsh` | 58 |
| `claude-code` | 51 |
| `codex` | 42 |
| `llm` | 42 |
| `deepseek` | 41 |
| `ai-agent` | 39 |
| `mcp` | 34 |
| `typescript` | 31 |
| `developer-tools` | 30 |
| `agent` | 28 |
| `ai` | 27 |
| `agent-skills` | 27 |
| `python` | 27 |
| `claude` | 24 |
| `windows` | 23 |
| `macos` | 21 |
| `rust` | 19 |
