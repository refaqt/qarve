# 2026-09-01 — Always-latest tooling submodules

**Role(s):** engineering

## What happened

Added copy-once root helpers `setup-tooling.sh` / `setup-tooling.bat` so agents and humans fetch latest `main` of `doqs/` and `.agents/` after clone. Set `branch = main` on those tooling submodules. Prepended **First step (required)** to `AGENTS.md` (agents: `bash setup-tooling.sh`; humans on Windows may double-click the `.bat`). Swept leftover `git submodule update --init` lines in onboarding, `repo.md`, and `doqs-workflow.md`. CI still checks out the recorded pin.

## Decisions

Working tree tracks `main` via the helper; gitlinks stay pins unless we freeze one. Helpers are copied from doqs templates, not written by doqs scripts. See [2026-09-01_always-latest-tooling-submodules.md](../decisions/2026-09-01_always-latest-tooling-submodules.md).

## Next Steps

Commit per repo when asked; do not push unless asked. Do not commit dirty submodule gitlinks after a local helper test.
