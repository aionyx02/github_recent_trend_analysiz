# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 750.0 | 244.0 | 215774 |
| forks | 104.1 | 23.0 | 25470 |
| open_issues | 6.7 | 1.0 | 345 |
| stars_per_day | 49.9 | 15.5 | 8631 |
| age_days | 18.5 | 21.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 215774 | 25470 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 24433 | 1182 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 21320 | 2454 | Python | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 14861 | 2682 | Python | Other |
| `zhu1090093659/dsh-web` | 7143 | 469 | TypeScript | Web |
| `yjh051108/dsh-routing-suite` | 7132 | 154 | JavaScript | Other |
| `sapientinc/PRAXIST` | 6778 | 588 | Python | Other |
| `MengTo/threeui` | 5367 | 519 | HTML | Web |
| `s1dashu/ip-as-logo-skill` | 5055 | 256 | Unknown | AI/ML |
| `lnkiai/m3e-canvas` | 4896 | 435 | TypeScript | Web |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 8631.0 | 215774 | 25d | Other |
| `ashemag/human-atlas` | 1136.0 | 2272 | 2d | Other |
| `EverettFish/holo-card-studio` | 1028.0 | 1028 | 1d | Other |
| `lnkiai/m3e-canvas` | 979.2 | 4896 | 5d | Web |
| `anywhere-labs/dsh-desktop` | 977.3 | 24433 | 25d | Other |
| `guillaumemeyer/watermarks-remover` | 789.6 | 21320 | 27d | AI/ML |
| `Rion-Wu-tech/wechat-intelligence-hub` | 634.0 | 1902 | 3d | AI/ML |
| `sapientinc/PRAXIST` | 616.2 | 6778 | 11d | Other |
| `pierrenade/short-video-generator-AI` | 607.0 | 1214 | 2d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 594.4 | 14861 | 25d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 398 | 554 | 260 | 72 | 40.5 | 6.5 |
| Other | 367 | 1146 | 226 | 169 | 67.6 | 7.5 |
| Web | 77 | 596 | 271 | 71 | 52.9 | 4.5 |
| Mobile | 48 | 386 | 237 | 32 | 28.6 | 9.0 |
| CLI/Tooling | 29 | 506 | 244 | 51 | 34.5 | 6.6 |
| Data | 28 | 310 | 232 | 28 | 29.2 | 5.6 |
| Game | 18 | 525 | 262 | 60 | 38.1 | 7.7 |
| DevOps | 12 | 308 | 172 | 36 | 24.4 | 2.4 |
| Security | 12 | 397 | 426 | 72 | 29.1 | 3.2 |
| Finance/Trading | 11 | 315 | 193 | 146 | 29.7 | 3.6 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.96  |         0.086 |      0.037 |
| forks       |   0.96  |   1     |         0.057 |      0.022 |
| open_issues |   0.086 |   0.057 |         1     |      0.084 |
| age_days    |   0.037 |   0.022 |         0.084 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.565 |         0.283 |      0.025 |
| forks       |   0.565 |   1     |         0.299 |     -0.012 |
| open_issues |   0.283 |   0.299 |         1     |      0.073 |
| age_days    |   0.025 |  -0.012 |         0.073 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 114 |
| `deepseek-harness` | 100 |
| `ai-agents` | 84 |
| `dsh` | 77 |
| `claude-code` | 69 |
| `codex` | 62 |
| `deepseek` | 57 |
| `llm` | 56 |
| `ai-agent` | 47 |
| `typescript` | 45 |
| `mcp` | 42 |
| `agent-skills` | 40 |
| `developer-tools` | 39 |
| `python` | 38 |
| `ai` | 33 |
| `agent` | 33 |
| `windows` | 29 |
| `local-first` | 27 |
| `claude` | 25 |
| `open-source` | 24 |
