# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 753.9 | 241.0 | 216991 |
| forks | 105.6 | 23.0 | 25651 |
| open_issues | 7.1 | 1.0 | 355 |
| stars_per_day | 51.3 | 15.7 | 8346 |
| age_days | 18.4 | 21.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 216991 | 25651 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 24703 | 1195 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 21468 | 2471 | Python | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 15006 | 2718 | Python | Other |
| `zhu1090093659/dsh-web` | 7218 | 474 | TypeScript | Web |
| `yjh051108/dsh-routing-suite` | 7140 | 157 | JavaScript | Other |
| `sapientinc/PRAXIST` | 6609 | 593 | Python | Other |
| `MengTo/threeui` | 5426 | 532 | HTML | Web |
| `lnkiai/m3e-canvas` | 5414 | 502 | TypeScript | Web |
| `s1dashu/ip-as-logo-skill` | 5090 | 257 | Unknown | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 8345.8 | 216991 | 26d | Other |
| `openai/NavierStokesAndEuler` | 1325.0 | 1325 | 1d | Other |
| `EverettFish/holo-card-studio` | 1203.0 | 1203 | 1d | Other |
| `anywhere-labs/dsh-desktop` | 950.1 | 24703 | 26d | Other |
| `lnkiai/m3e-canvas` | 902.3 | 5414 | 6d | Web |
| `ashemag/human-atlas` | 880.7 | 2642 | 3d | Other |
| `guillaumemeyer/watermarks-remover` | 766.7 | 21468 | 28d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 577.2 | 15006 | 26d | Other |
| `sapientinc/PRAXIST` | 550.8 | 6609 | 12d | Other |
| `Rion-Wu-tech/wechat-intelligence-hub` | 498.8 | 1995 | 4d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 389 | 564 | 260 | 76 | 39.7 | 6.7 |
| Other | 370 | 1152 | 228 | 169 | 70.9 | 8.3 |
| Web | 77 | 601 | 270 | 72 | 56.9 | 4.4 |
| Mobile | 49 | 378 | 240 | 30 | 26.4 | 10.6 |
| Data | 29 | 307 | 209 | 28 | 24.7 | 5.5 |
| CLI/Tooling | 28 | 527 | 256 | 54 | 30.3 | 6.0 |
| Game | 18 | 407 | 237 | 53 | 34.6 | 5.1 |
| DevOps | 15 | 277 | 152 | 37 | 53.2 | 2.1 |
| Security | 13 | 374 | 403 | 70 | 34.6 | 2.9 |
| Finance/Trading | 12 | 308 | 194 | 137 | 42.4 | 3.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.958 |         0.08  |      0.043 |
| forks       |   0.958 |   1     |         0.052 |      0.03  |
| open_issues |   0.08  |   0.052 |         1     |      0.104 |
| age_days    |   0.043 |   0.03  |         0.104 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.575 |         0.312 |      0.045 |
| forks       |   0.575 |   1     |         0.306 |     -0.002 |
| open_issues |   0.312 |   0.306 |         1     |      0.12  |
| age_days    |   0.045 |  -0.002 |         0.12  |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 114 |
| `deepseek-harness` | 99 |
| `ai-agents` | 86 |
| `dsh` | 77 |
| `claude-code` | 69 |
| `codex` | 60 |
| `deepseek` | 58 |
| `llm` | 56 |
| `typescript` | 45 |
| `ai-agent` | 44 |
| `mcp` | 43 |
| `agent-skills` | 40 |
| `developer-tools` | 39 |
| `python` | 36 |
| `agent` | 34 |
| `ai` | 30 |
| `windows` | 29 |
| `claude` | 24 |
| `local-first` | 24 |
| `open-source` | 23 |
