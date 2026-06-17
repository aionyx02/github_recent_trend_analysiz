# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 477.3 | 184.0 | 72723 |
| forks | 107.4 | 18.0 | 11460 |
| open_issues | 8.4 | 1.0 | 1627 |
| stars_per_day | 42.8 | 12.0 | 7108 |
| age_days | 17.9 | 19.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 72723 | 9300 | Python | AI/ML |
| `DietrichGebert/ponytail` | 28430 | 1257 | JavaScript | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 9491 | 849 | TypeScript | Other |
| `unicity-astrid/sdk-js` | 8256 | 36 | TypeScript | Other |
| `alibaba/open-code-review` | 7556 | 455 | Go | AI/ML |
| `anthropics/defending-code-reference-harness` | 6055 | 447 | Python | Security |
| `shadcn/improve` | 5061 | 179 | Unknown | Other |
| `AprilNEA/OpenLogi` | 5003 | 94 | Rust | Other |
| `helloianneo/ian-xiaohei-illustrations` | 4972 | 565 | Unknown | AI/ML |
| `zgwl/chinese-buy-us-stock-guide` | 4638 | 710 | Unknown | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `DietrichGebert/ponytail` | 7107.5 | 28430 | 4d | AI/ML |
| `pewdiepie-archdaemon/odysseus` | 4545.2 | 72723 | 16d | AI/ML |
| `XiaomiMiMo/MiMo-Code` | 1581.8 | 9491 | 6d | Other |
| `tamnd/kage` | 905.5 | 1811 | 2d | Other |
| `shadcn/improve` | 843.5 | 5061 | 6d | Other |
| `omnigent-ai/omnigent` | 645.8 | 3229 | 5d | AI/ML |
| `alchaincyf/loop-engineering-orange-book` | 583.0 | 583 | 1d | Other |
| `Plaer1/junction` | 496.0 | 496 | 1d | AI/ML |
| `lenucksi/aur-malware-check` | 350.5 | 1402 | 4d | CLI/Tooling |
| `EEliberto/IPA-Download` | 311.7 | 935 | 3d | Mobile |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 411 | 634 | 193 | 64 | 59.3 | 7.9 |
| Other | 395 | 383 | 176 | 85 | 31.8 | 6.8 |
| Web | 58 | 315 | 196 | 35 | 25.2 | 30.8 |
| Mobile | 37 | 330 | 206 | 39 | 36.5 | 5.8 |
| CLI/Tooling | 34 | 374 | 224 | 125 | 35.7 | 6.2 |
| Security | 16 | 749 | 304 | 116 | 52.2 | 6.5 |
| Finance/Trading | 15 | 177 | 165 | 2468 | 12.7 | 0.7 |
| Data | 13 | 257 | 145 | 32 | 32.5 | 3.3 |
| Game | 11 | 216 | 187 | 21 | 16.7 | 5.7 |
| DevOps | 10 | 191 | 157 | 20 | 18.9 | 2.0 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.421 |         0.571 |     -0.014 |
| forks       |   0.421 |   1     |         0.267 |      0.057 |
| open_issues |   0.571 |   0.267 |         1     |     -0.027 |
| age_days    |  -0.014 |   0.057 |        -0.027 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.617 |         0.334 |      0.009 |
| forks       |   0.617 |   1     |         0.339 |      0.06  |
| open_issues |   0.334 |   0.339 |         1     |      0.109 |
| age_days    |   0.009 |   0.06  |         0.109 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 62 |
| `llm` | 50 |
| `ai-agents` | 46 |
| `ai` | 46 |
| `codex` | 40 |
| `python` | 30 |
| `typescript` | 30 |
| `ai-agent` | 27 |
| `cli` | 27 |
| `macos` | 27 |
| `skills` | 23 |
| `mcp` | 23 |
| `developer-tools` | 21 |
| `open-source` | 21 |
| `claude` | 20 |
| `agent` | 20 |
| `prompt-engineering` | 19 |
| `self-hosted` | 18 |
| `agent-skills` | 16 |
| `rust` | 15 |
