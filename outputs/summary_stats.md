# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 506.9 | 177.0 | 77603 |
| forks | 67.8 | 17.5 | 10100 |
| open_issues | 8.0 | 1.0 | 1711 |
| stars_per_day | 39.5 | 12.1 | 4713 |
| age_days | 17.5 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 77603 | 10100 | Python | AI/ML |
| `DietrichGebert/ponytail` | 56561 | 2861 | JavaScript | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 10676 | 1005 | TypeScript | AI/ML |
| `unicity-astrid/book` | 7214 | 31 | Perl | Security |
| `unicity-astrid/handbook` | 7168 | 41 | Unknown | Other |
| `baidu/Unlimited-OCR` | 6947 | 566 | Python | Other |
| `shadcn/improve` | 6175 | 246 | Unknown | Other |
| `helloianneo/ian-xiaohei-illustrations` | 6084 | 723 | Unknown | AI/ML |
| `StarTrail-org/PixelRAG` | 5216 | 400 | Python | AI/ML |
| `zgwl/chinese-buy-us-stock-guide` | 5207 | 785 | Unknown | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 4713.4 | 56561 | 12d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 3233.5 | 77603 | 24d | AI/ML |
| `bozhouDev/codex-orange-book` | 1696.0 | 1696 | 1d | AI/ML |
| `baidu/Unlimited-OCR` | 1157.8 | 6947 | 6d | Other |
| `XiaomiMiMo/MiMo-Code` | 762.6 | 10676 | 14d | AI/ML |
| `zhongerxin/Cowart` | 467.8 | 2807 | 6d | Other |
| `shadcn/improve` | 441.1 | 6175 | 14d | Other |
| `unicity-astrid/book` | 400.8 | 7214 | 18d | Security |
| `unicity-astrid/handbook` | 398.2 | 7168 | 18d | Other |
| `omnigent-ai/omnigent` | 369.2 | 4800 | 13d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 410 | 737 | 196 | 78 | 54.4 | 9.6 |
| Other | 359 | 351 | 166 | 59 | 31.8 | 3.9 |
| Web | 61 | 363 | 159 | 35 | 25.9 | 30.7 |
| Mobile | 51 | 291 | 150 | 28 | 20.2 | 4.5 |
| CLI/Tooling | 35 | 289 | 178 | 24 | 20.7 | 5.0 |
| Security | 22 | 693 | 192 | 73 | 52.9 | 9.2 |
| Data | 20 | 377 | 200 | 73 | 29.1 | 3.5 |
| DevOps | 15 | 227 | 184 | 24 | 19.0 | 6.0 |
| Game | 15 | 202 | 174 | 12 | 17.4 | 2.3 |
| Finance/Trading | 12 | 198 | 172 | 543 | 15.3 | 0.6 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.808 |         0.533 |      0.017 |
| forks       |   0.808 |   1     |         0.553 |      0.025 |
| open_issues |   0.533 |   0.553 |         1     |      0.029 |
| age_days    |   0.017 |   0.025 |         0.029 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.577 |         0.342 |      0.069 |
| forks       |   0.577 |   1     |         0.332 |      0.039 |
| open_issues |   0.342 |   0.332 |         1     |      0.133 |
| age_days    |   0.069 |   0.039 |         0.133 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 61 |
| `llm` | 54 |
| `ai` | 53 |
| `ai-agents` | 52 |
| `codex` | 43 |
| `ai-agent` | 33 |
| `python` | 31 |
| `typescript` | 31 |
| `claude` | 30 |
| `macos` | 30 |
| `developer-tools` | 25 |
| `open-source` | 25 |
| `cli` | 24 |
| `mcp` | 24 |
| `agent-skills` | 21 |
| `swift` | 20 |
| `agent` | 18 |
| `anthropic` | 18 |
| `skills` | 18 |
| `prompt-engineering` | 16 |
