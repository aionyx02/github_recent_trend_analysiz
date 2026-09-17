# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 450.7 | 226.0 | 7256 |
| forks | 72.7 | 22.0 | 4718 |
| open_issues | 9.3 | 1.0 | 3452 |
| stars_per_day | 38.5 | 16.8 | 1186 |
| age_days | 16.9 | 17.5 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `lnkiai/m3e-canvas` | 7256 | 753 | TypeScript | Web |
| `MengTo/threeui` | 5884 | 561 | HTML | Web |
| `sapientinc/PRAXIST` | 5726 | 647 | Python | Other |
| `rakanki911/DLSS5-Swapper` | 5463 | 295 | JavaScript | Game |
| `s1dashu/ip-as-logo-skill` | 5309 | 268 | Unknown | AI/ML |
| `amagine-ai/Amagine3D` | 5133 | 247 | Python | Other |
| `XiaoDuoYa/codex-with-chatgpt` | 5087 | 500 | TypeScript | AI/ML |
| `crmne/spotifast` | 4306 | 191 | Rust | Other |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 4213 | 640 | TeX | Other |
| `bojieli/ai-infra-book` | 4064 | 286 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `ai-sucks-butt/ai-sucks-butt` | 1186.0 | 2372 | 2d | AI/ML |
| `browser-use/jev-ultrafast` | 733.0 | 733 | 1d | Other |
| `lnkiai/m3e-canvas` | 518.3 | 7256 | 14d | Web |
| `saragordic/window-sweaters` | 476.0 | 476 | 1d | Mobile |
| `theoephraim/awesome-cloudflare-selfhosted` | 446.0 | 446 | 1d | Other |
| `vinnylarouge/jevlike` | 438.0 | 438 | 1d | Other |
| `sdli1995/dlssg_for_sm86` | 357.4 | 3217 | 9d | Other |
| `FSECDEV/Threat-Intelligence-Hackers-Forums` | 353.0 | 353 | 1d | Other |
| `nilbuild/page-mascot` | 332.5 | 665 | 2d | AI/ML |
| `ashemag/human-atlas` | 326.5 | 3592 | 11d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 410 | 411 | 208 | 90 | 36.4 | 14.4 |
| AI/ML | 389 | 485 | 254 | 63 | 38.1 | 5.6 |
| Mobile | 64 | 358 | 214 | 35 | 43.4 | 7.0 |
| Web | 52 | 714 | 236 | 78 | 53.2 | 5.4 |
| Data | 18 | 343 | 314 | 25 | 41.0 | 8.4 |
| CLI/Tooling | 17 | 524 | 191 | 59 | 40.3 | 7.4 |
| Security | 15 | 243 | 199 | 53 | 44.3 | 3.2 |
| Game | 13 | 655 | 198 | 79 | 36.9 | 6.2 |
| DevOps | 12 | 213 | 156 | 21 | 17.5 | 3.3 |
| Finance/Trading | 10 | 373 | 188 | 172 | 38.2 | 3.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.332 |         0.044 |      0.079 |
| forks       |   0.332 |   1     |         0.021 |      0.031 |
| open_issues |   0.044 |   0.021 |         1     |     -0.026 |
| age_days    |   0.079 |   0.031 |        -0.026 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.508 |         0.284 |      0.035 |
| forks       |   0.508 |   1     |         0.29  |     -0.003 |
| open_issues |   0.284 |   0.29  |         1     |      0.056 |
| age_days    |   0.035 |  -0.003 |         0.056 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 69 |
| `ai-agents` | 63 |
| `codex` | 50 |
| `llm` | 45 |
| `python` | 37 |
| `ai-agent` | 35 |
| `developer-tools` | 34 |
| `agent-skills` | 30 |
| `ai` | 30 |
| `typescript` | 30 |
| `mcp` | 29 |
| `macos` | 29 |
| `react` | 23 |
| `rust` | 23 |
| `claude` | 23 |
| `self-hosted` | 22 |
| `windows` | 21 |
| `local-first` | 21 |
| `dsh-plugin` | 21 |
| `open-source` | 19 |
