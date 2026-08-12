# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 523.3 | 212.0 | 24725 |
| forks | 78.9 | 20.0 | 4704 |
| open_issues | 6.5 | 1.0 | 776 |
| stars_per_day | 43.2 | 14.8 | 1838 |
| age_days | 17.1 | 17.5 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 24725 | 4704 | Rust | AI/ML |
| `firecrawl/anydoc` | 14706 | 777 | Rust | Other |
| `andrewyng/openworker` | 14249 | 1950 | Python | Other |
| `Fei-Away/Codex-Dream-Skin` | 13596 | 1328 | JavaScript | AI/ML |
| `yc-software/qm` | 13155 | 1534 | TypeScript | AI/ML |
| `img2threejs/img2threejs` | 11179 | 841 | Python | AI/ML |
| `openai/codex-security` | 9665 | 667 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 8373 | 647 | Unknown | Other |
| `trycompai/crm` | 8258 | 945 | TypeScript | AI/ML |
| `bashalarmistalt/decimen-optical-transfer` | 5830 | 704 | TypeScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `firecrawl/anydoc` | 1838.2 | 14706 | 8d | Other |
| `SMNETSTUDIO/WeChat-AI` | 1487.0 | 1487 | 1d | Other |
| `yc-software/qm` | 1011.9 | 13155 | 13d | AI/ML |
| `xai-org/grok-build` | 883.0 | 24725 | 28d | AI/ML |
| `sohaibdevv/youtube-music` | 836.0 | 836 | 1d | Web |
| `trycompai/crm` | 750.7 | 8258 | 11d | AI/ML |
| `antirez/h3.c` | 704.0 | 1408 | 2d | Game |
| `andrewyng/openworker` | 647.7 | 14249 | 22d | Other |
| `MoonshotAI/Kimi-K3` | 558.2 | 8373 | 15d | Other |
| `Fei-Away/Codex-Dream-Skin` | 503.6 | 13596 | 27d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 402 | 453 | 192 | 57 | 41.0 | 4.2 |
| AI/ML | 361 | 696 | 231 | 101 | 48.3 | 9.7 |
| Web | 63 | 417 | 191 | 62 | 56.6 | 2.4 |
| Mobile | 58 | 354 | 239 | 30 | 28.8 | 6.7 |
| CLI/Tooling | 33 | 410 | 275 | 44 | 41.0 | 3.8 |
| Security | 27 | 377 | 203 | 73 | 27.2 | 19.9 |
| Game | 15 | 442 | 220 | 30 | 69.7 | 2.5 |
| Data | 14 | 370 | 182 | 32 | 25.9 | 1.7 |
| DevOps | 14 | 290 | 244 | 38 | 27.6 | 5.6 |
| Finance/Trading | 13 | 276 | 141 | 695 | 15.0 | 0.3 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.702 |         0.301 |      0.049 |
| forks       |   0.702 |   1     |         0.186 |      0.136 |
| open_issues |   0.301 |   0.186 |         1     |      0.069 |
| age_days    |   0.049 |   0.136 |         0.069 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.52  |         0.369 |      0.028 |
| forks       |   0.52  |   1     |         0.369 |      0.145 |
| open_issues |   0.369 |   0.369 |         1     |      0.062 |
| age_days    |   0.028 |   0.145 |         0.062 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 58 |
| `claude-code` | 58 |
| `codex` | 55 |
| `llm` | 49 |
| `ai` | 43 |
| `developer-tools` | 38 |
| `typescript` | 34 |
| `python` | 34 |
| `macos` | 28 |
| `rust` | 28 |
| `cli` | 27 |
| `agent-skills` | 27 |
| `open-source` | 26 |
| `agent` | 23 |
| `ai-agent` | 22 |
| `claude` | 22 |
| `mcp` | 22 |
| `self-hosted` | 20 |
| `local-first` | 20 |
| `terminal` | 19 |
