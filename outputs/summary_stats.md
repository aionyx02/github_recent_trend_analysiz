# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 439.7 | 202.0 | 37854 |
| forks | 108.7 | 19.0 | 9209 |
| open_issues | 8.6 | 1.0 | 3123 |
| stars_per_day | 53.5 | 14.6 | 18927 |
| age_days | 17.0 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 37854 | 4439 | JavaScript | AI/ML |
| `antirez/ds4` | 12833 | 1122 | C | Game |
| `BigPizzaV3/CodexPlusPlus` | 12023 | 751 | Rust | AI/ML |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6755 | 5137 | C++ | Other |
| `nexu-io/html-anything` | 5932 | 576 | HTML | AI/ML |
| `vercel-labs/zerolang` | 4817 | 311 | C | AI/ML |
| `V4bel/dirtyfrag` | 4811 | 775 | C | Other |
| `microsoft/SkillOpt` | 4598 | 453 | Python | AI/ML |
| `simplifaisoul/osiris` | 4277 | 862 | TypeScript | Data |
| `perplexityai/bumblebee` | 4197 | 372 | Go | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 18927.0 | 37854 | 2d | AI/ML |
| `b-nnett/goose` | 1156.0 | 1156 | 1d | Mobile |
| `asz798838958/aBaiAutoplus` | 629.0 | 1258 | 2d | AI/ML |
| `qiuqiubuchongle-cloud/chokepoint-atlas` | 478.0 | 478 | 1d | Other |
| `antirez/ds4` | 475.3 | 12833 | 27d | Game |
| `Gloridust/WechatOnCloud` | 451.0 | 1804 | 4d | Other |
| `op7418/guizang-social-card-skill` | 447.2 | 2683 | 6d | AI/ML |
| `BigPizzaV3/CodexPlusPlus` | 445.3 | 12023 | 27d | AI/ML |
| `AprilNEA/OpenLogi` | 385.6 | 3470 | 9d | Other |
| `ClaudioDrews/memory-os` | 348.5 | 697 | 2d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 426 | 345 | 188 | 132 | 32.6 | 11.4 |
| AI/ML | 368 | 582 | 226 | 77 | 88.0 | 7.3 |
| Web | 53 | 324 | 194 | 68 | 28.7 | 4.4 |
| CLI/Tooling | 40 | 314 | 201 | 67 | 36.6 | 4.6 |
| Mobile | 40 | 309 | 196 | 35 | 49.5 | 4.9 |
| Security | 19 | 261 | 163 | 45 | 22.6 | 2.1 |
| Game | 18 | 929 | 191 | 86 | 46.3 | 11.1 |
| Finance/Trading | 13 | 266 | 222 | 718 | 20.8 | 0.6 |
| DevOps | 12 | 341 | 170 | 93 | 20.7 | 8.5 |
| Data | 11 | 673 | 233 | 320 | 44.0 | 8.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.296 |         0.184 |      0.008 |
| forks       |   0.296 |   1     |         0.067 |     -0.03  |
| open_issues |   0.184 |   0.067 |         1     |      0.002 |
| age_days    |   0.008 |  -0.03  |         0.002 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.575 |         0.326 |      0.109 |
| forks       |   0.575 |   1     |         0.27  |      0.142 |
| open_issues |   0.326 |   0.27  |         1     |      0.072 |
| age_days    |   0.109 |   0.142 |         0.072 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 55 |
| `ai-agents` | 54 |
| `codex` | 39 |
| `llm` | 39 |
| `ai` | 38 |
| `typescript` | 37 |
| `cli` | 30 |
| `mcp` | 29 |
| `python` | 27 |
| `rust` | 26 |
| `agent` | 26 |
| `open-source` | 25 |
| `claude` | 23 |
| `macos` | 21 |
| `ai-agent` | 19 |
| `developer-tools` | 19 |
| `anthropic` | 18 |
| `skills` | 18 |
| `react` | 18 |
| `windows` | 16 |
