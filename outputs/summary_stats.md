# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 823.9 | 318.0 | 202829 |
| forks | 91.1 | 17.0 | 23352 |
| open_issues | 5.9 | 1.0 | 501 |
| stars_per_day | 64.9 | 17.6 | 13522 |
| age_days | 18.3 | 21.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 202829 | 23352 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 21754 | 1062 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 19162 | 2230 | Python | AI/ML |
| `firecrawl/anydoc` | 19143 | 1130 | Rust | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 13490 | 2305 | Python | Other |
| `trycompai/crm` | 9075 | 1121 | TypeScript | AI/ML |
| `pathwaycom/arc-task-gen` | 8691 | 57 | Python | Other |
| `MiniMax-AI/MiniMax-H3` | 7371 | 483 | Python | Other |
| `yjh051108/dsh-routing-suite` | 6939 | 141 | JavaScript | Other |
| `FareedKhan-dev/kimi-k3-in-c` | 6705 | 1094 | C | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 13521.9 | 202829 | 15d | Other |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 3832.0 | 3832 | 1d | Other |
| `sapientinc/PRAXIST` | 2081.0 | 2081 | 1d | Other |
| `anywhere-labs/dsh-desktop` | 1450.3 | 21754 | 15d | Other |
| `guillaumemeyer/watermarks-remover` | 1127.2 | 19162 | 17d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 899.3 | 13490 | 15d | Other |
| `firecrawl/anydoc` | 765.7 | 19143 | 25d | Other |
| `XiaoDuoYa/codex-with-chatgpt` | 688.0 | 688 | 1d | AI/ML |
| `b-nnett/grok-bot-0.18-reconstructed` | 683.6 | 3418 | 5d | Other |
| `MengTo/threeui` | 643.4 | 4504 | 7d | Web |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 499 | 1046 | 316 | 112 | 81.1 | 6.2 |
| AI/ML | 314 | 658 | 334 | 76 | 53.2 | 5.9 |
| Web | 59 | 639 | 339 | 85 | 51.3 | 3.8 |
| Mobile | 41 | 475 | 367 | 39 | 40.7 | 8.9 |
| Data | 25 | 325 | 282 | 19 | 27.6 | 2.4 |
| CLI/Tooling | 22 | 581 | 334 | 62 | 38.1 | 9.0 |
| Security | 15 | 369 | 314 | 68 | 21.6 | 2.9 |
| Game | 11 | 596 | 358 | 44 | 37.2 | 5.7 |
| DevOps | 8 | 444 | 228 | 87 | 25.8 | 2.8 |
| Finance/Trading | 6 | 230 | 188 | 120 | 88.7 | 2.5 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.972 |         0.1   |     -0.01  |
| forks       |   0.972 |   1     |         0.093 |     -0.03  |
| open_issues |   0.1   |   0.093 |         1     |     -0.069 |
| age_days    |  -0.01  |  -0.03  |        -0.069 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.407 |         0.256 |      0.037 |
| forks       |   0.407 |   1     |         0.572 |     -0.185 |
| open_issues |   0.256 |   0.572 |         1     |     -0.119 |
| age_days    |   0.037 |  -0.185 |        -0.119 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 81 |
| `deepseek-harness` | 77 |
| `ai-agents` | 60 |
| `dsh` | 59 |
| `claude-code` | 46 |
| `deepseek` | 42 |
| `llm` | 39 |
| `codex` | 39 |
| `ai-agent` | 34 |
| `typescript` | 32 |
| `mcp` | 32 |
| `agent` | 29 |
| `developer-tools` | 28 |
| `ai` | 27 |
| `agent-skills` | 25 |
| `python` | 25 |
| `windows` | 24 |
| `macos` | 23 |
| `rust` | 22 |
| `claude` | 20 |
