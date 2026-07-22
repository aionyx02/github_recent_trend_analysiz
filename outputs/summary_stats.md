# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 440.2 | 199.0 | 21599 |
| forks | 84.6 | 15.0 | 11509 |
| open_issues | 4.1 | 0.0 | 1194 |
| stars_per_day | 36.1 | 11.9 | 3086 |
| age_days | 19.1 | 23.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `xai-org/grok-build` | 21599 | 4033 | Rust | AI/ML |
| `JustVugg/colibri` | 17684 | 1681 | C | Game |
| `langchain-ai/openwiki` | 12831 | 889 | TypeScript | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 11684 | 1180 | JavaScript | AI/ML |
| `deepseek-ai/DeepSpec` | 6732 | 623 | Python | Other |
| `x4gKing/X4G` | 6283 | 11509 | Python | Other |
| `unicity-aos/aos-ce` | 6090 | 4 | Rust | AI/ML |
| `Yu9191/wloc` | 6061 | 1192 | JavaScript | Other |
| `elder-plinius/T3MP3ST` | 5080 | 1048 | TypeScript | AI/ML |
| `oso95/scroll-world` | 4757 | 547 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `xai-org/grok-build` | 3085.6 | 21599 | 7d | AI/ML |
| `Fei-Away/Codex-Dream-Skin` | 1947.3 | 11684 | 6d | AI/ML |
| `JustVugg/colibri` | 884.2 | 17684 | 20d | Game |
| `unicity-aos/aos-ce` | 676.7 | 6090 | 9d | AI/ML |
| `Blaizzy/nativ` | 671.0 | 671 | 1d | AI/ML |
| `lopopolo/harness-engineering` | 639.0 | 1917 | 3d | AI/ML |
| `langchain-ai/openwiki` | 442.4 | 12831 | 29d | AI/ML |
| `powerycy/goutoujunshi` | 409.0 | 409 | 1d | AI/ML |
| `x4gKing/X4G` | 369.6 | 6283 | 17d | Other |
| `oso95/scroll-world` | 317.1 | 4757 | 15d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 390 | 518 | 228 | 61 | 51.3 | 3.4 |
| Other | 233 | 520 | 261 | 149 | 37.6 | 9.4 |
| Web | 213 | 199 | 152 | 19 | 11.2 | 1.0 |
| Mobile | 31 | 422 | 233 | 40 | 35.9 | 4.9 |
| Finance/Trading | 30 | 237 | 194 | 508 | 20.6 | 0.3 |
| CLI/Tooling | 28 | 493 | 241 | 44 | 35.5 | 2.5 |
| Data | 27 | 234 | 151 | 9 | 10.2 | 0.4 |
| Game | 18 | 1298 | 266 | 117 | 67.4 | 6.8 |
| Security | 18 | 493 | 200 | 109 | 33.2 | 0.9 |
| DevOps | 12 | 190 | 164 | 7 | 11.7 | 0.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.443 |         0.109 |     -0.056 |
| forks       |   0.443 |   1     |         0.03  |     -0.055 |
| open_issues |   0.109 |   0.03  |         1     |      0.011 |
| age_days    |  -0.056 |  -0.055 |         0.011 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.806 |         0.581 |     -0.229 |
| forks       |   0.806 |   1     |         0.565 |     -0.23  |
| open_issues |   0.581 |   0.565 |         1     |     -0.075 |
| age_days    |  -0.229 |  -0.23  |        -0.075 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `llm` | 66 |
| `claude-code` | 63 |
| `python` | 61 |
| `ai-agents` | 60 |
| `claude` | 54 |
| `codex` | 50 |
| `ai` | 47 |
| `typescript` | 45 |
| `manga` | 43 |
| `manga-downloader` | 43 |
| `claude-opus` | 42 |
| `mcp` | 35 |
| `cli` | 33 |
| `macos` | 31 |
| `developer-tools` | 31 |
| `anthropic` | 31 |
| `local-first` | 28 |
| `rust` | 27 |
| `android` | 27 |
| `ai-agent` | 25 |
