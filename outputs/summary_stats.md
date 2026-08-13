# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 529.9 | 214.0 | 24923 |
| forks | 77.8 | 19.0 | 4730 |
| open_issues | 6.6 | 1.0 | 824 |
| stars_per_day | 47.0 | 15.4 | 3243 |
| age_days | 17.0 | 16.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 24923 | 4730 | Rust | AI/ML |
| `firecrawl/anydoc` | 15278 | 818 | Rust | Other |
| `andrewyng/openworker` | 14351 | 1970 | Python | Other |
| `Fei-Away/Codex-Dream-Skin` | 13636 | 1332 | JavaScript | AI/ML |
| `yc-software/qm` | 13308 | 1557 | TypeScript | AI/ML |
| `img2threejs/img2threejs` | 11493 | 882 | Python | AI/ML |
| `MoonshotAI/Kimi-K3` | 8402 | 652 | Unknown | Other |
| `trycompai/crm` | 8351 | 965 | TypeScript | AI/ML |
| `bashalarmistalt/decimen-optical-transfer` | 5913 | 717 | TypeScript | Other |
| `drumih/turbo-fieldfare` | 5899 | 350 | Swift | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `guillaumemeyer/watermarks-remover` | 3243.0 | 3243 | 1d | AI/ML |
| `firecrawl/anydoc` | 1697.6 | 15278 | 9d | Other |
| `yc-software/qm` | 950.6 | 13308 | 14d | AI/ML |
| `xai-org/grok-build` | 859.4 | 24923 | 29d | AI/ML |
| `sohaibdevv/youtube-music` | 851.0 | 851 | 1d | Web |
| `SMNETSTUDIO/WeChat-AI` | 817.0 | 1634 | 2d | Other |
| `trycompai/crm` | 695.9 | 8351 | 12d | AI/ML |
| `milind-soni/OpenMausBot` | 689.0 | 689 | 1d | Other |
| `andrewyng/openworker` | 624.0 | 14351 | 23d | Other |
| `shadcn-ui/chatbot-template` | 607.0 | 607 | 1d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 419 | 451 | 201 | 49 | 41.0 | 4.0 |
| AI/ML | 349 | 715 | 246 | 105 | 56.6 | 10.1 |
| Web | 62 | 419 | 198 | 71 | 66.4 | 2.2 |
| Mobile | 55 | 368 | 233 | 30 | 35.7 | 6.9 |
| CLI/Tooling | 33 | 430 | 284 | 47 | 35.5 | 5.2 |
| Security | 26 | 405 | 250 | 82 | 37.4 | 21.7 |
| DevOps | 15 | 300 | 236 | 37 | 27.0 | 5.6 |
| Data | 15 | 363 | 193 | 30 | 24.1 | 1.9 |
| Finance/Trading | 14 | 276 | 148 | 662 | 16.9 | 0.3 |
| Game | 12 | 535 | 245 | 37 | 71.2 | 3.6 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.72  |         0.285 |      0.053 |
| forks       |   0.72  |   1     |         0.185 |      0.136 |
| open_issues |   0.285 |   0.185 |         1     |      0.073 |
| age_days    |   0.053 |   0.136 |         0.073 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.528 |         0.404 |      0.035 |
| forks       |   0.528 |   1     |         0.401 |      0.135 |
| open_issues |   0.404 |   0.401 |         1     |      0.059 |
| age_days    |   0.035 |   0.135 |         0.059 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 57 |
| `claude-code` | 55 |
| `llm` | 52 |
| `codex` | 50 |
| `ai` | 44 |
| `developer-tools` | 36 |
| `python` | 35 |
| `typescript` | 33 |
| `agent-skills` | 27 |
| `rust` | 27 |
| `cli` | 27 |
| `macos` | 26 |
| `ai-agent` | 26 |
| `mcp` | 26 |
| `open-source` | 24 |
| `agent` | 24 |
| `claude` | 22 |
| `terminal` | 20 |
| `self-hosted` | 18 |
| `react` | 18 |
