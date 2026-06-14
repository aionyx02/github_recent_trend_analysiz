# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 452.4 | 183.0 | 70412 |
| forks | 104.0 | 18.0 | 11460 |
| open_issues | 13.6 | 1.0 | 5810 |
| stars_per_day | 41.1 | 12.6 | 5416 |
| age_days | 17.5 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 70412 | 8938 | Python | AI/ML |
| `unicity-astrid/sdk-js` | 8257 | 36 | TypeScript | Other |
| `XiaomiMiMo/MiMo-Code` | 8106 | 679 | TypeScript | Other |
| `alibaba/open-code-review` | 6749 | 378 | Go | AI/ML |
| `anthropics/defending-code-reference-harness` | 5827 | 423 | Python | Security |
| `vercel-labs/zerolang` | 5037 | 334 | C++ | AI/ML |
| `AprilNEA/OpenLogi` | 4817 | 92 | Rust | Other |
| `perplexityai/bumblebee` | 4436 | 403 | Go | Other |
| `helloianneo/ian-xiaohei-illustrations` | 4347 | 461 | Unknown | AI/ML |
| `zgwl/chinese-buy-us-stock-guide` | 4317 | 663 | Unknown | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 5416.3 | 70412 | 13d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 2702.0 | 8106 | 3d | Other |
| `DietrichGebert/ponytail` | 2429.0 | 2429 | 1d | AI/ML |
| `shadcn/improve` | 1256.7 | 3770 | 3d | Other |
| `lenucksi/aur-malware-check` | 678.0 | 678 | 1d | CLI/Tooling |
| `orange2ai/renwei-writing` | 488.0 | 488 | 1d | AI/ML |
| `omnigent-ai/omnigent` | 374.5 | 749 | 2d | AI/ML |
| `SkyBlue997/enableMacosAI` | 364.0 | 1092 | 3d | CLI/Tooling |
| `DanMcInerney/architect-loop` | 338.0 | 338 | 1d | AI/ML |
| `unicity-astrid/sdk-js` | 317.6 | 8257 | 26d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 409 | 379 | 178 | 88 | 33.0 | 19.8 |
| AI/ML | 393 | 587 | 187 | 62 | 53.5 | 8.6 |
| Web | 58 | 310 | 182 | 33 | 26.3 | 26.9 |
| CLI/Tooling | 40 | 338 | 218 | 108 | 46.0 | 5.1 |
| Mobile | 32 | 313 | 194 | 40 | 29.3 | 5.2 |
| Security | 17 | 655 | 202 | 102 | 61.9 | 5.3 |
| Game | 16 | 205 | 162 | 23 | 16.2 | 3.2 |
| Data | 12 | 537 | 306 | 210 | 43.0 | 5.9 |
| Finance/Trading | 12 | 210 | 226 | 2631 | 16.7 | 0.8 |
| DevOps | 11 | 171 | 157 | 14 | 18.3 | 1.9 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.44  |         0.218 |      -0    |
| forks       |   0.44  |   1     |         0.127 |       0.03 |
| open_issues |   0.218 |   0.127 |         1     |       0.03 |
| age_days    |  -0     |   0.03  |         0.03  |       1    |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.611 |         0.348 |      0.051 |
| forks       |   0.611 |   1     |         0.311 |      0.111 |
| open_issues |   0.348 |   0.311 |         1     |      0.098 |
| age_days    |   0.051 |   0.111 |         0.098 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 60 |
| `llm` | 55 |
| `ai` | 46 |
| `ai-agents` | 44 |
| `codex` | 42 |
| `typescript` | 31 |
| `cli` | 28 |
| `macos` | 26 |
| `python` | 26 |
| `open-source` | 23 |
| `ai-agent` | 22 |
| `claude` | 22 |
| `skills` | 22 |
| `developer-tools` | 21 |
| `mcp` | 21 |
| `agent` | 20 |
| `rust` | 17 |
| `prompt-engineering` | 17 |
| `anthropic` | 16 |
| `react` | 16 |
