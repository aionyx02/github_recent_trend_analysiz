# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 753.2 | 257.0 | 211760 |
| forks | 90.0 | 18.0 | 24834 |
| open_issues | 5.8 | 1.0 | 319 |
| stars_per_day | 50.5 | 14.4 | 10084 |
| age_days | 20.0 | 21.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 211760 | 24834 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 23515 | 1153 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 20439 | 2372 | Python | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 14428 | 2556 | Python | Other |
| `yjh051108/dsh-routing-suite` | 7068 | 148 | JavaScript | Other |
| `sapientinc/PRAXIST` | 7038 | 529 | Python | Other |
| `zhu1090093659/dsh-web` | 6825 | 447 | TypeScript | Web |
| `LaoFeng-mouse/flyingmouse-format` | 5376 | 462 | JavaScript | Other |
| `MengTo/threeui` | 5095 | 503 | HTML | Web |
| `s1dashu/ip-as-logo-skill` | 4913 | 243 | Unknown | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 10083.8 | 211760 | 21d | Other |
| `anywhere-labs/dsh-desktop` | 1119.8 | 23515 | 21d | Other |
| `sapientinc/PRAXIST` | 1005.4 | 7038 | 7d | Other |
| `lnkiai/m3e-canvas` | 932.0 | 932 | 1d | Web |
| `anthropics/commerce-agents` | 898.5 | 1797 | 2d | AI/ML |
| `guillaumemeyer/watermarks-remover` | 888.7 | 20439 | 23d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 687.0 | 14428 | 21d | Other |
| `MSNightmare/FalconFlank` | 466.0 | 466 | 1d | Security |
| `codejunkie99/fable-orchestrator` | 416.0 | 416 | 1d | AI/ML |
| `crmne/fastpotify` | 415.9 | 2911 | 7d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 455 | 967 | 242 | 118 | 54.9 | 5.5 |
| AI/ML | 338 | 616 | 307 | 71 | 48.1 | 6.1 |
| Web | 64 | 644 | 300 | 83 | 61.4 | 4.3 |
| Mobile | 45 | 442 | 278 | 34 | 34.4 | 11.0 |
| Data | 30 | 318 | 254 | 22 | 17.5 | 3.4 |
| CLI/Tooling | 22 | 682 | 386 | 69 | 42.4 | 8.5 |
| Security | 15 | 416 | 420 | 82 | 53.1 | 1.3 |
| Game | 13 | 515 | 266 | 35 | 60.3 | 8.2 |
| Finance/Trading | 9 | 319 | 193 | 103 | 64.1 | 2.4 |
| DevOps | 9 | 424 | 238 | 53 | 21.5 | 3.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.97  |         0.105 |     -0.001 |
| forks       |   0.97  |   1     |         0.082 |     -0.013 |
| open_issues |   0.105 |   0.082 |         1     |     -0.029 |
| age_days    |  -0.001 |  -0.013 |        -0.029 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.546 |         0.357 |     -0.112 |
| forks       |   0.546 |   1     |         0.519 |     -0.41  |
| open_issues |   0.357 |   0.519 |         1     |     -0.279 |
| age_days    |  -0.112 |  -0.41  |        -0.279 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 91 |
| `deepseek-harness` | 83 |
| `ai-agents` | 68 |
| `dsh` | 63 |
| `claude-code` | 54 |
| `deepseek` | 46 |
| `codex` | 46 |
| `llm` | 46 |
| `ai-agent` | 41 |
| `typescript` | 35 |
| `mcp` | 33 |
| `agent-skills` | 32 |
| `developer-tools` | 32 |
| `agent` | 29 |
| `python` | 29 |
| `ai` | 26 |
| `windows` | 25 |
| `claude` | 23 |
| `macos` | 22 |
| `prompt-engineering` | 20 |
