# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 762.6 | 246.0 | 218497 |
| forks | 104.2 | 23.0 | 25839 |
| open_issues | 7.2 | 1.0 | 369 |
| stars_per_day | 52.0 | 15.8 | 8092 |
| age_days | 18.5 | 20.5 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 218497 | 25839 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 25087 | 1205 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 21580 | 2485 | Python | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 15140 | 2752 | Python | Other |
| `zhu1090093659/dsh-web` | 7301 | 477 | TypeScript | Web |
| `yjh051108/dsh-routing-suite` | 7148 | 162 | JavaScript | Other |
| `sapientinc/PRAXIST` | 6325 | 608 | Python | Other |
| `lnkiai/m3e-canvas` | 5682 | 544 | TypeScript | Web |
| `MengTo/threeui` | 5495 | 538 | HTML | Web |
| `s1dashu/ip-as-logo-skill` | 5113 | 258 | Unknown | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 8092.5 | 218497 | 27d | Other |
| `openai/NavierStokesAndEuler` | 1635.0 | 1635 | 1d | Other |
| `anywhere-labs/dsh-desktop` | 929.1 | 25087 | 27d | Other |
| `lnkiai/m3e-canvas` | 811.7 | 5682 | 7d | Web |
| `ashemag/human-atlas` | 747.5 | 2990 | 4d | Other |
| `guillaumemeyer/watermarks-remover` | 744.1 | 21580 | 29d | AI/ML |
| `EverettFish/holo-card-studio` | 645.5 | 1291 | 2d | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 560.7 | 15140 | 27d | Other |
| `gazijarin/itsgiving` | 518.0 | 518 | 1d | Web |
| `sdli1995/dlssg_for_sm86` | 513.5 | 1027 | 2d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 391 | 566 | 264 | 71 | 39.6 | 6.9 |
| Other | 381 | 1140 | 228 | 169 | 70.2 | 8.3 |
| Web | 72 | 650 | 268 | 78 | 63.3 | 4.4 |
| Mobile | 50 | 388 | 248 | 31 | 30.3 | 10.2 |
| CLI/Tooling | 27 | 460 | 247 | 53 | 25.3 | 6.1 |
| Data | 24 | 331 | 282 | 24 | 23.8 | 7.1 |
| Game | 17 | 443 | 263 | 57 | 34.1 | 6.3 |
| DevOps | 14 | 293 | 169 | 42 | 49.0 | 2.5 |
| Security | 13 | 384 | 396 | 72 | 30.5 | 2.9 |
| Finance/Trading | 11 | 351 | 194 | 53 | 75.3 | 1.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.959 |         0.085 |      0.047 |
| forks       |   0.959 |   1     |         0.059 |      0.035 |
| open_issues |   0.085 |   0.059 |         1     |      0.102 |
| age_days    |   0.047 |   0.035 |         0.102 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.569 |         0.303 |      0.022 |
| forks       |   0.569 |   1     |         0.297 |     -0.021 |
| open_issues |   0.303 |   0.297 |         1     |      0.135 |
| age_days    |   0.022 |  -0.021 |         0.135 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 111 |
| `deepseek-harness` | 97 |
| `ai-agents` | 85 |
| `dsh` | 75 |
| `claude-code` | 72 |
| `codex` | 62 |
| `deepseek` | 60 |
| `llm` | 56 |
| `typescript` | 46 |
| `mcp` | 44 |
| `ai-agent` | 42 |
| `agent-skills` | 40 |
| `developer-tools` | 39 |
| `python` | 36 |
| `ai` | 33 |
| `agent` | 33 |
| `windows` | 31 |
| `claude` | 24 |
| `macos` | 23 |
| `local-first` | 23 |
