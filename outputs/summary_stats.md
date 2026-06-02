# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 424.8 | 204.0 | 24883 |
| forks | 149.3 | 19.0 | 8339 |
| open_issues | 8.0 | 1.0 | 2914 |
| stars_per_day | 61.2 | 15.2 | 24883 |
| age_days | 16.7 | 18.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `pewdiepie-archdaemon/odysseus` | 24883 | 3018 | JavaScript | AI/ML |
| `antirez/ds4` | 12752 | 1109 | C | Game |
| `BigPizzaV3/CodexPlusPlus` | 11163 | 714 | Rust | AI/ML |
| `FULU-Foundation/OrcaSlicer-bambulab` | 6733 | 5123 | C++ | Other |
| `nexu-io/html-anything` | 5826 | 569 | HTML | AI/ML |
| `V4bel/dirtyfrag` | 4803 | 775 | C | Other |
| `vercel-labs/zerolang` | 4797 | 309 | C | AI/ML |
| `microsoft/SkillOpt` | 4315 | 438 | Python | AI/ML |
| `simplifaisoul/osiris` | 4165 | 830 | TypeScript | Data |
| `perplexityai/bumblebee` | 4142 | 365 | Go | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `pewdiepie-archdaemon/odysseus` | 24883.0 | 24883 | 1d | AI/ML |
| `asz798838958/aBaiAutoplus` | 787.0 | 787 | 1d | AI/ML |
| `op7418/guizang-social-card-skill` | 503.4 | 2517 | 5d | AI/ML |
| `antirez/ds4` | 490.5 | 12752 | 26d | Game |
| `BigPizzaV3/CodexPlusPlus` | 429.3 | 11163 | 26d | AI/ML |
| `anomalyco/rift` | 403.0 | 403 | 1d | Other |
| `AprilNEA/OpenLogi` | 392.0 | 3136 | 8d | Other |
| `perplexityai/bumblebee` | 345.2 | 4142 | 12d | Other |
| `qiuqiubuchongle-cloud/chokepoint-atlas` | 341.0 | 341 | 1d | Other |
| `helloianneo/ian-xiaohei-illustrations` | 339.8 | 1699 | 5d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 422 | 342 | 194 | 153 | 34.8 | 10.8 |
| AI/ML | 367 | 549 | 226 | 119 | 108.0 | 6.9 |
| Web | 51 | 321 | 194 | 69 | 28.0 | 4.0 |
| Mobile | 39 | 286 | 209 | 26 | 26.7 | 4.4 |
| CLI/Tooling | 37 | 354 | 204 | 73 | 35.7 | 4.6 |
| Game | 22 | 792 | 195 | 70 | 59.7 | 9.9 |
| Finance/Trading | 22 | 242 | 196 | 1344 | 23.4 | 0.9 |
| Security | 19 | 267 | 182 | 42 | 28.4 | 1.9 |
| DevOps | 12 | 333 | 167 | 92 | 22.3 | 7.7 |
| Data | 9 | 717 | 230 | 113 | 50.1 | 6.7 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.184 |         0.166 |      0.032 |
| forks       |   0.184 |   1     |         0.038 |     -0.058 |
| open_issues |   0.166 |   0.038 |         1     |     -0.001 |
| age_days    |   0.032 |  -0.058 |        -0.001 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.539 |         0.3   |      0.115 |
| forks       |   0.539 |   1     |         0.257 |      0.174 |
| open_issues |   0.3   |   0.257 |         1     |      0.086 |
| age_days    |   0.115 |   0.174 |         0.086 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 52 |
| `ai-agents` | 49 |
| `typescript` | 41 |
| `llm` | 37 |
| `ai` | 34 |
| `codex` | 33 |
| `python` | 30 |
| `cli` | 30 |
| `mcp` | 27 |
| `open-source` | 27 |
| `claude` | 24 |
| `agent` | 24 |
| `rust` | 22 |
| `macos` | 22 |
| `anthropic` | 20 |
| `ai-agent` | 19 |
| `skills` | 18 |
| `openai` | 18 |
| `react` | 17 |
| `developer-tools` | 17 |
