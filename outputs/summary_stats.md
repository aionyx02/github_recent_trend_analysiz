# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 450.3 | 187.0 | 68790 |
| forks | 93.1 | 18.0 | 11460 |
| open_issues | 13.5 | 1.0 | 5639 |
| stars_per_day | 42.4 | 12.2 | 6254 |
| age_days | 17.8 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 68790 | 8642 | Python | AI/ML |
| `unicity-astrid/sdk-js` | 8254 | 36 | TypeScript | Other |
| `alibaba/open-code-review` | 6373 | 357 | Go | AI/ML |
| `anthropics/defending-code-reference-harness` | 5759 | 413 | Python | Security |
| `XiaomiMiMo/MiMo-Code` | 5645 | 448 | TypeScript | Other |
| `vercel-labs/zerolang` | 4999 | 331 | C++ | AI/ML |
| `AprilNEA/OpenLogi` | 4702 | 87 | Rust | Other |
| `perplexityai/bumblebee` | 4403 | 397 | Go | Other |
| `zgwl/chinese-buy-us-stock-guide` | 4210 | 651 | Unknown | Other |
| `microsoft/coreutils` | 3962 | 64 | Rust | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 6253.6 | 68790 | 11d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 5645.0 | 5645 | 1d | Other |
| `shadcn/improve` | 2084.0 | 2084 | 1d | Other |
| `MSNightmare/RoguePlanet` | 582.0 | 1164 | 2d | Security |
| `DietrichGebert/ponytail` | 385.0 | 385 | 1d | AI/ML |
| `NoopApp/noop` | 374.8 | 1499 | 4d | Data |
| `zgwl/chinese-buy-us-stock-guide` | 350.8 | 4210 | 12d | Other |
| `unicity-astrid/sdk-js` | 343.9 | 8254 | 24d | Other |
| `MSNightmare/GreatXML` | 338.0 | 338 | 1d | Security |
| `diffusionstudio/lottie` | 332.7 | 2329 | 7d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 412 | 380 | 180 | 56 | 44.1 | 19.6 |
| AI/ML | 386 | 590 | 200 | 75 | 46.7 | 8.5 |
| Web | 54 | 293 | 164 | 32 | 23.6 | 26.7 |
| CLI/Tooling | 42 | 309 | 194 | 66 | 26.4 | 4.5 |
| Mobile | 32 | 337 | 218 | 45 | 26.9 | 6.7 |
| Security | 20 | 575 | 213 | 85 | 75.6 | 3.9 |
| Game | 18 | 215 | 182 | 24 | 18.2 | 2.6 |
| Data | 14 | 506 | 396 | 181 | 48.5 | 7.4 |
| Finance/Trading | 11 | 213 | 227 | 2776 | 29.2 | 0.8 |
| DevOps | 11 | 171 | 156 | 14 | 10.2 | 1.9 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.448 |         0.202 |     -0.01  |
| forks       |   0.448 |   1     |         0.123 |      0.01  |
| open_issues |   0.202 |   0.123 |         1     |      0.021 |
| age_days    |  -0.01  |   0.01  |         0.021 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.607 |         0.338 |      0.074 |
| forks       |   0.607 |   1     |         0.292 |      0.099 |
| open_issues |   0.338 |   0.292 |         1     |      0.056 |
| age_days    |   0.074 |   0.099 |         0.056 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 54 |
| `llm` | 50 |
| `ai` | 43 |
| `ai-agents` | 42 |
| `codex` | 39 |
| `typescript` | 34 |
| `open-source` | 31 |
| `cli` | 25 |
| `macos` | 25 |
| `python` | 24 |
| `developer-tools` | 23 |
| `skills` | 22 |
| `mcp` | 21 |
| `agent` | 19 |
| `rust` | 19 |
| `react` | 19 |
| `claude` | 19 |
| `ai-agent` | 18 |
| `agent-skills` | 15 |
| `windows` | 15 |
