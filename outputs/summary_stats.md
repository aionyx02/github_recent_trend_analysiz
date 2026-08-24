# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 769.4 | 282.0 | 189552 |
| forks | 83.2 | 18.0 | 21150 |
| open_issues | 5.8 | 1.0 | 373 |
| stars_per_day | 66.6 | 18.7 | 18955 |
| age_days | 16.6 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 189552 | 21150 | TypeScript | Other |
| `anywhere-labs/deepseek-harness-desktop` | 19277 | 941 | TypeScript | Other |
| `firecrawl/anydoc` | 18148 | 1048 | Rust | Other |
| `guillaumemeyer/watermarks-remover` | 17592 | 2028 | Python | AI/ML |
| `yc-software/qm` | 14125 | 1690 | TypeScript | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 12020 | 1908 | Python | Other |
| `trycompai/crm` | 8857 | 1084 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 8594 | 689 | Unknown | Other |
| `MiniMax-AI/MiniMax-H3` | 6864 | 436 | Python | Other |
| `yjh051108/dsh-routing-suite` | 6728 | 130 | PowerShell | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 18955.2 | 189552 | 10d | Other |
| `anywhere-labs/deepseek-harness-desktop` | 1927.7 | 19277 | 10d | Other |
| `MengTo/threeui` | 1566.0 | 3132 | 2d | Web |
| `guillaumemeyer/watermarks-remover` | 1466.0 | 17592 | 12d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 1202.0 | 12020 | 10d | Other |
| `duty1g/x64dbg-mcp-server` | 1021.0 | 1021 | 1d | AI/ML |
| `firecrawl/anydoc` | 907.4 | 18148 | 20d | Other |
| `s1dashu/ip-as-logo-skill` | 797.4 | 3987 | 5d | AI/ML |
| `ShadowAqueduct/watermark-remover` | 761.0 | 761 | 1d | AI/ML |
| `yjh051108/dsh-routing-suite` | 747.6 | 6728 | 9d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 498 | 949 | 288 | 98 | 78.7 | 4.7 |
| AI/ML | 299 | 668 | 288 | 78 | 62.2 | 7.7 |
| Web | 67 | 586 | 267 | 65 | 67.7 | 3.4 |
| Mobile | 41 | 361 | 277 | 31 | 25.6 | 11.4 |
| CLI/Tooling | 26 | 581 | 268 | 48 | 44.2 | 6.3 |
| Data | 23 | 377 | 282 | 34 | 28.2 | 2.8 |
| Security | 16 | 335 | 230 | 63 | 30.4 | 2.5 |
| DevOps | 13 | 352 | 229 | 62 | 25.1 | 4.0 |
| Game | 11 | 670 | 279 | 53 | 47.7 | 6.2 |
| Finance/Trading | 6 | 319 | 177 | 195 | 19.0 | 2.5 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.982 |         0.117 |     -0.028 |
| forks       |   0.982 |   1     |         0.111 |     -0.03  |
| open_issues |   0.117 |   0.111 |         1     |      0.011 |
| age_days    |  -0.028 |  -0.03  |         0.011 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.441 |         0.291 |      0.031 |
| forks       |   0.441 |   1     |         0.552 |      0.032 |
| open_issues |   0.291 |   0.552 |         1     |      0.055 |
| age_days    |   0.031 |   0.032 |         0.055 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 73 |
| `deepseek-harness` | 65 |
| `dsh` | 55 |
| `ai-agents` | 46 |
| `deepseek` | 39 |
| `codex` | 37 |
| `claude-code` | 37 |
| `llm` | 36 |
| `typescript` | 34 |
| `ai` | 32 |
| `ai-agent` | 32 |
| `agent` | 26 |
| `developer-tools` | 26 |
| `mcp` | 25 |
| `python` | 25 |
| `windows` | 23 |
| `agent-skills` | 23 |
| `cli` | 20 |
| `macos` | 19 |
| `rust` | 19 |
