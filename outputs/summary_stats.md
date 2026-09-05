# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 757.7 | 258.0 | 212708 |
| forks | 89.8 | 17.0 | 24975 |
| open_issues | 5.9 | 1.0 | 329 |
| stars_per_day | 49.6 | 14.3 | 9669 |
| age_days | 20.4 | 22.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 212708 | 24975 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 23723 | 1160 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 20677 | 2389 | Python | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 14536 | 2582 | Python | Other |
| `yjh051108/dsh-routing-suite` | 7087 | 149 | JavaScript | Other |
| `zhu1090093659/dsh-web` | 6913 | 455 | TypeScript | Web |
| `sapientinc/PRAXIST` | 6202 | 539 | Python | Other |
| `LaoFeng-mouse/flyingmouse-format` | 5425 | 462 | JavaScript | Other |
| `MengTo/threeui` | 5151 | 508 | HTML | Web |
| `s1dashu/ip-as-logo-skill` | 4947 | 244 | Unknown | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 9668.5 | 212708 | 22d | Other |
| `lnkiai/m3e-canvas` | 1426.0 | 2852 | 2d | Web |
| `anywhere-labs/dsh-desktop` | 1078.3 | 23723 | 22d | Other |
| `guillaumemeyer/watermarks-remover` | 861.5 | 20677 | 24d | AI/ML |
| `sapientinc/PRAXIST` | 775.2 | 6202 | 8d | Other |
| `anthropics/commerce-agents` | 661.0 | 1983 | 3d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 660.7 | 14536 | 22d | Other |
| `danielblnc/DLSS-NR-on-AMD` | 551.0 | 551 | 1d | AI/ML |
| `anthropics/fermats-last-theorem` | 525.0 | 525 | 1d | Other |
| `MSNightmare/FalconFlank` | 509.0 | 509 | 1d | Security |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 459 | 963 | 243 | 119 | 54.8 | 5.3 |
| AI/ML | 341 | 615 | 303 | 68 | 45.3 | 6.4 |
| Web | 62 | 696 | 304 | 88 | 65.9 | 4.9 |
| Mobile | 43 | 448 | 280 | 34 | 31.8 | 11.1 |
| Data | 29 | 321 | 258 | 22 | 16.8 | 3.6 |
| CLI/Tooling | 22 | 690 | 387 | 67 | 39.7 | 8.5 |
| Game | 14 | 523 | 266 | 36 | 49.6 | 10.4 |
| Security | 13 | 387 | 375 | 72 | 59.5 | 1.4 |
| Finance/Trading | 9 | 356 | 193 | 104 | 61.9 | 2.2 |
| DevOps | 8 | 483 | 250 | 57 | 24.4 | 3.5 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.97  |         0.102 |      0.002 |
| forks       |   0.97  |   1     |         0.071 |     -0.012 |
| open_issues |   0.102 |   0.071 |         1     |     -0.029 |
| age_days    |   0.002 |  -0.012 |        -0.029 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.542 |         0.35  |     -0.142 |
| forks       |   0.542 |   1     |         0.528 |     -0.469 |
| open_issues |   0.35  |   0.528 |         1     |     -0.305 |
| age_days    |  -0.142 |  -0.469 |        -0.305 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 92 |
| `deepseek-harness` | 84 |
| `ai-agents` | 69 |
| `dsh` | 63 |
| `claude-code` | 55 |
| `deepseek` | 47 |
| `llm` | 47 |
| `codex` | 46 |
| `ai-agent` | 40 |
| `typescript` | 37 |
| `agent-skills` | 33 |
| `mcp` | 32 |
| `developer-tools` | 31 |
| `agent` | 29 |
| `python` | 29 |
| `ai` | 27 |
| `windows` | 25 |
| `claude` | 24 |
| `macos` | 21 |
| `prompt-engineering` | 20 |
