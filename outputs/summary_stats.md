# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 836.2 | 316.5 | 44785 |
| forks | 123.0 | 30.0 | 6937 |
| open_issues | 17.5 | 2.0 | 1756 |
| stars_per_day | 91.9 | 25.1 | 4478 |
| age_days | 16.0 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `storytold/photocraft` | 44785 | 6937 | Rust | Other |
| `NandhaKishorM/laya` | 32242 | 2871 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 22591 | 1658 | Python | AI/ML |
| `Niko1221/Strata` | 21158 | 1985 | C++ | AI/ML |
| `robbietilton/Compositor` | 15732 | 1483 | Swift | Mobile |
| `openai/math` | 13900 | 1545 | Lean | Other |
| `cdyforever/how-to-live-better` | 11065 | 791 | HTML | Web |
| `storytold/lightcraft` | 9539 | 3152 | Rust | Other |
| `storytold/filmcraft` | 9290 | 3517 | Rust | Other |
| `shihabal3amri/DiPlay` | 9214 | 1172 | Kotlin | Mobile |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `storytold/photocraft` | 4478.5 | 44785 | 10d | Other |
| `openai/math` | 3475.0 | 13900 | 4d | Other |
| `mhtsec/ARTEX` | 1529.0 | 3058 | 2d | AI/ML |
| `NandhaKishorM/laya` | 1465.5 | 32242 | 22d | AI/ML |
| `storytold/wordcraft` | 1352.3 | 4057 | 3d | Other |
| `Niko1221/Strata` | 1322.4 | 21158 | 16d | AI/ML |
| `storytold/lightcraft` | 953.9 | 9539 | 10d | Other |
| `browser-use/jev-ultrafast` | 941.3 | 22591 | 24d | AI/ML |
| `storytold/filmcraft` | 929.0 | 9290 | 10d | Other |
| `t4t5/omdrop-owl` | 921.5 | 1843 | 2d | CLI/Tooling |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 416 | 748 | 301 | 128 | 109.9 | 24.0 |
| AI/ML | 364 | 990 | 352 | 135 | 80.3 | 12.9 |
| Web | 67 | 616 | 280 | 99 | 50.1 | 6.9 |
| Mobile | 64 | 1055 | 376 | 104 | 82.0 | 22.0 |
| CLI/Tooling | 24 | 482 | 303 | 49 | 136.7 | 3.9 |
| Data | 21 | 764 | 350 | 144 | 84.4 | 11.3 |
| Game | 18 | 583 | 232 | 40 | 82.6 | 29.8 |
| Finance/Trading | 16 | 746 | 260 | 91 | 38.1 | 6.6 |
| Security | 6 | 620 | 377 | 134 | 178.9 | 2.5 |
| DevOps | 4 | 490 | 216 | 24 | 28.1 | 1.5 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.751 |         0.47  |      0.005 |
| forks       |   0.751 |   1     |         0.452 |     -0.053 |
| open_issues |   0.47  |   0.452 |         1     |     -0.067 |
| age_days    |   0.005 |  -0.053 |        -0.067 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.638 |         0.347 |      0.041 |
| forks       |   0.638 |   1     |         0.39  |      0.141 |
| open_issues |   0.347 |   0.39  |         1     |      0.063 |
| age_days    |   0.041 |   0.141 |         0.063 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 73 |
| `ai-agents` | 62 |
| `llm` | 59 |
| `macos` | 54 |
| `codex` | 53 |
| `jev` | 44 |
| `agent-skills` | 34 |
| `rust` | 32 |
| `developer-tools` | 32 |
| `windows` | 32 |
| `typescript` | 31 |
| `mcp` | 30 |
| `awesome-list` | 28 |
| `python` | 26 |
| `ai` | 26 |
| `linux` | 24 |
| `ai-agent` | 24 |
| `open-source` | 23 |
| `swift` | 22 |
| `awesome` | 22 |
