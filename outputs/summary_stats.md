# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 806.3 | 315.0 | 38920 |
| forks | 117.7 | 31.0 | 5649 |
| open_issues | 16.8 | 2.0 | 1866 |
| stars_per_day | 93.0 | 24.5 | 4486 |
| age_days | 16.2 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `storytold/photocraft` | 38920 | 5649 | Rust | Other |
| `NandhaKishorM/laya` | 32083 | 2851 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 22527 | 1655 | Python | AI/ML |
| `Niko1221/Strata` | 20242 | 1851 | C++ | AI/ML |
| `robbietilton/Compositor` | 15267 | 1422 | Swift | Mobile |
| `openai/math` | 13459 | 1477 | Lean | Other |
| `cdyforever/how-to-live-better` | 10835 | 774 | HTML | Web |
| `jaredpalmer/kev` | 8880 | 583 | Python | Other |
| `shihabal3amri/DiPlay` | 8767 | 1117 | Kotlin | Mobile |
| `storytold/lightcraft` | 8388 | 2550 | Rust | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `openai/math` | 4486.3 | 13459 | 3d | Other |
| `storytold/photocraft` | 4324.4 | 38920 | 9d | Other |
| `mhtsec/ARTEX` | 2719.0 | 2719 | 1d | AI/ML |
| `NandhaKishorM/laya` | 1527.8 | 32083 | 21d | AI/ML |
| `noahdunnagan/fsearch` | 1383.0 | 1383 | 1d | Other |
| `Niko1221/Strata` | 1349.5 | 20242 | 15d | AI/ML |
| `storytold/wordcraft` | 1265.5 | 2531 | 2d | Other |
| `nullmoth/nvidia-macos-driver` | 1067.5 | 2135 | 2d | Other |
| `alchaincyf/huashu-art-motion` | 1031.3 | 3094 | 3d | Other |
| `browser-use/jev-ultrafast` | 979.4 | 22527 | 23d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 417 | 707 | 300 | 120 | 112.1 | 24.2 |
| AI/ML | 363 | 975 | 351 | 131 | 82.5 | 11.3 |
| Mobile | 67 | 954 | 346 | 94 | 74.1 | 19.4 |
| Web | 66 | 604 | 282 | 95 | 60.8 | 6.5 |
| CLI/Tooling | 25 | 435 | 305 | 46 | 134.2 | 3.6 |
| Data | 20 | 749 | 346 | 146 | 89.4 | 11.1 |
| Finance/Trading | 17 | 749 | 266 | 95 | 37.9 | 6.6 |
| Game | 15 | 614 | 227 | 45 | 80.8 | 23.5 |
| Security | 6 | 603 | 376 | 185 | 39.4 | 5.7 |
| DevOps | 4 | 550 | 348 | 50 | 31.8 | 6.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.715 |         0.296 |     -0.006 |
| forks       |   0.715 |   1     |         0.255 |     -0.044 |
| open_issues |   0.296 |   0.255 |         1     |     -0.016 |
| age_days    |  -0.006 |  -0.044 |        -0.016 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.619 |         0.342 |      0.025 |
| forks       |   0.619 |   1     |         0.393 |      0.119 |
| open_issues |   0.342 |   0.393 |         1     |      0.064 |
| age_days    |   0.025 |   0.119 |         0.064 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 73 |
| `ai-agents` | 61 |
| `llm` | 58 |
| `codex` | 54 |
| `macos` | 49 |
| `jev` | 44 |
| `developer-tools` | 33 |
| `agent-skills` | 32 |
| `rust` | 30 |
| `ai` | 30 |
| `windows` | 30 |
| `mcp` | 29 |
| `typescript` | 28 |
| `awesome-list` | 28 |
| `python` | 26 |
| `ai-agent` | 24 |
| `cli` | 23 |
| `open-source` | 21 |
| `swift` | 21 |
| `linux` | 21 |
