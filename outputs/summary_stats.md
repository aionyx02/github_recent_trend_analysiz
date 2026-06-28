# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 509.6 | 176.0 | 78738 |
| forks | 66.6 | 17.0 | 10268 |
| open_issues | 8.3 | 1.0 | 1897 |
| stars_per_day | 38.6 | 12.5 | 4162 |
| age_days | 17.4 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 78738 | 10268 | Python | AI/ML |
| `DietrichGebert/ponytail` | 62428 | 3210 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 11266 | 872 | Python | Other |
| `XiaomiMiMo/MiMo-Code` | 10957 | 1054 | TypeScript | AI/ML |
| `unicity-astrid/book` | 7550 | 31 | Perl | Security |
| `unicity-astrid/handbook` | 7498 | 42 | Unknown | Other |
| `shadcn/improve` | 6346 | 254 | Unknown | Other |
| `StarTrail-org/PixelRAG` | 5533 | 435 | Python | AI/ML |
| `zgwl/chinese-buy-us-stock-guide` | 5362 | 803 | Unknown | Other |
| `omnigent-ai/omnigent` | 5174 | 646 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 4161.9 | 62428 | 15d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 2916.2 | 78738 | 27d | AI/ML |
| `deepseek-ai/DeepSpec` | 1686.0 | 1686 | 1d | Other |
| `baidu/Unlimited-OCR` | 1251.8 | 11266 | 9d | Other |
| `XiaomiMiMo/MiMo-Code` | 644.5 | 10957 | 17d | AI/ML |
| `bozhouDev/codex-orange-book` | 558.5 | 2234 | 4d | AI/ML |
| `bikini/exploitarium` | 380.2 | 1521 | 4d | Security |
| `shadcn/improve` | 373.3 | 6346 | 17d | Other |
| `unicity-astrid/book` | 359.5 | 7550 | 21d | Security |
| `unicity-astrid/handbook` | 357.0 | 7498 | 21d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 417 | 719 | 191 | 78 | 47.0 | 10.1 |
| Other | 351 | 354 | 166 | 44 | 35.5 | 3.3 |
| Web | 60 | 446 | 172 | 42 | 23.6 | 35.8 |
| Mobile | 48 | 310 | 160 | 29 | 19.0 | 4.9 |
| CLI/Tooling | 35 | 293 | 165 | 26 | 21.0 | 4.7 |
| Security | 23 | 744 | 208 | 90 | 67.3 | 8.0 |
| Data | 22 | 326 | 174 | 68 | 33.0 | 4.6 |
| Finance/Trading | 20 | 214 | 184 | 492 | 37.1 | 0.5 |
| Game | 13 | 183 | 142 | 10 | 21.5 | 4.1 |
| DevOps | 11 | 269 | 198 | 31 | 20.3 | 6.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.858 |         0.504 |      0.033 |
| forks       |   0.858 |   1     |         0.563 |      0.01  |
| open_issues |   0.504 |   0.563 |         1     |      0.051 |
| age_days    |   0.033 |   0.01  |         0.051 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.556 |         0.323 |      0.064 |
| forks       |   0.556 |   1     |         0.342 |      0.01  |
| open_issues |   0.323 |   0.342 |         1     |      0.101 |
| age_days    |   0.064 |   0.01  |         0.101 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 64 |
| `llm` | 59 |
| `ai` | 58 |
| `ai-agents` | 53 |
| `codex` | 45 |
| `claude` | 35 |
| `macos` | 32 |
| `ai-agent` | 31 |
| `typescript` | 30 |
| `python` | 28 |
| `developer-tools` | 26 |
| `mcp` | 26 |
| `open-source` | 24 |
| `agent-skills` | 23 |
| `cli` | 23 |
| `anthropic` | 19 |
| `skills` | 19 |
| `swift` | 18 |
| `rust` | 17 |
| `prompt-engineering` | 16 |
