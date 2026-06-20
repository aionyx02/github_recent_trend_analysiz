# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 484.2 | 194.0 | 74579 |
| forks | 93.2 | 17.0 | 11461 |
| open_issues | 8.2 | 1.0 | 1642 |
| stars_per_day | 39.3 | 13.1 | 5826 |
| age_days | 17.3 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 74579 | 9626 | Python | AI/ML |
| `DietrichGebert/ponytail` | 40784 | 1956 | JavaScript | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 9997 | 921 | TypeScript | AI/ML |
| `anthropics/defending-code-reference-harness` | 6104 | 462 | Python | Security |
| `shadcn/improve` | 5696 | 221 | Unknown | Other |
| `helloianneo/ian-xiaohei-illustrations` | 5374 | 624 | Unknown | AI/ML |
| `AprilNEA/OpenLogi` | 5170 | 98 | Rust | Other |
| `EpicGames/lore` | 4817 | 179 | Rust | Other |
| `zgwl/chinese-buy-us-stock-guide` | 4745 | 729 | Unknown | Other |
| `open-gsd/gsd-core` | 4563 | 278 | JavaScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 5826.3 | 40784 | 7d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 3925.2 | 74579 | 19d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 1110.8 | 9997 | 9d | AI/ML |
| `shadcn/improve` | 632.9 | 5696 | 9d | Other |
| `vercel/eve` | 573.3 | 1720 | 3d | AI/ML |
| `omnigent-ai/omnigent` | 513.6 | 4109 | 8d | AI/ML |
| `tamnd/kage` | 424.0 | 2120 | 5d | Other |
| `MstKail/polymarket-trading-bot-services-polyedge365` | 331.0 | 331 | 1d | Finance/Trading |
| `Forsy-AI/agent-apprenticeship` | 329.0 | 329 | 1d | AI/ML |
| `Waishnav/devspace` | 303.2 | 1516 | 5d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 404 | 700 | 202 | 68 | 57.1 | 9.9 |
| Other | 387 | 341 | 194 | 51 | 24.9 | 4.5 |
| Web | 55 | 333 | 179 | 38 | 24.6 | 32.3 |
| Mobile | 41 | 302 | 147 | 34 | 24.6 | 6.0 |
| CLI/Tooling | 34 | 303 | 182 | 22 | 28.5 | 6.1 |
| Finance/Trading | 19 | 218 | 224 | 2023 | 57.1 | 0.4 |
| DevOps | 17 | 179 | 144 | 20 | 25.4 | 4.1 |
| Security | 17 | 773 | 230 | 106 | 51.3 | 6.4 |
| Game | 13 | 215 | 177 | 12 | 20.9 | 3.2 |
| Data | 13 | 410 | 187 | 89 | 48.7 | 3.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.483 |         0.567 |      0     |
| forks       |   0.483 |   1     |         0.322 |      0.069 |
| open_issues |   0.567 |   0.322 |         1     |      0.008 |
| age_days    |   0     |   0.069 |         0.008 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.532 |         0.28  |      0.044 |
| forks       |   0.532 |   1     |         0.339 |      0.1   |
| open_issues |   0.28  |   0.339 |         1     |      0.174 |
| age_days    |   0.044 |   0.1   |         0.174 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 61 |
| `ai-agents` | 51 |
| `llm` | 50 |
| `ai` | 44 |
| `codex` | 44 |
| `ai-agent` | 32 |
| `typescript` | 31 |
| `macos` | 30 |
| `python` | 28 |
| `mcp` | 25 |
| `cli` | 24 |
| `open-source` | 24 |
| `claude` | 22 |
| `developer-tools` | 22 |
| `skills` | 22 |
| `agent-skills` | 21 |
| `prompt-engineering` | 20 |
| `swift` | 20 |
| `agent` | 18 |
| `rust` | 15 |
