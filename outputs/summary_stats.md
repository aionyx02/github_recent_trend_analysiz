# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 817.6 | 303.0 | 199957 |
| forks | 92.5 | 18.0 | 22830 |
| open_issues | 6.4 | 1.0 | 427 |
| stars_per_day | 62.5 | 17.8 | 15381 |
| age_days | 17.6 | 20.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 199957 | 22830 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 21139 | 1026 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 18713 | 2177 | Python | AI/ML |
| `firecrawl/anydoc` | 18642 | 1084 | Rust | Other |
| `yc-software/qm` | 14262 | 1708 | TypeScript | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 13175 | 2201 | Python | Other |
| `trycompai/crm` | 8995 | 1107 | TypeScript | AI/ML |
| `pathwaycom/arc-task-gen` | 7593 | 53 | Python | Other |
| `MiniMax-AI/MiniMax-H3` | 7246 | 476 | Python | Other |
| `yjh051108/dsh-routing-suite` | 6898 | 137 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 15381.3 | 199957 | 13d | Other |
| `anywhere-labs/dsh-desktop` | 1626.1 | 21139 | 13d | Other |
| `guillaumemeyer/watermarks-remover` | 1247.5 | 18713 | 15d | AI/ML |
| `b-nnett/grok-bot-0.18-reconstructed` | 1109.3 | 3328 | 3d | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 1013.5 | 13175 | 13d | Other |
| `MengTo/threeui` | 858.4 | 4292 | 5d | Web |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 846.0 | 846 | 1d | Other |
| `firecrawl/anydoc` | 810.5 | 18642 | 23d | Other |
| `wide-trace/open-higgsfield` | 781.0 | 781 | 1d | Other |
| `tobi/walgit` | 744.3 | 2233 | 3d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 492 | 1021 | 300 | 113 | 76.7 | 5.4 |
| AI/ML | 313 | 688 | 318 | 80 | 53.6 | 8.0 |
| Web | 62 | 599 | 312 | 77 | 55.5 | 3.7 |
| Mobile | 40 | 428 | 326 | 36 | 28.7 | 12.0 |
| Data | 27 | 376 | 281 | 32 | 32.5 | 3.1 |
| CLI/Tooling | 25 | 679 | 368 | 68 | 51.5 | 8.7 |
| Security | 16 | 372 | 318 | 74 | 24.1 | 4.3 |
| Game | 11 | 730 | 286 | 57 | 44.4 | 6.5 |
| DevOps | 9 | 406 | 208 | 77 | 27.2 | 2.2 |
| Finance/Trading | 5 | 180 | 174 | 126 | 17.8 | 3.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.972 |         0.114 |     -0.016 |
| forks       |   0.972 |   1     |         0.108 |     -0.03  |
| open_issues |   0.114 |   0.108 |         1     |      0.006 |
| age_days    |  -0.016 |  -0.03  |         0.006 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.458 |         0.315 |      0.032 |
| forks       |   0.458 |   1     |         0.575 |     -0.069 |
| open_issues |   0.315 |   0.575 |         1     |     -0.053 |
| age_days    |   0.032 |  -0.069 |        -0.053 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 79 |
| `deepseek-harness` | 74 |
| `dsh` | 58 |
| `ai-agents` | 53 |
| `deepseek` | 42 |
| `claude-code` | 41 |
| `typescript` | 35 |
| `llm` | 34 |
| `codex` | 34 |
| `ai-agent` | 34 |
| `mcp` | 28 |
| `agent` | 28 |
| `ai` | 27 |
| `developer-tools` | 26 |
| `python` | 24 |
| `agent-skills` | 23 |
| `windows` | 21 |
| `macos` | 20 |
| `rust` | 20 |
| `react` | 19 |
