# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 516.7 | 177.0 | 78014 |
| forks | 62.3 | 17.0 | 10158 |
| open_issues | 8.3 | 1.0 | 1769 |
| stars_per_day | 38.3 | 12.3 | 4546 |
| age_days | 17.6 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 78014 | 10158 | Python | AI/ML |
| `DietrichGebert/ponytail` | 59096 | 3013 | JavaScript | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 10806 | 1029 | TypeScript | AI/ML |
| `baidu/Unlimited-OCR` | 9850 | 747 | Python | Other |
| `unicity-astrid/book` | 7572 | 31 | Perl | Security |
| `unicity-astrid/handbook` | 7516 | 42 | Unknown | Other |
| `helloianneo/ian-xiaohei-illustrations` | 6232 | 742 | Unknown | AI/ML |
| `shadcn/improve` | 6231 | 251 | Unknown | Other |
| `StarTrail-org/PixelRAG` | 5371 | 420 | Python | AI/ML |
| `zgwl/chinese-buy-us-stock-guide` | 5288 | 791 | Unknown | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 4545.8 | 59096 | 13d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 3120.6 | 78014 | 25d | AI/ML |
| `baidu/Unlimited-OCR` | 1407.1 | 9850 | 7d | Other |
| `bozhouDev/codex-orange-book` | 1031.0 | 2062 | 2d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 720.4 | 10806 | 15d | AI/ML |
| `zhongerxin/Cowart` | 430.3 | 3012 | 7d | Other |
| `shadcn/improve` | 415.4 | 6231 | 15d | Other |
| `unicity-astrid/book` | 398.5 | 7572 | 19d | Security |
| `unicity-astrid/handbook` | 395.6 | 7516 | 19d | Other |
| `benchflow-ai/awesome-evals` | 395.0 | 395 | 1d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 425 | 732 | 194 | 77 | 51.2 | 9.7 |
| Other | 351 | 357 | 166 | 42 | 31.7 | 3.9 |
| Web | 59 | 386 | 165 | 37 | 23.3 | 32.8 |
| Mobile | 50 | 296 | 152 | 29 | 20.8 | 4.5 |
| CLI/Tooling | 34 | 303 | 212 | 25 | 20.2 | 5.4 |
| Data | 21 | 390 | 217 | 76 | 27.5 | 4.8 |
| Security | 21 | 750 | 201 | 77 | 49.5 | 9.2 |
| Game | 13 | 214 | 182 | 12 | 17.3 | 1.8 |
| DevOps | 13 | 243 | 184 | 26 | 18.9 | 6.7 |
| Finance/Trading | 13 | 197 | 176 | 506 | 16.8 | 0.5 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.881 |         0.518 |      0.024 |
| forks       |   0.881 |   1     |         0.595 |      0.011 |
| open_issues |   0.518 |   0.595 |         1     |      0.036 |
| age_days    |   0.024 |   0.011 |         0.036 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.585 |         0.35  |      0.082 |
| forks       |   0.585 |   1     |         0.345 |      0.035 |
| open_issues |   0.35  |   0.345 |         1     |      0.097 |
| age_days    |   0.082 |   0.035 |         0.097 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 64 |
| `llm` | 60 |
| `ai-agents` | 56 |
| `ai` | 56 |
| `codex` | 47 |
| `claude` | 34 |
| `ai-agent` | 34 |
| `python` | 32 |
| `typescript` | 31 |
| `macos` | 31 |
| `developer-tools` | 28 |
| `cli` | 25 |
| `mcp` | 25 |
| `agent-skills` | 24 |
| `open-source` | 23 |
| `anthropic` | 20 |
| `swift` | 20 |
| `skills` | 19 |
| `prompt-engineering` | 18 |
| `agent` | 18 |
