# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 432.1 | 195.5 | 21957 |
| forks | 85.8 | 14.0 | 11801 |
| open_issues | 3.7 | 0.0 | 946 |
| stars_per_day | 34.6 | 11.3 | 2745 |
| age_days | 19.5 | 23.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 21957 | 4130 | Rust | AI/ML |
| `JustVugg/colibri` | 18072 | 1744 | C | Game |
| `Fei-Away/Codex-Dream-Skin` | 11963 | 1197 | JavaScript | AI/ML |
| `unicity-aos/aos-ce` | 6765 | 8 | Rust | AI/ML |
| `deepseek-ai/DeepSpec` | 6746 | 625 | Python | Other |
| `x4gKing/X4G` | 6446 | 11801 | Python | Other |
| `Yu9191/wloc` | 6158 | 1215 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 5109 | 1058 | TypeScript | AI/ML |
| `oso95/scroll-world` | 4896 | 564 | JavaScript | Other |
| `bikini/exploitarium` | 4022 | 1150 | Python | Security |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `xai-org/grok-build` | 2744.6 | 21957 | 8d | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 1709.0 | 11963 | 7d | AI/ML |
| `JustVugg/colibri` | 860.6 | 18072 | 21d | Game |
| `Jakubantalik/thinking-orbs` | 703.0 | 703 | 1d | AI/ML |
| `unicity-aos/aos-ce` | 676.5 | 6765 | 10d | AI/ML |
| `lopopolo/harness-engineering` | 554.0 | 2216 | 4d | AI/ML |
| `0xhype/hyperliquid-tracker` | 503.0 | 503 | 1d | Finance/Trading |
| `gnipbao/story-to-handdrawn-video` | 460.0 | 460 | 1d | AI/ML |
| `Blaizzy/nativ` | 389.0 | 778 | 2d | AI/ML |
| `x4gKing/X4G` | 358.1 | 6446 | 18d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 386 | 503 | 227 | 60 | 47.8 | 2.9 |
| Other | 227 | 525 | 258 | 154 | 37.3 | 8.5 |
| Web | 222 | 196 | 151 | 19 | 10.6 | 0.9 |
| Finance/Trading | 30 | 239 | 212 | 547 | 29.9 | 1.2 |
| Mobile | 30 | 426 | 244 | 41 | 34.6 | 4.9 |
| Data | 28 | 227 | 151 | 9 | 9.6 | 0.3 |
| CLI/Tooling | 26 | 516 | 242 | 48 | 34.9 | 2.8 |
| Security | 21 | 453 | 185 | 103 | 37.1 | 1.0 |
| Game | 17 | 1380 | 282 | 124 | 73.5 | 7.8 |
| DevOps | 13 | 189 | 153 | 7 | 10.6 | 0.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.448 |         0.081 |     -0.08  |
| forks       |   0.448 |   1     |         0.028 |     -0.051 |
| open_issues |   0.081 |   0.028 |         1     |      0.003 |
| age_days    |  -0.08  |  -0.051 |         0.003 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.807 |         0.59  |     -0.326 |
| forks       |   0.807 |   1     |         0.583 |     -0.331 |
| open_issues |   0.59  |   0.583 |         1     |     -0.153 |
| age_days    |  -0.326 |  -0.331 |        -0.153 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 65 |
| `llm` | 63 |
| `ai-agents` | 60 |
| `python` | 60 |
| `claude` | 55 |
| `codex` | 54 |
| `ai` | 45 |
| `typescript` | 44 |
| `manga-downloader` | 44 |
| `claude-opus` | 44 |
| `manga` | 43 |
| `mcp` | 36 |
| `cli` | 34 |
| `developer-tools` | 32 |
| `anthropic` | 31 |
| `macos` | 30 |
| `local-first` | 28 |
| `rust` | 27 |
| `windows` | 26 |
| `open-source` | 25 |
