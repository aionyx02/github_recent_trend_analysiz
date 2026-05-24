---
type: release_policy
status: active
priority: p2
updated: 2026-05-24
context_policy: retrieve_when_planning
owner: project
---

# Release And Deployment

## Purpose

Record deployment and rollback expectations. Keep secrets out of this file.

## Release Checklist

- [ ] `npm run docs:refresh` passes (no FAIL lines).
- [ ] `python -m pytest -q` is green.
- [ ] `ruff check .` is clean.
- [ ] `requirements.txt` reflects every runtime import in `dashboard/app.py` + `src/visualize.py` + `src/config.py`.
- [ ] CSVs in `data/processed/` are current (re-run `python -m src.collect_all && python -m src.build_charts` if stale).
- [ ] README still renders correctly on GitHub (relative paths to `outputs/figures/*.png` intact).

## Validation Commands

```bash
ruff check .
python -m pytest -q
npm run docs:refresh
```

## Streamlit Community Cloud Deployment

The Streamlit dashboard is deployed at <https://share.streamlit.io> as a public, free, GitHub-integrated app. Runtime requirements are listed in the repo-root `requirements.txt`, theme in `.streamlit/config.toml`. The dashboard reads pre-collected CSVs from `data/processed/` and does **not** require `GITHUB_TOKEN` at runtime.

### First-time deploy (one-off)

1. Visit <https://share.streamlit.io> and authenticate with GitHub.
2. Click **Create app** → connect the repository (`aionyx02/github_recent_trend_analysiz`).
3. Pick branch `main`, main file path `dashboard/app.py`.
4. (Optional) under **Advanced settings**, set Python version to `3.13` if 3.14 is not yet available on Cloud.
5. Click **Deploy**. First build takes ~3-5 minutes; subsequent rebuilds ~30 seconds.

### Updates

Streamlit Cloud auto-rebuilds on every push to `main`. No manual step needed when:

- Dataset is regenerated (`data/processed/*.csv` committed).
- Dashboard code changes (`dashboard/app.py` or `src/*` imports).
- `requirements.txt` changes.

Cache is cleared automatically on rebuild because `@st.cache_data` decorators are keyed by file contents.

### Manage / debug

- App settings, logs, restart, delete: **Manage app** menu in the Streamlit Cloud sidebar.
- Reading logs: deploy logs live in **Manage app → Logs**; runtime errors surface to the same place.
- Pausing: free-tier apps sleep after inactivity; first request after a sleep takes ~10s to wake.

### When deployment fails

Most common failure: a Python dependency missing from `requirements.txt`. Cloud's stderr will name the failed import — add the package and push again. Avoid pinning exact versions in `requirements.txt`; use lower bounds (`>=`) so Cloud can pick its own platform wheels.

## Rollback Notes

- **Streamlit Cloud**: revert the app to a previous deploy via **Manage app → History**, or delete and recreate from an earlier commit.
- **Repo**: standard `git revert <commit>` is preferred over `git reset --hard` once anything is shared.
- **Data**: `data/processed/*.csv` is regeneratable from `data/raw/*.json`. The raw layer is gitignored but reproducible via `python -m src.collect_all` with a valid token.
- **Token leakage** (incident class): if a real `GITHUB_TOKEN` is ever committed, revoke at <https://github.com/settings/tokens> first, then rewrite history with `git rebase -i` and force-push. Local reflog must also be purged: `git reflog expire --expire=now --all && git gc --prune=now --aggressive`.
