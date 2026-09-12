# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 743.9 | 250.0 | 221115 |
| forks | 104.0 | 24.0 | 26193 |
| open_issues | 7.0 | 1.0 | 385 |
| stars_per_day | 50.9 | 16.6 | 7625 |
| age_days | 18.2 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 221115 | 26193 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 25846 | 1236 | TypeScript | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 15426 | 2835 | Python | Other |
| `yjh051108/dsh-routing-suite` | 7168 | 166 | JavaScript | Other |
| `sapientinc/PRAXIST` | 6670 | 643 | Python | Other |
| `lnkiai/m3e-canvas` | 6248 | 631 | TypeScript | Web |
| `MengTo/threeui` | 5643 | 547 | HTML | Web |
| `dataelement/dsh-desktop` | 5569 | 275 | TypeScript | AI/ML |
| `s1dashu/ip-as-logo-skill` | 5156 | 261 | Unknown | AI/ML |
| `CopilotKit/OpenBot` | 4762 | 596 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 7624.7 | 221115 | 29d | Other |
| `Faizpi/bank-sampah` | 920.0 | 920 | 1d | Other |
| `anywhere-labs/dsh-desktop` | 891.2 | 25846 | 29d | Other |
| `lnkiai/m3e-canvas` | 694.2 | 6248 | 9d | Web |
| `sumimakito/Mac-Duo` | 622.0 | 622 | 1d | Mobile |
| `openai/NavierStokesAndEuler` | 597.7 | 1793 | 3d | Other |
| `angusdevgo/IDM_Pro_Tool` | 558.0 | 558 | 1d | Other |
| `ashemag/human-atlas` | 540.2 | 3241 | 6d | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 531.9 | 15426 | 29d | Other |
| `sdli1995/dlssg_for_sm86` | 494.5 | 1978 | 4d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 397 | 508 | 261 | 66 | 37.0 | 7.0 |
| Other | 383 | 1155 | 238 | 172 | 69.6 | 7.7 |
| Web | 63 | 628 | 297 | 83 | 54.2 | 4.3 |
| Mobile | 49 | 376 | 232 | 32 | 53.0 | 8.3 |
| CLI/Tooling | 25 | 482 | 238 | 55 | 23.1 | 6.2 |
| Data | 24 | 346 | 332 | 24 | 20.7 | 6.9 |
| Game | 19 | 440 | 234 | 54 | 31.9 | 7.6 |
| DevOps | 15 | 314 | 181 | 41 | 29.7 | 5.3 |
| Security | 14 | 310 | 276 | 54 | 38.6 | 2.1 |
| Finance/Trading | 11 | 347 | 205 | 59 | 76.5 | 0.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.958 |         0.086 |      0.052 |
| forks       |   0.958 |   1     |         0.051 |      0.043 |
| open_issues |   0.086 |   0.051 |         1     |      0.095 |
| age_days    |   0.052 |   0.043 |         0.095 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.524 |         0.305 |      0.009 |
| forks       |   0.524 |   1     |         0.306 |     -0.016 |
| open_issues |   0.305 |   0.306 |         1     |      0.167 |
| age_days    |   0.009 |  -0.016 |         0.167 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 108 |
| `deepseek-harness` | 95 |
| `ai-agents` | 79 |
| `claude-code` | 74 |
| `dsh` | 69 |
| `deepseek` | 59 |
| `codex` | 54 |
| `llm` | 52 |
| `mcp` | 45 |
| `ai-agent` | 43 |
| `typescript` | 40 |
| `agent-skills` | 36 |
| `developer-tools` | 36 |
| `agent` | 29 |
| `windows` | 29 |
| `python` | 29 |
| `macos` | 25 |
| `ai` | 23 |
| `claude` | 22 |
| `local-first` | 22 |
