# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 453.6 | 199.0 | 62611 |
| forks | 106.6 | 18.0 | 11459 |
| open_issues | 12.2 | 1.0 | 4871 |
| stars_per_day | 38.8 | 13.1 | 8944 |
| age_days | 17.6 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 62611 | 7617 | Python | AI/ML |
| `unicity-astrid/sdk-js` | 8059 | 34 | TypeScript | Other |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6825 | 5157 | C++ | Other |
| `nexu-io/html-anything` | 6340 | 621 | HTML | AI/ML |
| `anthropics/defending-code-reference-harness` | 5244 | 346 | Python | Security |
| `alibaba/open-code-review` | 5101 | 253 | Go | AI/ML |
| `vercel-labs/zerolang` | 4916 | 320 | C | AI/ML |
| `simplifaisoul/osiris` | 4807 | 989 | TypeScript | Data |
| `AprilNEA/OpenLogi` | 4355 | 83 | Rust | Other |
| `perplexityai/bumblebee` | 4337 | 387 | Go | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 8944.4 | 62611 | 7d | AI/ML |
| `cpaczek/skylight` | 464.6 | 2323 | 5d | Web |
| `b-nnett/goose` | 458.6 | 2293 | 5d | Mobile |
| `JimLiu/baoyu-design` | 442.0 | 442 | 1d | AI/ML |
| `zgwl/chinese-buy-us-stock-guide` | 439.0 | 3512 | 8d | Other |
| `NoopApp/noop` | 408.0 | 408 | 1d | Data |
| `unicity-astrid/sdk-js` | 402.9 | 8059 | 20d | Other |
| `amElnagdy/guard-skills` | 402.0 | 402 | 1d | AI/ML |
| `anthropics/defending-code-reference-harness` | 327.8 | 5244 | 16d | Security |
| `helloianneo/ian-xiaohei-illustrations` | 315.2 | 3467 | 11d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 414 | 376 | 182 | 64 | 28.0 | 16.8 |
| AI/ML | 374 | 602 | 216 | 80 | 55.5 | 8.1 |
| Web | 48 | 354 | 201 | 84 | 30.7 | 27.3 |
| CLI/Tooling | 41 | 309 | 199 | 68 | 27.1 | 3.9 |
| Mobile | 35 | 348 | 216 | 44 | 32.0 | 6.2 |
| Security | 23 | 468 | 160 | 51 | 30.8 | 3.7 |
| Finance/Trading | 20 | 179 | 161 | 1826 | 25.9 | 0.5 |
| Game | 17 | 198 | 152 | 24 | 21.3 | 1.9 |
| Data | 16 | 655 | 320 | 217 | 62.6 | 21.8 |
| DevOps | 12 | 226 | 148 | 17 | 13.3 | 7.9 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.417 |         0.19  |     -0.017 |
| forks       |   0.417 |   1     |         0.104 |     -0.007 |
| open_issues |   0.19  |   0.104 |         1     |      0.006 |
| age_days    |  -0.017 |  -0.007 |         0.006 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.556 |         0.32  |      0.087 |
| forks       |   0.556 |   1     |         0.289 |      0.117 |
| open_issues |   0.32  |   0.289 |         1     |      0.082 |
| age_days    |   0.087 |   0.117 |         0.082 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 50 |
| `llm` | 46 |
| `ai-agents` | 43 |
| `typescript` | 42 |
| `ai` | 40 |
| `codex` | 36 |
| `open-source` | 33 |
| `cli` | 30 |
| `developer-tools` | 27 |
| `macos` | 26 |
| `rust` | 24 |
| `mcp` | 24 |
| `python` | 24 |
| `ai-agent` | 23 |
| `claude` | 22 |
| `agent` | 22 |
| `react` | 18 |
| `anthropic` | 17 |
| `skills` | 17 |
| `agent-skills` | 15 |
