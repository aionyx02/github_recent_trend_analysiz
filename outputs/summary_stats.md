# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 807.2 | 300.0 | 196201 |
| forks | 89.2 | 17.0 | 22243 |
| open_issues | 6.0 | 1.0 | 448 |
| stars_per_day | 62.6 | 18.1 | 16350 |
| age_days | 17.3 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 196201 | 22243 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 20394 | 993 | TypeScript | Other |
| `firecrawl/anydoc` | 18478 | 1072 | Rust | Other |
| `guillaumemeyer/watermarks-remover` | 18339 | 2124 | Python | AI/ML |
| `yc-software/qm` | 14204 | 1704 | TypeScript | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 12761 | 2081 | Python | Other |
| `trycompai/crm` | 8943 | 1103 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 8628 | 699 | Unknown | Other |
| `MiniMax-AI/MiniMax-H3` | 7110 | 462 | Python | Other |
| `yjh051108/dsh-routing-suite` | 6831 | 137 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 16350.1 | 196201 | 12d | Other |
| `anywhere-labs/dsh-desktop` | 1699.5 | 20394 | 12d | Other |
| `b-nnett/grok-bot-0.18-reconstructed` | 1314.0 | 2628 | 2d | Other |
| `guillaumemeyer/watermarks-remover` | 1309.9 | 18339 | 14d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 1063.4 | 12761 | 12d | Other |
| `MengTo/threeui` | 1006.0 | 4024 | 4d | Web |
| `firecrawl/anydoc` | 839.9 | 18478 | 22d | Other |
| `tobi/walgit` | 828.0 | 1656 | 2d | Other |
| `yjh051108/dsh-routing-suite` | 621.0 | 6831 | 11d | Other |
| `s1dashu/ip-as-logo-skill` | 615.6 | 4309 | 7d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 499 | 1007 | 301 | 108 | 75.7 | 5.0 |
| AI/ML | 305 | 685 | 304 | 79 | 54.3 | 7.9 |
| Web | 65 | 557 | 285 | 68 | 59.9 | 3.3 |
| Mobile | 41 | 402 | 305 | 34 | 28.4 | 12.4 |
| CLI/Tooling | 26 | 619 | 310 | 62 | 48.9 | 7.2 |
| Data | 26 | 371 | 281 | 32 | 30.3 | 3.0 |
| Security | 14 | 371 | 298 | 71 | 27.6 | 2.9 |
| DevOps | 10 | 380 | 213 | 75 | 26.0 | 3.4 |
| Game | 10 | 756 | 317 | 59 | 45.9 | 6.5 |
| Finance/Trading | 4 | 180 | 182 | 146 | 14.7 | 4.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.974 |         0.116 |     -0.018 |
| forks       |   0.974 |   1     |         0.112 |     -0.032 |
| open_issues |   0.116 |   0.112 |         1     |      0.02  |
| age_days    |  -0.018 |  -0.032 |         0.02  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.442 |         0.306 |      0.052 |
| forks       |   0.442 |   1     |         0.587 |     -0.025 |
| open_issues |   0.306 |   0.587 |         1     |     -0.002 |
| age_days    |   0.052 |  -0.025 |        -0.002 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 76 |
| `deepseek-harness` | 71 |
| `dsh` | 56 |
| `ai-agents` | 52 |
| `deepseek` | 42 |
| `claude-code` | 41 |
| `codex` | 36 |
| `llm` | 34 |
| `typescript` | 33 |
| `ai-agent` | 32 |
| `developer-tools` | 28 |
| `ai` | 27 |
| `mcp` | 27 |
| `agent` | 26 |
| `python` | 25 |
| `agent-skills` | 23 |
| `windows` | 21 |
| `macos` | 20 |
| `rust` | 20 |
| `claude` | 17 |
