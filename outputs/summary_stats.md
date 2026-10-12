# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 887.4 | 319.5 | 51488 |
| forks | 135.9 | 32.0 | 8453 |
| open_issues | 19.6 | 2.0 | 1837 |
| stars_per_day | 83.9 | 23.8 | 4681 |
| age_days | 16.7 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `storytold/photocraft` | 51488 | 8453 | Rust | Other |
| `NandhaKishorM/laya` | 32501 | 2899 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 22717 | 1673 | Python | AI/ML |
| `Niko1221/Strata` | 22416 | 2168 | C++ | AI/ML |
| `robbietilton/Compositor` | 16280 | 1552 | Swift | Mobile |
| `openai/math` | 14327 | 1617 | Lean | Other |
| `Ebony-Vinyl/dsh-our-free-model` | 11438 | 219 | JavaScript | AI/ML |
| `cdyforever/how-to-live-better` | 11365 | 806 | HTML | Web |
| `storytold/filmcraft` | 10973 | 4384 | Rust | Other |
| `storytold/lightcraft` | 10820 | 3806 | Rust | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `storytold/photocraft` | 4680.7 | 51488 | 11d | Other |
| `openai/math` | 2865.4 | 14327 | 5d | Other |
| `storytold/wordcraft` | 2021.2 | 8085 | 4d | Other |
| `wheresryan22/anatomy` | 1723.0 | 5169 | 3d | AI/ML |
| `liseami/CCBaga` | 1426.0 | 1426 | 1d | Other |
| `NandhaKishorM/laya` | 1413.1 | 32501 | 23d | AI/ML |
| `Niko1221/Strata` | 1318.6 | 22416 | 17d | AI/ML |
| `mhtsec/ARTEX` | 1171.0 | 3513 | 3d | AI/ML |
| `storytold/filmcraft` | 997.5 | 10973 | 11d | Other |
| `storytold/lightcraft` | 983.6 | 10820 | 11d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 393 | 832 | 301 | 154 | 95.7 | 27.0 |
| AI/ML | 382 | 1000 | 346 | 136 | 79.8 | 14.5 |
| Web | 72 | 607 | 288 | 84 | 49.9 | 6.5 |
| Mobile | 69 | 1063 | 378 | 108 | 86.5 | 23.4 |
| Game | 20 | 855 | 260 | 178 | 101.5 | 41.8 |
| Data | 20 | 828 | 418 | 155 | 70.6 | 12.9 |
| CLI/Tooling | 18 | 571 | 331 | 69 | 71.7 | 5.2 |
| Finance/Trading | 17 | 714 | 254 | 84 | 44.5 | 6.8 |
| Security | 5 | 654 | 224 | 124 | 118.9 | 2.8 |
| DevOps | 4 | 496 | 232 | 24 | 29.2 | 4.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.763 |         0.526 |     -0.007 |
| forks       |   0.763 |   1     |         0.511 |     -0.08  |
| open_issues |   0.526 |   0.511 |         1     |     -0.078 |
| age_days    |  -0.007 |  -0.08  |        -0.078 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.679 |         0.372 |      0.03  |
| forks       |   0.679 |   1     |         0.339 |      0.007 |
| open_issues |   0.372 |   0.339 |         1     |     -0.009 |
| age_days    |   0.03  |   0.007 |        -0.009 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 80 |
| `llm` | 63 |
| `ai-agents` | 62 |
| `codex` | 56 |
| `macos` | 54 |
| `jev` | 44 |
| `agent-skills` | 41 |
| `rust` | 33 |
| `developer-tools` | 32 |
| `windows` | 32 |
| `typescript` | 31 |
| `python` | 29 |
| `ai` | 29 |
| `mcp` | 29 |
| `awesome-list` | 28 |
| `open-source` | 27 |
| `react` | 25 |
| `ai-agent` | 25 |
| `linux` | 24 |
| `swift` | 23 |
