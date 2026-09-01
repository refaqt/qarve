# ADR — Always-latest tooling submodules

- **Date:** 2026-09-01
- **Status:** Accepted

## Context

`doqs/` and `.agents/` are tooling submodules. Agents and humans were told to `git submodule update --init --recursive`, which checks out the **recorded pin**. CI should stay on that pin, but daily work (humans, Claude Code, cloud agents) should see latest `main` of the shared kits without committing a gitlink bump after every fetch.

doqs must not write consumer-root files (`AGENTS.md`, `README.md`, `setup-tooling.*`). First-step wording for agents lives in [refaqt-agents](https://github.com/refaqt/refaqt-agents) templates.

## Decision

- Copy-once helpers `setup-tooling.sh` and `setup-tooling.bat` live at this **repo root** (templates in `doqs/templates/setup-tooling/`). They run `git submodule sync --recursive` then `git submodule update --init --recursive --remote`.
- `.gitmodules` sets `branch = main` only on tooling submodules (`doqs`, `.agents`). Extracted machine modules stay SHA-pinned without `branch`.
- **All agents, any OS:** `bash setup-tooling.sh`. **Humans on Windows** may double-click `setup-tooling.bat` (`pause` is OK there only). Agents must not run the `.bat`.
- Do not commit dirty submodule gitlinks after `--remote` unless freezing a pin. GitHub Actions keep `submodules: recursive` (recorded pin).
- `setup-tooling.sh` is stored with LF (`setup-tooling.sh text eol=lf` in `.gitattributes`).

## Consequences

- Working tree tracks latest `main` of the kits after the helper runs; the committed gitlink remains a pin for CI and clones that skip the helper.
- New machine repos copy the helpers from doqs templates to their own root; they never run them from `doqs/templates/setup-tooling/`.
- `AGENTS.md` first-step text is maintained in refaqt-agents and prepended here.
