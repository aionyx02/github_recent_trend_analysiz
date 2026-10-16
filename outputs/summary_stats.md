# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 1009.5 | 348.0 | 64162 |
| forks | 160.8 | 35.0 | 11167 |
| open_issues | 29.2 | 3.0 | 2276 |
| stars_per_day | 84.2 | 24.9 | 4277 |
| age_days | 17.2 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `storytold/photocraft` | 64162 | 11167 | Rust | Other |
| `NandhaKishorM/laya` | 33112 | 2975 | Python | AI/ML |
| `Niko1221/Strata` | 25892 | 2675 | C++ | AI/ML |
| `browser-use/jev-ultrafast` | 23058 | 1717 | Python | AI/ML |
| `Ebony-Vinyl/dsh-our-free-model` | 18696 | 383 | JavaScript | AI/ML |
| `robbietilton/Compositor` | 17146 | 1678 | Swift | Mobile |
| `openai/math` | 14990 | 1721 | Lean | Other |
| `storytold/pdfcraft` | 14690 | 5685 | Rust | Other |
| `storytold/filmcraft` | 14018 | 5780 | Rust | Other |
| `yetone/magpie` | 13946 | 974 | Go | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `storytold/photocraft` | 4277.5 | 64162 | 15d | Other |
| `wheresryan22/anatomy` | 1926.3 | 13484 | 7d | AI/ML |
| `storytold/wordcraft` | 1679.2 | 13434 | 8d | Other |
| `openai/math` | 1665.6 | 14990 | 9d | Other |
| `ahwootech/BRUTAL` | 1352.0 | 1352 | 1d | Game |
| `chenglou/handwired` | 1330.0 | 1330 | 1d | AI/ML |
| `Niko1221/Strata` | 1233.0 | 25892 | 21d | AI/ML |
| `NandhaKishorM/laya` | 1226.4 | 33112 | 27d | AI/ML |
| `Arekejoker/qwen21-nsfw-pose-skill` | 1164.0 | 2328 | 2d | AI/ML |
| `jhaizhou-ops/d2r-mobile` | 1140.0 | 3420 | 3d | Mobile |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 400 | 1089 | 355 | 143 | 86.3 | 17.7 |
| Other | 391 | 979 | 320 | 201 | 85.7 | 45.3 |
| Web | 62 | 752 | 339 | 112 | 52.9 | 12.0 |
| Mobile | 62 | 1202 | 380 | 133 | 95.6 | 27.5 |
| Game | 25 | 955 | 357 | 200 | 155.6 | 60.6 |
| Data | 17 | 941 | 431 | 77 | 58.6 | 11.2 |
| Finance/Trading | 17 | 752 | 302 | 85 | 46.1 | 7.8 |
| CLI/Tooling | 15 | 682 | 376 | 79 | 52.3 | 6.3 |
| DevOps | 6 | 431 | 238 | 37 | 20.1 | 5.2 |
| Security | 5 | 922 | 713 | 153 | 88.4 | 3.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.785 |         0.635 |      0.03  |
| forks       |   0.785 |   1     |         0.7   |     -0.045 |
| open_issues |   0.635 |   0.7   |         1     |     -0.052 |
| age_days    |   0.03  |  -0.045 |        -0.052 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.673 |         0.383 |      0.026 |
| forks       |   0.673 |   1     |         0.39  |      0.024 |
| open_issues |   0.383 |   0.39  |         1     |     -0.03  |
| age_days    |   0.026 |   0.024 |        -0.03  |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 94 |
| `ai-agents` | 74 |
| `llm` | 71 |
| `macos` | 62 |
| `codex` | 59 |
| `jev` | 41 |
| `agent-skills` | 38 |
| `developer-tools` | 36 |
| `mcp` | 36 |
| `windows` | 36 |
| `rust` | 34 |
| `ai` | 34 |
| `typescript` | 34 |
| `claude` | 33 |
| `python` | 31 |
| `open-source` | 31 |
| `ai-agent` | 29 |
| `awesome-list` | 26 |
| `linux` | 26 |
| `react` | 26 |
