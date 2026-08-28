# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 842.6 | 322.0 | 201879 |
| forks | 94.4 | 18.0 | 23181 |
| open_issues | 6.8 | 1.0 | 473 |
| stars_per_day | 66.2 | 18.3 | 14420 |
| age_days | 18.0 | 21.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 201879 | 23181 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 21516 | 1048 | TypeScript | Other |
| `firecrawl/anydoc` | 19031 | 1119 | Rust | Other |
| `guillaumemeyer/watermarks-remover` | 19008 | 2208 | Python | AI/ML |
| `yc-software/qm` | 14305 | 1715 | TypeScript | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 13377 | 2270 | Python | Other |
| `trycompai/crm` | 9054 | 1116 | TypeScript | AI/ML |
| `pathwaycom/arc-task-gen` | 8512 | 57 | Python | Other |
| `MiniMax-AI/MiniMax-H3` | 7322 | 478 | Python | Other |
| `yjh051108/dsh-routing-suite` | 6928 | 140 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 14419.9 | 201879 | 14d | Other |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 3644.0 | 3644 | 1d | Other |
| `anywhere-labs/dsh-desktop` | 1536.9 | 21516 | 14d | Other |
| `sapientinc/PRAXIST` | 1442.0 | 1442 | 1d | Other |
| `guillaumemeyer/watermarks-remover` | 1188.0 | 19008 | 16d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 955.5 | 13377 | 14d | Other |
| `wide-trace/open-higgsfield` | 942.0 | 942 | 1d | Other |
| `b-nnett/grok-bot-0.18-reconstructed` | 850.2 | 3401 | 4d | Other |
| `firecrawl/anydoc` | 793.0 | 19031 | 24d | Other |
| `MengTo/threeui` | 736.7 | 4420 | 6d | Web |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 503 | 1040 | 320 | 113 | 82.9 | 5.9 |
| AI/ML | 310 | 709 | 328 | 83 | 56.0 | 8.4 |
| Web | 60 | 626 | 324 | 82 | 50.8 | 4.3 |
| Mobile | 38 | 463 | 349 | 39 | 28.5 | 13.2 |
| CLI/Tooling | 25 | 701 | 402 | 70 | 48.7 | 9.6 |
| Data | 25 | 401 | 305 | 32 | 29.8 | 2.5 |
| Security | 16 | 377 | 327 | 74 | 22.7 | 4.6 |
| Game | 11 | 585 | 356 | 43 | 39.0 | 5.6 |
| DevOps | 7 | 482 | 238 | 84 | 30.4 | 2.7 |
| Finance/Trading | 5 | 183 | 180 | 125 | 16.1 | 3.4 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.971 |         0.103 |     -0.011 |
| forks       |   0.971 |   1     |         0.098 |     -0.026 |
| open_issues |   0.103 |   0.098 |         1     |     -0.024 |
| age_days    |  -0.011 |  -0.026 |        -0.024 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.422 |         0.277 |      0.049 |
| forks       |   0.422 |   1     |         0.591 |     -0.11  |
| open_issues |   0.277 |   0.591 |         1     |     -0.091 |
| age_days    |   0.049 |  -0.11  |        -0.091 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 77 |
| `deepseek-harness` | 73 |
| `ai-agents` | 57 |
| `dsh` | 56 |
| `claude-code` | 43 |
| `deepseek` | 40 |
| `codex` | 38 |
| `llm` | 36 |
| `ai-agent` | 33 |
| `typescript` | 32 |
| `mcp` | 31 |
| `agent` | 28 |
| `developer-tools` | 27 |
| `ai` | 25 |
| `agent-skills` | 25 |
| `python` | 25 |
| `windows` | 24 |
| `macos` | 22 |
| `rust` | 20 |
| `claude` | 18 |
