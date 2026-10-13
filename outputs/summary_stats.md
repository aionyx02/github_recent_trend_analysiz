# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 920.8 | 314.0 | 56202 |
| forks | 144.3 | 33.0 | 9427 |
| open_issues | 22.5 | 2.0 | 1937 |
| stars_per_day | 84.1 | 23.4 | 4684 |
| age_days | 16.8 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `storytold/photocraft` | 56202 | 9427 | Rust | Other |
| `NandhaKishorM/laya` | 32699 | 2927 | Python | AI/ML |
| `Niko1221/Strata` | 23430 | 2303 | C++ | AI/ML |
| `browser-use/jev-ultrafast` | 22801 | 1681 | Python | AI/ML |
| `robbietilton/Compositor` | 16638 | 1602 | Swift | Mobile |
| `openai/math` | 14586 | 1650 | Lean | Other |
| `Ebony-Vinyl/dsh-our-free-model` | 13572 | 261 | JavaScript | AI/ML |
| `storytold/pdfcraft` | 12207 | 4655 | Rust | Other |
| `storytold/filmcraft` | 12114 | 4887 | Rust | Other |
| `storytold/lightcraft` | 11706 | 4204 | Rust | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `storytold/photocraft` | 4683.5 | 56202 | 12d | Other |
| `openai/math` | 2431.0 | 14586 | 6d | Other |
| `storytold/wordcraft` | 2066.6 | 10333 | 5d | Other |
| `liseami/CCBaga` | 1983.0 | 1983 | 1d | Other |
| `wheresryan22/anatomy` | 1888.8 | 7555 | 4d | AI/ML |
| `NandhaKishorM/laya` | 1362.5 | 32699 | 24d | AI/ML |
| `Niko1221/Strata` | 1301.7 | 23430 | 18d | AI/ML |
| `onehumanbeing/esp32-iphone-agent` | 1272.0 | 1272 | 1d | AI/ML |
| `jhaizhou-ops/d2r-mobile` | 1018.0 | 1018 | 1d | Mobile |
| `storytold/pdfcraft` | 1017.2 | 12207 | 12d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 403 | 870 | 301 | 167 | 93.9 | 31.6 |
| AI/ML | 382 | 1022 | 334 | 139 | 81.7 | 16.0 |
| Web | 68 | 656 | 316 | 91 | 50.6 | 6.9 |
| Mobile | 66 | 1093 | 360 | 112 | 92.0 | 26.3 |
| Game | 20 | 915 | 272 | 196 | 91.5 | 46.7 |
| Data | 19 | 882 | 449 | 160 | 68.9 | 12.4 |
| CLI/Tooling | 17 | 619 | 379 | 70 | 65.4 | 6.1 |
| Finance/Trading | 16 | 750 | 262 | 84 | 45.8 | 7.5 |
| Security | 5 | 673 | 224 | 147 | 91.3 | 2.8 |
| DevOps | 4 | 508 | 244 | 25 | 28.3 | 4.8 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.772 |         0.561 |     -0.002 |
| forks       |   0.772 |   1     |         0.58  |     -0.075 |
| open_issues |   0.561 |   0.58  |         1     |     -0.076 |
| age_days    |  -0.002 |  -0.075 |        -0.076 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.689 |         0.378 |      0.005 |
| forks       |   0.689 |   1     |         0.353 |     -0.007 |
| open_issues |   0.378 |   0.353 |         1     |     -0.017 |
| age_days    |   0.005 |  -0.007 |        -0.017 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 86 |
| `ai-agents` | 64 |
| `llm` | 63 |
| `macos` | 59 |
| `codex` | 57 |
| `agent-skills` | 45 |
| `jev` | 43 |
| `rust` | 35 |
| `windows` | 33 |
| `developer-tools` | 31 |
| `mcp` | 31 |
| `typescript` | 31 |
| `python` | 30 |
| `ai` | 30 |
| `awesome-list` | 28 |
| `open-source` | 27 |
| `ai-agent` | 26 |
| `claude` | 25 |
| `linux` | 25 |
| `react` | 24 |
