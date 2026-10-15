# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 990.6 | 343.5 | 62167 |
| forks | 157.4 | 34.0 | 10730 |
| open_issues | 26.5 | 3.0 | 2040 |
| stars_per_day | 84.0 | 24.6 | 4440 |
| age_days | 17.1 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `storytold/photocraft` | 62167 | 10730 | Rust | Other |
| `NandhaKishorM/laya` | 32989 | 2961 | Python | AI/ML |
| `Niko1221/Strata` | 25032 | 2565 | C++ | AI/ML |
| `browser-use/jev-ultrafast` | 22969 | 1707 | Python | AI/ML |
| `Ebony-Vinyl/dsh-our-free-model` | 17242 | 343 | JavaScript | AI/ML |
| `robbietilton/Compositor` | 17009 | 1657 | Swift | Mobile |
| `openai/math` | 14870 | 1699 | Lean | Other |
| `storytold/pdfcraft` | 14058 | 5410 | Rust | Other |
| `storytold/filmcraft` | 13561 | 5564 | Rust | Other |
| `yetone/magpie` | 13237 | 918 | Go | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `storytold/photocraft` | 4440.5 | 62167 | 14d | Other |
| `wheresryan22/anatomy` | 1986.0 | 11916 | 6d | AI/ML |
| `openai/math` | 1858.8 | 14870 | 8d | Other |
| `storytold/wordcraft` | 1826.3 | 12784 | 7d | Other |
| `Arekejoker/qwen21-nsfw-pose-skill` | 1704.0 | 1704 | 1d | AI/ML |
| `jhaizhou-ops/d2r-mobile` | 1342.0 | 2684 | 2d | Mobile |
| `NandhaKishorM/laya` | 1268.8 | 32989 | 26d | AI/ML |
| `Niko1221/Strata` | 1251.6 | 25032 | 20d | AI/ML |
| `storytold/pdfcraft` | 1004.1 | 14058 | 14d | Other |
| `storytold/filmcraft` | 968.6 | 13561 | 14d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 398 | 1075 | 350 | 145 | 85.8 | 17.2 |
| Other | 392 | 958 | 324 | 191 | 86.4 | 39.9 |
| Web | 64 | 719 | 332 | 108 | 59.4 | 11.7 |
| Mobile | 62 | 1209 | 374 | 132 | 96.5 | 24.7 |
| Game | 25 | 866 | 303 | 188 | 114.5 | 53.4 |
| CLI/Tooling | 18 | 603 | 340 | 67 | 50.1 | 5.3 |
| Finance/Trading | 17 | 744 | 288 | 84 | 57.4 | 7.5 |
| Data | 16 | 975 | 497 | 79 | 63.8 | 10.3 |
| DevOps | 4 | 527 | 260 | 25 | 26.5 | 6.2 |
| Security | 4 | 836 | 470 | 180 | 76.7 | 3.5 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.782 |         0.6   |      0.023 |
| forks       |   0.782 |   1     |         0.664 |     -0.051 |
| open_issues |   0.6   |   0.664 |         1     |     -0.063 |
| age_days    |   0.023 |  -0.051 |        -0.063 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.68  |         0.384 |      0.03  |
| forks       |   0.68  |   1     |         0.393 |      0.022 |
| open_issues |   0.384 |   0.393 |         1     |     -0.009 |
| age_days    |   0.03  |   0.022 |        -0.009 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 89 |
| `llm` | 70 |
| `ai-agents` | 67 |
| `macos` | 62 |
| `codex` | 57 |
| `jev` | 42 |
| `agent-skills` | 39 |
| `windows` | 36 |
| `rust` | 35 |
| `developer-tools` | 34 |
| `mcp` | 34 |
| `python` | 32 |
| `ai` | 32 |
| `typescript` | 32 |
| `claude` | 30 |
| `open-source` | 28 |
| `awesome-list` | 28 |
| `ai-agent` | 28 |
| `linux` | 26 |
| `react` | 24 |
