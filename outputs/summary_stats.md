# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 813.8 | 319.5 | 207473 |
| forks | 90.0 | 18.0 | 24128 |
| open_issues | 6.1 | 1.0 | 545 |
| stars_per_day | 53.2 | 16.2 | 11526 |
| age_days | 19.8 | 22.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 207473 | 24128 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 22667 | 1112 | TypeScript | Other |
| `firecrawl/anydoc` | 19770 | 1187 | Rust | Other |
| `guillaumemeyer/watermarks-remover` | 19763 | 2296 | Python | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 14000 | 2451 | Python | Other |
| `pathwaycom/arc-task-gen` | 9746 | 62 | Python | Other |
| `yjh051108/dsh-routing-suite` | 7015 | 143 | JavaScript | Other |
| `zhu1090093659/dsh-web` | 6636 | 440 | TypeScript | Web |
| `arvids-unavailable/openGym` | 6509 | 1069 | JavaScript | Other |
| `sapientinc/PRAXIST` | 5727 | 494 | Python | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 11526.3 | 207473 | 18d | Other |
| `sapientinc/PRAXIST` | 1431.8 | 5727 | 4d | Other |
| `anywhere-labs/dsh-desktop` | 1259.3 | 22667 | 18d | Other |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 1053.0 | 4212 | 4d | Other |
| `guillaumemeyer/watermarks-remover` | 988.1 | 19763 | 20d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 777.8 | 14000 | 18d | Other |
| `GangTailorUpgrade/CoomeRtool` | 725.0 | 725 | 1d | Other |
| `firecrawl/anydoc` | 706.1 | 19770 | 28d | Other |
| `XiaoDuoYa/codex-with-chatgpt` | 686.0 | 2058 | 3d | AI/ML |
| `MengTo/threeui` | 485.2 | 4852 | 10d | Web |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 495 | 1040 | 320 | 113 | 64.9 | 6.2 |
| AI/ML | 314 | 629 | 342 | 72 | 45.1 | 6.0 |
| Web | 56 | 713 | 305 | 89 | 48.7 | 3.8 |
| Mobile | 44 | 470 | 298 | 37 | 30.3 | 9.5 |
| Data | 28 | 323 | 288 | 22 | 21.5 | 3.3 |
| CLI/Tooling | 22 | 655 | 407 | 68 | 41.2 | 10.9 |
| Security | 18 | 365 | 332 | 64 | 21.9 | 2.5 |
| Game | 9 | 575 | 322 | 35 | 31.8 | 7.6 |
| Finance/Trading | 7 | 340 | 193 | 98 | 67.5 | 2.1 |
| DevOps | 7 | 497 | 242 | 75 | 26.4 | 3.6 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.969 |         0.097 |     -0.011 |
| forks       |   0.969 |   1     |         0.085 |     -0.033 |
| open_issues |   0.097 |   0.085 |         1     |     -0.074 |
| age_days    |  -0.011 |  -0.033 |        -0.074 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.413 |         0.273 |     -0.002 |
| forks       |   0.413 |   1     |         0.598 |     -0.327 |
| open_issues |   0.273 |   0.598 |         1     |     -0.207 |
| age_days    |  -0.002 |  -0.327 |        -0.207 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 80 |
| `deepseek-harness` | 75 |
| `ai-agents` | 60 |
| `dsh` | 57 |
| `claude-code` | 50 |
| `llm` | 41 |
| `deepseek` | 40 |
| `codex` | 40 |
| `ai-agent` | 37 |
| `mcp` | 35 |
| `typescript` | 29 |
| `agent` | 29 |
| `developer-tools` | 28 |
| `python` | 27 |
| `ai` | 26 |
| `agent-skills` | 25 |
| `claude` | 23 |
| `windows` | 22 |
| `macos` | 21 |
| `rust` | 19 |
