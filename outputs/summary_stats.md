# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 658.7 | 218.0 | 140810 |
| forks | 72.2 | 20.0 | 14277 |
| open_issues | 6.5 | 1.0 | 914 |
| stars_per_day | 101.4 | 15.6 | 46937 |
| age_days | 16.3 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 140810 | 14277 | TypeScript | Other |
| `firecrawl/anydoc` | 16529 | 934 | Rust | Other |
| `andrewyng/openworker` | 14677 | 2037 | Python | Other |
| `yc-software/qm` | 13730 | 1622 | TypeScript | AI/ML |
| `guillaumemeyer/watermarks-remover` | 12273 | 1315 | Python | AI/ML |
| `anywhere-labs/deepseek-harness-desktop` | 10371 | 453 | TypeScript | Other |
| `trycompai/crm` | 8525 | 1005 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 8483 | 665 | Unknown | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 6471 | 950 | Python | Other |
| `bashalarmistalt/decimen-optical-transfer` | 6095 | 738 | TypeScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 46936.7 | 140810 | 3d | Other |
| `anywhere-labs/deepseek-harness-desktop` | 3457.0 | 10371 | 3d | Other |
| `guillaumemeyer/watermarks-remover` | 2454.6 | 12273 | 5d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 2157.0 | 6471 | 3d | Other |
| `xiaobright/dsh-anchored-standard` | 1628.5 | 3257 | 2d | Other |
| `yjh051108/dsh-routing-suite` | 1558.5 | 3117 | 2d | Other |
| `firecrawl/anydoc` | 1271.5 | 16529 | 13d | Other |
| `zhu1090093659/dsh-web-ui` | 942.0 | 3768 | 4d | Web |
| `yc-software/qm` | 762.8 | 13730 | 18d | AI/ML |
| `cordiverse/paper` | 664.0 | 1992 | 3d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 440 | 842 | 196 | 89 | 166.1 | 5.4 |
| AI/ML | 320 | 611 | 260 | 69 | 53.3 | 8.6 |
| Web | 73 | 434 | 219 | 44 | 71.6 | 3.7 |
| Mobile | 53 | 392 | 253 | 32 | 25.9 | 11.3 |
| CLI/Tooling | 38 | 381 | 221 | 39 | 47.4 | 6.2 |
| Security | 24 | 241 | 170 | 47 | 36.8 | 1.7 |
| DevOps | 17 | 329 | 268 | 50 | 40.3 | 5.9 |
| Data | 16 | 296 | 190 | 23 | 23.3 | 2.5 |
| Game | 11 | 618 | 275 | 43 | 69.1 | 3.9 |
| Finance/Trading | 8 | 330 | 204 | 201 | 26.9 | 1.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.98  |         0.096 |     -0.055 |
| forks       |   0.98  |   1     |         0.106 |     -0.051 |
| open_issues |   0.096 |   0.106 |         1     |      0.051 |
| age_days    |  -0.055 |  -0.051 |         0.051 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.618 |         0.388 |      0.022 |
| forks       |   0.618 |   1     |         0.401 |      0.037 |
| open_issues |   0.388 |   0.401 |         1     |      0.01  |
| age_days    |   0.022 |   0.037 |         0.01  |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 55 |
| `claude-code` | 47 |
| `dsh-plugin` | 41 |
| `llm` | 41 |
| `codex` | 41 |
| `ai` | 40 |
| `typescript` | 35 |
| `dsh` | 32 |
| `developer-tools` | 32 |
| `python` | 32 |
| `deepseek-harness` | 31 |
| `ai-agent` | 28 |
| `macos` | 27 |
| `agent` | 26 |
| `agent-skills` | 25 |
| `mcp` | 24 |
| `deepseek` | 23 |
| `windows` | 22 |
| `rust` | 22 |
| `react` | 21 |
