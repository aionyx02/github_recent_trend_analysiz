# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 451.5 | 224.0 | 7372 |
| forks | 69.0 | 22.0 | 3643 |
| open_issues | 10.2 | 1.0 | 3490 |
| stars_per_day | 45.0 | 16.6 | 3856 |
| age_days | 16.8 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `lnkiai/m3e-canvas` | 7372 | 766 | TypeScript | Web |
| `MengTo/threeui` | 5926 | 564 | HTML | Web |
| `sapientinc/PRAXIST` | 5743 | 664 | Python | Other |
| `rakanki911/DLSS5-Swapper` | 5661 | 297 | JavaScript | Game |
| `XiaoDuoYa/codex-with-chatgpt` | 5378 | 521 | TypeScript | AI/ML |
| `amagine-ai/Amagine3D` | 5313 | 256 | Python | Other |
| `eternity4719/HowToLiveBetter` | 4603 | 360 | HTML | Web |
| `crmne/spotifast` | 4349 | 196 | Rust | Other |
| `bojieli/ai-infra-book` | 4318 | 308 | Python | AI/ML |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 4211 | 640 | TeX | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `browser-use/jev-ultrafast` | 3856.0 | 3856 | 1d | Other |
| `tamaratran/fast-jev-compaction` | 2103.0 | 2103 | 1d | AI/ML |
| `TheoLeeCJ/openjev` | 1277.0 | 1277 | 1d | Other |
| `vinnylarouge/jevlike` | 792.0 | 792 | 1d | Other |
| `jarrodwatts/jev-trader` | 698.0 | 698 | 1d | AI/ML |
| `korcarc/text-humanizer` | 572.0 | 572 | 1d | AI/ML |
| `ctdal/cve-2026-41940-PoC` | 526.0 | 526 | 1d | Security |
| `lnkiai/m3e-canvas` | 491.5 | 7372 | 15d | Web |
| `yynxxxxx/gpt_sub_analysis` | 480.0 | 480 | 1d | Security |
| `eternity4719/HowToLiveBetter` | 460.3 | 4603 | 10d | Web |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 417 | 423 | 209 | 79 | 46.1 | 16.6 |
| AI/ML | 387 | 474 | 248 | 64 | 42.7 | 5.7 |
| Mobile | 60 | 373 | 232 | 37 | 39.0 | 7.7 |
| Web | 51 | 771 | 237 | 82 | 53.5 | 4.5 |
| Data | 18 | 352 | 322 | 30 | 39.9 | 8.4 |
| Security | 15 | 286 | 266 | 71 | 91.1 | 2.3 |
| CLI/Tooling | 14 | 262 | 204 | 23 | 40.9 | 4.6 |
| DevOps | 14 | 203 | 152 | 19 | 15.0 | 3.4 |
| Game | 12 | 698 | 184 | 83 | 37.7 | 6.7 |
| Finance/Trading | 12 | 353 | 188 | 146 | 67.7 | 2.9 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.388 |         0.043 |      0.06  |
| forks       |   0.388 |   1     |         0.03  |      0.005 |
| open_issues |   0.043 |   0.03  |         1     |     -0.031 |
| age_days    |   0.06  |   0.005 |        -0.031 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.524 |         0.286 |      0.026 |
| forks       |   0.524 |   1     |         0.304 |     -0.012 |
| open_issues |   0.286 |   0.304 |         1     |      0.054 |
| age_days    |   0.026 |  -0.012 |         0.054 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 66 |
| `ai-agents` | 59 |
| `codex` | 52 |
| `llm` | 44 |
| `ai-agent` | 35 |
| `python` | 35 |
| `mcp` | 31 |
| `agent-skills` | 31 |
| `developer-tools` | 31 |
| `typescript` | 31 |
| `macos` | 27 |
| `ai` | 26 |
| `react` | 24 |
| `rust` | 23 |
| `claude` | 22 |
| `windows` | 21 |
| `self-hosted` | 21 |
| `dsh-plugin` | 20 |
| `local-first` | 19 |
| `open-source` | 18 |
