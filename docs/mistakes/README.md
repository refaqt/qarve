# Mistakes log

One file per incident: `YYYY-MM-DD_short-topic.md`. Use template `doqs/templates/mistake-entry.md`.

Agents: read all recent entries (or this README’s prevention summary) at task start; append a new file after each mistake — do not use a single `mistakes.md` at repo root.

## Prevention rules (bootstrap)

- Do not edit `.FCStd` files in the agent — use FreeCAD and param CSV workflow.
- Do not hand-edit generated `bom/bom.csv` (root) or `cad/params.csv`.
- Run `doqs/scripts/validate_*.py` before claiming manifests or builds are valid.
