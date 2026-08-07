# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 503.7 | 202.5 | 24332 |
| forks | 105.5 | 22.5 | 4623 |
| open_issues | 6.1 | 1.0 | 606 |
| stars_per_day | 47.8 | 14.6 | 3130 |
| age_days | 17.4 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 24332 | 4623 | Rust | AI/ML |
| `andrewyng/openworker` | 13359 | 1803 | Python | Other |
| `Fei-Away/Codex-Dream-Skin` | 13357 | 1313 | JavaScript | AI/ML |
| `yc-software/qm` | 12120 | 1372 | TypeScript | AI/ML |
| `img2threejs/img2threejs` | 10105 | 754 | Python | AI/ML |
| `firecrawl/anydoc` | 9389 | 440 | Rust | Other |
| `openai/codex-security` | 9176 | 630 | TypeScript | AI/ML |
| `unicity-aos/aos-ce` | 8574 | 17 | Rust | AI/ML |
| `MoonshotAI/Kimi-K3` | 8160 | 619 | Unknown | Other |
| `trycompai/crm` | 7303 | 771 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `firecrawl/anydoc` | 3129.7 | 9389 | 3d | Other |
| `KKKKhazix/human-writing` | 1737.0 | 1737 | 1d | AI/ML |
| `Binaryify/open-kimi-ppt-skill` | 1574.0 | 1574 | 1d | AI/ML |
| `yc-software/qm` | 1515.0 | 12120 | 8d | AI/ML |
| `trycompai/crm` | 1217.2 | 7303 | 6d | AI/ML |
| `xai-org/grok-build` | 1057.9 | 24332 | 23d | AI/ML |
| `MoonshotAI/Kimi-K3` | 816.0 | 8160 | 10d | Other |
| `andrewyng/openworker` | 785.8 | 13359 | 17d | Other |
| `bashalarmistalt/decimen-optical-transfer` | 719.0 | 5033 | 7d | Other |
| `ZzzLc0405/photo-abstract-editorial` | 623.0 | 1246 | 2d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 406 | 660 | 222 | 122 | 58.0 | 7.8 |
| Other | 349 | 449 | 192 | 89 | 47.8 | 5.2 |
| Web | 64 | 373 | 206 | 109 | 34.7 | 3.0 |
| Mobile | 48 | 349 | 198 | 28 | 38.1 | 5.1 |
| CLI/Tooling | 32 | 372 | 229 | 41 | 35.2 | 2.7 |
| Security | 30 | 302 | 208 | 68 | 21.0 | 15.3 |
| Game | 21 | 294 | 175 | 24 | 29.1 | 2.2 |
| Finance/Trading | 18 | 206 | 140 | 668 | 11.3 | 0.4 |
| Data | 16 | 257 | 144 | 26 | 36.6 | 1.6 |
| DevOps | 16 | 208 | 204 | 27 | 26.7 | 2.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.514 |         0.323 |      0.001 |
| forks       |   0.514 |   1     |         0.127 |      0.133 |
| open_issues |   0.323 |   0.127 |         1     |      0.026 |
| age_days    |   0.001 |   0.133 |         0.026 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.487 |         0.375 |     -0     |
| forks       |   0.487 |   1     |         0.267 |      0.129 |
| open_issues |   0.375 |   0.267 |         1     |      0.032 |
| age_days    |  -0     |   0.129 |         0.032 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 70 |
| `codex` | 69 |
| `ai-agents` | 65 |
| `llm` | 58 |
| `ai` | 54 |
| `typescript` | 39 |
| `python` | 38 |
| `developer-tools` | 37 |
| `agent-skills` | 35 |
| `claude` | 33 |
| `cli` | 32 |
| `local-first` | 31 |
| `macos` | 29 |
| `mcp` | 29 |
| `ai-agent` | 26 |
| `agent` | 25 |
| `open-source` | 24 |
| `react` | 22 |
| `rust` | 22 |
| `desktop-app` | 21 |
