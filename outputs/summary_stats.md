# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 444.3 | 195.0 | 56617 |
| forks | 97.6 | 19.0 | 8899 |
| open_issues | 10.4 | 1.0 | 4292 |
| stars_per_day | 42.0 | 13.2 | 11323 |
| age_days | 17.4 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 56617 | 6767 | Python | AI/ML |
| `unicity-astrid/sdk-js` | 7172 | 17 | TypeScript | Other |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6799 | 5150 | C++ | Other |
| `nexu-io/html-anything` | 6178 | 604 | HTML | AI/ML |
| `microsoft/SkillOpt` | 5107 | 505 | Python | AI/ML |
| `vercel-labs/zerolang` | 4888 | 315 | C | AI/ML |
| `V4bel/dirtyfrag` | 4818 | 774 | C | Other |
| `simplifaisoul/osiris` | 4499 | 920 | TypeScript | Data |
| `perplexityai/bumblebee` | 4301 | 379 | Go | Other |
| `vercel-labs/zero-native` | 4110 | 171 | Zig | Web |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 11323.4 | 56617 | 5d | AI/ML |
| `b-nnett/goose` | 709.3 | 2128 | 3d | Mobile |
| `cpaczek/skylight` | 627.0 | 1881 | 3d | Web |
| `zgwl/chinese-buy-us-stock-guide` | 547.3 | 3284 | 6d | Other |
| `Jane-xiaoer/xiaoer-videolab` | 422.0 | 422 | 1d | Other |
| `unicity-astrid/sdk-js` | 398.4 | 7172 | 18d | Other |
| `AprilNEA/OpenLogi` | 338.6 | 4063 | 12d | Other |
| `op7418/guizang-social-card-skill` | 331.7 | 2985 | 9d | AI/ML |
| `asz798838958/aBaiAutoplus` | 308.2 | 1541 | 5d | AI/ML |
| `Gloridust/WechatOnCloud` | 303.7 | 2126 | 7d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 419 | 375 | 190 | 100 | 29.7 | 15.2 |
| AI/ML | 374 | 579 | 216 | 76 | 60.9 | 7.6 |
| Web | 51 | 390 | 200 | 76 | 37.5 | 4.9 |
| CLI/Tooling | 42 | 316 | 218 | 66 | 34.1 | 4.6 |
| Mobile | 35 | 325 | 195 | 41 | 37.7 | 6.2 |
| Security | 23 | 391 | 162 | 46 | 31.9 | 3.9 |
| Finance/Trading | 16 | 159 | 150 | 910 | 21.2 | 0.5 |
| Data | 15 | 602 | 293 | 194 | 44.5 | 24.8 |
| Game | 15 | 204 | 161 | 26 | 16.0 | 2.1 |
| DevOps | 10 | 242 | 146 | 19 | 15.5 | 7.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.44  |         0.203 |     -0.024 |
| forks       |   0.44  |   1     |         0.114 |     -0.014 |
| open_issues |   0.203 |   0.114 |         1     |      0.008 |
| age_days    |  -0.024 |  -0.014 |         0.008 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.536 |         0.321 |      0.094 |
| forks       |   0.536 |   1     |         0.292 |      0.105 |
| open_issues |   0.321 |   0.292 |         1     |      0.053 |
| age_days    |   0.094 |   0.105 |         0.053 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 51 |
| `llm` | 45 |
| `ai-agents` | 42 |
| `ai` | 40 |
| `typescript` | 39 |
| `codex` | 36 |
| `cli` | 30 |
| `open-source` | 26 |
| `rust` | 25 |
| `macos` | 25 |
| `python` | 25 |
| `agent` | 23 |
| `ai-agent` | 23 |
| `developer-tools` | 23 |
| `mcp` | 22 |
| `claude` | 21 |
| `skills` | 18 |
| `react` | 17 |
| `anthropic` | 16 |
| `openai` | 14 |
