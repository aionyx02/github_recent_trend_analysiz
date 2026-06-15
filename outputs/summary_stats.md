# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 452.5 | 182.0 | 71401 |
| forks | 104.8 | 18.0 | 11460 |
| open_issues | 13.6 | 1.0 | 5873 |
| stars_per_day | 45.5 | 12.2 | 5754 |
| age_days | 17.4 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 71401 | 9103 | Python | AI/ML |
| `DietrichGebert/ponytail` | 11507 | 474 | JavaScript | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 8827 | 762 | TypeScript | Other |
| `unicity-astrid/sdk-js` | 8257 | 36 | TypeScript | Other |
| `alibaba/open-code-review` | 7183 | 420 | Go | AI/ML |
| `anthropics/defending-code-reference-harness` | 5955 | 430 | Python | Security |
| `AprilNEA/OpenLogi` | 4868 | 92 | Rust | Other |
| `shadcn/improve` | 4662 | 160 | Unknown | Other |
| `helloianneo/ian-xiaohei-illustrations` | 4635 | 506 | Unknown | AI/ML |
| `perplexityai/bumblebee` | 4455 | 404 | Go | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 5753.5 | 11507 | 2d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 5100.1 | 71401 | 14d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 2206.8 | 8827 | 4d | Other |
| `tamnd/kage` | 1209.0 | 1209 | 1d | Other |
| `shadcn/improve` | 1165.5 | 4662 | 4d | Other |
| `lenucksi/aur-malware-check` | 509.5 | 1019 | 2d | CLI/Tooling |
| `omnigent-ai/omnigent` | 490.0 | 1470 | 3d | AI/ML |
| `EEliberto/IPA-Download` | 462.0 | 462 | 1d | Mobile |
| `mrtooher/fable-mode` | 370.0 | 370 | 1d | AI/ML |
| `orange2ai/renwei-writing` | 327.0 | 654 | 2d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 399 | 591 | 192 | 62 | 60.3 | 7.7 |
| Other | 399 | 377 | 177 | 80 | 35.4 | 20.8 |
| Web | 60 | 314 | 186 | 35 | 26.1 | 27.4 |
| CLI/Tooling | 40 | 332 | 210 | 106 | 38.7 | 5.3 |
| Mobile | 34 | 314 | 198 | 40 | 44.1 | 5.1 |
| Finance/Trading | 16 | 177 | 160 | 2238 | 12.4 | 0.7 |
| Security | 16 | 712 | 228 | 110 | 66.4 | 5.8 |
| Data | 14 | 359 | 174 | 173 | 56.5 | 3.1 |
| Game | 12 | 210 | 189 | 18 | 26.0 | 4.1 |
| DevOps | 10 | 188 | 160 | 16 | 33.7 | 2.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.441 |         0.205 |     -0.011 |
| forks       |   0.441 |   1     |         0.122 |      0.039 |
| open_issues |   0.205 |   0.122 |         1     |      0.033 |
| age_days    |  -0.011 |   0.039 |         0.033 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.6   |         0.355 |      0.007 |
| forks       |   0.6   |   1     |         0.322 |      0.07  |
| open_issues |   0.355 |   0.322 |         1     |      0.09  |
| age_days    |   0.007 |   0.07  |         0.09  |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 62 |
| `llm` | 50 |
| `ai` | 46 |
| `ai-agents` | 42 |
| `codex` | 40 |
| `typescript` | 32 |
| `python` | 29 |
| `cli` | 28 |
| `macos` | 26 |
| `ai-agent` | 25 |
| `skills` | 25 |
| `mcp` | 22 |
| `claude` | 21 |
| `open-source` | 21 |
| `developer-tools` | 20 |
| `agent` | 18 |
| `prompt-engineering` | 17 |
| `anthropic` | 17 |
| `react` | 17 |
| `agent-skills` | 16 |
