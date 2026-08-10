# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 515.5 | 200.0 | 24559 |
| forks | 84.7 | 19.5 | 4677 |
| open_issues | 6.1 | 1.0 | 689 |
| stars_per_day | 42.0 | 15.3 | 2160 |
| age_days | 16.8 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 24559 | 4677 | Rust | AI/ML |
| `andrewyng/openworker` | 14017 | 1912 | Python | Other |
| `Fei-Away/Codex-Dream-Skin` | 13487 | 1323 | JavaScript | AI/ML |
| `firecrawl/anydoc` | 12963 | 646 | Rust | Other |
| `yc-software/qm` | 12846 | 1487 | TypeScript | AI/ML |
| `img2threejs/img2threejs` | 10402 | 784 | Python | AI/ML |
| `openai/codex-security` | 9453 | 647 | TypeScript | AI/ML |
| `unicity-aos/aos-ce` | 8577 | 17 | Rust | AI/ML |
| `MoonshotAI/Kimi-K3` | 8302 | 635 | Unknown | Other |
| `trycompai/crm` | 8025 | 888 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `firecrawl/anydoc` | 2160.5 | 12963 | 6d | Other |
| `yc-software/qm` | 1167.8 | 12846 | 11d | AI/ML |
| `xai-org/grok-build` | 944.6 | 24559 | 26d | AI/ML |
| `trycompai/crm` | 891.7 | 8025 | 9d | AI/ML |
| `andrewyng/openworker` | 700.9 | 14017 | 20d | Other |
| `MengTo/kage` | 691.0 | 691 | 1d | Web |
| `MoonshotAI/Kimi-K3` | 638.6 | 8302 | 13d | Other |
| `bashalarmistalt/decimen-optical-transfer` | 562.3 | 5623 | 10d | Other |
| `FareedKhan-dev/kimi-k3-in-c` | 548.2 | 4386 | 8d | AI/ML |
| `KKKKhazix/human-writing` | 541.0 | 2164 | 4d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 385 | 437 | 188 | 75 | 39.6 | 4.2 |
| AI/ML | 373 | 702 | 223 | 98 | 50.7 | 8.4 |
| Web | 63 | 396 | 216 | 67 | 50.9 | 2.5 |
| Mobile | 57 | 333 | 192 | 28 | 28.7 | 5.9 |
| CLI/Tooling | 34 | 369 | 212 | 41 | 31.7 | 3.2 |
| Security | 30 | 388 | 228 | 70 | 22.5 | 17.4 |
| Game | 19 | 325 | 192 | 28 | 22.1 | 6.9 |
| Data | 14 | 359 | 172 | 33 | 30.4 | 2.3 |
| DevOps | 14 | 233 | 208 | 33 | 15.7 | 5.1 |
| Finance/Trading | 11 | 258 | 141 | 766 | 14.4 | 0.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.605 |         0.311 |      0.048 |
| forks       |   0.605 |   1     |         0.162 |      0.116 |
| open_issues |   0.311 |   0.162 |         1     |      0.061 |
| age_days    |   0.048 |   0.116 |         0.061 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.533 |         0.365 |      0.035 |
| forks       |   0.533 |   1     |         0.362 |      0.16  |
| open_issues |   0.365 |   0.362 |         1     |      0.096 |
| age_days    |   0.035 |   0.16  |         0.096 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 65 |
| `codex` | 62 |
| `ai-agents` | 59 |
| `llm` | 51 |
| `ai` | 45 |
| `developer-tools` | 39 |
| `typescript` | 35 |
| `python` | 33 |
| `cli` | 30 |
| `agent-skills` | 30 |
| `macos` | 29 |
| `claude` | 28 |
| `open-source` | 26 |
| `ai-agent` | 24 |
| `mcp` | 23 |
| `local-first` | 23 |
| `agent` | 22 |
| `rust` | 22 |
| `self-hosted` | 20 |
| `react` | 18 |
