# Onboarding — Qarve (DOQS)

## What this repository is

A **modular open-hardware** CNC machine project using the Documentation System (DOQS): text-first files, identical module layout at every depth, SysML for requirements, FreeCAD for geometry, OKH manifests for publishing.

Qarve is currently a **single top-level module**. Sub-assemblies will be added under `modules/` later.

## Prerequisites

- Git and [Git LFS](https://git-lfs.com/)
- Python 3.11+ (stdlib `tomllib` for validators)
- FreeCAD 1.1+ (Assembly workbench) for CAD work
- [SysIDE](https://github.com/sensmetry/sysml-2ls) or similar for SysML editing (optional)

## Setup

```powershell
git clone --recurse-submodules https://github.com/refaqt/qarve.git
cd qarve
git lfs install
git submodule update --init --recursive
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### DOQS tools path

Validators and templates live at **`qarve/doqs/`** (Git submodule). Run all `python doqs/scripts/...` commands from the **qarve repository root**.

A separate clone of [github.com/refaqt/doqs](https://github.com/refaqt/doqs) elsewhere on disk (e.g. `../doqs`) does **not** satisfy these paths. Use `git submodule update --init` after clone, or create a junction/symlink from `qarve/doqs` to your existing clone if you prefer that workflow.

## Validation (run from repo root)

```powershell
python doqs/scripts/validate_okh.py
python doqs/scripts/validate_build.py
python doqs/scripts/build_graph.py
python doqs/scripts/check_links.py
python bom/aggregate_bom.py
```

## Where to read

| Path | Content |
|------|---------|
| `docs/architecture.md` | Short overview — full spec in `doqs/docs/architecture.md` |
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
