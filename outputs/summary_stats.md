# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 766.3 | 258.5 | 210476 |
| forks | 88.9 | 18.0 | 24619 |
| open_issues | 5.7 | 1.0 | 308 |
| stars_per_day | 50.1 | 14.2 | 10524 |
| age_days | 19.8 | 21.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 210476 | 24619 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 23240 | 1141 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 20185 | 2335 | Python | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 14315 | 2527 | Python | Other |
| `pathwaycom/arc-task-gen` | 10358 | 66 | Python | Other |
| `yjh051108/dsh-routing-suite` | 7040 | 147 | JavaScript | Other |
| `sapientinc/PRAXIST` | 6900 | 508 | Python | Other |
| `zhu1090093659/dsh-web` | 6768 | 445 | TypeScript | Web |
| `LaoFeng-mouse/flyingmouse-format` | 5329 | 458 | JavaScript | Other |
| `ZzzLc0405/photo-abstract-editorial` | 5307 | 332 | Unknown | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 10523.8 | 210476 | 20d | Other |
| `anywhere-labs/dsh-desktop` | 1162.0 | 23240 | 20d | Other |
| `sapientinc/PRAXIST` | 1150.0 | 6900 | 6d | Other |
| `anthropics/commerce-agents` | 1063.0 | 1063 | 1d | AI/ML |
| `guillaumemeyer/watermarks-remover` | 917.5 | 20185 | 22d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 715.8 | 14315 | 20d | Other |
| `GangTailorUpgrade/undress-service` | 483.0 | 966 | 2d | AI/ML |
| `XiaoDuoYa/codex-with-chatgpt` | 465.4 | 2327 | 5d | AI/ML |
| `MengTo/threeui` | 419.8 | 5037 | 12d | Web |
| `crmne/fastpotify` | 417.5 | 2505 | 6d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 460 | 990 | 246 | 116 | 56.7 | 5.4 |
| AI/ML | 338 | 618 | 305 | 70 | 47.5 | 6.1 |
| Web | 62 | 648 | 306 | 85 | 52.1 | 3.4 |
| Mobile | 45 | 437 | 277 | 34 | 30.5 | 10.4 |
| Data | 29 | 316 | 250 | 22 | 18.2 | 3.4 |
| CLI/Tooling | 21 | 694 | 468 | 71 | 41.3 | 8.8 |
| Security | 16 | 391 | 350 | 72 | 37.4 | 1.1 |
| Game | 13 | 475 | 266 | 33 | 64.8 | 7.4 |
| Finance/Trading | 8 | 322 | 193 | 104 | 41.5 | 2.6 |
| DevOps | 8 | 450 | 237 | 58 | 23.1 | 3.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.969 |         0.102 |     -0.002 |
| forks       |   0.969 |   1     |         0.078 |     -0.018 |
| open_issues |   0.102 |   0.078 |         1     |     -0.029 |
| age_days    |  -0.002 |  -0.018 |        -0.029 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.557 |         0.362 |     -0.085 |
| forks       |   0.557 |   1     |         0.53  |     -0.372 |
| open_issues |   0.362 |   0.53  |         1     |     -0.244 |
| age_days    |  -0.085 |  -0.372 |        -0.244 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 90 |
| `deepseek-harness` | 84 |
| `ai-agents` | 70 |
| `dsh` | 63 |
| `claude-code` | 55 |
| `deepseek` | 46 |
| `codex` | 46 |
| `llm` | 46 |
| `ai-agent` | 39 |
| `mcp` | 38 |
| `typescript` | 35 |
| `developer-tools` | 33 |
| `agent` | 31 |
| `agent-skills` | 30 |
| `python` | 26 |
| `ai` | 25 |
| `windows` | 25 |
| `claude` | 24 |
| `macos` | 24 |
| `prompt-engineering` | 21 |
