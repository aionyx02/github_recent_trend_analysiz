# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 472.5 | 179.0 | 75309 |
| forks | 95.0 | 17.0 | 11460 |
| open_issues | 8.2 | 1.0 | 1645 |
| stars_per_day | 37.4 | 11.9 | 5552 |
| age_days | 17.6 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 75309 | 9771 | Python | AI/ML |
| `DietrichGebert/ponytail` | 44412 | 2169 | JavaScript | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 10131 | 938 | TypeScript | AI/ML |
| `anthropics/defending-code-reference-harness` | 6121 | 468 | Python | Security |
| `shadcn/improve` | 5818 | 229 | Unknown | Other |
| `helloianneo/ian-xiaohei-illustrations` | 5487 | 646 | Unknown | AI/ML |
| `AprilNEA/OpenLogi` | 5193 | 98 | Rust | Other |
| `zgwl/chinese-buy-us-stock-guide` | 4774 | 735 | Unknown | Other |
| `open-gsd/gsd-core` | 4637 | 283 | JavaScript | AI/ML |
| `omnigent-ai/omnigent` | 4242 | 476 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 5551.5 | 44412 | 8d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 3765.4 | 75309 | 20d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 1013.1 | 10131 | 10d | AI/ML |
| `shadcn/improve` | 581.8 | 5818 | 10d | Other |
| `Forsy-AI/agent-apprenticeship` | 560.0 | 560 | 1d | AI/ML |
| `vercel/eve` | 479.5 | 1918 | 4d | AI/ML |
| `omnigent-ai/omnigent` | 471.3 | 4242 | 9d | AI/ML |
| `tamnd/kage` | 365.7 | 2194 | 6d | Other |
| `zhongerxin/cowart` | 328.5 | 657 | 2d | Other |
| `MstKail/wc2026-crypto-sportsbook` | 328.0 | 328 | 1d | Finance/Trading |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 402 | 703 | 192 | 71 | 54.8 | 9.8 |
| Other | 369 | 315 | 172 | 53 | 23.4 | 4.4 |
| Web | 57 | 330 | 179 | 38 | 26.1 | 31.2 |
| Mobile | 46 | 292 | 144 | 31 | 21.9 | 6.0 |
| CLI/Tooling | 36 | 298 | 179 | 21 | 29.0 | 5.9 |
| Finance/Trading | 22 | 231 | 226 | 1760 | 44.1 | 0.4 |
| DevOps | 18 | 191 | 154 | 20 | 23.7 | 4.1 |
| Security | 18 | 752 | 214 | 102 | 46.0 | 8.6 |
| Data | 17 | 352 | 153 | 74 | 41.8 | 4.5 |
| Game | 15 | 189 | 140 | 11 | 15.6 | 2.9 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.487 |         0.565 |     -0.003 |
| forks       |   0.487 |   1     |         0.329 |      0.069 |
| open_issues |   0.565 |   0.329 |         1     |      0.011 |
| age_days    |  -0.003 |   0.069 |         0.011 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.599 |         0.326 |      0.038 |
| forks       |   0.599 |   1     |         0.311 |      0.039 |
| open_issues |   0.326 |   0.311 |         1     |      0.129 |
| age_days    |   0.038 |   0.039 |         0.129 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 59 |
| `ai-agents` | 50 |
| `llm` | 50 |
| `ai` | 43 |
| `codex` | 41 |
| `typescript` | 30 |
| `ai-agent` | 29 |
| `macos` | 29 |
| `python` | 28 |
| `claude` | 26 |
| `open-source` | 24 |
| `mcp` | 24 |
| `agent-skills` | 23 |
| `developer-tools` | 23 |
| `cli` | 23 |
| `swift` | 20 |
| `prompt-engineering` | 19 |
| `skills` | 19 |
| `agent` | 19 |
| `anthropic` | 14 |
