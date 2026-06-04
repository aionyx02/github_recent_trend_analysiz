# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 460.7 | 201.5 | 47174 |
| forks | 92.9 | 19.0 | 6467 |
| open_issues | 9.4 | 1.0 | 3496 |
| stars_per_day | 50.2 | 13.8 | 15725 |
| age_days | 17.3 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 47174 | 5419 | JavaScript | AI/ML |
| `BigPizzaV3/CodexPlusPlus` | 12961 | 810 | Rust | AI/ML |
| `antirez/ds4` | 12904 | 1124 | C | Game |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6777 | 5139 | C++ | Other |
| `nexu-io/html-anything` | 6009 | 582 | HTML | AI/ML |
| `vercel-labs/zerolang` | 4849 | 312 | C | AI/ML |
| `V4bel/dirtyfrag` | 4815 | 774 | C | Other |
| `microsoft/SkillOpt` | 4809 | 478 | Python | AI/ML |
| `simplifaisoul/osiris` | 4346 | 883 | TypeScript | Data |
| `unicity-astrid/sdk-js` | 4288 | 6 | TypeScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 15724.7 | 47174 | 3d | AI/ML |
| `b-nnett/goose` | 1537.0 | 1537 | 1d | Mobile |
| `cpaczek/skylight` | 981.0 | 981 | 1d | Web |
| `SenhorH/tab-labeler` | 549.0 | 549 | 1d | Other |
| `zgwl/chinese-buy-us-stock-guide` | 510.8 | 2043 | 4d | Other |
| `asz798838958/aBaiAutoplus` | 482.0 | 1446 | 3d | AI/ML |
| `BigPizzaV3/CodexPlusPlus` | 462.9 | 12961 | 28d | AI/ML |
| `antirez/ds4` | 460.9 | 12904 | 28d | Game |
| `Gloridust/WechatOnCloud` | 403.4 | 2017 | 5d | Other |
| `op7418/guizang-social-card-skill` | 402.6 | 2818 | 7d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 427 | 367 | 188 | 91 | 31.6 | 12.4 |
| AI/ML | 368 | 612 | 224 | 83 | 77.9 | 8.4 |
| Web | 52 | 348 | 198 | 71 | 40.6 | 4.4 |
| CLI/Tooling | 42 | 319 | 215 | 66 | 36.1 | 4.8 |
| Mobile | 38 | 327 | 206 | 38 | 59.0 | 5.1 |
| Game | 19 | 888 | 187 | 84 | 40.3 | 11.2 |
| Security | 19 | 263 | 163 | 51 | 25.6 | 3.3 |
| Finance/Trading | 13 | 183 | 157 | 738 | 19.1 | 0.4 |
| DevOps | 12 | 263 | 142 | 81 | 17.2 | 5.1 |
| Data | 10 | 772 | 298 | 236 | 44.6 | 5.6 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.475 |         0.245 |     -0.001 |
| forks       |   0.475 |   1     |         0.139 |     -0.012 |
| open_issues |   0.245 |   0.139 |         1     |      0.001 |
| age_days    |  -0.001 |  -0.012 |         0.001 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.571 |         0.332 |      0.096 |
| forks       |   0.571 |   1     |         0.301 |      0.131 |
| open_issues |   0.332 |   0.301 |         1     |      0.074 |
| age_days    |   0.096 |   0.131 |         0.074 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 51 |
| `ai-agents` | 48 |
| `llm` | 39 |
| `codex` | 38 |
| `ai` | 37 |
| `typescript` | 35 |
| `cli` | 31 |
| `open-source` | 27 |
| `rust` | 26 |
| `mcp` | 25 |
| `claude` | 24 |
| `agent` | 24 |
| `python` | 23 |
| `anthropic` | 22 |
| `macos` | 21 |
| `ai-agent` | 19 |
| `skills` | 18 |
| `react` | 17 |
| `developer-tools` | 17 |
| `terminal` | 15 |
