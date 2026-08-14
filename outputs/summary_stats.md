# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 598.6 | 218.0 | 77659 |
| forks | 65.7 | 19.0 | 6736 |
| open_issues | 7.0 | 1.0 | 887 |
| stars_per_day | 129.6 | 15.9 | 77659 |
| age_days | 16.5 | 16.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 77659 | 6736 | TypeScript | Other |
| `firecrawl/anydoc` | 15879 | 863 | Rust | Other |
| `andrewyng/openworker` | 14458 | 1995 | Python | Other |
| `Fei-Away/Codex-Dream-Skin` | 13686 | 1335 | JavaScript | AI/ML |
| `yc-software/qm` | 13495 | 1586 | TypeScript | AI/ML |
| `img2threejs/img2threejs` | 11643 | 904 | Python | AI/ML |
| `MoonshotAI/Kimi-K3` | 8435 | 656 | Unknown | Other |
| `trycompai/crm` | 8415 | 988 | TypeScript | AI/ML |
| `guillaumemeyer/watermarks-remover` | 6032 | 645 | Python | AI/ML |
| `bashalarmistalt/decimen-optical-transfer` | 5988 | 727 | TypeScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 77659.0 | 77659 | 1d | Other |
| `guillaumemeyer/watermarks-remover` | 3016.0 | 6032 | 2d | AI/ML |
| `firecrawl/anydoc` | 1587.9 | 15879 | 10d | Other |
| `zhu1090093659/dsh-web-ui` | 1239.0 | 1239 | 1d | Web |
| `xoreaxeaxeax/skitter-creek-bath-salts` | 1216.0 | 1216 | 1d | Other |
| `Leutenegger/book-to-skill` | 1047.0 | 1047 | 1d | AI/ML |
| `cordiverse/paper` | 986.0 | 986 | 1d | Other |
| `yc-software/qm` | 899.7 | 13495 | 15d | AI/ML |
| `trycompai/crm` | 647.3 | 8415 | 13d | AI/ML |
| `dmmulroy/anti-slop` | 624.0 | 624 | 1d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 417 | 658 | 199 | 66 | 232.6 | 4.1 |
| AI/ML | 351 | 659 | 256 | 76 | 59.7 | 10.5 |
| Web | 68 | 427 | 208 | 46 | 89.8 | 2.7 |
| Mobile | 55 | 373 | 228 | 30 | 29.8 | 10.3 |
| CLI/Tooling | 33 | 456 | 284 | 49 | 35.2 | 4.6 |
| Security | 28 | 340 | 197 | 77 | 40.3 | 19.7 |
| DevOps | 15 | 307 | 262 | 40 | 26.1 | 5.9 |
| Data | 15 | 366 | 195 | 37 | 25.9 | 2.3 |
| Game | 12 | 551 | 255 | 39 | 61.3 | 3.7 |
| Finance/Trading | 6 | 382 | 228 | 208 | 22.6 | 2.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.927 |         0.14  |     -0.033 |
| forks       |   0.927 |   1     |         0.176 |     -0.024 |
| open_issues |   0.14  |   0.176 |         1     |      0.085 |
| age_days    |  -0.033 |  -0.024 |         0.085 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.589 |         0.361 |      0.05  |
| forks       |   0.589 |   1     |         0.415 |      0.092 |
| open_issues |   0.361 |   0.415 |         1     |      0.083 |
| age_days    |   0.05  |   0.092 |         0.083 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 61 |
| `claude-code` | 58 |
| `llm` | 52 |
| `codex` | 50 |
| `ai` | 49 |
| `typescript` | 36 |
| `developer-tools` | 36 |
| `python` | 35 |
| `agent-skills` | 30 |
| `macos` | 27 |
| `ai-agent` | 27 |
| `open-source` | 26 |
| `rust` | 26 |
| `cli` | 26 |
| `agent` | 25 |
| `mcp` | 25 |
| `claude` | 23 |
| `self-hosted` | 21 |
| `local-first` | 21 |
| `terminal` | 21 |
