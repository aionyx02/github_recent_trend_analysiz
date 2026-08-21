# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 745.8 | 272.0 | 176859 |
| forks | 79.8 | 19.0 | 19199 |
| open_issues | 6.5 | 1.0 | 1007 |
| stars_per_day | 78.8 | 20.3 | 25266 |
| age_days | 15.8 | 14.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 176859 | 19199 | TypeScript | Other |
| `firecrawl/anydoc` | 17637 | 1015 | Rust | Other |
| `anywhere-labs/deepseek-harness-desktop` | 16897 | 810 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 16204 | 1843 | Python | AI/ML |
| `yc-software/qm` | 14016 | 1669 | TypeScript | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 10846 | 1632 | Python | Other |
| `trycompai/crm` | 8739 | 1051 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 8556 | 679 | Unknown | Other |
| `MiniMax-AI/MiniMax-H3` | 6571 | 402 | Python | Other |
| `yjh051108/dsh-routing-suite` | 6486 | 119 | PowerShell | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 25265.6 | 176859 | 7d | Other |
| `anywhere-labs/deepseek-harness-desktop` | 2413.9 | 16897 | 7d | Other |
| `guillaumemeyer/watermarks-remover` | 1800.4 | 16204 | 9d | AI/ML |
| `s1dashu/ip-as-logo-skill` | 1636.5 | 3273 | 2d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 1549.4 | 10846 | 7d | Other |
| `yjh051108/dsh-routing-suite` | 1081.0 | 6486 | 6d | Other |
| `firecrawl/anydoc` | 1037.5 | 17637 | 17d | Other |
| `yetone/cumora` | 931.3 | 2794 | 3d | AI/ML |
| `Leutenegger/watermarks-remover` | 926.0 | 926 | 1d | AI/ML |
| `Leutenegger/vanity-eth` | 801.0 | 801 | 1d | CLI/Tooling |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 485 | 912 | 264 | 92 | 98.8 | 4.3 |
| AI/ML | 301 | 680 | 297 | 80 | 67.6 | 10.4 |
| Web | 67 | 513 | 254 | 48 | 55.3 | 3.1 |
| Mobile | 45 | 445 | 289 | 37 | 33.7 | 13.8 |
| CLI/Tooling | 37 | 494 | 255 | 48 | 60.3 | 6.0 |
| Data | 20 | 374 | 256 | 34 | 27.3 | 2.4 |
| Security | 18 | 320 | 213 | 66 | 76.5 | 2.1 |
| DevOps | 12 | 375 | 270 | 70 | 32.8 | 3.6 |
| Game | 10 | 673 | 299 | 52 | 56.9 | 5.6 |
| Finance/Trading | 5 | 344 | 176 | 230 | 25.8 | 3.6 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.985 |         0.066 |     -0.036 |
| forks       |   0.985 |   1     |         0.063 |     -0.033 |
| open_issues |   0.066 |   0.063 |         1     |      0.064 |
| age_days    |  -0.036 |  -0.033 |         0.064 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.5   |         0.355 |      0.024 |
| forks       |   0.5   |   1     |         0.523 |      0.108 |
| open_issues |   0.355 |   0.523 |         1     |      0.116 |
| age_days    |   0.024 |   0.108 |         0.116 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 62 |
| `deepseek-harness` | 52 |
| `ai-agents` | 49 |
| `dsh` | 47 |
| `claude-code` | 43 |
| `codex` | 42 |
| `typescript` | 36 |
| `developer-tools` | 35 |
| `llm` | 34 |
| `deepseek` | 32 |
| `ai-agent` | 32 |
| `ai` | 31 |
| `python` | 27 |
| `macos` | 26 |
| `agent` | 26 |
| `mcp` | 25 |
| `agent-skills` | 23 |
| `cli` | 23 |
| `windows` | 22 |
| `rust` | 21 |
