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

Qarve is a **modular open-hardware CNC** machine using the [DOQS](https://github.com/refaqt/doqs) documentation system. Validators and templates live in the **`doqs/`** submodule at the repo root.

| Activity | Path |
| --- | --- |
| Design session log | `docs/dev-log/YYYY-MM-DD_topic.md` |
| AI task audit | `docs/prompts-log/YYYY-MM.md` |
| Mistakes | `docs/mistakes/YYYY-MM-DD_topic.md` |
| ADRs | `docs/decisions/YYYY-MM-DD_topic.md` |
| Architecture overview | `docs/architecture.md` → `doqs/docs/architecture.md` |
| Requirements (authoritative) | `architecture/*.sysml` |

Repo-specific skills: [`.agents-local/skills/`](.agents-local/skills/).

## Hard rules

1. **Never edit `.FCStd` files** — geometry changes happen in FreeCAD manually.
2. **Requirements live in SysML** (`architecture/`) — do not duplicate as standalone requirement docs.
3. **Run validators** after OKH or build changes: `python doqs/scripts/validate_okh.py` (and siblings).
4. **Prefer** CSV/TOML/SysML output; validate before commit.
5. For OTRL/ODRL or naming, read `doqs/docs/readiness-levels.md` and `doqs/docs/naming.md`.

## Logging rule

After completing any task, append an entry to `docs/prompts-log/YYYY-MM.md` (current year-month).

Format:

---

### HH:MM — Short task title

**Prompt:** "..."

**Actions:**

- ...

**Files changed:**

- `path/to/file` — created / modified / deleted

**Outcome:** One sentence.

---

## Skills

| Skill | Path |
| --- | --- |
| Activity log | `.agents/skills/log/SKILL.md` |
| Mistake log | `.agents/skills/mistake-log/SKILL.md` |
| Maintain patterns | `.agents/skills/maintain-patterns/SKILL.md` |
| Prompts log | `.agents-local/skills/prompts-log/SKILL.md` |
| FreeCAD debugging | `.agents-local/skills/freecad/SKILL.md` |
| DOQS naming | `.agents-local/skills/doqs-naming/SKILL.md` |

## Pointed tasks

Example: *"Look at `bom/bom.csv` (when present) and draft `[[part]]` entries using `doqs/templates/okh-module-with-parts.toml`."*

See `.cursor/rules/` for Cursor-specific adapters and scoped rules.
