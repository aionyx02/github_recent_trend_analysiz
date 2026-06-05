# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 470.6 | 200.0 | 53148 |
| forks | 94.1 | 19.0 | 6659 |
| open_issues | 10.8 | 1.0 | 3877 |
| stars_per_day | 45.7 | 13.1 | 13287 |
| age_days | 17.5 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 53148 | 6253 | Python | AI/ML |
| `BigPizzaV3/CodexPlusPlus` | 13825 | 857 | Rust | AI/ML |
| `antirez/ds4` | 12976 | 1130 | C | Game |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6788 | 5144 | C++ | Other |
| `unicity-astrid/sdk-js` | 6638 | 15 | TypeScript | Other |
| `nexu-io/html-anything` | 6120 | 599 | HTML | AI/ML |
| `microsoft/SkillOpt` | 5006 | 497 | Python | AI/ML |
| `vercel-labs/zerolang` | 4874 | 315 | C | AI/ML |
| `V4bel/dirtyfrag` | 4817 | 773 | C | Other |
| `simplifaisoul/osiris` | 4448 | 912 | TypeScript | Data |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 13287.0 | 53148 | 4d | AI/ML |
| `b-nnett/goose` | 1025.0 | 2050 | 2d | Mobile |
| `cpaczek/skylight` | 656.0 | 1312 | 2d | Web |
| `zgwl/chinese-buy-us-stock-guide` | 617.2 | 3086 | 5d | Other |
| `BigPizzaV3/CodexPlusPlus` | 476.7 | 13825 | 29d | AI/ML |
| `antirez/ds4` | 447.4 | 12976 | 29d | Game |
| `tastyeffectco/sandboxes` | 409.0 | 409 | 1d | AI/ML |
| `unicity-astrid/sdk-js` | 390.5 | 6638 | 17d | Other |
| `asz798838958/aBaiAutoplus` | 376.5 | 1506 | 4d | AI/ML |
| `op7418/guizang-social-card-skill` | 365.4 | 2923 | 8d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 421 | 373 | 186 | 90 | 30.3 | 14.2 |
| AI/ML | 378 | 619 | 224 | 78 | 68.3 | 8.9 |
| Web | 52 | 359 | 194 | 72 | 36.3 | 4.6 |
| CLI/Tooling | 41 | 303 | 207 | 66 | 32.2 | 4.9 |
| Mobile | 35 | 356 | 223 | 41 | 48.8 | 6.3 |
| Security | 19 | 344 | 182 | 49 | 37.5 | 3.2 |
| Game | 17 | 958 | 187 | 90 | 41.6 | 11.9 |
| Data | 14 | 619 | 294 | 199 | 33.4 | 29.7 |
| Finance/Trading | 13 | 173 | 157 | 1046 | 13.9 | 0.4 |
| DevOps | 10 | 238 | 144 | 19 | 16.5 | 6.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.466 |         0.226 |     -0.006 |
| forks       |   0.466 |   1     |         0.13  |     -0.013 |
| open_issues |   0.226 |   0.13  |         1     |      0.008 |
| age_days    |  -0.006 |  -0.013 |         0.008 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.561 |         0.314 |      0.071 |
| forks       |   0.561 |   1     |         0.293 |      0.113 |
| open_issues |   0.314 |   0.293 |         1     |      0.068 |
| age_days    |   0.071 |   0.113 |         0.068 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 49 |
| `llm` | 48 |
| `ai-agents` | 45 |
| `ai` | 40 |
| `typescript` | 38 |
| `codex` | 36 |
| `cli` | 32 |
| `open-source` | 27 |
| `mcp` | 26 |
| `python` | 26 |
| `rust` | 25 |
| `agent` | 24 |
| `macos` | 24 |
| `claude` | 23 |
| `ai-agent` | 21 |
| `developer-tools` | 20 |
| `skills` | 18 |
| `react` | 18 |
| `anthropic` | 16 |
| `local-first` | 15 |
