# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 958.3 | 330.0 | 59520 |
| forks | 151.8 | 33.0 | 10131 |
| open_issues | 24.5 | 2.0 | 1981 |
| stars_per_day | 83.7 | 23.9 | 4578 |
| age_days | 17.0 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `storytold/photocraft` | 59520 | 10131 | Rust | Other |
| `NandhaKishorM/laya` | 32844 | 2947 | Python | AI/ML |
| `Niko1221/Strata` | 24191 | 2435 | C++ | AI/ML |
| `browser-use/jev-ultrafast` | 22879 | 1694 | Python | AI/ML |
| `robbietilton/Compositor` | 16842 | 1636 | Swift | Mobile |
| `Ebony-Vinyl/dsh-our-free-model` | 15310 | 289 | JavaScript | AI/ML |
| `openai/math` | 14745 | 1680 | Lean | Other |
| `storytold/pdfcraft` | 13239 | 5032 | Rust | Other |
| `storytold/filmcraft` | 12884 | 5218 | Rust | Other |
| `yetone/magpie` | 12403 | 839 | Go | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `storytold/photocraft` | 4578.5 | 59520 | 13d | Other |
| `openai/math` | 2106.4 | 14745 | 7d | Other |
| `storytold/wordcraft` | 1975.0 | 11850 | 6d | Other |
| `wheresryan22/anatomy` | 1807.4 | 9037 | 5d | AI/ML |
| `jhaizhou-ops/d2r-mobile` | 1599.0 | 1599 | 1d | Mobile |
| `NandhaKishorM/laya` | 1313.8 | 32844 | 25d | AI/ML |
| `Niko1221/Strata` | 1273.2 | 24191 | 19d | AI/ML |
| `Arekejoker/qwen21-nsfw-pose-skill` | 1103.0 | 1103 | 1d | AI/ML |
| `liseami/CCBaga` | 1102.5 | 2205 | 2d | Other |
| `storytold/pdfcraft` | 1018.4 | 13239 | 13d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 394 | 918 | 307 | 181 | 90.2 | 36.6 |
| AI/ML | 390 | 1053 | 350 | 141 | 83.7 | 15.6 |
| Web | 68 | 679 | 346 | 101 | 57.0 | 8.5 |
| Mobile | 67 | 1133 | 382 | 118 | 95.0 | 27.3 |
| Game | 20 | 955 | 288 | 208 | 87.0 | 55.5 |
| Data | 18 | 920 | 491 | 168 | 62.6 | 9.9 |
| Finance/Trading | 18 | 695 | 248 | 78 | 51.0 | 6.5 |
| CLI/Tooling | 16 | 636 | 337 | 74 | 59.9 | 5.2 |
| Security | 5 | 698 | 226 | 151 | 73.9 | 2.8 |
| DevOps | 4 | 517 | 252 | 25 | 27.3 | 6.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.778 |         0.575 |      0.01  |
| forks       |   0.778 |   1     |         0.633 |     -0.062 |
| open_issues |   0.575 |   0.633 |         1     |     -0.073 |
| age_days    |   0.01  |  -0.062 |        -0.073 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.691 |         0.38  |      0.02  |
| forks       |   0.691 |   1     |         0.363 |      0.013 |
| open_issues |   0.38  |   0.363 |         1     |     -0.015 |
| age_days    |   0.02  |   0.013 |        -0.015 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 88 |
| `llm` | 67 |
| `macos` | 64 |
| `ai-agents` | 63 |
| `codex` | 57 |
| `jev` | 42 |
| `agent-skills` | 41 |
| `windows` | 36 |
| `rust` | 35 |
| `python` | 33 |
| `developer-tools` | 33 |
| `typescript` | 33 |
| `ai` | 31 |
| `mcp` | 31 |
| `open-source` | 28 |
| `claude` | 28 |
| `awesome-list` | 28 |
| `linux` | 27 |
| `ai-agent` | 26 |
| `react` | 24 |
