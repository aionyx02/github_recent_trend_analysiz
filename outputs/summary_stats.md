# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 503.9 | 200.5 | 24419 |
| forks | 98.1 | 21.0 | 4639 |
| open_issues | 6.2 | 1.0 | 673 |
| stars_per_day | 43.4 | 13.8 | 2846 |
| age_days | 17.4 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 24419 | 4639 | Rust | AI/ML |
| `andrewyng/openworker` | 13659 | 1844 | Python | Other |
| `Fei-Away/Codex-Dream-Skin` | 13405 | 1316 | JavaScript | AI/ML |
| `yc-software/qm` | 12372 | 1414 | TypeScript | AI/ML |
| `firecrawl/anydoc` | 11382 | 529 | Rust | Other |
| `img2threejs/img2threejs` | 10209 | 766 | Python | AI/ML |
| `openai/codex-security` | 9291 | 639 | TypeScript | AI/ML |
| `unicity-aos/aos-ce` | 8576 | 17 | Rust | AI/ML |
| `MoonshotAI/Kimi-K3` | 8198 | 622 | Unknown | Other |
| `trycompai/crm` | 7558 | 812 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `firecrawl/anydoc` | 2845.5 | 11382 | 4d | Other |
| `yc-software/qm` | 1374.7 | 12372 | 9d | AI/ML |
| `trycompai/crm` | 1079.7 | 7558 | 7d | AI/ML |
| `xai-org/grok-build` | 1017.5 | 24419 | 24d | AI/ML |
| `KKKKhazix/human-writing` | 959.0 | 1918 | 2d | AI/ML |
| `Binaryify/open-kimi-ppt-skill` | 794.0 | 1588 | 2d | AI/ML |
| `andrewyng/openworker` | 758.8 | 13659 | 18d | Other |
| `MoonshotAI/Kimi-K3` | 745.3 | 8198 | 11d | Other |
| `bashalarmistalt/decimen-optical-transfer` | 648.6 | 5189 | 8d | Other |
| `Fei-Away/Codex-Dream-Skin` | 582.8 | 13405 | 23d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 401 | 671 | 216 | 118 | 50.8 | 8.2 |
| Other | 343 | 448 | 193 | 89 | 45.7 | 4.9 |
| Web | 65 | 358 | 197 | 62 | 31.6 | 2.9 |
| Mobile | 55 | 321 | 181 | 26 | 32.8 | 5.7 |
| CLI/Tooling | 34 | 368 | 230 | 40 | 31.9 | 2.9 |
| Security | 31 | 304 | 217 | 68 | 21.6 | 15.6 |
| Game | 21 | 302 | 175 | 25 | 27.0 | 2.2 |
| Data | 18 | 273 | 143 | 25 | 38.3 | 1.5 |
| Finance/Trading | 16 | 214 | 140 | 618 | 11.4 | 0.4 |
| DevOps | 16 | 217 | 206 | 28 | 21.5 | 3.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.545 |         0.309 |      0.008 |
| forks       |   0.545 |   1     |         0.136 |      0.122 |
| open_issues |   0.309 |   0.136 |         1     |      0.029 |
| age_days    |   0.008 |   0.122 |         0.029 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.524 |         0.365 |     -0.004 |
| forks       |   0.524 |   1     |         0.305 |      0.135 |
| open_issues |   0.365 |   0.305 |         1     |      0.018 |
| age_days    |  -0.004 |   0.135 |         0.018 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 68 |
| `codex` | 67 |
| `ai-agents` | 61 |
| `llm` | 56 |
| `ai` | 51 |
| `developer-tools` | 39 |
| `typescript` | 37 |
| `python` | 37 |
| `agent-skills` | 33 |
| `cli` | 32 |
| `claude` | 31 |
| `macos` | 30 |
| `local-first` | 30 |
| `mcp` | 28 |
| `open-source` | 26 |
| `agent` | 23 |
| `ai-agent` | 23 |
| `react` | 22 |
| `rust` | 21 |
| `desktop-app` | 20 |
