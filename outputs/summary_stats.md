# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 471.0 | 192.0 | 73282 |
| forks | 102.9 | 17.0 | 11461 |
| open_issues | 8.0 | 1.0 | 1621 |
| stars_per_day | 43.1 | 12.8 | 6814 |
| age_days | 17.3 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 73282 | 9409 | Python | AI/ML |
| `DietrichGebert/ponytail` | 34072 | 1552 | JavaScript | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 9692 | 878 | TypeScript | AI/ML |
| `anthropics/defending-code-reference-harness` | 6077 | 452 | Python | Security |
| `shadcn/improve` | 5352 | 206 | Unknown | Other |
| `helloianneo/ian-xiaohei-illustrations` | 5146 | 583 | Unknown | AI/ML |
| `AprilNEA/OpenLogi` | 5095 | 98 | Rust | Other |
| `zgwl/chinese-buy-us-stock-guide` | 4681 | 719 | Unknown | Other |
| `perplexityai/bumblebee` | 4489 | 408 | Go | Other |
| `KunAgent/Kun` | 4439 | 391 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 6814.4 | 34072 | 5d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 4310.7 | 73282 | 17d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 1384.6 | 9692 | 7d | AI/ML |
| `vercel/eve` | 1070.0 | 1070 | 1d | AI/ML |
| `shadcn/improve` | 764.6 | 5352 | 7d | Other |
| `tamnd/kage` | 643.3 | 1930 | 3d | Other |
| `omnigent-ai/omnigent` | 611.8 | 3671 | 6d | AI/ML |
| `Plaer1/junction` | 504.0 | 504 | 1d | AI/ML |
| `rebel0789/codexpro` | 337.0 | 337 | 1d | AI/ML |
| `alchaincyf/loop-engineering-orange-book` | 328.0 | 656 | 2d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 405 | 658 | 198 | 69 | 64.5 | 9.1 |
| Other | 405 | 344 | 194 | 85 | 27.8 | 4.7 |
| Web | 58 | 319 | 182 | 62 | 22.9 | 30.4 |
| Mobile | 38 | 325 | 189 | 37 | 31.3 | 5.7 |
| CLI/Tooling | 34 | 376 | 200 | 125 | 32.8 | 6.1 |
| Security | 14 | 820 | 318 | 126 | 54.0 | 7.4 |
| DevOps | 13 | 178 | 139 | 21 | 20.1 | 3.8 |
| Finance/Trading | 12 | 180 | 158 | 2398 | 22.6 | 0.6 |
| Game | 11 | 211 | 189 | 14 | 16.5 | 3.6 |
| Data | 10 | 319 | 203 | 40 | 54.8 | 2.6 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.45  |         0.579 |     -0.011 |
| forks       |   0.45  |   1     |         0.296 |      0.071 |
| open_issues |   0.579 |   0.296 |         1     |     -0.006 |
| age_days    |  -0.011 |   0.071 |        -0.006 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.569 |         0.301 |      0.041 |
| forks       |   0.569 |   1     |         0.342 |      0.108 |
| open_issues |   0.301 |   0.342 |         1     |      0.144 |
| age_days    |   0.041 |   0.108 |         0.144 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 60 |
| `llm` | 49 |
| `ai-agents` | 48 |
| `codex` | 44 |
| `ai` | 43 |
| `typescript` | 30 |
| `macos` | 29 |
| `ai-agent` | 28 |
| `python` | 26 |
| `cli` | 24 |
| `mcp` | 24 |
| `skills` | 23 |
| `claude` | 20 |
| `developer-tools` | 20 |
| `open-source` | 20 |
| `agent` | 20 |
| `prompt-engineering` | 19 |
| `agent-skills` | 18 |
| `swift` | 17 |
| `rust` | 15 |
