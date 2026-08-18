# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 682.2 | 217.5 | 154478 |
| forks | 77.7 | 21.0 | 15970 |
| open_issues | 7.1 | 1.0 | 939 |
| stars_per_day | 92.7 | 16.0 | 38620 |
| age_days | 16.2 | 16.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 154478 | 15970 | TypeScript | Other |
| `firecrawl/anydoc` | 16799 | 961 | Rust | Other |
| `andrewyng/openworker` | 14749 | 2045 | Python | Other |
| `yc-software/qm` | 13832 | 1636 | TypeScript | AI/ML |
| `guillaumemeyer/watermarks-remover` | 13781 | 1516 | Python | AI/ML |
| `anywhere-labs/deepseek-harness-desktop` | 12518 | 568 | TypeScript | Other |
| `trycompai/crm` | 8577 | 1013 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 8497 | 668 | Unknown | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 7980 | 1157 | Python | Other |
| `MiniMax-AI/MiniMax-H3` | 6192 | 378 | Python | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 38619.5 | 154478 | 4d | Other |
| `anywhere-labs/deepseek-harness-desktop` | 3129.5 | 12518 | 4d | Other |
| `guillaumemeyer/watermarks-remover` | 2296.8 | 13781 | 6d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 1995.0 | 7980 | 4d | Other |
| `yjh051108/dsh-routing-suite` | 1883.3 | 5650 | 3d | Other |
| `yetone/cumora` | 1879.0 | 1879 | 1d | AI/ML |
| `firecrawl/anydoc` | 1199.9 | 16799 | 14d | Other |
| `xiaobright/dsh-anchored-standard` | 1158.7 | 3476 | 3d | Other |
| `zhu1090093659/dsh-web-ui` | 861.2 | 4306 | 5d | Web |
| `yc-software/qm` | 728.0 | 13832 | 19d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 401 | 949 | 202 | 107 | 158.2 | 6.4 |
| AI/ML | 348 | 594 | 238 | 68 | 54.7 | 9.1 |
| Web | 76 | 439 | 222 | 43 | 61.1 | 3.8 |
| Mobile | 56 | 370 | 224 | 30 | 26.6 | 10.1 |
| CLI/Tooling | 39 | 380 | 223 | 40 | 40.2 | 5.1 |
| Security | 23 | 251 | 178 | 51 | 31.0 | 2.0 |
| DevOps | 20 | 286 | 227 | 45 | 30.0 | 5.8 |
| Data | 16 | 295 | 203 | 26 | 24.8 | 3.1 |
| Game | 13 | 555 | 275 | 39 | 52.0 | 3.6 |
| Finance/Trading | 8 | 333 | 208 | 210 | 23.4 | 1.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.981 |         0.095 |     -0.047 |
| forks       |   0.981 |   1     |         0.101 |     -0.044 |
| open_issues |   0.095 |   0.101 |         1     |      0.048 |
| age_days    |  -0.047 |  -0.044 |         0.048 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.599 |         0.369 |      0.044 |
| forks       |   0.599 |   1     |         0.311 |      0.043 |
| open_issues |   0.369 |   0.311 |         1     |      0.043 |
| age_days    |   0.044 |   0.043 |         0.043 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 64 |
| `dsh-plugin` | 52 |
| `claude-code` | 48 |
| `llm` | 43 |
| `codex` | 43 |
| `ai` | 42 |
| `deepseek-harness` | 42 |
| `dsh` | 41 |
| `typescript` | 38 |
| `developer-tools` | 38 |
| `ai-agent` | 32 |
| `python` | 32 |
| `agent` | 31 |
| `deepseek` | 29 |
| `macos` | 28 |
| `mcp` | 25 |
| `agent-skills` | 24 |
| `windows` | 24 |
| `rust` | 24 |
| `cli` | 22 |
