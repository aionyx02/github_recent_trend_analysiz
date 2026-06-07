# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 452.5 | 197.0 | 59927 |
| forks | 106.0 | 19.0 | 11339 |
| open_issues | 11.7 | 1.0 | 4499 |
| stars_per_day | 39.0 | 13.3 | 9988 |
| age_days | 17.6 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 59927 | 7230 | Python | AI/ML |
| `unicity-astrid/sdk-js` | 7735 | 21 | TypeScript | Other |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6812 | 5150 | C++ | Other |
| `nexu-io/html-anything` | 6229 | 610 | HTML | AI/ML |
| `microsoft/SkillOpt` | 5252 | 530 | Python | AI/ML |
| `vercel-labs/zerolang` | 4909 | 318 | C | AI/ML |
| `anthropics/defending-code-reference-harness` | 4875 | 309 | Python | Security |
| `simplifaisoul/osiris` | 4568 | 944 | TypeScript | Data |
| `perplexityai/bumblebee` | 4315 | 382 | Go | Other |
| `AprilNEA/OpenLogi` | 4198 | 78 | Rust | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 9987.8 | 59927 | 6d | AI/ML |
| `b-nnett/goose` | 545.5 | 2182 | 4d | Mobile |
| `cpaczek/skylight` | 535.5 | 2142 | 4d | Web |
| `zgwl/chinese-buy-us-stock-guide` | 485.1 | 3396 | 7d | Other |
| `unicity-astrid/sdk-js` | 407.1 | 7735 | 19d | Other |
| `anthropics/defending-code-reference-harness` | 325.0 | 4875 | 15d | Security |
| `AprilNEA/OpenLogi` | 322.9 | 4198 | 13d | Other |
| `helloianneo/ian-xiaohei-illustrations` | 320.6 | 3206 | 10d | AI/ML |
| `op7418/guizang-social-card-skill` | 303.5 | 3035 | 10d | AI/ML |
| `Gloridust/WechatOnCloud` | 269.4 | 2155 | 8d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 416 | 372 | 186 | 117 | 27.9 | 15.8 |
| AI/ML | 381 | 590 | 209 | 77 | 56.0 | 7.8 |
| Web | 50 | 407 | 194 | 82 | 33.9 | 24.2 |
| CLI/Tooling | 39 | 326 | 223 | 71 | 29.5 | 4.9 |
| Mobile | 35 | 332 | 197 | 42 | 34.4 | 6.2 |
| Security | 21 | 478 | 199 | 53 | 34.3 | 4.1 |
| Finance/Trading | 17 | 167 | 151 | 858 | 17.9 | 0.5 |
| Data | 16 | 604 | 312 | 187 | 38.9 | 21.9 |
| Game | 14 | 213 | 176 | 28 | 14.9 | 2.2 |
| DevOps | 11 | 233 | 146 | 18 | 14.6 | 7.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.402 |         0.207 |     -0.02  |
| forks       |   0.402 |   1     |         0.107 |     -0.018 |
| open_issues |   0.207 |   0.107 |         1     |     -0.001 |
| age_days    |  -0.02  |  -0.018 |        -0.001 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.544 |         0.299 |      0.096 |
| forks       |   0.544 |   1     |         0.281 |      0.109 |
| open_issues |   0.299 |   0.281 |         1     |      0.045 |
| age_days    |   0.096 |   0.109 |         0.045 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 50 |
| `llm` | 45 |
| `ai-agents` | 44 |
| `typescript` | 41 |
| `ai` | 40 |
| `codex` | 36 |
| `open-source` | 33 |
| `cli` | 32 |
| `macos` | 26 |
| `developer-tools` | 26 |
| `rust` | 25 |
| `python` | 25 |
| `ai-agent` | 24 |
| `agent` | 23 |
| `mcp` | 23 |
| `claude` | 21 |
| `react` | 18 |
| `skills` | 18 |
| `anthropic` | 16 |
| `openai` | 15 |
