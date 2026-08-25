# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 790.3 | 295.0 | 193219 |
| forks | 86.6 | 17.0 | 21715 |
| open_issues | 5.9 | 1.0 | 443 |
| stars_per_day | 66.7 | 18.7 | 17565 |
| age_days | 16.9 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 193219 | 21715 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 19913 | 967 | TypeScript | Other |
| `firecrawl/anydoc` | 18338 | 1061 | Rust | Other |
| `guillaumemeyer/watermarks-remover` | 18023 | 2080 | Python | AI/ML |
| `yc-software/qm` | 14165 | 1696 | TypeScript | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 12407 | 2004 | Python | Other |
| `trycompai/crm` | 8896 | 1097 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 8612 | 695 | Unknown | Other |
| `MiniMax-AI/MiniMax-H3` | 6985 | 451 | Python | Other |
| `yjh051108/dsh-routing-suite` | 6773 | 132 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 17565.4 | 193219 | 11d | Other |
| `b-nnett/grok-bot-0.18-reconstructed` | 2106.0 | 2106 | 1d | Other |
| `anywhere-labs/dsh-desktop` | 1810.3 | 19913 | 11d | Other |
| `guillaumemeyer/watermarks-remover` | 1386.4 | 18023 | 13d | AI/ML |
| `MengTo/threeui` | 1223.3 | 3670 | 3d | Web |
| `tobi/walgit` | 1219.0 | 1219 | 1d | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 1127.9 | 12407 | 11d | Other |
| `firecrawl/anydoc` | 873.2 | 18338 | 21d | Other |
| `ShadowAqueduct/watermark-remover` | 782.0 | 782 | 1d | AI/ML |
| `s1dashu/ip-as-logo-skill` | 698.3 | 4190 | 6d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 504 | 979 | 298 | 103 | 81.3 | 4.9 |
| AI/ML | 304 | 676 | 301 | 79 | 58.6 | 7.7 |
| Web | 63 | 544 | 278 | 67 | 58.3 | 3.1 |
| Mobile | 39 | 389 | 305 | 34 | 31.5 | 12.5 |
| CLI/Tooling | 26 | 599 | 285 | 60 | 42.9 | 6.0 |
| Data | 24 | 378 | 283 | 33 | 26.0 | 2.8 |
| Security | 16 | 342 | 248 | 64 | 27.6 | 2.4 |
| DevOps | 10 | 377 | 208 | 73 | 27.6 | 3.3 |
| Game | 10 | 741 | 316 | 58 | 48.0 | 6.3 |
| Finance/Trading | 4 | 178 | 181 | 146 | 15.9 | 4.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.977 |         0.119 |     -0.024 |
| forks       |   0.977 |   1     |         0.114 |     -0.036 |
| open_issues |   0.119 |   0.114 |         1     |      0.015 |
| age_days    |  -0.024 |  -0.036 |         0.015 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.431 |         0.311 |      0.049 |
| forks       |   0.431 |   1     |         0.59  |     -0.007 |
| open_issues |   0.311 |   0.59  |         1     |      0.039 |
| age_days    |   0.049 |  -0.007 |         0.039 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 73 |
| `deepseek-harness` | 67 |
| `dsh` | 55 |
| `ai-agents` | 51 |
| `claude-code` | 40 |
| `deepseek` | 39 |
| `codex` | 37 |
| `llm` | 36 |
| `typescript` | 34 |
| `ai-agent` | 32 |
| `ai` | 29 |
| `developer-tools` | 27 |
| `mcp` | 26 |
| `python` | 26 |
| `agent` | 25 |
| `agent-skills` | 23 |
| `windows` | 21 |
| `rust` | 20 |
| `claude` | 18 |
| `cli` | 18 |
