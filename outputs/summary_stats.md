# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 480.6 | 182.0 | 76367 |
| forks | 53.1 | 6.0 | 4058 |
| open_issues | 5.7 | 0.0 | 1178 |
| stars_per_day | 34.4 | 9.6 | 3182 |
| age_days | 18.2 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `DietrichGebert/ponytail` | 76367 | 4058 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 13550 | 1109 | Python | Other |
| `XiaomiMiMo/MiMo-Code` | 11566 | 1133 | TypeScript | AI/ML |
| `langchain-ai/openwiki` | 8293 | 548 | TypeScript | AI/ML |
| `shadcn/improve` | 7256 | 302 | Unknown | Other |
| `omnigent-ai/omnigent` | 6511 | 863 | Python | AI/ML |
| `deepseek-ai/DeepSpec` | 6351 | 551 | Python | Other |
| `cobusgreyling/loop-engineering` | 6308 | 808 | JavaScript | AI/ML |
| `zhongerxin/Cowart` | 4026 | 320 | JavaScript | Other |
| `makerspet/oomwoo` | 3813 | 172 | Python | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 3182.0 | 76367 | 24d | AI/ML |
| `MaximeRivest/riddle` | 817.0 | 817 | 1d | Other |
| `baidu/Unlimited-OCR` | 752.8 | 13550 | 18d | Other |
| `elder-plinius/T3MP3ST` | 721.0 | 2884 | 4d | AI/ML |
| `deepseek-ai/DeepSpec` | 635.1 | 6351 | 10d | Other |
| `ammaarreshi/Generals-Mac-iOS-iPad` | 610.0 | 1220 | 2d | Mobile |
| `514-labs/dnsglobe` | 593.0 | 593 | 1d | CLI/Tooling |
| `langchain-ai/openwiki` | 592.4 | 8293 | 14d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 444.8 | 11566 | 26d | AI/ML |
| `jamesob/local-llm` | 368.3 | 1105 | 3d | CLI/Tooling |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Web | 388 | 195 | 182 | 2 | 11.1 | 0.1 |
| AI/ML | 290 | 838 | 289 | 95 | 55.2 | 9.6 |
| Other | 175 | 608 | 284 | 76 | 50.8 | 12.7 |
| Security | 36 | 354 | 182 | 64 | 20.9 | 2.3 |
| Data | 35 | 264 | 182 | 10 | 17.5 | 1.5 |
| Mobile | 23 | 519 | 246 | 36 | 61.5 | 12.3 |
| CLI/Tooling | 19 | 621 | 298 | 47 | 86.5 | 3.6 |
| DevOps | 15 | 324 | 209 | 13 | 16.5 | 5.6 |
| Finance/Trading | 12 | 253 | 194 | 574 | 21.8 | 0.2 |
| Game | 7 | 266 | 235 | 20 | 39.3 | 2.9 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.635 |         0.189 |      0.039 |
| forks       |   0.635 |   1     |         0.182 |     -0.031 |
| open_issues |   0.189 |   0.182 |         1     |      0.004 |
| age_days    |   0.039 |  -0.031 |         0.004 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.709 |         0.528 |      0.013 |
| forks       |   0.709 |   1     |         0.664 |     -0.017 |
| open_issues |   0.528 |   0.664 |         1     |     -0.025 |
| age_days    |   0.013 |  -0.017 |        -0.025 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 42 |
| `claude-code` | 40 |
| `ai` | 37 |
| `llm` | 34 |
| `codex` | 29 |
| `claude` | 26 |
| `macos` | 23 |
| `mcp` | 21 |
| `open-source` | 19 |
| `ai-agent` | 18 |
| `typescript` | 18 |
| `agent-skills` | 17 |
| `developer-tools` | 17 |
| `cli` | 17 |
| `swift` | 14 |
| `react` | 13 |
| `prompt-engineering` | 12 |
| `python` | 12 |
| `rust` | 12 |
| `anthropic` | 11 |
