# Agent kit (Qarve / DOQS)

Three layers: shared [refaqt-agents](https://github.com/refaqt/refaqt-agents) at `.agents/`, Qarve-local kit at `.agents-local/`, and these Cursor adapters.

Entry point: [`AGENTS.md`](../AGENTS.md). Claude Code: [`CLAUDE.md`](../CLAUDE.md) imports `AGENTS.md`.

## Always-on rules

- `core.mdc` — `.agents/rules/core.md` + `.agents-local/rules/repo.md`
- `repo-profile.mdc` — `.agents-local/rules/repo.md`
- `living-docs.mdc` — `.agents/rules/living-docs.md` + `.agents-local/rules/living-docs.md`

## Scoped rules (load when relevant)

| Rule | Topics |
|------|--------|
| `doqs-workflow.mdc` | validators, modules, builds, commits |
| `freecad.mdc` | cad/, params, sync, debugging workflow |
| `sysml-okh.mdc` | .sysml, okh.toml |
| `planning-and-testing.mdc` | multi-file work, Python tests |
| `python.mdc` | `**/*.py` |
| `powershell.mdc` | Windows shell |
| `communication.mdc` | response style |
| `subagents.mdc` | delegation |

Rule bodies live in `.agents/rules/` and `.agents-local/rules/`. This folder holds thin `.mdc` adapters only.

## Skills

Skills are **not** duplicated under `.cursor/skills/`. Load from:

| Skill | Path |
| --- | --- |
| Shared process | `.agents/skills/` |
| Qarve-local | `.agents-local/skills/` |
| DOQS domain | `doqs/skills/` (via `.agents-local/` symlinks) |

Claude Code discovers the same skills via symlinks in `.claude/skills/`.

## Bootstrap

Primary stubs: `.agents/bootstrap/docs/`. DOQS templates: `doqs/templates/`. Legacy fallback: `.cursor/bootstrap/docs/` (do not copy over DOQS folder-based mistakes/decisions).

See `docs/decisions/` for layout ADRs.
