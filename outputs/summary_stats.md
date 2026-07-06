# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 487.7 | 182.0 | 75440 |
| forks | 48.6 | 4.0 | 3997 |
| open_issues | 4.3 | 0.0 | 723 |
| stars_per_day | 34.7 | 10.1 | 3280 |
| age_days | 17.8 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `DietrichGebert/ponytail` | 75440 | 3997 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 13436 | 1089 | Python | Other |
| `XiaomiMiMo/MiMo-Code` | 11506 | 1126 | TypeScript | AI/ML |
| `unicity-astrid/book` | 7534 | 31 | Perl | Security |
| `unicity-astrid/handbook` | 7480 | 42 | Unknown | Other |
| `shadcn/improve` | 6964 | 284 | Unknown | Other |
| `omnigent-ai/omnigent` | 6352 | 829 | Python | AI/ML |
| `langchain-ai/openwiki` | 6309 | 423 | TypeScript | AI/ML |
| `deepseek-ai/DeepSpec` | 6286 | 541 | Python | Other |
| `cobusgreyling/loop-engineering` | 6109 | 787 | JavaScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 3280.0 | 75440 | 23d | AI/ML |
| `ammaarreshi/Generals-Mac-iOS-iPad` | 954.0 | 954 | 1d | Mobile |
| `baidu/Unlimited-OCR` | 790.4 | 13436 | 17d | Other |
| `elder-plinius/T3MP3ST` | 706.7 | 2120 | 3d | AI/ML |
| `deepseek-ai/DeepSpec` | 698.4 | 6286 | 9d | Other |
| `CalmNoteDepot/MECCHA-CHAMELEON-VISION-ULTIMATE` | 533.0 | 533 | 1d | Other |
| `jamesob/local-llm` | 488.5 | 977 | 2d | CLI/Tooling |
| `langchain-ai/openwiki` | 485.3 | 6309 | 13d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 460.2 | 11506 | 25d | AI/ML |
| `514-labs/dnsglobe` | 421.0 | 421 | 1d | CLI/Tooling |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Web | 388 | 194 | 182 | 2 | 11.3 | 0.1 |
| AI/ML | 280 | 834 | 295 | 87 | 54.3 | 9.8 |
| Other | 184 | 618 | 276 | 85 | 50.1 | 5.5 |
| Security | 37 | 546 | 182 | 62 | 28.6 | 2.2 |
| Data | 35 | 320 | 182 | 33 | 20.7 | 2.1 |
| Mobile | 23 | 550 | 266 | 36 | 80.5 | 9.1 |
| CLI/Tooling | 18 | 618 | 345 | 47 | 90.2 | 4.2 |
| DevOps | 15 | 316 | 197 | 13 | 17.0 | 5.5 |
| Game | 12 | 258 | 200 | 11 | 17.7 | 1.8 |
| Finance/Trading | 8 | 287 | 280 | 295 | 16.8 | 0.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.66  |         0.336 |      0.052 |
| forks       |   0.66  |   1     |         0.327 |     -0.023 |
| open_issues |   0.336 |   0.327 |         1     |      0.084 |
| age_days    |   0.052 |  -0.023 |         0.084 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.741 |         0.542 |      0.057 |
| forks       |   0.741 |   1     |         0.67  |      0.056 |
| open_issues |   0.542 |   0.67  |         1     |      0.064 |
| age_days    |   0.057 |   0.056 |         0.064 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `ai-agents` | 39 |
| `claude-code` | 37 |
| `ai` | 33 |
| `llm` | 30 |
| `codex` | 27 |
| `claude` | 23 |
| `macos` | 22 |
| `mcp` | 17 |
| `typescript` | 17 |
| `open-source` | 17 |
| `agent-skills` | 16 |
| `cli` | 16 |
| `ai-agent` | 16 |
| `developer-tools` | 15 |
| `swift` | 13 |
| `react` | 12 |
| `prompt-engineering` | 11 |
| `gilisoft` | 11 |
| `gilisoft-download` | 11 |
| `gilisoft-install` | 11 |
