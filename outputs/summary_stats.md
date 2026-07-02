# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 491.2 | 235.5 | 71046 |
| forks | 51.9 | 8.5 | 3665 |
| open_issues | 8.2 | 0.0 | 3604 |
| stars_per_day | 95.9 | 46.3 | 3739 |
| age_days | 11.7 | 9.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `DietrichGebert/ponytail` | 71046 | 3665 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 12934 | 1033 | Python | Other |
| `XiaomiMiMo/MiMo-Code` | 11253 | 1099 | TypeScript | AI/ML |
| `unicity-astrid/book` | 7536 | 31 | Perl | Security |
| `unicity-astrid/handbook` | 7484 | 42 | Unknown | Other |
| `XxHuberrr/Mineradio` | 6647 | 492 | HTML | Web |
| `shadcn/improve` | 6557 | 270 | Unknown | Other |
| `omnigent-ai/omnigent` | 5988 | 762 | Python | AI/ML |
| `deepseek-ai/DeepSpec` | 5823 | 470 | Python | Other |
| `cobusgreyling/loop-engineering` | 4758 | 603 | JavaScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 3739.3 | 71046 | 19d | AI/ML |
| `deepseek-ai/DeepSpec` | 1164.6 | 5823 | 5d | Other |
| `baidu/Unlimited-OCR` | 994.9 | 12934 | 13d | Other |
| `mekos2772/ios-location-spoofer` | 909.0 | 909 | 1d | Mobile |
| `TianhangZhuzth/Fundamental-Ava` | 731.0 | 731 | 1d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 535.9 | 11253 | 21d | AI/ML |
| `Krishnagangwal/CS-Fundamentals` | 457.7 | 1373 | 3d | Data |
| `bikini/exploitarium` | 422.1 | 3377 | 8d | Security |
| `baairon/torlink` | 397.7 | 2386 | 6d | CLI/Tooling |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 357.0 | 1071 | 3d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 416 | 387 | 240 | 25 | 138.2 | 2.6 |
| AI/ML | 313 | 709 | 259 | 66 | 54.9 | 8.4 |
| Web | 96 | 354 | 151 | 27 | 51.8 | 40.9 |
| Game | 36 | 243 | 254 | 2 | 172.1 | 0.4 |
| Data | 29 | 349 | 219 | 46 | 94.8 | 2.6 |
| Mobile | 27 | 555 | 243 | 49 | 78.0 | 8.5 |
| Finance/Trading | 25 | 260 | 230 | 471 | 49.8 | 0.2 |
| CLI/Tooling | 24 | 455 | 237 | 33 | 67.2 | 4.7 |
| Security | 23 | 868 | 271 | 114 | 80.5 | 4.4 |
| DevOps | 11 | 292 | 205 | 17 | 45.1 | 5.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.617 |         0.074 |      0.086 |
| forks       |   0.617 |   1     |         0.122 |      0.107 |
| open_issues |   0.074 |   0.122 |         1     |      0.086 |
| age_days    |   0.086 |   0.107 |         0.086 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.522 |         0.384 |      0.216 |
| forks       |   0.522 |   1     |         0.637 |      0.692 |
| open_issues |   0.384 |   0.637 |         1     |      0.553 |
| age_days    |   0.216 |   0.692 |         0.553 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 49 |
| `ai-agents` | 44 |
| `ai` | 43 |
| `llm` | 41 |
| `claude` | 36 |
| `codex` | 33 |
| `python` | 29 |
| `typescript` | 26 |
| `claude-opus` | 24 |
| `anthropic` | 22 |
| `ai-agent` | 21 |
| `open-source` | 21 |
| `macos` | 21 |
| `developer-tools` | 19 |
| `cli` | 18 |
| `mcp` | 18 |
| `agent-skills` | 17 |
| `prompt-engineering` | 15 |
| `react` | 15 |
| `skills` | 13 |
