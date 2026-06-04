# Project skills

Reusable patterns specific to this DOQS repository. Check before implementing; update when a pattern changes.

## Resolve parametric model before CAD sync

**When to use:** Changing dimensions for a named model (default, 500mm, …).

**Pattern:**

```powershell
cd modules/x-axis
python cad/resolve_params.py 500mm
# Then inside FreeCAD: run cad/sync_params.py
```

**Gotchas:** `cad/params.csv` is gitignored — never edit by hand. Every alias must exist in `default.csv`.

**Last used:** 2026-06-04 repository bootstrap

## Validate before commit

**When to use:** After editing any `okh.toml`, build lockfile, or SysML import.

**Pattern:**

```powershell
python doqs/scripts/validate_okh.py
python doqs/scripts/validate_build.py
python doqs/scripts/build_graph.py
python doqs/scripts/check_links.py
```

**Gotchas:** Run from repository root. `doqs/` manifests are excluded automatically.

**Last used:** 2026-06-04 repository bootstrap

## OKH parts from BOM

**When to use:** Agent asked to add manufactured parts to a module manifest.

**Pattern:** Point agent at `modules/<name>/bom/bom.csv` and template `doqs/templates/okh-module-with-parts.toml`.

**Gotchas:** Do not invent geometry — no `.FCStd` edits by agents.

**Last used:** 2026-06-04 repository bootstrap
