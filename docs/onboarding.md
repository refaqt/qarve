# Onboarding — Qarve (DOQS)

## What this repository is

A **modular open-hardware** CNC machine project using the Documentation System (DOQS): text-first files, identical module layout at every depth, SysML for requirements, FreeCAD for geometry, OKH manifests for publishing.

Qarve is currently a **single top-level module**. Sub-assemblies will be added under `modules/` later.

## Prerequisites

- Git and [Git LFS](https://git-lfs.com/)
- Python 3.11+ (stdlib `tomllib` for validators)
- FreeCAD 1.1+ (Assembly workbench) for CAD work
- [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/) once, for graphical SysML in SysON (optional until you edit models in the browser)

## Setup

```powershell
git clone --recurse-submodules https://github.com/refaqt/qarve.git
cd qarve
git lfs install
bash setup-tooling.sh
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### DOQS tools path

Validators and templates live at **`qarve/doqs/`** (Git submodule). Run all `python doqs/scripts/...` commands from the **qarve repository root**.

A separate clone of [github.com/refaqt/doqs](https://github.com/refaqt/doqs) elsewhere on disk (e.g. `../doqs`) does **not** satisfy these paths. Use `bash setup-tooling.sh` after clone (agents, any OS), or create a junction/symlink from `qarve/doqs` to your existing clone if you prefer that workflow. Humans on Windows may double-click `setup-tooling.bat`.

## Validation (run from repo root)

```powershell
python doqs/scripts/validate_all.py
python doqs/scripts/build_graph.py
python bom/aggregate_bom.py
```

`validate_all.py` runs `validate_okh`, `validate_licenses`, `check_names`, `check_links`, and `validate_build`. To create or refresh split-licence files (`LICENSE`, `LICENSES/`, `TRADEMARKS.md`, per-directory stubs):

```powershell
python doqs/scripts/apply_licenses.py
```

## Graphical SysML (SysON)

Requirements live in `architecture/*.sysml`. To edit them in Eclipse SysON:

1. Install Docker Desktop once (see [doqs/docs/syson.md](../doqs/docs/syson.md)).
2. Double-click `syson.bat` at this repository root (or run `bash syson.sh`).
3. In the control panel, click **Open**, edit in SysON, then click **Save**.
4. Review `git diff` before committing.

Do not use SysON’s homepage **Download** (JSON zip). **Save** writes textual `.sysml` back into `architecture/`.

Agents: `python doqs/scripts/syson.py ui` (do not run `syson.bat`).

## Where to read

| Path | Content |
|------|---------|
| `docs/architecture.md` | Short overview — full spec in `doqs/docs/architecture.md` |
| `LICENSE` / `LICENSES/` / `TRADEMARKS.md` | Split-licence overview, full texts, reserved marks |
| `doqs/docs/readiness-levels.md` | OTRL / ODRL definitions |
| `architecture/*.sysml` | Authoritative requirements and interfaces |
| `modules/*/architecture/` | Sub-module SysML (when `modules/` is populated) |
| `docs/log/` | Activity log (dated entries) |
| `docs/mistakes/` | Incident log (dated files) |
| `docs/decisions/` | ADRs (dated files) |
| `docs/skills.md` | Pointer to `.agents-local/skills/patterns/SKILL.md` |
| `AGENTS.md` | Agent entry point (Cursor, Claude Code, cloud agents) |
| `.agents/` | Git submodule — shared refaqt-agents rules and skills |
| `.agents-local/` | Qarve-only agent rules and skills |
| `.cursor/rules/` | Cursor adapters + DOQS-scoped rules |
| `.claude/skills/` | Claude Code skill symlinks |
| `doqs/templates/` | Entry templates |

## Design session checklist

See root `CONTRIBUTING.md` and the DOQS architecture document in `doqs/docs/architecture.md`.

## Cursor / Claude / agents

- Entry point: [`AGENTS.md`](../AGENTS.md)
- Shared kit: [`.agents/`](../.agents/) ([refaqt-agents](https://github.com/refaqt/refaqt-agents))
- Repo-specific rules: [`.agents-local/rules/`](../.agents-local/rules/)
- Repo-specific skills: [`.agents-local/skills/`](../.agents-local/skills/)
- Cursor adapters: [`.cursor/rules/`](../.cursor/rules/)

Use the shared [`log`](../.agents/skills/log/SKILL.md) skill when a session is worth recording.
