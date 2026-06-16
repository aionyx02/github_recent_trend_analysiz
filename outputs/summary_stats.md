# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 471.1 | 187.5 | 72069 |
| forks | 109.3 | 18.0 | 11460 |
| open_issues | 8.1 | 1.0 | 1571 |
| stars_per_day | 45.0 | 12.4 | 6662 |
| age_days | 17.6 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 72069 | 9222 | Python | AI/ML |
| `DietrichGebert/ponytail` | 19985 | 841 | JavaScript | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 9232 | 813 | TypeScript | Other |
| `unicity-astrid/sdk-js` | 8256 | 36 | TypeScript | Other |
| `alibaba/open-code-review` | 7348 | 439 | Go | AI/ML |
| `anthropics/defending-code-reference-harness` | 6018 | 437 | Python | Security |
| `shadcn/improve` | 4937 | 172 | Unknown | Other |
| `AprilNEA/OpenLogi` | 4924 | 93 | Rust | Other |
| `helloianneo/ian-xiaohei-illustrations` | 4810 | 537 | Unknown | AI/ML |
| `perplexityai/bumblebee` | 4472 | 405 | Go | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 6661.7 | 19985 | 3d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 4804.6 | 72069 | 15d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 1846.4 | 9232 | 5d | Other |
| `tamnd/kage` | 1661.0 | 1661 | 1d | Other |
| `shadcn/improve` | 987.4 | 4937 | 5d | Other |
| `omnigent-ai/omnigent` | 546.5 | 2186 | 4d | AI/ML |
| `lenucksi/aur-malware-check` | 416.3 | 1249 | 3d | CLI/Tooling |
| `alchaincyf/loop-engineering-orange-book` | 415.0 | 415 | 1d | Other |
| `royalbhati/sqltoerdiagram` | 373.0 | 373 | 1d | Data |
| `EEliberto/IPA-Download` | 312.5 | 625 | 2d | Mobile |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 403 | 622 | 201 | 64 | 60.0 | 7.9 |
| Other | 396 | 387 | 180 | 88 | 35.3 | 6.5 |
| Web | 59 | 306 | 183 | 35 | 25.6 | 29.2 |
| CLI/Tooling | 41 | 338 | 201 | 119 | 36.2 | 5.4 |
| Mobile | 35 | 327 | 207 | 40 | 41.5 | 5.2 |
| Finance/Trading | 16 | 172 | 160 | 2313 | 13.4 | 0.7 |
| Security | 15 | 776 | 405 | 121 | 59.8 | 6.5 |
| Game | 14 | 198 | 156 | 16 | 20.7 | 4.5 |
| Data | 11 | 420 | 175 | 102 | 72.2 | 4.7 |
| DevOps | 10 | 187 | 156 | 19 | 22.9 | 2.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.421 |         0.586 |     -0.011 |
| forks       |   0.421 |   1     |         0.264 |      0.046 |
| open_issues |   0.586 |   0.264 |         1     |     -0.032 |
| age_days    |  -0.011 |   0.046 |        -0.032 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.623 |         0.334 |      0.015 |
| forks       |   0.623 |   1     |         0.32  |      0.063 |
| open_issues |   0.334 |   0.32  |         1     |      0.094 |
| age_days    |   0.015 |   0.063 |         0.094 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 66 |
| `llm` | 51 |
| `ai` | 47 |
| `ai-agents` | 46 |
| `codex` | 41 |
| `typescript` | 31 |
| `python` | 31 |
| `cli` | 27 |
| `ai-agent` | 26 |
| `macos` | 25 |
| `skills` | 24 |
| `claude` | 22 |
| `developer-tools` | 22 |
| `open-source` | 22 |
| `mcp` | 22 |
| `prompt-engineering` | 19 |
| `agent` | 18 |
| `rust` | 17 |
| `anthropic` | 17 |
| `react` | 17 |
