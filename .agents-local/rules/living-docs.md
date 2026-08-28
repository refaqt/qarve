# Qarve living documentation

Repo-specific paths and update triggers. Shared rules:
[`.agents/rules/living-docs.md`](../../.agents/rules/living-docs.md).

## Narrative docs

| Location | Purpose | Update when |
| --- | --- | --- |
| `docs/log/YYYY-MM-DD_topic.md` | Activity log (any role) | A working session worth recording |
| `docs/mistakes/YYYY-MM-DD_topic.md` | Incidents | After mistakes (skill: [`.agents/skills/mistake-log/SKILL.md`](../../.agents/skills/mistake-log/SKILL.md)) |
| `docs/decisions/` | ADRs | Non-trivial choices (template: [`.agents/templates/adr.md`](../../.agents/templates/adr.md)) |
| `.agents-local/skills/patterns/SKILL.md` | Reusable agent patterns | New project-specific pattern |
| `docs/onboarding.md` | Setup and validation | Tooling or workflow changes |
| `docs/architecture.md` | Human overview (SysML remains authoritative) | Layout or major modules change |

Use the shared [`log`](../../.agents/skills/log/SKILL.md) skill when adding log entries.
Update `docs/log/README.md` index when adding a file.

## System model (`architecture/`)

| Location | Purpose | Update when |
| --- | --- | --- |
| `architecture/*.sysml` | Machine requirements, composition | System scope changes |
| `modules/*/architecture/*.sysml` | Module requirements, ports | Module behaviour or interfaces change |

Also update `okh.toml` `[[provides-interface]]` / `[[consumes-interface]]` when ports change.

## Generated artefacts

Regenerate — do not hand-edit:

- `graph/usage-graph.json` — `python doqs/scripts/build_graph.py`
- Root `bom/bom.csv` — `python bom/aggregate_bom.py`
- `cad/params.csv` — `python cad/resolve_params.py <model>`

Generic stubs: [`.agents/bootstrap/docs/`](../../.agents/bootstrap/docs/).

If living-doc folders are missing, bootstrap from [`.agents/bootstrap/docs/`](../../.agents/bootstrap/docs/).
