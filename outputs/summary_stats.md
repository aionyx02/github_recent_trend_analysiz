# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 424.6 | 226.0 | 13745 |
| forks | 188.9 | 19.5 | 6864 |
| open_issues | 7.4 | 1.0 | 2701 |
| stars_per_day | 50.1 | 16.4 | 13745 |
| age_days | 16.7 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 13745 | 1755 | JavaScript | AI/ML |
| `antirez/ds4` | 12663 | 1095 | C | Game |
| `BigPizzaV3/CodexPlusPlus` | 10259 | 674 | Rust | AI/ML |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6702 | 5118 | C++ | Other |
| `nexu-io/html-anything` | 5693 | 558 | HTML | AI/ML |
| `V4bel/dirtyfrag` | 4795 | 774 | C | Other |
| `vercel-labs/zerolang` | 4770 | 306 | C | AI/ML |
| `perplexityai/bumblebee` | 4079 | 354 | Go | Other |
| `vercel-labs/zero-native` | 4063 | 164 | Zig | Web |
| `simplifaisoul/osiris` | 3994 | 790 | TypeScript | Data |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 13745.0 | 13745 | 1d | AI/ML |
| `op7418/guizang-social-card-skill` | 584.5 | 2338 | 4d | AI/ML |
| `antirez/ds4` | 506.5 | 12663 | 25d | Game |
| `asz798838958/aBaiAutoplus` | 435.0 | 435 | 1d | AI/ML |
| `BigPizzaV3/CodexPlusPlus` | 410.4 | 10259 | 25d | AI/ML |
| `helloianneo/ian-xiaohei-illustrations` | 393.0 | 1572 | 4d | AI/ML |
| `perplexityai/bumblebee` | 370.8 | 4079 | 11d | Other |
| `liyue-aigc/female-portrait-director` | 358.0 | 358 | 1d | AI/ML |
| `FULU-Foundation/OrcaSlicer-bambulab` | 335.1 | 6702 | 20d | Other |
| `Sophomoresty/gemini-web2api` | 334.7 | 1004 | 3d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 405 | 357 | 212 | 147 | 33.3 | 10.6 |
| AI/ML | 371 | 521 | 249 | 124 | 76.0 | 6.0 |
| Web | 47 | 335 | 189 | 73 | 31.9 | 3.8 |
| CLI/Tooling | 37 | 359 | 205 | 72 | 35.3 | 4.3 |
| Finance/Trading | 36 | 295 | 272 | 1979 | 39.9 | 0.7 |
| Mobile | 34 | 321 | 253 | 26 | 24.0 | 3.7 |
| Game | 27 | 745 | 282 | 56 | 60.2 | 7.9 |
| Security | 20 | 268 | 201 | 77 | 33.1 | 1.8 |
| DevOps | 12 | 333 | 184 | 89 | 39.2 | 7.8 |
| Data | 11 | 611 | 229 | 90 | 54.0 | 8.4 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.13  |         0.116 |      0.048 |
| forks       |   0.13  |   1     |         0.018 |     -0.097 |
| open_issues |   0.116 |   0.018 |         1     |     -0.001 |
| age_days    |   0.048 |  -0.097 |        -0.001 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.457 |         0.292 |      0.063 |
| forks       |   0.457 |   1     |         0.228 |      0.144 |
| open_issues |   0.292 |   0.228 |         1     |      0.105 |
| age_days    |   0.063 |   0.144 |         0.105 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 53 |
| `claude-code` | 52 |
| `typescript` | 50 |
| `ai` | 36 |
| `llm` | 34 |
| `python` | 31 |
| `codex` | 31 |
| `open-source` | 31 |
| `cli` | 29 |
| `mcp` | 28 |
| `claude` | 26 |
| `rust` | 23 |
| `agent` | 22 |
| `trading-bot` | 21 |
| `ai-agent` | 19 |
| `anthropic` | 19 |
| `skills` | 19 |
| `macos` | 19 |
| `developer-tools` | 18 |
| `openai` | 18 |
