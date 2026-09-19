# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 460.0 | 232.5 | 7465 |
| forks | 72.9 | 22.0 | 3648 |
| open_issues | 10.8 | 1.0 | 3308 |
| stars_per_day | 49.7 | 17.3 | 3694 |
| age_days | 16.5 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `lnkiai/m3e-canvas` | 7465 | 778 | TypeScript | Web |
| `browser-use/jev-ultrafast` | 6451 | 415 | Python | Other |
| `sapientinc/PRAXIST` | 6185 | 681 | Python | Other |
| `MengTo/threeui` | 5957 | 566 | HTML | Web |
| `rakanki911/DLSS5-Swapper` | 5835 | 308 | JavaScript | Game |
| `eternity4719/HowToLiveBetter` | 5528 | 417 | HTML | Web |
| `XiaoDuoYa/codex-with-chatgpt` | 5515 | 535 | TypeScript | AI/ML |
| `bojieli/ai-infra-book` | 4452 | 315 | Python | AI/ML |
| `crmne/spotifast` | 4384 | 199 | Rust | Other |
| `HEJustinSun/my-girlfriend-jingtian-latex` | 4212 | 638 | TeX | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `tamaratran/fast-jev-compaction` | 3694.0 | 3694 | 1d | AI/ML |
| `browser-use/jev-ultrafast` | 3225.5 | 6451 | 2d | Other |
| `TheoLeeCJ/SemIf` | 857.0 | 1714 | 2d | Other |
| `robbietilton/Compositor` | 719.5 | 1439 | 2d | Mobile |
| `TianyuCodings/NanoJev` | 604.0 | 604 | 1d | Other |
| `yynxxxxx/gpt_sub_analysis` | 529.0 | 529 | 1d | Security |
| `eternity4719/HowToLiveBetter` | 502.5 | 5528 | 11d | Web |
| `jarrodwatts/jev-trader` | 497.5 | 995 | 2d | AI/ML |
| `NandhaKishorM/laya` | 492.0 | 492 | 1d | Other |
| `arvindear/wp2shell-PoC` | 476.0 | 476 | 1d | Security |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 414 | 425 | 215 | 83 | 50.4 | 17.8 |
| AI/ML | 384 | 491 | 255 | 66 | 48.1 | 5.9 |
| Mobile | 61 | 393 | 232 | 49 | 46.9 | 7.8 |
| Web | 52 | 788 | 239 | 82 | 53.7 | 4.6 |
| Data | 19 | 351 | 328 | 91 | 40.3 | 7.9 |
| CLI/Tooling | 16 | 221 | 205 | 14 | 58.7 | 1.4 |
| Security | 15 | 313 | 278 | 73 | 105.1 | 2.5 |
| DevOps | 14 | 200 | 152 | 19 | 13.5 | 3.7 |
| Finance/Trading | 13 | 343 | 170 | 129 | 49.7 | 2.6 |
| Game | 12 | 716 | 186 | 85 | 49.9 | 7.1 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.387 |         0.044 |      0.062 |
| forks       |   0.387 |   1     |         0.032 |      0.01  |
| open_issues |   0.044 |   0.032 |         1     |     -0.026 |
| age_days    |   0.062 |   0.01  |        -0.026 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.522 |         0.28  |      0.055 |
| forks       |   0.522 |   1     |         0.308 |     -0.009 |
| open_issues |   0.28  |   0.308 |         1     |      0.069 |
| age_days    |   0.055 |  -0.009 |         0.069 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 65 |
| `ai-agents` | 59 |
| `codex` | 53 |
| `llm` | 46 |
| `python` | 36 |
| `ai-agent` | 33 |
| `developer-tools` | 32 |
| `mcp` | 31 |
| `macos` | 29 |
| `agent-skills` | 29 |
| `typescript` | 29 |
| `ai` | 26 |
| `react` | 24 |
| `rust` | 22 |
| `windows` | 22 |
| `claude` | 21 |
| `self-hosted` | 21 |
| `open-source` | 20 |
| `local-first` | 19 |
| `linux` | 16 |
