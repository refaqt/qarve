# Agent guide — Qarve (DOQS)

Entry point for Cursor, Claude Code, and other agents working in this repository.

## Shared kit

This repo mounts [refaqt/refaqt-agents](https://github.com/refaqt/refaqt-agents) at [`.agents/`](.agents/).

1. Read [`.agents/rules/core.md`](.agents/rules/core.md) and [`.agents/rules/living-docs.md`](.agents/rules/living-docs.md).
2. Read [`docs/mistakes/`](docs/mistakes/) and state which prevention rules apply.
3. Read [`docs/architecture.md`](docs/architecture.md), then **`doqs/docs/architecture.md`** before non-trivial work.
4. Before new coding solutions, check [`.agents-local/skills/patterns/SKILL.md`](.agents-local/skills/patterns/SKILL.md) if present.

If `.agents/` is empty: `git submodule update --init --recursive`.

## This repository

Qarve is a **modular open-hardware CNC** machine using the [DOQS](https://github.com/refaqt/doqs) documentation system. Repo profile, folder map, hard rules, and living-doc paths: [`.agents-local/rules/repo.md`](.agents-local/rules/repo.md) and [`.agents-local/rules/living-docs.md`](.agents-local/rules/living-docs.md).

Repo-specific skills: [`.agents-local/skills/`](.agents-local/skills/).

## Skills

| Skill | Path |
| --- | --- |
| Activity log | [`.agents/skills/log/SKILL.md`](.agents/skills/log/SKILL.md) |
| Mistake log | [`.agents/skills/mistake-log/SKILL.md`](.agents/skills/mistake-log/SKILL.md) |
| Maintain patterns | [`.agents/skills/maintain-patterns/SKILL.md`](.agents/skills/maintain-patterns/SKILL.md) |
| Coding patterns | [`.agents-local/skills/patterns/SKILL.md`](.agents-local/skills/patterns/SKILL.md) |
| FreeCAD debugging | [`.agents-local/skills/freecad/SKILL.md`](.agents-local/skills/freecad/SKILL.md) |
| DOQS naming | [`.agents-local/skills/doqs-naming/SKILL.md`](.agents-local/skills/doqs-naming/SKILL.md) |

See `.cursor/rules/` for Cursor-specific adapters and scoped rules.
