# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 763.1 | 282.0 | 185887 |
| forks | 81.4 | 17.5 | 20594 |
| open_issues | 5.8 | 1.0 | 418 |
| stars_per_day | 69.3 | 19.5 | 20654 |
| age_days | 16.3 | 16.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 185887 | 20594 | TypeScript | Other |
| `anywhere-labs/deepseek-harness-desktop` | 18536 | 906 | TypeScript | Other |
| `firecrawl/anydoc` | 17965 | 1037 | Rust | Other |
| `guillaumemeyer/watermarks-remover` | 17147 | 1968 | Python | AI/ML |
| `yc-software/qm` | 14084 | 1685 | TypeScript | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 11626 | 1813 | Python | Other |
| `trycompai/crm` | 8814 | 1075 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 8581 | 687 | Unknown | Other |
| `MiniMax-AI/MiniMax-H3` | 6752 | 423 | Python | Other |
| `yjh051108/dsh-routing-suite` | 6663 | 126 | PowerShell | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 20654.1 | 185887 | 9d | Other |
| `MengTo/threeui` | 2140.0 | 2140 | 1d | Web |
| `anywhere-labs/deepseek-harness-desktop` | 2059.6 | 18536 | 9d | Other |
| `guillaumemeyer/watermarks-remover` | 1558.8 | 17147 | 11d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 1291.8 | 11626 | 9d | Other |
| `s1dashu/ip-as-logo-skill` | 955.2 | 3821 | 4d | AI/ML |
| `firecrawl/anydoc` | 945.5 | 17965 | 19d | Other |
| `yjh051108/dsh-routing-suite` | 832.9 | 6663 | 8d | Other |
| `Leutenegger/vanity-eth` | 803.0 | 803 | 1d | CLI/Tooling |
| `yc-software/qm` | 586.8 | 14084 | 24d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 497 | 934 | 286 | 95 | 82.6 | 4.7 |
| AI/ML | 301 | 664 | 286 | 78 | 57.5 | 7.4 |
| Web | 67 | 557 | 263 | 55 | 77.4 | 3.0 |
| Mobile | 41 | 453 | 320 | 37 | 30.2 | 15.6 |
| CLI/Tooling | 28 | 572 | 295 | 48 | 72.3 | 5.7 |
| Data | 21 | 378 | 257 | 34 | 28.0 | 2.6 |
| Security | 16 | 349 | 218 | 67 | 52.7 | 2.6 |
| DevOps | 13 | 348 | 222 | 61 | 27.0 | 3.9 |
| Game | 10 | 706 | 310 | 57 | 53.0 | 7.1 |
| Finance/Trading | 6 | 318 | 174 | 194 | 20.6 | 2.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.983 |         0.115 |     -0.031 |
| forks       |   0.983 |   1     |         0.112 |     -0.031 |
| open_issues |   0.115 |   0.112 |         1     |      0.016 |
| age_days    |  -0.031 |  -0.031 |         0.016 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.455 |         0.314 |      0.049 |
| forks       |   0.455 |   1     |         0.569 |      0.062 |
| open_issues |   0.314 |   0.569 |         1     |      0.058 |
| age_days    |   0.049 |   0.062 |         0.058 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 70 |
| `deepseek-harness` | 60 |
| `dsh` | 55 |
| `ai-agents` | 46 |
| `codex` | 42 |
| `claude-code` | 39 |
| `deepseek` | 37 |
| `llm` | 36 |
| `typescript` | 35 |
| `ai` | 31 |
| `developer-tools` | 29 |
| `ai-agent` | 29 |
| `agent` | 26 |
| `python` | 25 |
| `mcp` | 24 |
| `agent-skills` | 23 |
| `windows` | 22 |
| `macos` | 21 |
| `cli` | 20 |
| `rust` | 19 |
