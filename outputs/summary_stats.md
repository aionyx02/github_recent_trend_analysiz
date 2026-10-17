# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 963.6 | 344.0 | 65509 |
| forks | 152.2 | 35.0 | 11425 |
| open_issues | 30.8 | 3.0 | 2557 |
| stars_per_day | 79.1 | 25.0 | 4094 |
| age_days | 17.2 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `storytold/photocraft` | 65509 | 11425 | Rust | Other |
| `NandhaKishorM/laya` | 33215 | 2984 | Python | AI/ML |
| `Niko1221/Strata` | 26541 | 2771 | C++ | AI/ML |
| `Ebony-Vinyl/dsh-our-free-model` | 20430 | 427 | JavaScript | AI/ML |
| `storytold/pdfcraft` | 15199 | 5826 | Rust | Other |
| `openai/math` | 15063 | 1739 | Lean | Other |
| `yetone/magpie` | 14518 | 1032 | Go | AI/ML |
| `wheresryan22/anatomy` | 14421 | 1101 | JavaScript | AI/ML |
| `storytold/filmcraft` | 14354 | 5923 | Rust | Other |
| `storytold/wordcraft` | 13810 | 3592 | Rust | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `storytold/photocraft` | 4094.3 | 65509 | 16d | Other |
| `wheresryan22/anatomy` | 1802.6 | 14421 | 8d | AI/ML |
| `chenglou/handwired` | 1632.0 | 1632 | 1d | AI/ML |
| `storytold/wordcraft` | 1534.4 | 13810 | 9d | Other |
| `openai/math` | 1506.3 | 15063 | 10d | Other |
| `Niko1221/Strata` | 1206.4 | 26541 | 22d | AI/ML |
| `NandhaKishorM/laya` | 1186.2 | 33215 | 28d | AI/ML |
| `Supermedo/uncharted_pc` | 1118.0 | 1118 | 1d | Other |
| `feder-cr/git-ai` | 1096.0 | 1096 | 1d | AI/ML |
| `storytold/pdfcraft` | 949.9 | 15199 | 16d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 401 | 1042 | 360 | 124 | 79.4 | 17.4 |
| Other | 388 | 977 | 311 | 206 | 86.4 | 49.3 |
| Web | 62 | 766 | 349 | 116 | 52.4 | 12.9 |
| Mobile | 62 | 874 | 376 | 92 | 72.9 | 28.7 |
| Game | 29 | 903 | 386 | 183 | 114.5 | 59.0 |
| CLI/Tooling | 17 | 569 | 235 | 64 | 47.4 | 3.5 |
| Data | 15 | 1047 | 571 | 86 | 61.9 | 13.5 |
| Finance/Trading | 14 | 411 | 296 | 70 | 30.5 | 4.3 |
| DevOps | 6 | 446 | 251 | 39 | 19.8 | 5.8 |
| Security | 6 | 854 | 577 | 156 | 68.6 | 5.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.826 |         0.671 |      0.022 |
| forks       |   0.826 |   1     |         0.76  |     -0.027 |
| open_issues |   0.671 |   0.76  |         1     |     -0.037 |
| age_days    |   0.022 |  -0.027 |        -0.037 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.66  |         0.357 |      0.031 |
| forks       |   0.66  |   1     |         0.357 |      0.034 |
| open_issues |   0.357 |   0.357 |         1     |     -0.022 |
| age_days    |   0.031 |   0.034 |        -0.022 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 97 |
| `ai-agents` | 74 |
| `llm` | 74 |
| `macos` | 63 |
| `codex` | 62 |
| `jev` | 41 |
| `mcp` | 41 |
| `windows` | 40 |
| `agent-skills` | 38 |
| `developer-tools` | 37 |
| `python` | 36 |
| `rust` | 35 |
| `claude` | 34 |
| `ai` | 33 |
| `typescript` | 33 |
| `open-source` | 30 |
| `ai-agent` | 29 |
| `linux` | 28 |
| `awesome-list` | 26 |
| `react` | 25 |
