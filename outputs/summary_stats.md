# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 482.4 | 193.0 | 73904 |
| forks | 93.6 | 17.0 | 11461 |
| open_issues | 8.2 | 1.0 | 1644 |
| stars_per_day | 44.9 | 13.8 | 6426 |
| age_days | 16.9 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 73904 | 9509 | Python | AI/ML |
| `DietrichGebert/ponytail` | 38554 | 1813 | JavaScript | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 9857 | 904 | TypeScript | AI/ML |
| `anthropics/defending-code-reference-harness` | 6090 | 455 | Python | Security |
| `shadcn/improve` | 5554 | 212 | Unknown | Other |
| `helloianneo/ian-xiaohei-illustrations` | 5258 | 604 | Unknown | AI/ML |
| `AprilNEA/OpenLogi` | 5136 | 99 | Rust | Other |
| `zgwl/chinese-buy-us-stock-guide` | 4706 | 720 | Unknown | Other |
| `perplexityai/bumblebee` | 4531 | 411 | Go | Other |
| `open-gsd/gsd-core` | 4498 | 276 | JavaScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 6425.7 | 38554 | 6d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 4105.8 | 73904 | 18d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 1232.1 | 9857 | 8d | AI/ML |
| `vercel/eve` | 750.5 | 1501 | 2d | AI/ML |
| `shadcn/improve` | 694.2 | 5554 | 8d | Other |
| `omnigent-ai/omnigent` | 558.6 | 3910 | 7d | AI/ML |
| `Plaer1/junction` | 510.0 | 510 | 1d | AI/ML |
| `tamnd/kage` | 508.0 | 2032 | 4d | Other |
| `ApothecarySeize/Maya-2026-Animation-Workflow` | 320.0 | 320 | 1d | Other |
| `Waishnav/devspace` | 271.5 | 1086 | 4d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 404 | 344 | 188 | 49 | 33.0 | 4.7 |
| AI/ML | 394 | 698 | 206 | 76 | 62.7 | 9.8 |
| Web | 54 | 332 | 183 | 38 | 24.8 | 33.0 |
| Mobile | 41 | 317 | 177 | 35 | 30.1 | 5.7 |
| CLI/Tooling | 31 | 404 | 229 | 34 | 32.1 | 6.4 |
| Finance/Trading | 18 | 194 | 201 | 2039 | 46.9 | 0.4 |
| Security | 18 | 697 | 204 | 103 | 57.4 | 6.0 |
| DevOps | 14 | 178 | 136 | 16 | 24.5 | 3.8 |
| Game | 14 | 202 | 138 | 11 | 36.7 | 2.9 |
| Data | 12 | 294 | 169 | 34 | 45.6 | 2.3 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.477 |         0.563 |      0.003 |
| forks       |   0.477 |   1     |         0.314 |      0.075 |
| open_issues |   0.563 |   0.314 |         1     |      0.008 |
| age_days    |   0.003 |   0.075 |         0.008 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.58  |         0.3   |      0.103 |
| forks       |   0.58  |   1     |         0.36  |      0.183 |
| open_issues |   0.3   |   0.36  |         1     |      0.194 |
| age_days    |   0.103 |   0.183 |         0.194 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 57 |
| `ai-agents` | 47 |
| `llm` | 47 |
| `ai` | 43 |
| `codex` | 41 |
| `windows` | 39 |
| `workflow` | 35 |
| `macos` | 29 |
| `ai-agent` | 28 |
| `typescript` | 28 |
| `python` | 27 |
| `developer-tools` | 23 |
| `mcp` | 23 |
| `cli` | 22 |
| `open-source` | 22 |
| `skills` | 22 |
| `claude` | 21 |
| `agent` | 19 |
| `prompt-engineering` | 18 |
| `swift` | 18 |
