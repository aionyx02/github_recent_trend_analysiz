# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 391.7 | 181.0 | 14264 |
| forks | 62.3 | 10.0 | 9865 |
| open_issues | 4.0 | 0.0 | 1200 |
| stars_per_day | 32.1 | 11.7 | 1026 |
| age_days | 16.3 | 16.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `baidu/Unlimited-OCR` | 14264 | 1197 | Python | Other |
| `JustVugg/colibri` | 13335 | 1101 | C | Game |
| `langchain-ai/openwiki` | 11404 | 787 | TypeScript | AI/ML |
| `deepseek-ai/DeepSpec` | 6652 | 600 | Python | Other |
| `x4gKing/X4G` | 5335 | 9865 | Python | Other |
| `elder-plinius/T3MP3ST` | 4739 | 998 | TypeScript | AI/ML |
| `Yu9191/wloc` | 4649 | 883 | JavaScript | Other |
| `zhongerxin/Cowart` | 4625 | 350 | JavaScript | Other |
| `bikini/exploitarium` | 3917 | 1130 | Python | Security |
| `baairon/torlink` | 3596 | 236 | TypeScript | CLI/Tooling |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `JustVugg/colibri` | 1025.8 | 13335 | 13d | Game |
| `littledivy/mimic` | 919.0 | 919 | 1d | Other |
| `baidu/Unlimited-OCR` | 548.6 | 14264 | 26d | Other |
| `x4gKing/X4G` | 533.5 | 5335 | 10d | Other |
| `langchain-ai/openwiki` | 518.4 | 11404 | 22d | AI/ML |
| `withmarbleapp/os-taxonomy` | 513.5 | 3081 | 6d | Other |
| `mereyabdenbekuly-ctrl/clodex-ide` | 401.5 | 803 | 2d | Security |
| `elder-plinius/T3MP3ST` | 394.9 | 4739 | 12d | AI/ML |
| `MDX-Tom/gpt-5.6-instruct` | 374.3 | 1123 | 3d | AI/ML |
| `deepseek-ai/DeepSpec` | 369.6 | 6652 | 18d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 384 | 409 | 211 | 51 | 30.9 | 3.5 |
| Web | 236 | 181 | 151 | 19 | 13.1 | 0.5 |
| Other | 221 | 568 | 287 | 145 | 52.4 | 9.7 |
| Data | 33 | 246 | 151 | 9 | 13.8 | 1.4 |
| Game | 24 | 793 | 190 | 60 | 68.7 | 4.3 |
| Finance/Trading | 23 | 223 | 154 | 49 | 23.0 | 0.3 |
| CLI/Tooling | 21 | 525 | 192 | 37 | 39.9 | 2.1 |
| Mobile | 21 | 460 | 260 | 41 | 43.1 | 6.2 |
| Security | 21 | 429 | 178 | 83 | 44.3 | 1.0 |
| DevOps | 16 | 291 | 164 | 12 | 17.0 | 1.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.39  |         0.129 |      0.062 |
| forks       |   0.39  |   1     |         0.036 |     -0.047 |
| open_issues |   0.129 |   0.036 |         1     |      0.023 |
| age_days    |   0.062 |  -0.047 |         0.023 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.808 |         0.601 |      0.105 |
| forks       |   0.808 |   1     |         0.619 |      0.102 |
| open_issues |   0.601 |   0.619 |         1     |      0.134 |
| age_days    |   0.105 |   0.102 |         0.134 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 67 |
| `llm` | 66 |
| `claude-code` | 64 |
| `claude` | 54 |
| `python` | 50 |
| `claude-opus` | 49 |
| `ai` | 47 |
| `manga` | 45 |
| `manga-downloader` | 45 |
| `typescript` | 41 |
| `codex` | 40 |
| `anthropic` | 36 |
| `developer-tools` | 34 |
| `cli` | 33 |
| `mcp` | 30 |
| `macos` | 28 |
| `open-source` | 27 |
| `hentai` | 27 |
| `manga-reader` | 25 |
| `react` | 23 |
