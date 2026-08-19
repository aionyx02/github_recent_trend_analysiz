# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 711.1 | 229.0 | 162961 |
| forks | 76.1 | 20.0 | 17200 |
| open_issues | 6.9 | 1.0 | 954 |
| stars_per_day | 88.3 | 17.8 | 32592 |
| age_days | 15.7 | 14.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 162961 | 17200 | TypeScript | Other |
| `firecrawl/anydoc` | 17081 | 979 | Rust | Other |
| `andrewyng/openworker` | 14796 | 2046 | Python | Other |
| `guillaumemeyer/watermarks-remover` | 14699 | 1640 | Python | AI/ML |
| `anywhere-labs/deepseek-harness-desktop` | 14198 | 657 | TypeScript | Other |
| `yc-software/qm` | 13912 | 1650 | TypeScript | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 9380 | 1379 | Python | Other |
| `trycompai/crm` | 8626 | 1030 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 8512 | 671 | Unknown | Other |
| `MiniMax-AI/MiniMax-H3` | 6318 | 386 | Python | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 32592.2 | 162961 | 5d | Other |
| `anywhere-labs/deepseek-harness-desktop` | 2839.6 | 14198 | 5d | Other |
| `yetone/cumora` | 2514.0 | 2514 | 1d | AI/ML |
| `guillaumemeyer/watermarks-remover` | 2099.9 | 14699 | 7d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 1876.0 | 9380 | 5d | Other |
| `yjh051108/dsh-routing-suite` | 1538.2 | 6153 | 4d | Other |
| `s1dashu/ip-as-logo-skill` | 1278.0 | 1278 | 1d | AI/ML |
| `cinderline/northcinder` | 1159.0 | 1159 | 1d | AI/ML |
| `firecrawl/anydoc` | 1138.7 | 17081 | 15d | Other |
| `xiaobright/dsh-anchored-standard` | 898.8 | 3595 | 4d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 446 | 921 | 210 | 96 | 127.5 | 5.8 |
| AI/ML | 327 | 629 | 263 | 70 | 66.9 | 9.5 |
| Web | 70 | 492 | 238 | 48 | 59.8 | 4.0 |
| Mobile | 52 | 391 | 268 | 31 | 30.4 | 10.3 |
| CLI/Tooling | 37 | 405 | 243 | 43 | 36.8 | 5.6 |
| Security | 20 | 282 | 202 | 60 | 30.5 | 2.2 |
| Data | 16 | 325 | 212 | 24 | 29.5 | 2.6 |
| DevOps | 13 | 347 | 279 | 63 | 36.4 | 4.5 |
| Game | 11 | 650 | 308 | 47 | 54.5 | 4.0 |
| Finance/Trading | 8 | 325 | 180 | 148 | 28.0 | 2.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.985 |         0.095 |     -0.038 |
| forks       |   0.985 |   1     |         0.102 |     -0.033 |
| open_issues |   0.095 |   0.102 |         1     |      0.07  |
| age_days    |  -0.038 |  -0.033 |         0.07  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.599 |         0.417 |      0.097 |
| forks       |   0.599 |   1     |         0.475 |      0.146 |
| open_issues |   0.417 |   0.475 |         1     |      0.132 |
| age_days    |   0.097 |   0.146 |         0.132 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 57 |
| `dsh-plugin` | 56 |
| `dsh` | 44 |
| `deepseek-harness` | 44 |
| `claude-code` | 44 |
| `codex` | 40 |
| `ai` | 39 |
| `typescript` | 39 |
| `llm` | 38 |
| `developer-tools` | 35 |
| `ai-agent` | 34 |
| `python` | 32 |
| `deepseek` | 30 |
| `macos` | 28 |
| `agent` | 28 |
| `mcp` | 26 |
| `windows` | 23 |
| `agent-skills` | 22 |
| `linux` | 21 |
| `cli` | 21 |
