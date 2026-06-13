# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 451.0 | 185.0 | 69608 |
| forks | 97.3 | 17.0 | 11460 |
| open_issues | 13.4 | 1.0 | 5733 |
| stars_per_day | 40.6 | 12.7 | 5801 |
| age_days | 17.7 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 69608 | 8807 | Python | AI/ML |
| `unicity-astrid/sdk-js` | 8255 | 36 | TypeScript | Other |
| `XiaomiMiMo/MiMo-Code` | 7464 | 590 | TypeScript | Other |
| `alibaba/open-code-review` | 6510 | 369 | Go | AI/ML |
| `anthropics/defending-code-reference-harness` | 5794 | 418 | Python | Security |
| `vercel-labs/zerolang` | 5017 | 332 | C++ | AI/ML |
| `AprilNEA/OpenLogi` | 4743 | 91 | Rust | Other |
| `perplexityai/bumblebee` | 4418 | 400 | Go | Other |
| `zgwl/chinese-buy-us-stock-guide` | 4265 | 658 | Unknown | Other |
| `helloianneo/ian-xiaohei-illustrations` | 4125 | 411 | Unknown | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 5800.7 | 69608 | 12d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 3732.0 | 7464 | 2d | Other |
| `shadcn/improve` | 1267.0 | 2534 | 2d | Other |
| `DietrichGebert/ponytail` | 1062.0 | 1062 | 1d | AI/ML |
| `MSNightmare/GreatXML` | 437.0 | 437 | 1d | Security |
| `SkyBlue997/enableMacosAI` | 412.0 | 824 | 2d | CLI/Tooling |
| `MSNightmare/RoguePlanet` | 409.0 | 1227 | 3d | Security |
| `joeseesun/qiaomu-goal-meta-skill` | 371.0 | 371 | 1d | AI/ML |
| `unicity-astrid/sdk-js` | 330.2 | 8255 | 25d | Other |
| `zgwl/chinese-buy-us-stock-guide` | 328.1 | 4265 | 13d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 416 | 378 | 177 | 70 | 36.7 | 19.0 |
| AI/ML | 380 | 596 | 200 | 69 | 49.3 | 8.7 |
| Web | 55 | 302 | 180 | 33 | 24.9 | 27.0 |
| CLI/Tooling | 42 | 307 | 206 | 82 | 38.6 | 4.7 |
| Mobile | 35 | 320 | 203 | 42 | 28.7 | 6.4 |
| Security | 19 | 608 | 202 | 92 | 73.7 | 4.4 |
| Game | 18 | 215 | 172 | 22 | 16.8 | 2.9 |
| Data | 13 | 521 | 314 | 194 | 45.1 | 6.2 |
| Finance/Trading | 11 | 218 | 228 | 2776 | 21.0 | 0.7 |
| DevOps | 11 | 173 | 157 | 14 | 9.7 | 2.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.451 |         0.212 |     -0.005 |
| forks       |   0.451 |   1     |         0.128 |      0.017 |
| open_issues |   0.212 |   0.128 |         1     |      0.025 |
| age_days    |  -0.005 |   0.017 |         0.025 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.609 |         0.341 |      0.05  |
| forks       |   0.609 |   1     |         0.297 |      0.093 |
| open_issues |   0.341 |   0.297 |         1     |      0.087 |
| age_days    |   0.05  |   0.093 |         0.087 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 55 |
| `llm` | 49 |
| `ai` | 43 |
| `codex` | 42 |
| `ai-agents` | 40 |
| `typescript` | 30 |
| `open-source` | 28 |
| `cli` | 27 |
| `macos` | 26 |
| `python` | 25 |
| `agent` | 22 |
| `skills` | 22 |
| `developer-tools` | 20 |
| `claude` | 19 |
| `ai-agent` | 18 |
| `react` | 18 |
| `mcp` | 18 |
| `rust` | 16 |
| `agent-skills` | 15 |
| `windows` | 15 |
