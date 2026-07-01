# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 469.5 | 213.0 | 69771 |
| forks | 46.4 | 7.5 | 3597 |
| open_issues | 7.6 | 0.0 | 3020 |
| stars_per_day | 73.2 | 49.5 | 3876 |
| age_days | 11.6 | 9.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `DietrichGebert/ponytail` | 69771 | 3597 | JavaScript | AI/ML |
| `baidu/Unlimited-OCR` | 12677 | 997 | Python | Other |
| `XiaomiMiMo/MiMo-Code` | 11162 | 1088 | TypeScript | AI/ML |
| `unicity-astrid/book` | 7536 | 31 | Perl | Security |
| `unicity-astrid/handbook` | 7484 | 42 | Unknown | Other |
| `shadcn/improve` | 6480 | 269 | Unknown | Other |
| `XxHuberrr/Mineradio` | 6201 | 469 | HTML | Web |
| `omnigent-ai/omnigent` | 5857 | 742 | Python | AI/ML |
| `deepseek-ai/DeepSpec` | 5640 | 448 | Python | Other |
| `cobusgreyling/loop-engineering` | 4565 | 583 | JavaScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 3876.2 | 69771 | 18d | AI/ML |
| `deepseek-ai/DeepSpec` | 1410.0 | 5640 | 4d | Other |
| `baidu/Unlimited-OCR` | 1056.4 | 12677 | 12d | Other |
| `TianhangZhuzth/Fundamental-Ava` | 665.0 | 665 | 1d | AI/ML |
| `Krishnagangwal/CS-Fundamentals` | 634.0 | 1268 | 2d | Data |
| `XiaomiMiMo/MiMo-Code` | 558.1 | 11162 | 20d | AI/ML |
| `yynxxxxx/Codex-5.5-codex-instruct-5.5` | 464.0 | 928 | 2d | Other |
| `bikini/exploitarium` | 440.3 | 3082 | 7d | Security |
| `baairon/torlink` | 394.2 | 1971 | 5d | CLI/Tooling |
| `Yu9191/wloc` | 361.2 | 2167 | 6d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 347 | 648 | 229 | 57 | 58.9 | 7.7 |
| Other | 286 | 447 | 220 | 37 | 95.9 | 3.6 |
| Web | 193 | 245 | 152 | 12 | 69.8 | 17.3 |
| Data | 36 | 308 | 152 | 40 | 89.5 | 2.2 |
| Mobile | 29 | 501 | 223 | 66 | 43.1 | 7.2 |
| CLI/Tooling | 27 | 417 | 222 | 28 | 62.1 | 4.0 |
| Finance/Trading | 27 | 231 | 215 | 246 | 65.4 | 0.2 |
| Security | 25 | 781 | 223 | 104 | 79.1 | 4.4 |
| Game | 16 | 225 | 204 | 5 | 83.4 | 0.8 |
| DevOps | 14 | 246 | 172 | 12 | 45.6 | 4.3 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.686 |         0.09  |      0.087 |
| forks       |   0.686 |   1     |         0.151 |      0.126 |
| open_issues |   0.09  |   0.151 |         1     |      0.087 |
| age_days    |   0.087 |   0.126 |         0.087 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.737 |         0.518 |      0.501 |
| forks       |   0.737 |   1     |         0.636 |      0.71  |
| open_issues |   0.518 |   0.636 |         1     |      0.551 |
| age_days    |   0.501 |   0.71  |         0.551 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 56 |
| `ai` | 50 |
| `ai-agents` | 49 |
| `llm` | 49 |
| `python` | 43 |
| `claude` | 42 |
| `claude-opus` | 39 |
| `manga-downloader` | 39 |
| `manga` | 35 |
| `codex` | 31 |
| `anthropic` | 31 |
| `typescript` | 31 |
| `open-source` | 26 |
| `macos` | 25 |
| `cli` | 24 |
| `android` | 23 |
| `developer-tools` | 22 |
| `ai-agent` | 20 |
| `agent-skills` | 19 |
| `mcp` | 19 |
