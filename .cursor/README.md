# Agent kit (Qarve / DOQS)

Project rules and skills for Cursor agents working on this open-hardware repository.

## Always-on rules

- `core.mdc` — workflow, mistakes, prompts log, no FCStd edits
- `repo-profile.mdc` — SysML, FreeCAD, OKH, DOQS

## Scoped rules (load when relevant)

| Rule | Topics |
|------|--------|
| `living-docs.mdc` | dev-log, mistakes/, decisions/, architecture.md |
| `doqs-workflow.mdc` | validators, modules, builds, commits |
| `freecad.mdc` | cad/, params, sync |
| `sysml-okh.mdc` | .sysml, okh.toml |
| `prompts-log.mdc` | docs/prompts-log/ |
| `planning-and-testing.mdc` | multi-file work, Python tests |
| `python.mdc` | `**/*.py` |
| `powershell.mdc` | Windows shell |
| `communication.mdc` | response style |
| `subagents.mdc` | delegation |

## Skills

- `mistake-log` — dated files in `docs/mistakes/`
- `prompts-log` — monthly AI log
- `project-skills-md` — `docs/skills.md` patterns

## Portable kit origin

Adapted from a generic coding-project `.cursor` bootstrap. DOQS uses **folder-based** narrative docs; see `docs/decisions/2026-06-04_adopt-doqs-layout.md`.

## Bootstrap stubs

`.cursor/bootstrap/docs/` seeds `docs/onboarding.md`, `docs/architecture.md`, `docs/skills.md` if missing. Do not copy coding-only `mistakes.md` / `decisions.md` stubs over DOQS folders.
