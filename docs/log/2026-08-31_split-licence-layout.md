# 2026-08-31 — Split-licence layout

**Role(s):** engineering

## What happened

- Applied the DOQS split-licence kit at the Qarve repository root: `LICENSE` overview,
  `LICENSES/` full texts (CERN-OHL-S-2.0, GPL-3.0, CC BY-SA 4.0), `TRADEMARKS.md`, and
  per-directory `LICENSE` stubs for existing first-level content folders.
- Bumped the `doqs/` submodule to latest main plus a follow-up fix so
  `apply_licenses.py` / `validate_licenses.py` skip the `.agents/` tooling submodule.
- Pointed README, `okh.toml`, onboarding, CI, and agent rules at `validate_all.py`.

## Decisions

- Follow the DOQS content-type split rather than a single CERN-OHL-S blanket at repo root.
  See `docs/decisions/2026-08-31_adopt-doqs-split-licence.md`.

## Next Steps

- Merge the companion doqs branch `cursor/skip-agents-licence-scan-3e45` so machine
  repos on doqs `main` also skip `.agents/`.
