# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 820.5 | 319.5 | 205979 |
| forks | 91.0 | 18.0 | 23878 |
| open_issues | 6.1 | 1.0 | 540 |
| stars_per_day | 56.0 | 16.7 | 12116 |
| age_days | 19.4 | 22.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 205979 | 23878 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 22373 | 1096 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 19605 | 2277 | Python | AI/ML |
| `firecrawl/anydoc` | 19570 | 1163 | Rust | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 13855 | 2409 | Python | Other |
| `pathwaycom/arc-task-gen` | 9128 | 61 | Python | Other |
| `yjh051108/dsh-routing-suite` | 6993 | 141 | JavaScript | Other |
| `FareedKhan-dev/kimi-k3-in-c` | 6893 | 1114 | C | AI/ML |
| `zhu1090093659/dsh-web` | 6572 | 439 | TypeScript | Web |
| `arvids-unavailable/openGym` | 6388 | 1039 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 12116.4 | 205979 | 17d | Other |
| `sapientinc/PRAXIST` | 1807.0 | 5421 | 3d | Other |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 1393.3 | 4180 | 3d | Other |
| `anywhere-labs/dsh-desktop` | 1316.1 | 22373 | 17d | Other |
| `guillaumemeyer/watermarks-remover` | 1031.8 | 19605 | 19d | AI/ML |
| `XiaoDuoYa/codex-with-chatgpt` | 845.5 | 1691 | 2d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 815.0 | 13855 | 17d | Other |
| `firecrawl/anydoc` | 724.8 | 19570 | 27d | Other |
| `MetaMask-AI/metamask-desktop` | 614.0 | 1228 | 2d | Finance/Trading |
| `Nanako0129/sepia` | 570.5 | 1141 | 2d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 495 | 1035 | 317 | 113 | 67.1 | 6.2 |
| AI/ML | 316 | 643 | 340 | 75 | 48.6 | 6.0 |
| Web | 59 | 762 | 326 | 91 | 50.3 | 3.9 |
| Mobile | 42 | 475 | 362 | 36 | 32.4 | 9.6 |
| Data | 25 | 336 | 304 | 21 | 23.3 | 2.7 |
| CLI/Tooling | 22 | 634 | 399 | 66 | 42.4 | 10.7 |
| Security | 17 | 371 | 333 | 64 | 24.8 | 2.5 |
| Game | 10 | 536 | 302 | 35 | 30.7 | 6.7 |
| Finance/Trading | 7 | 338 | 193 | 97 | 97.2 | 2.7 |
| DevOps | 7 | 491 | 242 | 75 | 27.5 | 3.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.97  |         0.098 |     -0.012 |
| forks       |   0.97  |   1     |         0.085 |     -0.033 |
| open_issues |   0.098 |   0.085 |         1     |     -0.079 |
| age_days    |  -0.012 |  -0.033 |        -0.079 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.426 |         0.267 |      0.001 |
| forks       |   0.426 |   1     |         0.59  |     -0.273 |
| open_issues |   0.267 |   0.59  |         1     |     -0.185 |
| age_days    |   0.001 |  -0.273 |        -0.185 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 80 |
| `deepseek-harness` | 76 |
| `ai-agents` | 60 |
| `dsh` | 57 |
| `claude-code` | 51 |
| `llm` | 41 |
| `deepseek` | 40 |
| `codex` | 40 |
| `ai-agent` | 38 |
| `mcp` | 34 |
| `typescript` | 30 |
| `agent` | 29 |
| `developer-tools` | 28 |
| `python` | 27 |
| `agent-skills` | 26 |
| `ai` | 25 |
| `windows` | 23 |
| `claude` | 21 |
| `macos` | 21 |
| `rust` | 20 |
