# Summary Statistics

_Sample size: 1000 repos_

## Overall

| Metric | Mean | Median | Max |
|---|---:|---:|---:|
| stars | 481.7 | 238.0 | 10344 |
| forks | 76.5 | 23.0 | 3643 |
| open_issues | 11.5 | 1.0 | 3203 |
| stars_per_day | 55.5 | 18.5 | 3448 |
| age_days | 16.2 | 17.0 | 29 |

## Top 10 by stars

| Repo | Stars | Forks | Language | Category |
|---|---:|---:|---|---|
| `browser-use/jev-ultrafast` | 10344 | 626 | Python | Other |
| `lnkiai/m3e-canvas` | 7714 | 803 | TypeScript | Web |
| `eternity4719/HowToLiveBetter` | 6573 | 487 | HTML | Web |
| `sapientinc/PRAXIST` | 6361 | 699 | Python | Other |
| `rakanki911/DLSS5-Swapper` | 5987 | 320 | JavaScript | Game |
| `MengTo/threeui` | 5983 | 571 | HTML | Web |
| `XiaoDuoYa/codex-with-chatgpt` | 5655 | 540 | TypeScript | AI/ML |
| `bojieli/ai-infra-book` | 4647 | 328 | Python | AI/ML |
| `tamaratran/fast-jev-compaction` | 4594 | 255 | TypeScript | AI/ML |
| `crmne/spotifast` | 4440 | 204 | Rust | Other |

## Top 10 by stars_per_day (breakout)

| Repo | Stars/day | Stars | Age | Category |
|---|---:|---:|---:|---|
| `browser-use/jev-ultrafast` | 3448.0 | 10344 | 3d | Other |
| `tamaratran/fast-jev-compaction` | 2297.0 | 4594 | 2d | AI/ML |
| `NandhaKishorM/laya` | 2194.0 | 2194 | 1d | Other |
| `robbietilton/Compositor` | 1070.7 | 3212 | 3d | Mobile |
| `bespokelabsai/nimble` | 794.0 | 794 | 1d | Data |
| `TheoLeeCJ/SemIf` | 721.0 | 2163 | 3d | Other |
| `TianyuCodings/NanoJev` | 601.5 | 1203 | 2d | Other |
| `arvindear/wp2shell-PoC` | 563.0 | 563 | 1d | Security |
| `eternity4719/HowToLiveBetter` | 547.8 | 6573 | 12d | Web |
| `githubnext/localjev` | 541.0 | 541 | 1d | Other |

## Per-category heat

| Category | Count | Mean stars | Median stars | Mean forks | Mean stars/day | Mean issues |
|---|---:|---:|---:|---:|---:|---:|
| Other | 410 | 460 | 232 | 88 | 59.1 | 19.8 |
| AI/ML | 381 | 494 | 255 | 67 | 50.2 | 5.7 |
| Mobile | 62 | 430 | 236 | 60 | 57.9 | 8.1 |
| Web | 55 | 779 | 240 | 80 | 52.5 | 3.9 |
| CLI/Tooling | 18 | 387 | 219 | 29 | 52.5 | 3.5 |
| Data | 18 | 408 | 346 | 124 | 76.4 | 8.6 |
| Finance/Trading | 17 | 315 | 176 | 101 | 58.5 | 2.6 |
| Security | 15 | 324 | 283 | 75 | 86.5 | 2.6 |
| DevOps | 13 | 212 | 167 | 22 | 18.2 | 4.1 |
| Game | 11 | 756 | 207 | 89 | 71.0 | 8.4 |

## Correlations

**Pearson** (linear)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.383 |         0.042 |      0.062 |
| forks       |   0.383 |   1     |         0.035 |      0.028 |
| open_issues |   0.042 |   0.035 |         1     |     -0.019 |
| age_days    |   0.062 |   0.028 |        -0.019 |      1     |

**Spearman** (rank)

|             |   stars |   forks |   open_issues |   age_days |
|:------------|--------:|--------:|--------------:|-----------:|
| stars       |   1     |   0.518 |         0.269 |      0.06  |
| forks       |   0.518 |   1     |         0.307 |      0.025 |
| open_issues |   0.269 |   0.307 |         1     |      0.076 |
| age_days    |   0.06  |   0.025 |         0.076 |      1     |

## Top 20 topics

| Topic | Repos |
|---|---:|
| `claude-code` | 64 |
| `ai-agents` | 61 |
| `codex` | 53 |
| `llm` | 47 |
| `ai-agent` | 34 |
| `developer-tools` | 33 |
| `python` | 33 |
| `mcp` | 31 |
| `agent-skills` | 30 |
| `typescript` | 30 |
| `macos` | 28 |
| `ai` | 26 |
| `react` | 23 |
| `rust` | 22 |
| `windows` | 22 |
| `claude` | 21 |
| `self-hosted` | 21 |
| `open-source` | 20 |
| `awesome-list` | 18 |
| `local-first` | 17 |
