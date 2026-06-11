# Summary Statistics

_Sample size: 700 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 591.2 | 250.5 | 67654 |
| forks | 116.5 | 25.0 | 11460 |
| open_issues | 17.8 | 1.0 | 5493 |
| stars_per_day | 51.9 | 16.3 | 6765 |
| age_days | 18.0 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 67654 | 8462 | Python | AI/ML |
| `unicity-astrid/sdk-js` | 8255 | 36 | TypeScript | Other |
| `alibaba/open-code-review` | 6159 | 334 | Go | AI/ML |
| `anthropics/defending-code-reference-harness` | 5703 | 409 | Python | Security |
| `simplifaisoul/osiris` | 5226 | 1056 | TypeScript | Data |
| `vercel-labs/zerolang` | 4976 | 326 | C++ | AI/ML |
| `AprilNEA/OpenLogi` | 4644 | 86 | Rust | Other |
| `perplexityai/bumblebee` | 4388 | 395 | Go | Other |
| `zgwl/chinese-buy-us-stock-guide` | 4117 | 640 | Unknown | Other |
| `microsoft/coreutils` | 3890 | 64 | Rust | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 6765.4 | 67654 | 10d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 3026.0 | 3026 | 1d | Other |
| `shadcn/improve` | 1331.0 | 1331 | 1d | Other |
| `MSNightmare/RoguePlanet` | 1016.0 | 1016 | 1d | Security |
| `NoopApp/noop` | 477.7 | 1433 | 3d | Data |
| `zgwl/chinese-buy-us-stock-guide` | 374.3 | 4117 | 11d | Other |
| `unicity-astrid/sdk-js` | 358.9 | 8255 | 23d | Other |
| `diffusionstudio/lottie` | 352.2 | 2113 | 6d | AI/ML |
| `jmmy9609-design/gpt-pp` | 343.0 | 343 | 1d | Other |
| `apple/coreai-models` | 330.5 | 661 | 2d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 280 | 756 | 256 | 90 | 60.2 | 11.2 |
| Other | 278 | 495 | 242 | 57 | 49.3 | 26.5 |
| Web | 33 | 394 | 233 | 43 | 30.9 | 41.7 |
| CLI/Tooling | 30 | 390 | 250 | 53 | 26.0 | 5.9 |
| Mobile | 26 | 405 | 275 | 53 | 34.2 | 6.7 |
| Security | 15 | 744 | 293 | 106 | 105.7 | 6.1 |
| Data | 13 | 912 | 497 | 272 | 74.0 | 6.9 |
| Game | 11 | 283 | 205 | 36 | 22.4 | 2.6 |
| Finance/Trading | 8 | 235 | 230 | 3811 | 22.2 | 0.4 |
| DevOps | 6 | 213 | 169 | 19 | 12.7 | 0.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.459 |         0.2   |     -0.023 |
| forks       |   0.459 |   1     |         0.124 |     -0.007 |
| open_issues |   0.2   |   0.124 |         1     |      0.016 |
| age_days    |  -0.023 |  -0.007 |         0.016 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.575 |         0.343 |      0.049 |
| forks       |   0.575 |   1     |         0.295 |      0.097 |
| open_issues |   0.343 |   0.295 |         1     |      0.004 |
| age_days    |   0.049 |   0.097 |         0.004 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 38 |
| `llm` | 34 |
| `ai` | 33 |
| `codex` | 31 |
| `ai-agents` | 30 |
| `typescript` | 24 |
| `open-source` | 21 |
| `macos` | 21 |
| `agent` | 18 |
| `cli` | 18 |
| `rust` | 17 |
| `mcp` | 16 |
| `developer-tools` | 16 |
| `react` | 15 |
| `claude` | 15 |
| `skills` | 15 |
| `ai-agent` | 14 |
| `windows` | 12 |
| `cursor` | 12 |
| `python` | 12 |
