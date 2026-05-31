# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 410.0 | 225.0 | 12580 |
| forks | 176.1 | 19.0 | 6864 |
| open_issues | 6.6 | 1.0 | 2180 |
| stars_per_day | 35.1 | 16.4 | 603 |
| age_days | 16.7 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `antirez/ds4` | 12580 | 1078 | C | Game |
| `BigPizzaV3/CodexPlusPlus` | 9115 | 615 | Rust | AI/ML |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6678 | 5101 | C++ | Other |
| `nexu-io/html-anything` | 5506 | 545 | HTML | AI/ML |
| `darrylmorley/whatcable` | 4949 | 155 | Swift | Mobile |
| `V4bel/dirtyfrag` | 4790 | 770 | C | Other |
| `vercel-labs/zerolang` | 4744 | 305 | C | AI/ML |
| `vercel-labs/zero-native` | 4040 | 164 | Zig | Web |
| `perplexityai/bumblebee` | 4000 | 346 | Go | Other |
| `simplifaisoul/osiris` | 3786 | 758 | TypeScript | Data |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `op7418/guizang-social-card-skill` | 603.3 | 1810 | 3d | AI/ML |
| `antirez/ds4` | 524.2 | 12580 | 24d | Game |
| `helloianneo/ian-xiaohei-illustrations` | 419.7 | 1259 | 3d | AI/ML |
| `perplexityai/bumblebee` | 400.0 | 4000 | 10d | Other |
| `BigPizzaV3/CodexPlusPlus` | 379.8 | 9115 | 24d | AI/ML |
| `FULU-Foundation/OrcaSlicer-bambulab` | 351.5 | 6678 | 19d | Other |
| `Sophomoresty/gemini-web2api` | 339.5 | 679 | 2d | AI/ML |
| `MatinSenPai/SenPaiScanner` | 330.0 | 660 | 2d | Other |
| `vercel-labs/zerolang` | 316.3 | 4744 | 15d | AI/ML |
| `bonus-2026/crypto-casino-bonus` | 312.0 | 312 | 1d | Finance/Trading |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 401 | 345 | 215 | 127 | 31.7 | 9.2 |
| AI/ML | 384 | 473 | 241 | 110 | 37.0 | 5.1 |
| Web | 47 | 347 | 175 | 77 | 25.5 | 4.0 |
| Finance/Trading | 38 | 279 | 264 | 1863 | 52.3 | 0.7 |
| Mobile | 35 | 457 | 251 | 29 | 32.8 | 3.9 |
| CLI/Tooling | 31 | 403 | 240 | 83 | 32.9 | 4.7 |
| Game | 26 | 751 | 286 | 57 | 59.1 | 7.9 |
| Security | 17 | 302 | 283 | 95 | 32.5 | 2.6 |
| DevOps | 11 | 337 | 149 | 95 | 27.7 | 8.5 |
| Data | 10 | 626 | 218 | 95 | 37.6 | 8.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.121 |         0.1   |      0.104 |
| forks       |   0.121 |   1     |         0.014 |     -0.1   |
| open_issues |   0.1   |   0.014 |         1     |     -0     |
| age_days    |   0.104 |  -0.1   |        -0     |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.452 |         0.272 |      0.081 |
| forks       |   0.452 |   1     |         0.232 |      0.125 |
| open_issues |   0.272 |   0.232 |         1     |      0.102 |
| age_days    |   0.081 |   0.125 |         0.102 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 52 |
| `claude-code` | 51 |
| `typescript` | 49 |
| `llm` | 36 |
| `ai` | 35 |
| `codex` | 31 |
| `python` | 30 |
| `open-source` | 30 |
| `mcp` | 29 |
| `cli` | 29 |
| `claude` | 26 |
| `rust` | 23 |
| `trading-bot` | 22 |
| `ai-agent` | 21 |
| `agent` | 20 |
| `skills` | 19 |
| `anthropic` | 19 |
| `macos` | 18 |
| `openai` | 18 |
| `react` | 17 |
