# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 740.6 | 241.0 | 213600 |
| forks | 98.1 | 22.0 | 25120 |
| open_issues | 6.7 | 1.0 | 329 |
| stars_per_day | 50.6 | 16.0 | 9287 |
| age_days | 18.1 | 20.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `deepseek-ai/deepseek-harness` | 213600 | 25120 | TypeScript | Other |
| `anywhere-labs/dsh-desktop` | 23891 | 1159 | TypeScript | Other |
| `guillaumemeyer/watermarks-remover` | 20880 | 2404 | Python | AI/ML |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 14622 | 2616 | Python | Other |
| `yjh051108/dsh-routing-suite` | 7105 | 151 | JavaScript | Other |
| `zhu1090093659/dsh-web` | 6977 | 458 | TypeScript | Web |
| `sapientinc/PRAXIST` | 6428 | 556 | Python | Other |
| `MengTo/threeui` | 5214 | 510 | HTML | Web |
| `deeplethe/utopia` | 4983 | 451 | Rust | AI/ML |
| `s1dashu/ip-as-logo-skill` | 4975 | 248 | Unknown | AI/ML |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `deepseek-ai/deepseek-harness` | 9287.0 | 213600 | 23d | Other |
| `lnkiai/m3e-canvas` | 1355.0 | 4065 | 3d | Web |
| `anywhere-labs/dsh-desktop` | 1038.7 | 23891 | 23d | Other |
| `ashemag/human-atlas` | 843.0 | 843 | 1d | Other |
| `guillaumemeyer/watermarks-remover` | 835.2 | 20880 | 25d | AI/ML |
| `anthropics/fermats-last-theorem` | 762.0 | 762 | 1d | Other |
| `sapientinc/PRAXIST` | 714.2 | 6428 | 9d | Other |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 635.7 | 14622 | 23d | Other |
| `Rion-Wu-tech/wechat-intelligence-hub` | 549.0 | 549 | 1d | AI/ML |
| `anthropics/commerce-agents` | 536.8 | 2147 | 4d | AI/ML |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| AI/ML | 398 | 551 | 259 | 66 | 40.5 | 6.6 |
| Other | 356 | 1149 | 226 | 165 | 69.5 | 7.5 |
| Web | 81 | 591 | 237 | 73 | 56.2 | 4.2 |
| Mobile | 48 | 362 | 226 | 30 | 34.0 | 8.5 |
| Data | 32 | 278 | 186 | 23 | 23.5 | 4.5 |
| CLI/Tooling | 31 | 538 | 240 | 52 | 28.3 | 7.2 |
| Game | 19 | 449 | 200 | 29 | 37.9 | 9.8 |
| Security | 13 | 388 | 380 | 67 | 39.3 | 3.0 |
| Finance/Trading | 11 | 313 | 193 | 146 | 40.8 | 3.6 |
| DevOps | 11 | 390 | 210 | 49 | 21.0 | 2.6 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.966 |         0.088 |       0.03 |
| forks       |   0.966 |   1     |         0.065 |       0.02 |
| open_issues |   0.088 |   0.065 |         1     |       0.07 |
| age_days    |   0.03  |   0.02  |         0.07  |       1    |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.564 |         0.298 |      0.042 |
| forks       |   0.564 |   1     |         0.325 |      0.008 |
| open_issues |   0.298 |   0.325 |         1     |      0.053 |
| age_days    |   0.042 |   0.008 |         0.053 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `dsh-plugin` | 113 |
| `deepseek-harness` | 102 |
| `ai-agents` | 82 |
| `dsh` | 76 |
| `claude-code` | 67 |
| `codex` | 61 |
| `deepseek` | 58 |
| `llm` | 58 |
| `ai-agent` | 49 |
| `typescript` | 44 |
| `mcp` | 43 |
| `agent-skills` | 42 |
| `python` | 39 |
| `developer-tools` | 39 |
| `ai` | 37 |
| `agent` | 35 |
| `local-first` | 29 |
| `claude` | 28 |
| `windows` | 28 |
| `macos` | 24 |
