# 2026-08-31 — apply_licenses wrote into .agents

## What happened

Running `python doqs/scripts/apply_licenses.py` from the machine root wrote a
CERN-OHL-S machine licence kit into the `.agents/` submodule (refaqt-agents),
overwriting its GPL `LICENSE`. The files were reverted; `.agents/` was left clean.

## Why it went wrong

`iter_submodule_paths` treated every non-`doqs` Git submodule as an extracted
machine module. Qarve also mounts [refaqt-agents](https://github.com/refaqt/refaqt-agents)
at `.agents/`, which is tooling, not a module (no `okh.toml`).

## Prevention rule

After `apply_licenses.py`, confirm `.agents/` and `doqs/` are unmodified.
`apply_licenses.py` / `validate_licenses.py` must skip tooling submodules
(`doqs/`, `.agents/`) and any submodule without `okh.toml`.

## Related

- `docs/decisions/2026-08-31_adopt-doqs-split-licence.md`
- doqs commit `a472e09` (`cursor/skip-agents-licence-scan-3e45`)
