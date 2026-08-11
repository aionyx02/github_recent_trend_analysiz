# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 518.9 | 202.5 | 24640 |
| forks | 77.4 | 19.0 | 4688 |
| open_issues | 6.3 | 1.0 | 733 |
| stars_per_day | 42.1 | 14.8 | 1974 |
| age_days | 16.9 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 24640 | 4688 | Rust | AI/ML |
| `andrewyng/openworker` | 14125 | 1928 | Python | Other |
| `firecrawl/anydoc` | 13816 | 707 | Rust | Other |
| `Fei-Away/Codex-Dream-Skin` | 13542 | 1326 | JavaScript | AI/ML |
| `yc-software/qm` | 12999 | 1506 | TypeScript | AI/ML |
| `img2threejs/img2threejs` | 10741 | 805 | Python | AI/ML |
| `openai/codex-security` | 9542 | 654 | TypeScript | AI/ML |
| `unicity-aos/aos-ce` | 8576 | 17 | Rust | AI/ML |
| `MoonshotAI/Kimi-K3` | 8343 | 641 | Unknown | Other |
| `trycompai/crm` | 8142 | 908 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `firecrawl/anydoc` | 1973.7 | 13816 | 7d | Other |
| `SMNETSTUDIO/WeChat-AI` | 1115.0 | 1115 | 1d | Other |
| `yc-software/qm` | 1083.2 | 12999 | 12d | AI/ML |
| `xai-org/grok-build` | 912.6 | 24640 | 27d | AI/ML |
| `trycompai/crm` | 814.2 | 8142 | 10d | AI/ML |
| `andrewyng/openworker` | 672.6 | 14125 | 21d | Other |
| `antirez/h3.c` | 660.0 | 660 | 1d | Game |
| `MoonshotAI/Kimi-K3` | 595.9 | 8343 | 14d | Other |
| `FareedKhan-dev/kimi-k3-in-c` | 526.0 | 4734 | 9d | AI/ML |
| `bashalarmistalt/decimen-optical-transfer` | 521.7 | 5739 | 11d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 386 | 443 | 188 | 56 | 40.8 | 4.1 |
| AI/ML | 364 | 712 | 224 | 99 | 49.1 | 9.1 |
| Web | 62 | 403 | 188 | 63 | 48.9 | 2.3 |
| Mobile | 60 | 334 | 198 | 28 | 27.5 | 6.0 |
| CLI/Tooling | 36 | 372 | 226 | 40 | 34.0 | 3.4 |
| Security | 32 | 368 | 212 | 67 | 20.5 | 17.0 |
| Game | 18 | 354 | 187 | 28 | 58.0 | 5.8 |
| Data | 15 | 359 | 181 | 32 | 26.7 | 2.1 |
| DevOps | 14 | 235 | 211 | 36 | 17.2 | 5.4 |
| Finance/Trading | 13 | 270 | 141 | 693 | 15.5 | 0.3 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.688 |         0.305 |      0.055 |
| forks       |   0.688 |   1     |         0.188 |      0.125 |
| open_issues |   0.305 |   0.188 |         1     |      0.067 |
| age_days    |   0.055 |   0.125 |         0.067 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.533 |         0.37  |      0.042 |
| forks       |   0.533 |   1     |         0.345 |      0.161 |
| open_issues |   0.37  |   0.345 |         1     |      0.089 |
| age_days    |   0.042 |   0.161 |         0.089 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 60 |
| `ai-agents` | 59 |
| `codex` | 58 |
| `llm` | 51 |
| `ai` | 46 |
| `developer-tools` | 37 |
| `python` | 37 |
| `typescript` | 35 |
| `macos` | 29 |
| `agent-skills` | 28 |
| `open-source` | 28 |
| `cli` | 27 |
| `claude` | 26 |
| `rust` | 26 |
| `mcp` | 24 |
| `ai-agent` | 23 |
| `agent` | 22 |
| `local-first` | 22 |
| `self-hosted` | 21 |
| `windows` | 19 |
