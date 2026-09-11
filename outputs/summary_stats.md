# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 746.9 | 247.5 | 220023 |
| forks | 102.2 | 23.0 | 26046 |
| open_issues | 7.0 | 1.0 | 374 |
| stars_per_day | 51.6 | 16.1 | 7858 |
| age_days | 18.2 | 20.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 220023 | 26046 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 25585 | 1230 | TypeScript | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 15303 | 2807 | Python | Other |
| `zhu1090093659/dsh-web` | 7392 | 487 | TypeScript | Web |
| `yjh051108/dsh-routing-suite` | 7170 | 165 | JavaScript | Other |
| `sapientinc/PRAXIST` | 6560 | 626 | Python | Other |
| `lnkiai/m3e-canvas` | 6017 | 597 | TypeScript | Web |
| `MengTo/threeui` | 5566 | 541 | HTML | Web |
| `dataelement/dsh-desktop` | 5219 | 268 | TypeScript | AI/ML |
| `s1dashu/ip-as-logo-skill` | 5136 | 258 | Unknown | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 7858.0 | 220023 | 28d | Other |
| `Faizpi/bank-sampah` | 918.0 | 918 | 1d | Other |
| `anywhere-labs/dsh-desktop` | 913.8 | 25585 | 28d | Other |
| `openai/NavierStokesAndEuler` | 875.5 | 1751 | 2d | Other |
| `lnkiai/m3e-canvas` | 752.1 | 6017 | 8d | Web |
| `ashemag/human-atlas` | 634.2 | 3171 | 5d | Other |
| `Edge0-AI/Edge0` | 592.5 | 1185 | 2d | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 546.5 | 15303 | 28d | Other |
| `sdli1995/dlssg_for_sm86` | 540.0 | 1620 | 3d | Other |
| `sapientinc/PRAXIST` | 468.6 | 6560 | 14d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 395 | 505 | 260 | 63 | 37.7 | 6.7 |
| Other | 383 | 1155 | 232 | 168 | 72.7 | 8.0 |
| Web | 67 | 696 | 286 | 86 | 59.5 | 4.9 |
| Mobile | 46 | 378 | 256 | 31 | 36.2 | 8.2 |
| CLI/Tooling | 25 | 488 | 247 | 55 | 24.9 | 6.0 |
| Data | 25 | 326 | 265 | 23 | 21.4 | 6.6 |
| Game | 18 | 441 | 248 | 55 | 34.3 | 7.1 |
| DevOps | 16 | 280 | 169 | 38 | 30.5 | 4.9 |
| Security | 13 | 351 | 371 | 61 | 36.3 | 2.2 |
| Finance/Trading | 12 | 314 | 194 | 134 | 43.3 | 3.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.96  |         0.092 |      0.049 |
| forks       |   0.96  |   1     |         0.067 |      0.038 |
| open_issues |   0.092 |   0.067 |         1     |      0.088 |
| age_days    |   0.049 |   0.038 |         0.088 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.545 |         0.309 |      0.014 |
| forks       |   0.545 |   1     |         0.325 |     -0.014 |
| open_issues |   0.309 |   0.325 |         1     |      0.154 |
| age_days    |   0.014 |  -0.014 |         0.154 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 110 |
| `deepseek-harness` | 95 |
| `ai-agents` | 80 |
| `dsh` | 73 |
| `claude-code` | 73 |
| `deepseek` | 59 |
| `codex` | 57 |
| `llm` | 53 |
| `mcp` | 44 |
| `typescript` | 43 |
| `ai-agent` | 42 |
| `agent-skills` | 37 |
| `developer-tools` | 35 |
| `python` | 33 |
| `agent` | 31 |
| `windows` | 30 |
| `ai` | 28 |
| `macos` | 24 |
| `claude` | 23 |
| `local-first` | 22 |
