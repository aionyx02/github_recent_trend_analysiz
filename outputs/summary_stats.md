# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 440.4 | 228.0 | 6868 |
| forks | 70.2 | 21.0 | 4554 |
| open_issues | 5.5 | 1.0 | 145 |
| stars_per_day | 36.2 | 16.3 | 572 |
| age_days | 17.3 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `lnkiai/m3e-canvas` | 6868 | 701 | TypeScript | Web |
| `sapientinc/PRAXIST` | 6777 | 689 | Python | Other |
| `MengTo/threeui` | 5796 | 555 | HTML | Web |
| `s1dashu/ip-as-logo-skill` | 5257 | 265 | Unknown | AI/ML |
| `CopilotKit/OpenBot` | 4918 | 625 | TypeScript | AI/ML |
| `rakanki911/DLSS5-Swapper` | 4839 | 259 | JavaScript | Game |
| `amagine-ai/Amagine3D` | 4793 | 213 | Python | Other |
| `XiaoDuoYa/codex-with-chatgpt` | 4352 | 456 | TypeScript | AI/ML |
| `crmne/spotifast` | 4102 | 184 | Rust | Other |
| `wang2122/sprix-sage-router` | 3689 | 187 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `lnkiai/m3e-canvas` | 572.3 | 6868 | 12d | Web |
| `Chuloo/mural` | 461.5 | 923 | 2d | Mobile |
| `ai-sucks-butt/ai-sucks-butt` | 440.0 | 440 | 1d | AI/ML |
| `nilbuild/page-mascot` | 428.0 | 428 | 1d | AI/ML |
| `sdli1995/dlssg_for_sm86` | 415.0 | 2905 | 7d | Other |
| `yifanzhang-pro/recurrent-looped-tranformer` | 387.5 | 775 | 2d | AI/ML |
| `ashemag/human-atlas` | 386.6 | 3479 | 9d | Other |
| `sapientinc/PRAXIST` | 376.5 | 6777 | 18d | Other |
| `rizqinrr/viserys-agent` | 325.5 | 651 | 2d | Other |
| `zjwzcx/Awesome-Astra-Embodied-AI` | 322.0 | 644 | 2d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 398 | 488 | 258 | 64 | 38.8 | 5.7 |
| Other | 391 | 401 | 217 | 86 | 33.9 | 5.2 |
| Mobile | 58 | 358 | 210 | 35 | 40.9 | 6.5 |
| Web | 50 | 661 | 266 | 76 | 49.0 | 4.5 |
| Data | 30 | 244 | 146 | 14 | 18.9 | 5.3 |
| CLI/Tooling | 16 | 545 | 240 | 74 | 26.9 | 11.9 |
| Game | 16 | 545 | 226 | 63 | 33.6 | 5.0 |
| DevOps | 15 | 207 | 145 | 18 | 17.7 | 3.5 |
| Security | 14 | 255 | 180 | 52 | 25.7 | 3.5 |
| Finance/Trading | 12 | 338 | 196 | 145 | 45.4 | 3.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.338 |         0.246 |      0.042 |
| forks       |   0.338 |   1     |         0.075 |      0.005 |
| open_issues |   0.246 |   0.075 |         1     |      0.021 |
| age_days    |   0.042 |   0.005 |         0.021 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.53  |         0.326 |      0.011 |
| forks       |   0.53  |   1     |         0.321 |     -0.017 |
| open_issues |   0.326 |   0.321 |         1     |      0.094 |
| age_days    |   0.011 |  -0.017 |         0.094 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 72 |
| `ai-agents` | 69 |
| `codex` | 52 |
| `llm` | 46 |
| `mcp` | 40 |
| `python` | 37 |
| `ai-agent` | 37 |
| `dsh-plugin` | 35 |
| `agent-skills` | 32 |
| `deepseek-harness` | 32 |
| `developer-tools` | 31 |
| `typescript` | 31 |
| `ai` | 29 |
| `react` | 24 |
| `macos` | 24 |
| `windows` | 23 |
| `deepseek` | 22 |
| `local-first` | 22 |
| `claude` | 21 |
| `rust` | 20 |
