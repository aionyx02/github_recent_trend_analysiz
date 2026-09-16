# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 453.4 | 233.0 | 7047 |
| forks | 72.4 | 21.0 | 4638 |
| open_issues | 6.0 | 1.0 | 586 |
| stars_per_day | 37.1 | 16.5 | 1033 |
| age_days | 17.4 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `lnkiai/m3e-canvas` | 7047 | 731 | TypeScript | Web |
| `sapientinc/PRAXIST` | 6544 | 705 | Python | Other |
| `MengTo/threeui` | 5842 | 559 | HTML | Web |
| `s1dashu/ip-as-logo-skill` | 5279 | 266 | Unknown | AI/ML |
| `rakanki911/DLSS5-Swapper` | 5174 | 278 | JavaScript | Game |
| `CopilotKit/OpenBot` | 4980 | 633 | TypeScript | AI/ML |
| `amagine-ai/Amagine3D` | 4980 | 241 | Python | Other |
| `XiaoDuoYa/codex-with-chatgpt` | 4689 | 481 | TypeScript | AI/ML |
| `crmne/spotifast` | 4245 | 184 | Rust | Other |
| `bojieli/ai-infra-book` | 3774 | 263 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `ai-sucks-butt/ai-sucks-butt` | 1033.0 | 1033 | 1d | AI/ML |
| `nilbuild/page-mascot` | 584.0 | 584 | 1d | AI/ML |
| `lnkiai/m3e-canvas` | 542.1 | 7047 | 13d | Web |
| `letorig/video-generator-client` | 516.0 | 516 | 1d | Web |
| `sdli1995/dlssg_for_sm86` | 387.6 | 3101 | 8d | Other |
| `Chuloo/mural` | 385.7 | 1157 | 3d | Mobile |
| `ashemag/human-atlas` | 354.1 | 3541 | 10d | Other |
| `sapientinc/PRAXIST` | 344.4 | 6544 | 19d | Other |
| `saragordic/window-sweaters` | 310.0 | 310 | 1d | Mobile |
| `rakanki911/DLSS5-Swapper` | 304.4 | 5174 | 17d | Game |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 395 | 505 | 264 | 65 | 39.4 | 5.9 |
| Other | 392 | 412 | 220 | 91 | 33.3 | 6.7 |
| Mobile | 59 | 359 | 212 | 36 | 44.0 | 7.4 |
| Web | 51 | 700 | 288 | 80 | 60.2 | 3.6 |
| Data | 30 | 254 | 155 | 14 | 22.5 | 4.9 |
| CLI/Tooling | 16 | 516 | 198 | 59 | 25.1 | 6.2 |
| Game | 16 | 570 | 232 | 65 | 32.9 | 5.4 |
| Security | 16 | 244 | 161 | 50 | 33.7 | 3.1 |
| DevOps | 15 | 199 | 144 | 16 | 16.4 | 2.9 |
| Finance/Trading | 10 | 370 | 188 | 171 | 44.2 | 3.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.335 |         0.141 |      0.061 |
| forks       |   0.335 |   1     |         0.043 |      0.019 |
| open_issues |   0.141 |   0.043 |         1     |     -0.022 |
| age_days    |   0.061 |   0.019 |        -0.022 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.521 |         0.321 |      0.022 |
| forks       |   0.521 |   1     |         0.331 |     -0.01  |
| open_issues |   0.321 |   0.331 |         1     |      0.062 |
| age_days    |   0.022 |  -0.01  |         0.062 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 70 |
| `ai-agents` | 67 |
| `codex` | 52 |
| `llm` | 47 |
| `python` | 37 |
| `mcp` | 36 |
| `ai-agent` | 35 |
| `agent-skills` | 32 |
| `developer-tools` | 32 |
| `ai` | 31 |
| `typescript` | 31 |
| `macos` | 26 |
| `dsh-plugin` | 26 |
| `react` | 23 |
| `windows` | 23 |
| `deepseek-harness` | 22 |
| `claude` | 22 |
| `local-first` | 21 |
| `rust` | 20 |
| `self-hosted` | 20 |
