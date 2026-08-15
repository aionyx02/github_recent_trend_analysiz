# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 606.4 | 213.5 | 102234 |
| forks | 67.2 | 19.0 | 9691 |
| open_issues | 7.2 | 1.0 | 886 |
| stars_per_day | 160.3 | 15.9 | 102234 |
| age_days | 16.3 | 16.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 102234 | 9691 | TypeScript | Other |
| `firecrawl/anydoc` | 16149 | 891 | Rust | Other |
| `andrewyng/openworker` | 14524 | 2015 | Python | Other |
| `yc-software/qm` | 13577 | 1597 | TypeScript | AI/ML |
| `guillaumemeyer/watermarks-remover` | 8669 | 889 | Python | AI/ML |
| `MoonshotAI/Kimi-K3` | 8447 | 657 | Unknown | Other |
| `trycompai/crm` | 8447 | 998 | TypeScript | AI/ML |
| `bashalarmistalt/decimen-optical-transfer` | 6034 | 731 | TypeScript | Other |
| `drumih/turbo-fieldfare` | 5980 | 356 | Swift | AI/ML |
| `MiniMax-AI/MiniMax-H3` | 5968 | 359 | Python | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 102234.0 | 102234 | 1d | Other |
| `anywhere-labs/deepseek-harness-desktop` | 3125.0 | 3125 | 1d | Other |
| `guillaumemeyer/watermarks-remover` | 2889.7 | 8669 | 3d | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 1725.0 | 1725 | 1d | Other |
| `xoreaxeaxeax/skitter-creek-bath-salts` | 1601.0 | 1601 | 1d | Other |
| `firecrawl/anydoc` | 1468.1 | 16149 | 11d | Other |
| `cordiverse/paper` | 1409.0 | 1409 | 1d | Other |
| `xiaobright/dsh-anchored-standard` | 1121.0 | 1121 | 1d | Other |
| `zhu1090093659/dsh-web-ui` | 1082.0 | 2164 | 2d | Web |
| `Leutenegger/book-to-skill` | 1080.0 | 1080 | 1d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 431 | 718 | 195 | 74 | 297.4 | 4.6 |
| AI/ML | 340 | 602 | 244 | 72 | 61.4 | 10.1 |
| Web | 67 | 457 | 219 | 44 | 85.3 | 3.6 |
| Mobile | 56 | 374 | 233 | 30 | 29.5 | 10.6 |
| CLI/Tooling | 33 | 441 | 238 | 44 | 35.0 | 4.9 |
| Security | 26 | 323 | 199 | 79 | 39.8 | 21.9 |
| DevOps | 15 | 295 | 228 | 45 | 37.8 | 6.2 |
| Data | 15 | 303 | 187 | 24 | 21.7 | 2.3 |
| Game | 11 | 595 | 269 | 41 | 58.5 | 3.8 |
| Finance/Trading | 6 | 384 | 226 | 220 | 21.5 | 2.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.958 |         0.107 |     -0.051 |
| forks       |   0.958 |   1     |         0.132 |     -0.043 |
| open_issues |   0.107 |   0.132 |         1     |      0.089 |
| age_days    |  -0.051 |  -0.043 |         0.089 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.601 |         0.368 |      0.042 |
| forks       |   0.601 |   1     |         0.399 |      0.08  |
| open_issues |   0.368 |   0.399 |         1     |      0.054 |
| age_days    |   0.042 |   0.08  |         0.054 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 58 |
| `llm` | 50 |
| `claude-code` | 50 |
| `codex` | 48 |
| `ai` | 46 |
| `typescript` | 36 |
| `python` | 32 |
| `developer-tools` | 31 |
| `macos` | 27 |
| `agent` | 27 |
| `ai-agent` | 25 |
| `rust` | 25 |
| `cli` | 24 |
| `dsh-plugin` | 23 |
| `open-source` | 23 |
| `agent-skills` | 22 |
| `mcp` | 22 |
| `self-hosted` | 21 |
| `claude` | 20 |
| `react` | 20 |
