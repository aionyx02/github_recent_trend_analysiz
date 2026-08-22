# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 762.3 | 285.0 | 182411 |
| forks | 80.4 | 18.0 | 20016 |
| open_issues | 5.6 | 1.0 | 343 |
| stars_per_day | 73.4 | 20.5 | 22801 |
| age_days | 16.0 | 15.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 182411 | 20016 | TypeScript | Other |
| `firecrawl/anydoc` | 17804 | 1026 | Rust | Other |
| `anywhere-labs/deepseek-harness-desktop` | 17803 | 868 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 16724 | 1923 | Python | AI/ML |
| `yc-software/qm` | 14051 | 1680 | TypeScript | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 11265 | 1719 | Python | Other |
| `trycompai/crm` | 8785 | 1065 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 8571 | 679 | Unknown | Other |
| `MiniMax-AI/MiniMax-H3` | 6655 | 410 | Python | Other |
| `yjh051108/dsh-routing-suite` | 6591 | 125 | PowerShell | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 22801.4 | 182411 | 8d | Other |
| `anywhere-labs/deepseek-harness-desktop` | 2225.4 | 17803 | 8d | Other |
| `guillaumemeyer/watermarks-remover` | 1672.4 | 16724 | 10d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 1408.1 | 11265 | 8d | Other |
| `s1dashu/ip-as-logo-skill` | 1181.3 | 3544 | 3d | AI/ML |
| `firecrawl/anydoc` | 989.1 | 17804 | 18d | Other |
| `yjh051108/dsh-routing-suite` | 941.6 | 6591 | 7d | Other |
| `MengTo/threeui` | 828.0 | 828 | 1d | Web |
| `Leutenegger/vanity-eth` | 803.0 | 803 | 1d | CLI/Tooling |
| `yetone/cumora` | 719.8 | 2879 | 4d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 495 | 929 | 281 | 92 | 89.8 | 4.4 |
| AI/ML | 299 | 683 | 296 | 79 | 61.9 | 7.3 |
| Web | 64 | 543 | 264 | 53 | 64.7 | 2.9 |
| Mobile | 43 | 438 | 298 | 37 | 31.1 | 14.9 |
| CLI/Tooling | 34 | 539 | 319 | 51 | 64.0 | 5.7 |
| Data | 19 | 392 | 257 | 36 | 27.3 | 2.4 |
| Security | 18 | 334 | 214 | 66 | 70.9 | 2.2 |
| DevOps | 12 | 360 | 232 | 64 | 29.6 | 3.8 |
| Game | 10 | 692 | 306 | 54 | 53.5 | 6.6 |
| Finance/Trading | 6 | 314 | 169 | 194 | 22.2 | 2.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.984 |         0.119 |     -0.034 |
| forks       |   0.984 |   1     |         0.114 |     -0.033 |
| open_issues |   0.119 |   0.114 |         1     |      0.022 |
| age_days    |  -0.034 |  -0.033 |         0.022 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.465 |         0.325 |      0.02  |
| forks       |   0.465 |   1     |         0.566 |      0.085 |
| open_issues |   0.325 |   0.566 |         1     |      0.091 |
| age_days    |   0.02  |   0.085 |         0.091 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 65 |
| `deepseek-harness` | 56 |
| `dsh` | 50 |
| `ai-agents` | 44 |
| `codex` | 40 |
| `claude-code` | 37 |
| `deepseek` | 35 |
| `typescript` | 35 |
| `llm` | 33 |
| `developer-tools` | 30 |
| `ai` | 29 |
| `ai-agent` | 28 |
| `agent` | 25 |
| `python` | 25 |
| `mcp` | 24 |
| `macos` | 23 |
| `cli` | 23 |
| `windows` | 22 |
| `agent-skills` | 21 |
| `rust` | 21 |
