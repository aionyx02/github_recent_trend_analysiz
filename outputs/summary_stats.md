# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 514.8 | 202.5 | 24496 |
| forks | 84.8 | 19.5 | 4663 |
| open_issues | 6.0 | 1.0 | 696 |
| stars_per_day | 42.2 | 15.7 | 2455 |
| age_days | 16.9 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 24496 | 4663 | Rust | AI/ML |
| `andrewyng/openworker` | 13849 | 1882 | Python | Other |
| `Fei-Away/Codex-Dream-Skin` | 13437 | 1321 | JavaScript | AI/ML |
| `yc-software/qm` | 12605 | 1452 | TypeScript | AI/ML |
| `firecrawl/anydoc` | 12276 | 593 | Rust | Other |
| `img2threejs/img2threejs` | 10275 | 773 | Python | AI/ML |
| `openai/codex-security` | 9367 | 641 | TypeScript | AI/ML |
| `unicity-aos/aos-ce` | 8575 | 17 | Rust | AI/ML |
| `MoonshotAI/Kimi-K3` | 8267 | 630 | Unknown | Other |
| `trycompai/crm` | 7844 | 852 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `firecrawl/anydoc` | 2455.2 | 12276 | 5d | Other |
| `yc-software/qm` | 1260.5 | 12605 | 10d | AI/ML |
| `trycompai/crm` | 980.5 | 7844 | 8d | AI/ML |
| `xai-org/grok-build` | 979.8 | 24496 | 25d | AI/ML |
| `andrewyng/openworker` | 728.9 | 13849 | 19d | Other |
| `MoonshotAI/Kimi-K3` | 688.9 | 8267 | 12d | Other |
| `KKKKhazix/human-writing` | 670.7 | 2012 | 3d | AI/ML |
| `bashalarmistalt/decimen-optical-transfer` | 597.2 | 5375 | 9d | Other |
| `Fei-Away/Codex-Dream-Skin` | 559.9 | 13437 | 24d | AI/ML |
| `FareedKhan-dev/kimi-k3-in-c` | 555.6 | 3889 | 7d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 387 | 429 | 189 | 74 | 40.6 | 4.2 |
| AI/ML | 368 | 725 | 231 | 101 | 51.4 | 8.6 |
| Web | 60 | 392 | 214 | 69 | 46.0 | 2.8 |
| Mobile | 51 | 346 | 205 | 29 | 31.0 | 6.5 |
| CLI/Tooling | 32 | 380 | 232 | 41 | 28.0 | 3.2 |
| Security | 32 | 322 | 210 | 67 | 21.5 | 15.4 |
| Game | 21 | 302 | 177 | 23 | 25.7 | 1.8 |
| Data | 21 | 278 | 147 | 22 | 33.7 | 1.5 |
| DevOps | 16 | 216 | 200 | 28 | 18.5 | 4.2 |
| Finance/Trading | 12 | 244 | 141 | 703 | 13.7 | 0.6 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.605 |         0.308 |      0.04  |
| forks       |   0.605 |   1     |         0.16  |      0.104 |
| open_issues |   0.308 |   0.16  |         1     |      0.047 |
| age_days    |   0.04  |   0.104 |         0.047 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.545 |         0.383 |      0.057 |
| forks       |   0.545 |   1     |         0.387 |      0.207 |
| open_issues |   0.383 |   0.387 |         1     |      0.121 |
| age_days    |   0.057 |   0.207 |         0.121 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 64 |
| `codex` | 58 |
| `ai-agents` | 57 |
| `llm` | 52 |
| `ai` | 46 |
| `developer-tools` | 38 |
| `typescript` | 33 |
| `python` | 33 |
| `agent-skills` | 32 |
| `cli` | 30 |
| `macos` | 29 |
| `claude` | 28 |
| `open-source` | 25 |
| `mcp` | 25 |
| `local-first` | 24 |
| `ai-agent` | 23 |
| `rust` | 21 |
| `agent` | 20 |
| `desktop-app` | 19 |
| `terminal` | 18 |
