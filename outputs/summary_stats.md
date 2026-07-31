# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 479.8 | 202.0 | 23626 |
| forks | 122.6 | 22.0 | 13038 |
| open_issues | 5.2 | 1.0 | 339 |
| stars_per_day | 38.7 | 12.8 | 2541 |
| age_days | 18.0 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 23626 | 4493 | Rust | AI/ML |
| `JustVugg/colibri` | 21318 | 2217 | C | Game |
| `Fei-Away/Codex-Dream-Skin` | 12845 | 1282 | JavaScript | AI/ML |
| `andrewyng/openworker` | 11149 | 1491 | Python | Other |
| `img2threejs/img2threejs` | 8666 | 656 | Python | AI/ML |
| `unicity-aos/aos-ce` | 8087 | 16 | Rust | AI/ML |
| `MoonshotAI/Kimi-K3` | 7623 | 518 | Unknown | Other |
| `openai/codex-security` | 7503 | 487 | TypeScript | AI/ML |
| `x4gKing/X4G` | 7131 | 13038 | Python | Other |
| `oso95/scroll-world` | 6097 | 724 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `MoonshotAI/Kimi-K3` | 2541.0 | 7623 | 3d | Other |
| `xai-org/grok-build` | 1476.6 | 23626 | 16d | AI/ML |
| `andrewyng/openworker` | 1114.9 | 11149 | 10d | Other |
| `Fei-Away/Codex-Dream-Skin` | 856.3 | 12845 | 15d | AI/ML |
| `JustVugg/colibri` | 735.1 | 21318 | 29d | Game |
| `bashalarmistalt/decimen-optical-transfer` | 610.0 | 610 | 1d | Other |
| `img2threejs/img2threejs` | 577.7 | 8666 | 15d | AI/ML |
| `talivia-group/talivia` | 504.0 | 504 | 1d | Data |
| `mshumer/Claude-of-Duty` | 487.8 | 2439 | 5d | Other |
| `digimata/quill` | 449.3 | 2696 | 6d | Mobile |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 409 | 564 | 222 | 121 | 39.4 | 5.9 |
| Other | 350 | 443 | 188 | 134 | 44.5 | 5.1 |
| Web | 73 | 337 | 203 | 91 | 26.6 | 4.0 |
| Mobile | 45 | 339 | 175 | 26 | 29.5 | 5.2 |
| CLI/Tooling | 30 | 358 | 212 | 29 | 28.0 | 3.4 |
| Security | 29 | 268 | 192 | 59 | 20.8 | 5.0 |
| Finance/Trading | 17 | 181 | 140 | 748 | 12.9 | 0.5 |
| Game | 17 | 1517 | 219 | 146 | 58.8 | 8.8 |
| Data | 17 | 229 | 127 | 21 | 47.3 | 1.2 |
| DevOps | 13 | 229 | 204 | 21 | 17.9 | 2.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.431 |         0.346 |      0.013 |
| forks       |   0.431 |   1     |         0.094 |      0.056 |
| open_issues |   0.346 |   0.094 |         1     |     -0.012 |
| age_days    |   0.013 |   0.056 |        -0.012 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.512 |         0.356 |      0.014 |
| forks       |   0.512 |   1     |         0.245 |     -0.032 |
| open_issues |   0.356 |   0.245 |         1     |      0.005 |
| age_days    |   0.014 |  -0.032 |         0.005 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 75 |
| `llm` | 72 |
| `ai-agents` | 69 |
| `codex` | 69 |
| `ai` | 48 |
| `claude` | 46 |
| `developer-tools` | 42 |
| `python` | 40 |
| `typescript` | 39 |
| `local-first` | 37 |
| `mcp` | 36 |
| `cli` | 35 |
| `ai-agent` | 31 |
| `agent-skills` | 31 |
| `rust` | 31 |
| `macos` | 30 |
| `windows` | 30 |
| `react` | 26 |
| `desktop-app` | 26 |
| `agent` | 23 |
