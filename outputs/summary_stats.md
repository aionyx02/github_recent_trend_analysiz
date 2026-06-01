# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 419.1 | 224.0 | 12649 |
| forks | 188.9 | 19.5 | 6864 |
| open_issues | 7.5 | 1.0 | 2662 |
| stars_per_day | 46.8 | 16.4 | 11586 |
| age_days | 16.8 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `antirez/ds4` | 12649 | 1095 | C | Game |
| `pewdiepie-archdaemon/odysseus` | 11586 | 1518 | JavaScript | AI/ML |
| `BigPizzaV3/CodexPlusPlus` | 10069 | 664 | Rust | AI/ML |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6701 | 5117 | C++ | Other |
| `nexu-io/html-anything` | 5659 | 552 | HTML | AI/ML |
| `V4bel/dirtyfrag` | 4794 | 772 | C | Other |
| `vercel-labs/zerolang` | 4769 | 306 | C | AI/ML |
| `perplexityai/bumblebee` | 4069 | 353 | Go | Other |
| `vercel-labs/zero-native` | 4062 | 164 | Zig | Web |
| `simplifaisoul/osiris` | 3969 | 787 | TypeScript | Data |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 11586.0 | 11586 | 1d | AI/ML |
| `op7418/guizang-social-card-skill` | 563.8 | 2255 | 4d | AI/ML |
| `antirez/ds4` | 506.0 | 12649 | 25d | Game |
| `BigPizzaV3/CodexPlusPlus` | 402.8 | 10069 | 25d | AI/ML |
| `helloianneo/ian-xiaohei-illustrations` | 384.8 | 1539 | 4d | AI/ML |
| `perplexityai/bumblebee` | 369.9 | 4069 | 11d | Other |
| `FULU-Foundation/OrcaSlicer-bambulab` | 335.1 | 6701 | 20d | Other |
| `liyue-aigc/female-portrait-director` | 333.0 | 333 | 1d | AI/ML |
| `Sophomoresty/gemini-web2api` | 324.3 | 973 | 3d | AI/ML |
| `GordenSun/GordenPPTSkill` | 306.0 | 1224 | 4d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 408 | 353 | 210 | 146 | 32.2 | 10.6 |
| AI/ML | 369 | 512 | 246 | 123 | 69.1 | 6.0 |
| Web | 46 | 337 | 186 | 73 | 31.1 | 3.9 |
| Finance/Trading | 37 | 289 | 266 | 1937 | 39.7 | 0.8 |
| CLI/Tooling | 36 | 360 | 198 | 73 | 35.7 | 4.4 |
| Mobile | 34 | 321 | 253 | 26 | 23.9 | 3.7 |
| Game | 26 | 766 | 298 | 58 | 57.2 | 8.3 |
| Security | 21 | 259 | 184 | 74 | 31.3 | 1.6 |
| DevOps | 12 | 332 | 175 | 89 | 37.6 | 7.8 |
| Data | 11 | 608 | 219 | 89 | 53.0 | 8.4 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.127 |         0.103 |      0.055 |
| forks       |   0.127 |   1     |         0.016 |     -0.096 |
| open_issues |   0.103 |   0.016 |         1     |      0.001 |
| age_days    |   0.055 |  -0.096 |         0.001 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.445 |         0.306 |      0.063 |
| forks       |   0.445 |   1     |         0.227 |      0.14  |
| open_issues |   0.306 |   0.227 |         1     |      0.117 |
| age_days    |   0.063 |   0.14  |         0.117 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 52 |
| `claude-code` | 52 |
| `typescript` | 50 |
| `ai` | 35 |
| `llm` | 35 |
| `python` | 31 |
| `codex` | 31 |
| `open-source` | 31 |
| `cli` | 29 |
| `mcp` | 28 |
| `claude` | 26 |
| `rust` | 23 |
| `agent` | 22 |
| `trading-bot` | 22 |
| `ai-agent` | 19 |
| `anthropic` | 19 |
| `skills` | 19 |
| `macos` | 19 |
| `developer-tools` | 18 |
| `openai` | 18 |
