# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 495.7 | 204.5 | 24260 |
| forks | 104.1 | 23.0 | 4606 |
| open_issues | 5.8 | 1.0 | 549 |
| stars_per_day | 48.3 | 13.5 | 2978 |
| age_days | 17.7 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 24260 | 4606 | Rust | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 13299 | 1308 | JavaScript | AI/ML |
| `andrewyng/openworker` | 13214 | 1779 | Python | Other |
| `yc-software/qm` | 11856 | 1319 | TypeScript | AI/ML |
| `img2threejs/img2threejs` | 9977 | 742 | Python | AI/ML |
| `openai/codex-security` | 8937 | 621 | TypeScript | AI/ML |
| `unicity-aos/aos-ce` | 8574 | 17 | Rust | AI/ML |
| `MoonshotAI/Kimi-K3` | 8119 | 616 | Unknown | Other |
| `trycompai/crm` | 6751 | 681 | TypeScript | Other |
| `firecrawl/anydoc` | 5957 | 281 | Rust | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `firecrawl/anydoc` | 2978.5 | 5957 | 2d | Other |
| `yc-software/qm` | 1693.7 | 11856 | 7d | AI/ML |
| `KKKKhazix/human-writing` | 1375.0 | 1375 | 1d | AI/ML |
| `trycompai/crm` | 1350.2 | 6751 | 5d | Other |
| `xai-org/grok-build` | 1102.7 | 24260 | 22d | AI/ML |
| `Binaryify/open-kimi-ppt-skill` | 964.0 | 964 | 1d | AI/ML |
| `MoonshotAI/Kimi-K3` | 902.1 | 8119 | 9d | Other |
| `andrewyng/openworker` | 825.9 | 13214 | 16d | Other |
| `bashalarmistalt/decimen-optical-transfer` | 793.3 | 4760 | 6d | Other |
| `FareedKhan-dev/kimi-k3-in-c` | 667.0 | 2668 | 4d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 413 | 631 | 219 | 118 | 55.6 | 7.4 |
| Other | 354 | 446 | 186 | 87 | 51.6 | 4.9 |
| Web | 65 | 383 | 207 | 105 | 34.5 | 3.1 |
| Mobile | 46 | 343 | 198 | 26 | 39.5 | 4.5 |
| CLI/Tooling | 33 | 367 | 229 | 39 | 33.7 | 3.2 |
| Security | 29 | 295 | 201 | 71 | 22.7 | 14.6 |
| Finance/Trading | 18 | 206 | 140 | 668 | 12.1 | 0.4 |
| Game | 18 | 313 | 198 | 28 | 29.4 | 2.3 |
| DevOps | 14 | 264 | 242 | 29 | 15.4 | 3.3 |
| Data | 10 | 311 | 213 | 40 | 26.9 | 2.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.515 |         0.324 |     -0.013 |
| forks       |   0.515 |   1     |         0.125 |      0.102 |
| open_issues |   0.324 |   0.125 |         1     |      0.014 |
| age_days    |  -0.013 |   0.102 |         0.014 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.491 |         0.384 |     -0.022 |
| forks       |   0.491 |   1     |         0.259 |      0.054 |
| open_issues |   0.384 |   0.259 |         1     |      0.031 |
| age_days    |  -0.022 |   0.054 |         0.031 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 76 |
| `codex` | 74 |
| `ai-agents` | 67 |
| `llm` | 57 |
| `ai` | 52 |
| `typescript` | 39 |
| `developer-tools` | 39 |
| `python` | 38 |
| `agent-skills` | 37 |
| `local-first` | 35 |
| `claude` | 34 |
| `cli` | 32 |
| `mcp` | 31 |
| `macos` | 30 |
| `agent` | 26 |
| `ai-agent` | 24 |
| `desktop-app` | 24 |
| `rust` | 24 |
| `open-source` | 23 |
| `react` | 23 |
