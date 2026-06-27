# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 504.5 | 175.5 | 78306 |
| forks | 66.2 | 17.0 | 10210 |
| open_issues | 8.4 | 1.0 | 1893 |
| stars_per_day | 37.4 | 12.4 | 4330 |
| age_days | 17.4 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 78306 | 10210 | Python | AI/ML |
| `DietrichGebert/ponytail` | 60620 | 3098 | JavaScript | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 10893 | 1042 | TypeScript | AI/ML |
| `baidu/Unlimited-OCR` | 10692 | 808 | Python | Other |
| `unicity-astrid/book` | 7558 | 31 | Perl | Security |
| `unicity-astrid/handbook` | 7506 | 42 | Unknown | Other |
| `shadcn/improve` | 6284 | 251 | Unknown | Other |
| `StarTrail-org/PixelRAG` | 5434 | 426 | Python | AI/ML |
| `zgwl/chinese-buy-us-stock-guide` | 5316 | 792 | Unknown | Other |
| `omnigent-ai/omnigent` | 5037 | 619 | Python | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 4330.0 | 60620 | 14d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 3011.8 | 78306 | 26d | AI/ML |
| `baidu/Unlimited-OCR` | 1336.5 | 10692 | 8d | Other |
| `bozhouDev/codex-orange-book` | 723.0 | 2169 | 3d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 680.8 | 10893 | 16d | AI/ML |
| `winsznx/theeleven` | 535.0 | 535 | 1d | AI/ML |
| `shadcn/improve` | 392.8 | 6284 | 16d | Other |
| `zhongerxin/Cowart` | 387.5 | 3100 | 8d | Other |
| `unicity-astrid/book` | 377.9 | 7558 | 20d | Security |
| `unicity-astrid/handbook` | 375.3 | 7506 | 20d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 420 | 708 | 193 | 77 | 48.8 | 9.8 |
| Other | 353 | 360 | 166 | 44 | 31.4 | 4.0 |
| Web | 61 | 396 | 169 | 38 | 22.7 | 34.2 |
| Mobile | 49 | 302 | 157 | 28 | 19.9 | 4.7 |
| CLI/Tooling | 33 | 299 | 168 | 25 | 20.2 | 5.2 |
| Security | 22 | 710 | 198 | 78 | 52.6 | 8.0 |
| Finance/Trading | 19 | 200 | 187 | 527 | 31.0 | 0.4 |
| Data | 18 | 365 | 212 | 80 | 26.5 | 5.3 |
| Game | 14 | 180 | 143 | 10 | 26.0 | 2.2 |
| DevOps | 11 | 241 | 185 | 27 | 19.0 | 5.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.857 |         0.501 |      0.028 |
| forks       |   0.857 |   1     |         0.562 |      0.001 |
| open_issues |   0.501 |   0.562 |         1     |      0.045 |
| age_days    |   0.028 |   0.001 |         0.045 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.548 |         0.346 |      0.083 |
| forks       |   0.548 |   1     |         0.339 |      0.009 |
| open_issues |   0.346 |   0.339 |         1     |      0.095 |
| age_days    |   0.083 |   0.009 |         0.095 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 64 |
| `llm` | 60 |
| `ai` | 57 |
| `ai-agents` | 56 |
| `codex` | 45 |
| `claude` | 36 |
| `ai-agent` | 30 |
| `macos` | 30 |
| `typescript` | 29 |
| `python` | 28 |
| `developer-tools` | 27 |
| `cli` | 26 |
| `mcp` | 25 |
| `agent-skills` | 24 |
| `open-source` | 22 |
| `anthropic` | 21 |
| `skills` | 20 |
| `prompt-engineering` | 18 |
| `agent` | 18 |
| `swift` | 18 |
