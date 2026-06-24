# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 500.0 | 182.0 | 77071 |
| forks | 65.0 | 17.0 | 10025 |
| open_issues | 7.9 | 1.0 | 1706 |
| stars_per_day | 40.0 | 12.3 | 4868 |
| age_days | 17.5 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 77071 | 10025 | Python | AI/ML |
| `DietrichGebert/ponytail` | 53550 | 2679 | JavaScript | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 10556 | 991 | TypeScript | AI/ML |
| `unicity-astrid/book` | 6669 | 27 | Perl | Security |
| `unicity-astrid/handbook` | 6619 | 37 | Unknown | Other |
| `shadcn/improve` | 6100 | 245 | Unknown | Other |
| `helloianneo/ian-xiaohei-illustrations` | 5956 | 703 | Unknown | AI/ML |
| `zgwl/chinese-buy-us-stock-guide` | 4994 | 757 | Unknown | Other |
| `baidu/Unlimited-OCR` | 4985 | 353 | Python | Other |
| `StarTrail-org/PixelRAG` | 4934 | 380 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 4868.2 | 53550 | 11d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 3350.9 | 77071 | 23d | AI/ML |
| `baidu/Unlimited-OCR` | 997.0 | 4985 | 5d | Other |
| `bozhouDev/codex-orange-book` | 879.0 | 879 | 1d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 812.0 | 10556 | 13d | AI/ML |
| `zhongerxin/Cowart` | 508.0 | 2540 | 5d | Other |
| `shadcn/improve` | 469.2 | 6100 | 13d | Other |
| `unicity-astrid/book` | 392.3 | 6669 | 17d | Security |
| `unicity-astrid/handbook` | 389.4 | 6619 | 17d | Other |
| `omnigent-ai/omnigent` | 386.9 | 4643 | 12d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 405 | 735 | 206 | 78 | 54.4 | 9.1 |
| Other | 375 | 339 | 165 | 56 | 32.5 | 4.3 |
| Web | 62 | 351 | 174 | 33 | 30.8 | 30.0 |
| Mobile | 49 | 298 | 147 | 30 | 21.0 | 5.1 |
| CLI/Tooling | 33 | 287 | 178 | 24 | 21.9 | 4.9 |
| Data | 18 | 386 | 181 | 76 | 29.5 | 5.2 |
| Security | 18 | 773 | 192 | 83 | 47.2 | 8.9 |
| Game | 16 | 192 | 152 | 11 | 19.2 | 2.2 |
| DevOps | 15 | 229 | 188 | 25 | 20.8 | 4.7 |
| Finance/Trading | 9 | 221 | 210 | 513 | 16.5 | 0.9 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.814 |         0.534 |      0.011 |
| forks       |   0.814 |   1     |         0.553 |      0.02  |
| open_issues |   0.534 |   0.553 |         1     |      0.022 |
| age_days    |   0.011 |   0.02  |         0.022 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.578 |         0.334 |      0.097 |
| forks       |   0.578 |   1     |         0.35  |      0.062 |
| open_issues |   0.334 |   0.35  |         1     |      0.145 |
| age_days    |   0.097 |   0.062 |         0.145 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 61 |
| `llm` | 54 |
| `ai-agents` | 52 |
| `ai` | 50 |
| `codex` | 45 |
| `claude` | 34 |
| `ai-agent` | 32 |
| `python` | 31 |
| `typescript` | 30 |
| `macos` | 28 |
| `developer-tools` | 27 |
| `mcp` | 25 |
| `cli` | 23 |
| `open-source` | 23 |
| `agent-skills` | 22 |
| `prompt-engineering` | 19 |
| `agent` | 19 |
| `anthropic` | 18 |
| `skills` | 18 |
| `swift` | 18 |
