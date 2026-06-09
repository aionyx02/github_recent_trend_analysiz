# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 459.8 | 193.5 | 64503 |
| forks | 100.4 | 18.0 | 11460 |
| open_issues | 12.8 | 1.0 | 5069 |
| stars_per_day | 38.3 | 13.2 | 8063 |
| age_days | 17.6 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 64503 | 7900 | Python | AI/ML |
| `unicity-astrid/sdk-js` | 8207 | 36 | TypeScript | Other |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6834 | 5159 | C++ | Other |
| `nexu-io/html-anything` | 6460 | 631 | HTML | AI/ML |
| `alibaba/open-code-review` | 5618 | 280 | Go | AI/ML |
| `anthropics/defending-code-reference-harness` | 5448 | 375 | Python | Security |
| `simplifaisoul/osiris` | 5080 | 1029 | TypeScript | Data |
| `vercel-labs/zerolang` | 4938 | 323 | C++ | AI/ML |
| `AprilNEA/OpenLogi` | 4434 | 84 | Rust | Other |
| `perplexityai/bumblebee` | 4356 | 392 | Go | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 8062.9 | 64503 | 8d | AI/ML |
| `JimLiu/baoyu-design` | 576.0 | 576 | 1d | AI/ML |
| `NoopApp/noop` | 572.0 | 572 | 1d | Data |
| `GordenSun/GordenSuperPPTSkills` | 509.0 | 509 | 1d | AI/ML |
| `zgwl/chinese-buy-us-stock-guide` | 426.0 | 3834 | 9d | Other |
| `vorpus/performativeUI` | 407.0 | 407 | 1d | Other |
| `cpaczek/skylight` | 403.0 | 2418 | 6d | Web |
| `unicity-astrid/sdk-js` | 390.8 | 8207 | 21d | Other |
| `b-nnett/goose` | 388.2 | 2329 | 6d | Mobile |
| `anthropics/defending-code-reference-harness` | 320.5 | 5448 | 17d | Security |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 420 | 374 | 178 | 57 | 27.6 | 17.2 |
| AI/ML | 374 | 614 | 210 | 81 | 55.0 | 8.6 |
| Web | 50 | 353 | 190 | 81 | 27.7 | 28.5 |
| CLI/Tooling | 41 | 320 | 214 | 69 | 26.3 | 4.0 |
| Mobile | 35 | 355 | 217 | 45 | 29.1 | 6.5 |
| Security | 22 | 495 | 155 | 55 | 31.8 | 4.0 |
| Game | 16 | 214 | 179 | 26 | 20.3 | 2.1 |
| Data | 16 | 687 | 322 | 229 | 70.0 | 24.1 |
| Finance/Trading | 14 | 176 | 174 | 2316 | 25.1 | 0.4 |
| DevOps | 12 | 162 | 148 | 14 | 11.5 | 1.9 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.439 |         0.193 |     -0.007 |
| forks       |   0.439 |   1     |         0.112 |      0.012 |
| open_issues |   0.193 |   0.112 |         1     |      0.013 |
| age_days    |  -0.007 |   0.012 |         0.013 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.57  |         0.307 |      0.096 |
| forks       |   0.57  |   1     |         0.288 |      0.123 |
| open_issues |   0.307 |   0.288 |         1     |      0.092 |
| age_days    |   0.096 |   0.123 |         0.092 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 49 |
| `llm` | 46 |
| `ai-agents` | 42 |
| `ai` | 41 |
| `codex` | 37 |
| `typescript` | 36 |
| `open-source` | 32 |
| `cli` | 28 |
| `developer-tools` | 27 |
| `macos` | 26 |
| `python` | 24 |
| `agent` | 23 |
| `rust` | 22 |
| `mcp` | 22 |
| `claude` | 21 |
| `ai-agent` | 21 |
| `skills` | 20 |
| `react` | 19 |
| `agent-skills` | 15 |
| `windows` | 15 |
