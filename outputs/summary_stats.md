# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 489.7 | 186.5 | 76559 |
| forks | 73.7 | 16.0 | 9965 |
| open_issues | 7.9 | 1.0 | 1694 |
| stars_per_day | 42.9 | 13.0 | 5095 |
| age_days | 17.1 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 76559 | 9965 | Python | AI/ML |
| `DietrichGebert/ponytail` | 50951 | 2508 | JavaScript | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 10411 | 977 | TypeScript | AI/ML |
| `shadcn/improve` | 6016 | 241 | Unknown | Other |
| `helloianneo/ian-xiaohei-illustrations` | 5814 | 690 | Unknown | AI/ML |
| `AprilNEA/OpenLogi` | 5251 | 100 | Rust | Other |
| `zgwl/chinese-buy-us-stock-guide` | 4842 | 742 | Unknown | Other |
| `unicity-astrid/book` | 4605 | 17 | Perl | Security |
| `omnigent-ai/omnigent` | 4505 | 518 | Python | AI/ML |
| `unicity-astrid/handbook` | 4483 | 24 | Unknown | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 5095.1 | 50951 | 10d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 3480.0 | 76559 | 22d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 867.6 | 10411 | 12d | AI/ML |
| `kanavtwtgg/birds.cafe` | 633.0 | 633 | 1d | Other |
| `zhongerxin/Cowart` | 552.8 | 2211 | 4d | Other |
| `shadcn/improve` | 501.3 | 6016 | 12d | Other |
| `omnigent-ai/omnigent` | 409.5 | 4505 | 11d | AI/ML |
| `lyra81604/zhengxi-views` | 394.5 | 789 | 2d | AI/ML |
| `vercel/eve` | 391.0 | 2346 | 6d | AI/ML |
| `baidu/Unlimited-OCR` | 311.8 | 1247 | 4d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 396 | 330 | 161 | 51 | 39.4 | 4.4 |
| AI/ML | 388 | 738 | 210 | 78 | 54.3 | 9.1 |
| Web | 56 | 368 | 192 | 35 | 28.5 | 32.8 |
| Mobile | 45 | 312 | 152 | 32 | 23.9 | 4.8 |
| CLI/Tooling | 35 | 273 | 188 | 22 | 22.5 | 4.5 |
| Game | 17 | 200 | 177 | 9 | 41.2 | 2.1 |
| Finance/Trading | 17 | 243 | 229 | 933 | 30.1 | 0.5 |
| DevOps | 16 | 218 | 176 | 24 | 21.6 | 4.3 |
| Security | 16 | 703 | 226 | 88 | 46.8 | 9.2 |
| Data | 14 | 438 | 176 | 92 | 37.4 | 9.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.695 |         0.549 |      0.011 |
| forks       |   0.695 |   1     |         0.475 |      0.046 |
| open_issues |   0.549 |   0.475 |         1     |      0.02  |
| age_days    |   0.011 |   0.046 |         0.02  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.575 |         0.31  |      0.078 |
| forks       |   0.575 |   1     |         0.346 |      0.125 |
| open_issues |   0.31  |   0.346 |         1     |      0.179 |
| age_days    |   0.078 |   0.125 |         0.179 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 56 |
| `ai-agents` | 50 |
| `llm` | 47 |
| `ai` | 46 |
| `codex` | 43 |
| `python` | 38 |
| `skills` | 30 |
| `claude` | 29 |
| `typescript` | 29 |
| `ai-agent` | 27 |
| `macos` | 27 |
| `developer-tools` | 26 |
| `open-source` | 26 |
| `mcp` | 25 |
| `cli` | 24 |
| `agent-skills` | 21 |
| `prompt-engineering` | 19 |
| `swift` | 18 |
| `agent` | 17 |
| `anthropic` | 15 |
