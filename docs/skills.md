# Project skills

Reusable patterns specific to this DOQS repository. Check before implementing; update when a pattern changes.

## Resolve parametric model before CAD sync

**When to use:** Changing dimensions for a named model (default, 500mm, …) on a module that has `cad/params/`.

**Pattern:**

```powershell
# From repo root for top-level CAD, or modules/<name>/ for a sub-assembly
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

**Gotchas:** Run from repository root. `doqs/` must be initialized as a submodule at `qarve/doqs/`.

**Last used:** 2026-06-19 single top-level module

## FreeCAD master sketches in Body_master

**When to use:** Top-down CAD where an assembly `.FCStd` drives child part geometry via `SubShapeBinder`, and a part fails to appear in Assembly **Insert**.

**Pattern:**

- In the assembly file: `Master sketches` group → `Body_master` (`PartDesign::Body`) → sketches constrained to **Body origin planes**.
- Child parts: `SubShapeBinder` → sketches inside `Body_master` (not Assembly origin planes).
- Assembly object holds joints and inserted part links only.

**Gotchas:** Binder from part back to assembly document creates a cycle (assembly → part → assembly). Do not constrain master sketches to `Assembly` origin planes. See `doqs/docs/decisions/2026-06-24_freecad-master-sketches-body.md`.

**Last used:** 2026-06-23 spindle clamp design

## OKH parts from BOM

**When to use:** Agent asked to add manufactured parts to a module manifest.

**Pattern:** Point agent at `<module>/bom/bom.csv` and template `doqs/templates/okh-module-with-parts.toml`.

**Gotchas:** Do not invent geometry — no `.FCStd` edits by agents.

**Last used:** 2026-06-04 repository bootstrap
