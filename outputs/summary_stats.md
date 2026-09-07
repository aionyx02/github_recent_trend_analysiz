# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 738.9 | 242.0 | 214806 |
| forks | 101.8 | 22.0 | 25308 |
| open_issues | 6.6 | 1.0 | 336 |
| stars_per_day | 52.3 | 15.5 | 8950 |
| age_days | 18.2 | 20.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 214806 | 25308 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 24152 | 1172 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 21143 | 2433 | Python | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 14749 | 2644 | Python | Other |
| `yjh051108/dsh-routing-suite` | 7119 | 152 | JavaScript | Other |
| `zhu1090093659/dsh-web` | 7084 | 465 | TypeScript | Web |
| `sapientinc/PRAXIST` | 6491 | 574 | Python | Other |
| `MengTo/threeui` | 5297 | 511 | HTML | Web |
| `s1dashu/ip-as-logo-skill` | 5017 | 253 | Unknown | AI/ML |
| `lnkiai/m3e-canvas` | 4523 | 387 | TypeScript | Web |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 8950.2 | 214806 | 24d | Other |
| `ashemag/human-atlas` | 1744.0 | 1744 | 1d | Other |
| `pierrenade/short-video-generator-AI` | 1141.0 | 1141 | 1d | AI/ML |
| `lnkiai/m3e-canvas` | 1130.8 | 4523 | 4d | Web |
| `anywhere-labs/dsh-desktop` | 1006.3 | 24152 | 24d | Other |
| `vinzdg/codenotch` | 818.0 | 818 | 1d | AI/ML |
| `guillaumemeyer/watermarks-remover` | 813.2 | 21143 | 26d | AI/ML |
| `Rion-Wu-tech/wechat-intelligence-hub` | 802.0 | 1604 | 2d | AI/ML |
| `sapientinc/PRAXIST` | 649.1 | 6491 | 10d | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 614.5 | 14749 | 24d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 394 | 541 | 260 | 70 | 42.6 | 6.4 |
| Other | 359 | 1150 | 223 | 169 | 70.8 | 7.6 |
| Web | 79 | 591 | 273 | 72 | 58.7 | 4.4 |
| Mobile | 49 | 369 | 237 | 30 | 27.4 | 8.8 |
| Data | 32 | 290 | 195 | 24 | 33.5 | 4.8 |
| CLI/Tooling | 31 | 549 | 249 | 51 | 35.2 | 6.7 |
| Game | 19 | 477 | 235 | 55 | 37.5 | 6.6 |
| DevOps | 14 | 320 | 200 | 37 | 33.9 | 1.9 |
| Security | 12 | 394 | 420 | 72 | 33.5 | 3.1 |
| Finance/Trading | 11 | 314 | 193 | 146 | 34.1 | 3.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.962 |         0.084 |      0.033 |
| forks       |   0.962 |   1     |         0.058 |      0.02  |
| open_issues |   0.084 |   0.058 |         1     |      0.074 |
| age_days    |   0.033 |   0.02  |         0.074 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.561 |         0.285 |      0.02  |
| forks       |   0.561 |   1     |         0.308 |     -0.001 |
| open_issues |   0.285 |   0.308 |         1     |      0.065 |
| age_days    |   0.02  |  -0.001 |         0.065 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 112 |
| `deepseek-harness` | 101 |
| `ai-agents` | 83 |
| `dsh` | 75 |
| `claude-code` | 69 |
| `codex` | 61 |
| `deepseek` | 57 |
| `llm` | 57 |
| `ai-agent` | 48 |
| `typescript` | 44 |
| `mcp` | 41 |
| `agent-skills` | 40 |
| `developer-tools` | 39 |
| `python` | 38 |
| `ai` | 37 |
| `agent` | 33 |
| `windows` | 28 |
| `local-first` | 27 |
| `claude` | 26 |
| `macos` | 25 |
