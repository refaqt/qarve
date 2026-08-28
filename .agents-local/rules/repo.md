# Qarve repository profile

Agent-only. Humans: see `README.md` and `docs/onboarding.md`.

## What this repository is

Qarve is an open-hardware modular CNC machine using the [DOQS](https://github.com/refaqt/doqs)
documentation system. The repository root is the **top-level DOQS module**; sub-assemblies will
live under `modules/` when added (empty today).

Shared agent kit: [refaqt/refaqt-agents](https://github.com/refaqt/refaqt-agents) at `.agents/`.
DOQS validators and templates: `doqs/` submodule.

## Where things go

| You are adding | It goes in |
| --- | --- |
| A day's work write-up | `docs/log/YYYY-MM-DD_topic.md` |
| Why a choice was made | `docs/decisions/YYYY-MM-DD_topic.md` |
| Something that went wrong | `docs/mistakes/YYYY-MM-DD_topic.md` |
| System requirements | `architecture/*.sysml` |
| Module requirements | `modules/*/architecture/*.sysml` |
| FreeCAD geometry | `cad/` (manual edits only) |
| Parameters | `cad/params/*.csv` → `cad/resolve_params.py` |
| Physical machine lockfile | `builds/<id>/build.toml` |
| A reusable coding pattern | `.agents-local/skills/patterns/SKILL.md` |

## doqs references

| Read | When |
| --- | --- |
| `doqs/docs/architecture.md` | New modules, versioning, interfaces, builds |
| `doqs/docs/readiness-levels.md` | OTRL / ODRL in `okh.toml` |
| `doqs/docs/naming.md` | Naming modules, parts, interfaces |
| `doqs/docs/agent-guide.md` | Three-layer agent model |
| `doqs/templates/` | Log, ADR, mistake, OKH entry templates |

`docs/architecture.md` is a short overview — SysML remains authoritative.

Before non-trivial work, read `docs/architecture.md`, then **`doqs/docs/architecture.md`**
(run `git submodule update --init` if missing). Read relevant `architecture/*.sysml`.

## Stack and execution

- **SysML** in `architecture/` and, when present, `modules/*/architecture/`.
- **FreeCAD** 1.1+ with Assembly workbench; parameters via `cad/params/*.csv` and `sync_params.py`.
- **OKH** manifests: `okh.toml` per module; validate with `doqs/scripts/validate_okh.py`.
- Run commands from the **repository root**.
- If `doqs/` or `.agents/` is empty: `git submodule update --init --recursive`.
- Before new solutions, read `.agents-local/skills/patterns/SKILL.md` and use the
  `maintain-patterns` skill.

## Hard rules

1. **Never edit `.FCStd` files** — geometry changes happen in FreeCAD manually.
2. **Requirements live in SysML** (`architecture/`) — do not duplicate as standalone requirement docs.
3. **Run validators** after OKH or build changes: `python doqs/scripts/validate_okh.py` (and siblings).
4. **Prefer** CSV/TOML/SysML output; validate before commit.
5. For OTRL/ODRL or naming, read `doqs/docs/readiness-levels.md` and `doqs/docs/naming.md`.

## Validate

```bash
python doqs/scripts/validate_okh.py
python doqs/scripts/validate_build.py
python doqs/scripts/build_graph.py
python doqs/scripts/check_links.py
python bom/aggregate_bom.py
```

## Conventions

- **Commits:** `<type>(<scope>): <description>` — `feat`, `fix`, `docs`, `cad`, `arch`, `okh`,
  `firmware`, `chore`, `refactor`, `interface`, `model`, `build`, `params`
- Qarve is currently a single top-level module; `modules/` is reserved for future sub-assemblies.
