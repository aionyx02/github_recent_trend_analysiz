# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 462.2 | 190.5 | 66147 |
| forks | 95.6 | 18.0 | 11460 |
| open_issues | 13.0 | 1.0 | 5392 |
| stars_per_day | 37.5 | 12.8 | 7350 |
| age_days | 17.9 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 66147 | 8176 | Python | AI/ML |
| `unicity-astrid/sdk-js` | 8253 | 36 | TypeScript | Other |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6846 | 5163 | C++ | Other |
| `nexu-io/html-anything` | 6528 | 639 | HTML | AI/ML |
| `alibaba/open-code-review` | 5968 | 310 | Go | AI/ML |
| `anthropics/defending-code-reference-harness` | 5625 | 398 | Python | Security |
| `simplifaisoul/osiris` | 5178 | 1049 | TypeScript | Data |
| `vercel-labs/zerolang` | 4954 | 324 | C++ | AI/ML |
| `AprilNEA/OpenLogi` | 4494 | 84 | Rust | Other |
| `perplexityai/bumblebee` | 4369 | 393 | Go | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 7349.7 | 66147 | 9d | AI/ML |
| `NoopApp/noop` | 655.0 | 1310 | 2d | Data |
| `MSNightmare/RoguePlanet` | 543.0 | 543 | 1d | Security |
| `apple/coreai-models` | 480.0 | 480 | 1d | AI/ML |
| `zgwl/chinese-buy-us-stock-guide` | 402.1 | 4021 | 10d | Other |
| `xiaohuailabs/xiaohu-video-translate` | 401.0 | 401 | 1d | AI/ML |
| `Tencent-Hunyuan/UniRL` | 383.0 | 383 | 1d | Other |
| `unicity-astrid/sdk-js` | 375.1 | 8253 | 22d | Other |
| `diffusionstudio/lottie` | 369.4 | 1847 | 5d | AI/ML |
| `cpaczek/skylight` | 355.9 | 2491 | 7d | Web |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 413 | 376 | 176 | 57 | 27.6 | 18.2 |
| AI/ML | 383 | 612 | 204 | 77 | 51.4 | 8.9 |
| Web | 54 | 314 | 170 | 38 | 24.8 | 27.0 |
| CLI/Tooling | 43 | 315 | 200 | 66 | 23.4 | 4.1 |
| Mobile | 34 | 335 | 210 | 47 | 31.8 | 6.1 |
| Security | 21 | 546 | 228 | 68 | 56.7 | 4.5 |
| Data | 16 | 747 | 346 | 216 | 73.7 | 6.2 |
| Game | 14 | 236 | 194 | 30 | 20.6 | 2.4 |
| DevOps | 12 | 166 | 149 | 14 | 11.0 | 1.7 |
| Finance/Trading | 10 | 204 | 216 | 3048 | 21.9 | 0.4 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.454 |         0.192 |     -0.007 |
| forks       |   0.454 |   1     |         0.115 |      0.012 |
| open_issues |   0.192 |   0.115 |         1     |      0.015 |
| age_days    |  -0.007 |   0.012 |         0.015 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.596 |         0.315 |      0.062 |
| forks       |   0.596 |   1     |         0.283 |      0.081 |
| open_issues |   0.315 |   0.283 |         1     |      0.066 |
| age_days    |   0.062 |   0.081 |         0.066 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 50 |
| `llm` | 47 |
| `ai-agents` | 43 |
| `ai` | 41 |
| `codex` | 37 |
| `open-source` | 33 |
| `typescript` | 33 |
| `cli` | 27 |
| `macos` | 26 |
| `developer-tools` | 26 |
| `python` | 25 |
| `rust` | 23 |
| `mcp` | 22 |
| `claude` | 20 |
| `agent` | 20 |
| `ai-agent` | 20 |
| `react` | 20 |
| `skills` | 20 |
| `windows` | 15 |
| `agent-skills` | 14 |
