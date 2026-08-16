# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 633.8 | 217.0 | 120475 |
| forks | 71.6 | 20.0 | 11873 |
| open_issues | 6.9 | 1.0 | 888 |
| stars_per_day | 117.5 | 15.5 | 60238 |
| age_days | 16.4 | 16.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 120475 | 11873 | TypeScript | Other |
| `firecrawl/anydoc` | 16310 | 912 | Rust | Other |
| `andrewyng/openworker` | 14576 | 2020 | Python | Other |
| `yc-software/qm` | 13648 | 1605 | TypeScript | AI/ML |
| `guillaumemeyer/watermarks-remover` | 10050 | 1038 | Python | AI/ML |
| `trycompai/crm` | 8487 | 1003 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 8468 | 660 | Unknown | Other |
| `anywhere-labs/deepseek-harness-desktop` | 7032 | 302 | TypeScript | Other |
| `MiniMax-AI/MiniMax-H3` | 6127 | 364 | Python | Other |
| `bashalarmistalt/decimen-optical-transfer` | 6062 | 733 | TypeScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 60237.5 | 120475 | 2d | Other |
| `anywhere-labs/deepseek-harness-desktop` | 3516.0 | 7032 | 2d | Other |
| `guillaumemeyer/watermarks-remover` | 2512.5 | 10050 | 4d | AI/ML |
| `xiaobright/dsh-anchored-standard` | 2499.0 | 2499 | 1d | Other |
| `yjh051108/dsh-routing-suite` | 2133.0 | 2133 | 1d | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 1734.5 | 3469 | 2d | Other |
| `firecrawl/anydoc` | 1359.2 | 16310 | 12d | Other |
| `zhu1090093659/dsh-web-ui` | 972.7 | 2918 | 3d | Web |
| `cordiverse/paper` | 845.5 | 1691 | 2d | Other |
| `xoreaxeaxeax/skitter-creek-bath-salts` | 844.0 | 1688 | 2d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 432 | 791 | 200 | 84 | 203.6 | 5.4 |
| AI/ML | 333 | 606 | 255 | 72 | 56.4 | 8.3 |
| Web | 68 | 420 | 214 | 43 | 74.7 | 3.5 |
| Mobile | 56 | 385 | 267 | 32 | 27.1 | 11.0 |
| CLI/Tooling | 35 | 382 | 222 | 39 | 48.0 | 5.1 |
| Security | 28 | 314 | 188 | 75 | 29.2 | 20.8 |
| DevOps | 17 | 287 | 227 | 45 | 33.2 | 6.1 |
| Data | 15 | 308 | 189 | 25 | 28.4 | 2.8 |
| Game | 10 | 646 | 279 | 43 | 59.2 | 4.1 |
| Finance/Trading | 6 | 390 | 228 | 244 | 20.8 | 2.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.965 |         0.101 |     -0.055 |
| forks       |   0.965 |   1     |         0.122 |     -0.044 |
| open_issues |   0.101 |   0.122 |         1     |      0.068 |
| age_days    |  -0.055 |  -0.044 |         0.068 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.606 |         0.39  |      0.019 |
| forks       |   0.606 |   1     |         0.405 |      0.065 |
| open_issues |   0.39  |   0.405 |         1     |      0.031 |
| age_days    |   0.019 |   0.065 |         0.031 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 57 |
| `claude-code` | 47 |
| `llm` | 43 |
| `ai` | 42 |
| `codex` | 42 |
| `typescript` | 34 |
| `python` | 33 |
| `developer-tools` | 30 |
| `dsh-plugin` | 29 |
| `macos` | 27 |
| `ai-agent` | 26 |
| `agent` | 26 |
| `dsh` | 23 |
| `rust` | 23 |
| `mcp` | 23 |
| `deepseek` | 22 |
| `deepseek-harness` | 22 |
| `agent-skills` | 22 |
| `cli` | 21 |
| `open-source` | 20 |
