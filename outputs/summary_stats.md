# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 817.4 | 316.0 | 204112 |
| forks | 91.0 | 17.0 | 23591 |
| open_issues | 5.9 | 1.0 | 528 |
| stars_per_day | 60.1 | 17.0 | 12757 |
| age_days | 18.8 | 22.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 204112 | 23591 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 21992 | 1077 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 19353 | 2256 | Python | AI/ML |
| `firecrawl/anydoc` | 19270 | 1143 | Rust | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 13641 | 2348 | Python | Other |
| `trycompai/crm` | 9123 | 1135 | TypeScript | AI/ML |
| `pathwaycom/arc-task-gen` | 8925 | 58 | Python | Other |
| `yjh051108/dsh-routing-suite` | 6961 | 140 | JavaScript | Other |
| `FareedKhan-dev/kimi-k3-in-c` | 6741 | 1098 | C | AI/ML |
| `zhu1090093659/dsh-web` | 6489 | 433 | TypeScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 12757.0 | 204112 | 16d | Other |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 2053.5 | 4107 | 2d | Other |
| `sapientinc/PRAXIST` | 1617.5 | 3235 | 2d | Other |
| `anywhere-labs/dsh-desktop` | 1374.5 | 21992 | 16d | Other |
| `XiaoDuoYa/codex-with-chatgpt` | 1181.0 | 1181 | 1d | AI/ML |
| `guillaumemeyer/watermarks-remover` | 1075.2 | 19353 | 18d | AI/ML |
| `MetaMask-AI/metamask-desktop` | 936.0 | 936 | 1d | Finance/Trading |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 852.6 | 13641 | 16d | Other |
| `Nanako0129/sepia` | 809.0 | 809 | 1d | AI/ML |
| `firecrawl/anydoc` | 741.2 | 19270 | 26d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 497 | 1028 | 315 | 111 | 72.0 | 6.0 |
| AI/ML | 313 | 671 | 340 | 78 | 53.1 | 6.1 |
| Web | 60 | 634 | 314 | 83 | 46.3 | 3.7 |
| Mobile | 42 | 488 | 365 | 39 | 36.2 | 9.2 |
| Data | 26 | 322 | 297 | 20 | 24.3 | 2.5 |
| CLI/Tooling | 22 | 592 | 338 | 62 | 36.4 | 9.2 |
| Security | 16 | 362 | 313 | 67 | 30.2 | 2.9 |
| Game | 10 | 545 | 334 | 38 | 30.4 | 6.8 |
| DevOps | 8 | 444 | 230 | 74 | 25.9 | 2.4 |
| Finance/Trading | 6 | 310 | 188 | 120 | 167.2 | 3.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.971 |         0.097 |     -0.011 |
| forks       |   0.971 |   1     |         0.086 |     -0.031 |
| open_issues |   0.097 |   0.086 |         1     |     -0.069 |
| age_days    |  -0.011 |  -0.031 |        -0.069 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.418 |         0.26  |      0.025 |
| forks       |   0.418 |   1     |         0.578 |     -0.221 |
| open_issues |   0.26  |   0.578 |         1     |     -0.149 |
| age_days    |   0.025 |  -0.221 |        -0.149 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 81 |
| `deepseek-harness` | 78 |
| `ai-agents` | 60 |
| `dsh` | 59 |
| `claude-code` | 46 |
| `deepseek` | 42 |
| `llm` | 39 |
| `codex` | 38 |
| `ai-agent` | 34 |
| `mcp` | 33 |
| `typescript` | 32 |
| `agent` | 29 |
| `ai` | 27 |
| `developer-tools` | 26 |
| `agent-skills` | 25 |
| `python` | 25 |
| `windows` | 24 |
| `macos` | 22 |
| `rust` | 22 |
| `claude` | 19 |
