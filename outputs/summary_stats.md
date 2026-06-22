# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 469.3 | 184.5 | 76031 |
| forks | 89.2 | 16.0 | 11460 |
| open_issues | 7.7 | 1.0 | 1672 |
| stars_per_day | 37.2 | 12.1 | 5362 |
| age_days | 17.5 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 76031 | 9892 | Python | AI/ML |
| `DietrichGebert/ponytail` | 48262 | 2366 | JavaScript | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 10291 | 961 | TypeScript | AI/ML |
| `shadcn/improve` | 5921 | 235 | Unknown | Other |
| `helloianneo/ian-xiaohei-illustrations` | 5622 | 664 | Unknown | AI/ML |
| `AprilNEA/OpenLogi` | 5230 | 100 | Rust | Other |
| `zgwl/chinese-buy-us-stock-guide` | 4818 | 736 | Unknown | Other |
| `omnigent-ai/omnigent` | 4412 | 500 | Python | AI/ML |
| `op7418/guizang-social-card-skill` | 3878 | 338 | HTML | AI/ML |
| `diffusionstudio/lottie` | 3602 | 192 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 5362.4 | 48262 | 9d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 3620.5 | 76031 | 21d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 935.5 | 10291 | 11d | AI/ML |
| `zhongerxin/Cowart` | 588.3 | 1765 | 3d | Other |
| `shadcn/improve` | 538.3 | 5921 | 11d | Other |
| `lyra81604/zhengxi-views` | 494.0 | 494 | 1d | AI/ML |
| `omnigent-ai/omnigent` | 441.2 | 4412 | 10d | AI/ML |
| `vercel/eve` | 439.6 | 2198 | 5d | AI/ML |
| `tamnd/kage` | 323.7 | 2266 | 7d | Other |
| `Forsy-AI/agent-apprenticeship` | 322.5 | 645 | 2d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 401 | 700 | 198 | 74 | 54.3 | 8.6 |
| Other | 368 | 324 | 174 | 54 | 25.0 | 4.7 |
| Web | 59 | 323 | 179 | 34 | 23.8 | 30.7 |
| Mobile | 47 | 299 | 144 | 31 | 21.1 | 4.0 |
| CLI/Tooling | 36 | 302 | 168 | 21 | 29.9 | 4.6 |
| Finance/Trading | 21 | 240 | 230 | 1537 | 33.2 | 0.5 |
| Data | 18 | 357 | 152 | 72 | 38.3 | 3.8 |
| DevOps | 17 | 204 | 165 | 22 | 22.4 | 4.2 |
| Security | 17 | 446 | 187 | 83 | 34.7 | 9.8 |
| Game | 16 | 187 | 136 | 9 | 27.3 | 2.4 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.518 |         0.559 |     -0.003 |
| forks       |   0.518 |   1     |         0.353 |      0.062 |
| open_issues |   0.559 |   0.353 |         1     |      0.006 |
| age_days    |  -0.003 |   0.062 |         0.006 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.568 |         0.306 |      0.033 |
| forks       |   0.568 |   1     |         0.293 |      0.023 |
| open_issues |   0.306 |   0.293 |         1     |      0.12  |
| age_days    |   0.033 |   0.023 |         0.12  |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 57 |
| `ai-agents` | 52 |
| `llm` | 49 |
| `ai` | 46 |
| `codex` | 41 |
| `typescript` | 30 |
| `claude` | 27 |
| `ai-agent` | 27 |
| `macos` | 27 |
| `python` | 26 |
| `open-source` | 26 |
| `developer-tools` | 24 |
| `cli` | 24 |
| `mcp` | 24 |
| `agent-skills` | 22 |
| `prompt-engineering` | 18 |
| `skills` | 18 |
| `swift` | 18 |
| `agent` | 17 |
| `anthropic` | 15 |
