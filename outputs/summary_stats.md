# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 734.5 | 298.0 | 49285 |
| forks | 99.3 | 30.0 | 4223 |
| open_issues | 14.2 | 2.0 | 1760 |
| stars_per_day | 66.3 | 21.8 | 7275 |
| age_days | 17.1 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `eternity4719/HowToLiveBetter` | 49285 | 3944 | HTML | Web |
| `NandhaKishorM/laya` | 31323 | 2764 | Python | AI/ML |
| `browser-use/jev-ultrafast` | 22242 | 1611 | Python | AI/ML |
| `Niko1221/Strata` | 16502 | 1435 | C++ | AI/ML |
| `storytold/photocraft` | 12759 | 1664 | Rust | Other |
| `robbietilton/Compositor` | 10539 | 987 | Swift | Mobile |
| `cdyforever/how-to-live-better` | 9089 | 619 | HTML | Web |
| `jaredpalmer/kev` | 8632 | 566 | Python | Other |
| `zai-org/ZCode` | 7490 | 2288 | TypeScript | AI/ML |
| `tamaratran/fast-jev-compaction` | 7458 | 511 | TypeScript | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `openai/math` | 7275.0 | 7275 | 1d | Other |
| `storytold/photocraft` | 2126.5 | 12759 | 6d | Other |
| `NandhaKishorM/laya` | 1740.2 | 31323 | 18d | AI/ML |
| `eternity4719/HowToLiveBetter` | 1699.5 | 49285 | 29d | Web |
| `Niko1221/Strata` | 1375.2 | 16502 | 12d | AI/ML |
| `alchaincyf/huashu-art-motion` | 1256.0 | 1256 | 1d | Other |
| `browser-use/jev-ultrafast` | 1112.1 | 22242 | 20d | AI/ML |
| `rehan-remade/universal-modder` | 820.0 | 4920 | 6d | AI/ML |
| `kargulstudio/sales-crm` | 808.5 | 1617 | 2d | Other |
| `KKKKhazix/AIHOT` | 790.9 | 6327 | 8d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 403 | 562 | 279 | 81 | 68.5 | 19.8 |
| AI/ML | 367 | 866 | 329 | 111 | 70.5 | 10.1 |
| Mobile | 73 | 774 | 274 | 135 | 53.6 | 17.5 |
| Web | 67 | 1245 | 237 | 127 | 72.5 | 5.3 |
| CLI/Tooling | 22 | 399 | 234 | 50 | 35.5 | 5.2 |
| Data | 18 | 696 | 328 | 146 | 64.6 | 13.1 |
| Finance/Trading | 18 | 699 | 242 | 93 | 56.5 | 5.8 |
| Game | 15 | 549 | 230 | 51 | 47.3 | 22.1 |
| Security | 10 | 503 | 372 | 118 | 23.4 | 4.0 |
| DevOps | 7 | 450 | 300 | 35 | 24.3 | 7.9 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.659 |         0.098 |      0.014 |
| forks       |   0.659 |   1     |         0.124 |      0.043 |
| open_issues |   0.098 |   0.124 |         1     |      0.05  |
| age_days    |   0.014 |   0.043 |         0.05  |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.622 |         0.304 |      0.019 |
| forks       |   0.622 |   1     |         0.306 |     -0.026 |
| open_issues |   0.304 |   0.306 |         1     |     -0.018 |
| age_days    |   0.019 |  -0.026 |        -0.018 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 75 |
| `ai-agents` | 60 |
| `llm` | 58 |
| `codex` | 57 |
| `jev` | 46 |
| `macos` | 44 |
| `agent-skills` | 39 |
| `developer-tools` | 33 |
| `rust` | 32 |
| `python` | 29 |
| `mcp` | 29 |
| `typescript` | 29 |
| `awesome-list` | 29 |
| `windows` | 26 |
| `ai` | 24 |
| `ai-agent` | 23 |
| `awesome` | 23 |
| `cli` | 22 |
| `claude` | 21 |
| `typesafe` | 21 |
