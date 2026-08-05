# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 493.8 | 208.0 | 24170 |
| forks | 104.5 | 22.0 | 4575 |
| open_issues | 5.7 | 1.0 | 517 |
| stars_per_day | 47.1 | 13.5 | 2550 |
| age_days | 17.8 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 24170 | 4575 | Rust | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 13220 | 1300 | JavaScript | AI/ML |
| `andrewyng/openworker` | 12947 | 1748 | Python | Other |
| `yc-software/qm` | 11382 | 1256 | TypeScript | AI/ML |
| `img2threejs/img2threejs` | 9752 | 728 | Python | AI/ML |
| `unicity-aos/aos-ce` | 8574 | 17 | Rust | AI/ML |
| `openai/codex-security` | 8558 | 592 | TypeScript | AI/ML |
| `MoonshotAI/Kimi-K3` | 8071 | 606 | Unknown | Other |
| `oso95/scroll-world` | 7497 | 844 | JavaScript | Other |
| `trycompai/crm` | 5252 | 549 | TypeScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `firecrawl/anydoc` | 2550.0 | 2550 | 1d | Other |
| `yc-software/qm` | 1897.0 | 11382 | 6d | AI/ML |
| `trycompai/crm` | 1313.0 | 5252 | 4d | Other |
| `xai-org/grok-build` | 1151.0 | 24170 | 21d | AI/ML |
| `MoonshotAI/Kimi-K3` | 1008.9 | 8071 | 8d | Other |
| `bashalarmistalt/decimen-optical-transfer` | 920.8 | 4604 | 5d | Other |
| `andrewyng/openworker` | 863.1 | 12947 | 15d | Other |
| `FareedKhan-dev/kimi-k3-in-c` | 738.7 | 2216 | 3d | AI/ML |
| `thebuggeddev/anatomy` | 661.5 | 1323 | 2d | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 661.0 | 13220 | 20d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 410 | 621 | 230 | 116 | 49.7 | 7.2 |
| Other | 354 | 458 | 192 | 92 | 53.0 | 4.9 |
| Web | 69 | 369 | 203 | 99 | 36.7 | 3.1 |
| Mobile | 44 | 332 | 205 | 24 | 46.8 | 4.6 |
| CLI/Tooling | 32 | 363 | 223 | 39 | 40.5 | 3.1 |
| Security | 29 | 292 | 191 | 71 | 19.6 | 13.7 |
| Finance/Trading | 20 | 190 | 140 | 595 | 11.4 | 0.3 |
| Game | 18 | 343 | 229 | 26 | 43.2 | 2.2 |
| DevOps | 14 | 256 | 234 | 28 | 16.0 | 3.1 |
| Data | 10 | 323 | 254 | 39 | 27.6 | 3.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.509 |         0.328 |     -0.007 |
| forks       |   0.509 |   1     |         0.12  |      0.096 |
| open_issues |   0.328 |   0.12  |         1     |      0.004 |
| age_days    |  -0.007 |   0.096 |         0.004 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.521 |         0.405 |     -0.002 |
| forks       |   0.521 |   1     |         0.282 |      0.049 |
| open_issues |   0.405 |   0.282 |         1     |      0.073 |
| age_days    |  -0.002 |   0.049 |         0.073 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 73 |
| `codex` | 68 |
| `llm` | 66 |
| `ai-agents` | 65 |
| `ai` | 53 |
| `typescript` | 40 |
| `developer-tools` | 40 |
| `python` | 37 |
| `claude` | 36 |
| `agent-skills` | 35 |
| `local-first` | 32 |
| `cli` | 30 |
| `macos` | 29 |
| `mcp` | 29 |
| `ai-agent` | 26 |
| `agent` | 25 |
| `windows` | 25 |
| `open-source` | 24 |
| `desktop-app` | 24 |
| `rust` | 24 |
