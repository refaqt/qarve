# Top-level CAD

- **FreeCAD:** v1.1+ with built-in Assembly workbench.
- **Relative paths:** `Edit → Preferences → General → Document → Use relative paths when saving external links`.

## Paths

| Path | Purpose |
|------|---------|
| `assemblies/machine.FCStd` | Top assembly (future; may link into `modules/*/cad/` when sub-assemblies exist) |
| `assemblies/spindle-assembly/` | Spindle stack assembly |
| `assemblies/spindle-clamp/` | Spindle clamp sub-assembly |
| `parts/spindle/` | Purchased spindle model (JGY-80) and reference images |
| `parts/spindle-clamp-base/` | Clamp base part (recess for spindle clearance) |
| `parts/spindle-clamp-jaw/` | Clamp jaw part |
| `parts/spindle-clamp-flex/` | Clamp flex part |
| `exports/` | `.step`, `.stl` committed after significant changes |

## Top-down design (spindle clamp)

Master sketches for the clamp live in `spindle-clamp.FCStd` inside a `Master sketches` group and a dedicated `Body_master` (`PartDesign::Body`). Sketches use **that Body's origin planes**, not the `Assembly` object's origin planes. Child parts (`spindle-clamp-base`, `spindle-clamp-jaw`) consume geometry via `SubShapeBinder` pointing at sketches inside `Body_master`.

This avoids a circular document dependency (assembly → part → assembly) that blocks Assembly **Insert**. See `doqs/docs/decisions/2026-06-24_freecad-master-sketches-body.md` and `doqs/docs/architecture.md` (Top-down design and master sketches).

Binary `.FCStd` / `.stl` use Git LFS (see root `.gitattributes`).

## After you save a model

Every `.FCStd` has a `.fingerprint.json` beside it. It lists the size, the
position and the volume of each object, so a change to the geometry can be read
as text in a pull request. The checks fail when a model and its measurement
disagree.

Run this from the repository root after saving, and commit the model and the
measurement together:

```powershell
python cad/fingerprint_models.py
```

The script opens each model, measures it and closes it. It never saves a
`.FCStd`: geometry changes stay manual, in the FreeCAD window. The run ends by
naming any model whose geometry moves when FreeCAD refreshes it, which means the
saved file no longer matches its own sketches and joints.

Why this repository measures models instead of rebuilding them:
[`docs/decisions/2026-09-22_fingerprints-for-hand-drawn-models.md`](../docs/decisions/2026-09-22_fingerprints-for-hand-drawn-models.md).
