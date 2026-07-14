# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 386.3 | 176.5 | 14211 |
| forks | 62.0 | 10.0 | 9474 |
| open_issues | 4.0 | 0.0 | 1188 |
| stars_per_day | 31.8 | 10.4 | 891 |
| age_days | 16.1 | 15.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `baidu/Unlimited-OCR` | 14211 | 1194 | Python | Other |
| `langchain-ai/openwiki` | 10995 | 753 | TypeScript | AI/ML |
| `JustVugg/colibri` | 10696 | 843 | C | Game |
| `deepseek-ai/DeepSpec` | 6626 | 593 | Python | Other |
| `x4gKing/X4G` | 5084 | 9474 | Python | Other |
| `elder-plinius/T3MP3ST` | 4660 | 985 | TypeScript | AI/ML |
| `zhongerxin/Cowart` | 4543 | 344 | JavaScript | Other |
| `Yu9191/wloc` | 4508 | 849 | JavaScript | Other |
| `bikini/exploitarium` | 3907 | 1122 | Python | Security |
| `baairon/torlink` | 3558 | 234 | TypeScript | CLI/Tooling |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `JustVugg/colibri` | 891.3 | 10696 | 12d | Game |
| `littledivy/mimic` | 797.0 | 797 | 1d | Other |
| `mereyabdenbekuly-ctrl/clodex-ide` | 699.0 | 699 | 1d | Security |
| `withmarbleapp/os-taxonomy` | 595.2 | 2976 | 5d | Other |
| `baidu/Unlimited-OCR` | 568.4 | 14211 | 25d | Other |
| `x4gKing/X4G` | 564.9 | 5084 | 9d | Other |
| `langchain-ai/openwiki` | 523.6 | 10995 | 21d | AI/ML |
| `x4gKing/Marzban-Panel` | 518.0 | 518 | 1d | Other |
| `x4gKing/Marzban-Node` | 431.0 | 431 | 1d | Other |
| `elder-plinius/T3MP3ST` | 423.6 | 4660 | 11d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 388 | 402 | 204 | 50 | 30.8 | 3.5 |
| Web | 239 | 178 | 151 | 17 | 14.1 | 0.5 |
| Other | 223 | 564 | 286 | 145 | 49.6 | 9.5 |
| Data | 34 | 254 | 151 | 11 | 14.8 | 1.5 |
| Mobile | 21 | 453 | 262 | 39 | 37.9 | 6.0 |
| Finance/Trading | 20 | 215 | 152 | 60 | 15.5 | 0.3 |
| CLI/Tooling | 19 | 533 | 193 | 39 | 35.4 | 1.5 |
| Game | 19 | 811 | 225 | 60 | 76.9 | 5.8 |
| Security | 19 | 452 | 199 | 91 | 63.2 | 3.9 |
| DevOps | 18 | 301 | 182 | 16 | 27.7 | 1.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.382 |         0.134 |      0.07  |
| forks       |   0.382 |   1     |         0.037 |     -0.043 |
| open_issues |   0.134 |   0.037 |         1     |      0.021 |
| age_days    |   0.07  |  -0.043 |         0.021 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.763 |         0.57  |      0.135 |
| forks       |   0.763 |   1     |         0.632 |      0.146 |
| open_issues |   0.57  |   0.632 |         1     |      0.15  |
| age_days    |   0.135 |   0.146 |         0.15  |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 69 |
| `llm` | 65 |
| `ai-agents` | 65 |
| `claude` | 56 |
| `python` | 49 |
| `claude-opus` | 48 |
| `manga` | 47 |
| `manga-downloader` | 47 |
| `ai` | 46 |
| `codex` | 41 |
| `typescript` | 40 |
| `anthropic` | 37 |
| `developer-tools` | 36 |
| `cli` | 31 |
| `mcp` | 30 |
| `open-source` | 28 |
| `hentai` | 27 |
| `macos` | 26 |
| `manga-reader` | 26 |
| `agent-skills` | 24 |
