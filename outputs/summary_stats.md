# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 458.4 | 238.5 | 7177 |
| forks | 76.2 | 22.0 | 4319 |
| open_issues | 5.7 | 1.0 | 143 |
| stars_per_day | 38.9 | 16.2 | 646 |
| age_days | 17.8 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `yjh051108/dsh-routing-suite` | 7177 | 168 | JavaScript | Other |
| `sapientinc/PRAXIST` | 6711 | 663 | Python | Other |
| `lnkiai/m3e-canvas` | 6402 | 653 | TypeScript | Web |
| `MengTo/threeui` | 5694 | 550 | HTML | Web |
| `s1dashu/ip-as-logo-skill` | 5197 | 262 | Unknown | AI/ML |
| `CopilotKit/OpenBot` | 4837 | 608 | TypeScript | AI/ML |
| `amagine-ai/Amagine3D` | 4408 | 194 | Python | Other |
| `EvoMap/AutoResearch` | 4268 | 291 | Python | AI/ML |
| `XiaoDuoYa/codex-with-chatgpt` | 4156 | 438 | TypeScript | AI/ML |
| `rakanki911/DLSS5-Swapper` | 4103 | 212 | JavaScript | Game |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `Faizpi/bank-sampah` | 646.0 | 646 | 1d | Other |
| `lnkiai/m3e-canvas` | 640.2 | 6402 | 10d | Web |
| `rizqinrr/viserys-agent` | 627.0 | 627 | 1d | Other |
| `ashemag/human-atlas` | 474.3 | 3320 | 7d | Other |
| `openai/NavierStokesAndEuler` | 461.5 | 1846 | 4d | Other |
| `sdli1995/dlssg_for_sm86` | 461.0 | 2305 | 5d | Other |
| `sapientinc/PRAXIST` | 419.4 | 6711 | 16d | Other |
| `eternityspring/reelbench-skills` | 412.0 | 412 | 1d | AI/ML |
| `Edge0-AI/Edge0` | 380.5 | 1522 | 4d | Other |
| `sumimakito/Mac-Duo` | 372.0 | 744 | 2d | Mobile |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 390 | 472 | 250 | 63 | 36.9 | 5.6 |
| Other | 382 | 455 | 231 | 100 | 41.2 | 5.8 |
| Web | 59 | 647 | 297 | 90 | 51.6 | 4.9 |
| Mobile | 54 | 358 | 214 | 31 | 41.4 | 7.5 |
| Data | 31 | 306 | 215 | 19 | 17.4 | 5.4 |
| CLI/Tooling | 21 | 541 | 249 | 71 | 25.1 | 9.8 |
| Game | 20 | 446 | 208 | 53 | 29.6 | 4.0 |
| DevOps | 16 | 310 | 176 | 34 | 26.2 | 4.9 |
| Security | 16 | 289 | 254 | 50 | 35.8 | 2.7 |
| Finance/Trading | 11 | 352 | 206 | 157 | 79.0 | 3.4 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.301 |         0.262 |      0.044 |
| forks       |   0.301 |   1     |         0.058 |      0.006 |
| open_issues |   0.262 |   0.058 |         1     |      0.059 |
| age_days    |   0.044 |   0.006 |         0.059 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.534 |         0.331 |      0.004 |
| forks       |   0.534 |   1     |         0.32  |     -0.015 |
| open_issues |   0.331 |   0.32  |         1     |      0.168 |
| age_days    |   0.004 |  -0.015 |         0.168 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 78 |
| `ai-agents` | 72 |
| `deepseek-harness` | 72 |
| `claude-code` | 70 |
| `codex` | 51 |
| `dsh` | 47 |
| `llm` | 47 |
| `deepseek` | 42 |
| `ai-agent` | 41 |
| `mcp` | 40 |
| `typescript` | 38 |
| `developer-tools` | 33 |
| `agent-skills` | 32 |
| `python` | 31 |
| `windows` | 29 |
| `ai` | 28 |
| `macos` | 26 |
| `react` | 23 |
| `agent` | 22 |
| `claude` | 21 |
