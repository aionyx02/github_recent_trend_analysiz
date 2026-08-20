# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 719.6 | 246.0 | 169810 |
| forks | 76.3 | 20.0 | 18223 |
| open_issues | 6.3 | 1.0 | 974 |
| stars_per_day | 83.9 | 18.7 | 28302 |
| age_days | 15.6 | 14.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 169810 | 18223 | TypeScript | Other |
| `firecrawl/anydoc` | 17340 | 996 | Rust | Other |
| `anywhere-labs/deepseek-harness-desktop` | 15740 | 749 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 15490 | 1750 | Python | AI/ML |
| `yc-software/qm` | 13966 | 1661 | TypeScript | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 10262 | 1508 | Python | Other |
| `trycompai/crm` | 8689 | 1043 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 8537 | 674 | Unknown | Other |
| `MiniMax-AI/MiniMax-H3` | 6421 | 393 | Python | Other |
| `yjh051108/dsh-routing-suite` | 6367 | 114 | PowerShell | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 28301.7 | 169810 | 6d | Other |
| `anywhere-labs/deepseek-harness-desktop` | 2623.3 | 15740 | 6d | Other |
| `s1dashu/ip-as-logo-skill` | 2462.0 | 2462 | 1d | AI/ML |
| `guillaumemeyer/watermarks-remover` | 1936.2 | 15490 | 8d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 1710.3 | 10262 | 6d | Other |
| `yetone/cumora` | 1366.0 | 2732 | 2d | AI/ML |
| `yjh051108/dsh-routing-suite` | 1273.4 | 6367 | 5d | Other |
| `firecrawl/anydoc` | 1083.8 | 17340 | 16d | Other |
| `Leutenegger/watermarks-remover` | 915.0 | 915 | 1d | AI/ML |
| `xiaobright/dsh-anchored-standard` | 730.0 | 3650 | 5d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 458 | 906 | 230 | 91 | 112.4 | 4.7 |
| AI/ML | 319 | 652 | 281 | 75 | 72.4 | 9.6 |
| Web | 69 | 492 | 236 | 47 | 55.6 | 2.8 |
| Mobile | 52 | 404 | 268 | 32 | 35.4 | 10.8 |
| CLI/Tooling | 37 | 435 | 255 | 45 | 38.7 | 5.8 |
| Data | 20 | 341 | 227 | 34 | 26.5 | 2.1 |
| Security | 16 | 295 | 192 | 60 | 29.5 | 2.1 |
| DevOps | 12 | 371 | 266 | 67 | 36.4 | 3.6 |
| Game | 10 | 719 | 329 | 53 | 55.2 | 4.6 |
| Finance/Trading | 7 | 337 | 174 | 169 | 25.9 | 2.3 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.986 |         0.07  |     -0.038 |
| forks       |   0.986 |   1     |         0.064 |     -0.034 |
| open_issues |   0.07  |   0.064 |         1     |      0.051 |
| age_days    |  -0.038 |  -0.034 |         0.051 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.555 |         0.383 |      0.054 |
| forks       |   0.555 |   1     |         0.489 |      0.122 |
| open_issues |   0.383 |   0.489 |         1     |      0.111 |
| age_days    |   0.054 |   0.122 |         0.111 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 58 |
| `ai-agents` | 51 |
| `deepseek-harness` | 47 |
| `dsh` | 46 |
| `claude-code` | 45 |
| `codex` | 43 |
| `typescript` | 38 |
| `ai` | 36 |
| `llm` | 36 |
| `developer-tools` | 36 |
| `ai-agent` | 32 |
| `deepseek` | 31 |
| `python` | 29 |
| `agent` | 28 |
| `macos` | 27 |
| `mcp` | 26 |
| `windows` | 23 |
| `cli` | 23 |
| `agent-skills` | 22 |
| `linux` | 20 |
