# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 515.9 | 246.0 | 14270 |
| forks | 82.5 | 24.0 | 3643 |
| open_issues | 11.6 | 1.0 | 2872 |
| stars_per_day | 65.8 | 19.2 | 4993 |
| age_days | 16.0 | 16.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `browser-use/jev-ultrafast` | 14270 | 873 | Python | Other |
| `eternity4719/HowToLiveBetter` | 10354 | 706 | HTML | Web |
| `lnkiai/m3e-canvas` | 7891 | 823 | TypeScript | Web |
| `NandhaKishorM/laya` | 7492 | 637 | Python | Other |
| `sapientinc/PRAXIST` | 6495 | 718 | Python | Other |
| `rakanki911/DLSS5-Swapper` | 6149 | 323 | JavaScript | Game |
| `tamaratran/fast-jev-compaction` | 5792 | 310 | TypeScript | AI/ML |
| `XiaoDuoYa/codex-with-chatgpt` | 5773 | 552 | TypeScript | AI/ML |
| `zai-org/ZCode` | 4993 | 1398 | TypeScript | AI/ML |
| `bojieli/ai-infra-book` | 4846 | 350 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `zai-org/ZCode` | 4993.0 | 4993 | 1d | AI/ML |
| `NandhaKishorM/laya` | 3746.0 | 7492 | 2d | Other |
| `browser-use/jev-ultrafast` | 3567.5 | 14270 | 4d | Other |
| `mizorewww/laya-mlx` | 2609.0 | 2609 | 1d | AI/ML |
| `tamaratran/fast-jev-compaction` | 1930.7 | 5792 | 3d | AI/ML |
| `robbietilton/Compositor` | 1026.2 | 4105 | 4d | Mobile |
| `eternity4719/HowToLiveBetter` | 796.5 | 10354 | 13d | Web |
| `TheoLeeCJ/SemIf` | 708.5 | 2834 | 4d | Other |
| `bespokelabsai/nimble` | 698.5 | 1397 | 2d | Data |
| `mizorewww/laya-coreml` | 635.0 | 635 | 1d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 414 | 498 | 243 | 92 | 63.3 | 19.7 |
| AI/ML | 377 | 537 | 264 | 76 | 72.6 | 5.9 |
| Mobile | 62 | 459 | 239 | 70 | 59.9 | 8.2 |
| Web | 53 | 776 | 244 | 77 | 55.0 | 3.7 |
| Data | 20 | 404 | 293 | 119 | 84.0 | 8.1 |
| Finance/Trading | 19 | 351 | 231 | 99 | 74.9 | 2.6 |
| CLI/Tooling | 18 | 412 | 240 | 33 | 44.3 | 3.9 |
| Security | 14 | 314 | 286 | 80 | 61.9 | 2.4 |
| DevOps | 13 | 219 | 167 | 22 | 16.2 | 4.1 |
| Game | 10 | 850 | 238 | 99 | 63.9 | 10.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.398 |         0.047 |      0.028 |
| forks       |   0.398 |   1     |         0.041 |      0.027 |
| open_issues |   0.047 |   0.041 |         1     |     -0.011 |
| age_days    |   0.028 |   0.027 |        -0.011 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.539 |         0.296 |      0.056 |
| forks       |   0.539 |   1     |         0.314 |      0.049 |
| open_issues |   0.296 |   0.314 |         1     |      0.038 |
| age_days    |   0.056 |   0.049 |         0.038 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 58 |
| `ai-agents` | 56 |
| `codex` | 48 |
| `llm` | 48 |
| `ai-agent` | 34 |
| `typescript` | 32 |
| `python` | 32 |
| `developer-tools` | 31 |
| `mcp` | 30 |
| `macos` | 30 |
| `agent-skills` | 30 |
| `ai` | 25 |
| `windows` | 23 |
| `react` | 21 |
| `rust` | 21 |
| `jev` | 20 |
| `awesome-list` | 20 |
| `claude` | 19 |
| `open-source` | 19 |
| `self-hosted` | 19 |
