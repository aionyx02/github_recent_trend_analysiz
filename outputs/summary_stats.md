# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 758.0 | 301.0 | 31883 |
| forks | 111.1 | 31.0 | 4435 |
| open_issues | 15.4 | 2.0 | 1774 |
| stars_per_day | 80.9 | 22.0 | 6385 |
| age_days | 16.7 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `NandhaKishorM/laya` | 31883 | 2834 | Python | AI/ML |
| `storytold/photocraft` | 31619 | 4435 | Rust | Other |
| `browser-use/jev-ultrafast` | 22449 | 1644 | Python | AI/ML |
| `Niko1221/Strata` | 19113 | 1725 | C++ | AI/ML |
| `robbietilton/Compositor` | 14480 | 1339 | Swift | Mobile |
| `openai/math` | 12770 | 1356 | Lean | Other |
| `cdyforever/how-to-live-better` | 10504 | 743 | HTML | Web |
| `jaredpalmer/kev` | 8800 | 576 | Python | Other |
| `shihabal3amri/DiPlay` | 8009 | 1013 | Kotlin | Mobile |
| `zai-org/ZCode` | 7588 | 2311 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `openai/math` | 6385.0 | 12770 | 2d | Other |
| `storytold/photocraft` | 3952.4 | 31619 | 8d | Other |
| `mhtsec/ARTEX` | 1888.0 | 1888 | 1d | AI/ML |
| `nullmoth/nvidia-macos-driver` | 1644.0 | 1644 | 1d | Other |
| `NandhaKishorM/laya` | 1594.2 | 31883 | 20d | AI/ML |
| `alchaincyf/huashu-art-motion` | 1376.0 | 2752 | 2d | Other |
| `Niko1221/Strata` | 1365.2 | 19113 | 14d | AI/ML |
| `storytold/wordcraft` | 1193.0 | 1193 | 1d | Other |
| `alejandrobujan/tendedero` | 1149.0 | 1149 | 1d | Mobile |
| `LoreanXavier/pt-pc` | 1116.0 | 1116 | 1d | Game |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 405 | 650 | 281 | 112 | 96.1 | 22.6 |
| AI/ML | 371 | 926 | 338 | 124 | 74.6 | 10.0 |
| Web | 71 | 546 | 257 | 84 | 63.3 | 5.6 |
| Mobile | 70 | 897 | 312 | 88 | 68.2 | 18.6 |
| CLI/Tooling | 20 | 405 | 230 | 53 | 32.1 | 4.8 |
| Data | 18 | 754 | 334 | 156 | 80.5 | 11.4 |
| Finance/Trading | 18 | 710 | 250 | 95 | 41.1 | 6.2 |
| Game | 16 | 579 | 218 | 52 | 109.2 | 23.3 |
| Security | 6 | 595 | 374 | 184 | 55.0 | 7.2 |
| DevOps | 5 | 452 | 222 | 39 | 27.6 | 7.2 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.687 |         0.242 |     -0.032 |
| forks       |   0.687 |   1     |         0.195 |     -0.055 |
| open_issues |   0.242 |   0.195 |         1     |     -0.02  |
| age_days    |  -0.032 |  -0.055 |        -0.02  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.64  |         0.324 |     -0.015 |
| forks       |   0.64  |   1     |         0.323 |     -0.034 |
| open_issues |   0.324 |   0.323 |         1     |     -0.076 |
| age_days    |  -0.015 |  -0.034 |        -0.076 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 73 |
| `ai-agents` | 61 |
| `llm` | 57 |
| `codex` | 52 |
| `macos` | 48 |
| `jev` | 46 |
| `agent-skills` | 34 |
| `developer-tools` | 33 |
| `rust` | 30 |
| `mcp` | 29 |
| `awesome-list` | 29 |
| `ai` | 28 |
| `typescript` | 28 |
| `windows` | 28 |
| `python` | 27 |
| `awesome` | 23 |
| `ai-agent` | 23 |
| `cli` | 22 |
| `open-source` | 21 |
| `typesafe` | 21 |
