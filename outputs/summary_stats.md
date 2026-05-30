# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 414.9 | 231.5 | 12490 |
| forks | 166.4 | 19.0 | 6864 |
| open_issues | 4.6 | 1.0 | 207 |
| stars_per_day | 37.5 | 17.6 | 604 |
| age_days | 16.5 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `antirez/ds4` | 12490 | 1067 | C | Game |
| `BigPizzaV3/CodexPlusPlus` | 8599 | 573 | Rust | AI/ML |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6655 | 5091 | C++ | Other |
| `nexu-io/html-anything` | 5399 | 538 | HTML | AI/ML |
| `darrylmorley/whatcable` | 4821 | 151 | Swift | Mobile |
| `V4bel/dirtyfrag` | 4788 | 768 | C | Other |
| `vercel-labs/zerolang` | 4712 | 302 | C | AI/ML |
| `vercel-labs/zero-native` | 4034 | 162 | Zig | Web |
| `perplexityai/bumblebee` | 3936 | 339 | Go | Other |
| `simplifaisoul/osiris` | 3618 | 718 | TypeScript | Data |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `op7418/guizang-social-card-skill` | 604.0 | 1208 | 2d | AI/ML |
| `antirez/ds4` | 543.0 | 12490 | 23d | Game |
| `helloianneo/ian-xiaohei-illustrations` | 477.5 | 955 | 2d | AI/ML |
| `Michaelliv/pi-dynamic-workflows` | 469.0 | 469 | 1d | Other |
| `perplexityai/bumblebee` | 437.3 | 3936 | 9d | Other |
| `MatinSenPai/SenPaiScanner` | 414.0 | 414 | 1d | Other |
| `2aronS/Duel-Agents` | 406.0 | 406 | 1d | AI/ML |
| `Sophomoresty/gemini-web2api` | 406.0 | 406 | 1d | AI/ML |
| `alfiyahkamilah1239298/WallpaperDownloader-26` | 400.0 | 400 | 1d | Game |
| `BigPizzaV3/CodexPlusPlus` | 373.9 | 8599 | 23d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 400 | 350 | 216 | 102 | 34.2 | 4.0 |
| AI/ML | 376 | 488 | 247 | 104 | 39.4 | 5.4 |
| Web | 46 | 361 | 195 | 82 | 25.5 | 4.5 |
| Mobile | 37 | 446 | 258 | 29 | 31.3 | 3.6 |
| Finance/Trading | 34 | 290 | 267 | 2142 | 57.2 | 0.7 |
| Game | 33 | 623 | 215 | 44 | 64.5 | 6.1 |
| CLI/Tooling | 30 | 410 | 243 | 123 | 32.7 | 4.8 |
| Security | 22 | 262 | 202 | 76 | 35.2 | 2.5 |
| Data | 13 | 499 | 184 | 70 | 34.3 | 6.2 |
| DevOps | 9 | 387 | 327 | 111 | 47.7 | 9.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.125 |         0.552 |      0.11  |
| forks       |   0.125 |   1     |         0.022 |     -0.091 |
| open_issues |   0.552 |   0.022 |         1     |      0.067 |
| age_days    |   0.11  |  -0.091 |         0.067 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.491 |         0.302 |      0.1   |
| forks       |   0.491 |   1     |         0.265 |      0.212 |
| open_issues |   0.302 |   0.265 |         1     |      0.119 |
| age_days    |   0.1   |   0.212 |         0.119 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 52 |
| `ai-agents` | 45 |
| `typescript` | 44 |
| `llm` | 35 |
| `ai` | 33 |
| `mcp` | 30 |
| `codex` | 30 |
| `cli` | 29 |
| `python` | 28 |
| `claude` | 25 |
| `open-source` | 25 |
| `trading-bot` | 20 |
| `agent` | 19 |
| `skills` | 19 |
| `anthropic` | 19 |
| `rust` | 19 |
| `ai-agent` | 19 |
| `macos` | 18 |
| `cursor` | 18 |
| `openai` | 17 |
