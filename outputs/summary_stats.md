# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 458.1 | 174.0 | 74215 |
| forks | 53.0 | 8.0 | 3901 |
| open_issues | 4.6 | 0.0 | 715 |
| stars_per_day | 38.4 | 25.2 | 3373 |
| age_days | 13.5 | 11.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `DietrichGebert/ponytail` | 74215 | 3901 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 13297 | 1078 | Python | Other |
| `XiaomiMiMo/MiMo-Code` | 11434 | 1117 | TypeScript | AI/ML |
| `unicity-astrid/book` | 7535 | 31 | Perl | Security |
| `unicity-astrid/handbook` | 7482 | 42 | Unknown | Other |
| `shadcn/improve` | 6886 | 276 | Unknown | Other |
| `omnigent-ai/omnigent` | 6266 | 818 | Python | AI/ML |
| `deepseek-ai/DeepSpec` | 6207 | 527 | Python | Other |
| `cobusgreyling/loop-engineering` | 5732 | 755 | JavaScript | AI/ML |
| `zhongerxin/Cowart` | 3831 | 298 | JavaScript | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 3373.4 | 74215 | 22d | AI/ML |
| `baidu/Unlimited-OCR` | 831.1 | 13297 | 16d | Other |
| `jamesob/local-llm` | 812.0 | 812 | 1d | CLI/Tooling |
| `deepseek-ai/DeepSpec` | 775.9 | 6207 | 8d | Other |
| `xuchonglang/investing-for-beginners` | 673.0 | 673 | 1d | Other |
| `Kulaxyz/token-diet` | 528.0 | 528 | 1d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 476.4 | 11434 | 24d | AI/ML |
| `ammaarreshi/Generals-Mac-iOS-iPad` | 466.0 | 466 | 1d | Mobile |
| `bikini/exploitarium` | 332.9 | 3662 | 11d | Security |
| `baairon/torlink` | 332.9 | 2996 | 9d | CLI/Tooling |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 386 | 616 | 200 | 73 | 43.3 | 7.5 |
| Web | 244 | 175 | 151 | 5 | 24.6 | 0.2 |
| Other | 211 | 540 | 245 | 75 | 44.2 | 4.9 |
| Data | 38 | 283 | 151 | 31 | 31.1 | 2.0 |
| Mobile | 25 | 482 | 238 | 30 | 61.2 | 7.8 |
| CLI/Tooling | 23 | 490 | 221 | 38 | 70.4 | 5.8 |
| Security | 20 | 863 | 204 | 122 | 48.8 | 4.5 |
| DevOps | 19 | 260 | 191 | 10 | 21.6 | 4.2 |
| Finance/Trading | 19 | 200 | 151 | 124 | 23.3 | 0.2 |
| Game | 15 | 229 | 195 | 9 | 17.0 | 1.6 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.619 |         0.32  |      0.094 |
| forks       |   0.619 |   1     |         0.295 |      0.08  |
| open_issues |   0.32  |   0.295 |         1     |      0.141 |
| age_days    |   0.094 |   0.08  |         0.141 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.744 |         0.533 |      0.545 |
| forks       |   0.744 |   1     |         0.608 |      0.6   |
| open_issues |   0.533 |   0.608 |         1     |      0.469 |
| age_days    |   0.545 |   0.6   |         0.469 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 64 |
| `llm` | 57 |
| `ai-agents` | 56 |
| `claude` | 55 |
| `ai` | 52 |
| `claude-opus` | 50 |
| `manga-downloader` | 47 |
| `manga` | 46 |
| `python` | 45 |
| `anthropic` | 39 |
| `typescript` | 38 |
| `codex` | 34 |
| `open-source` | 34 |
| `macos` | 32 |
| `cli` | 31 |
| `developer-tools` | 30 |
| `android` | 29 |
| `hentai` | 28 |
| `video-download-tool` | 28 |
| `mcp` | 25 |
