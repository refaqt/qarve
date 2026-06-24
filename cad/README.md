# Top-level CAD

- **FreeCAD:** v1.1+ with built-in Assembly workbench.
- **Relative paths:** `Edit → Preferences → General → Document → Use relative paths when saving external links`.

## Paths

| Path | Purpose |
|------|---------|
| `assemblies/machine.FCStd` | Top assembly (future; may link into `modules/*/cad/` when sub-assemblies exist) |
| `assemblies/spindle-assembly/` | Spindle stack assembly |
| `assemblies/spindle-clamp/` | Spindle clamp sub-assembly |
| `assemblies/spindle-clamp/spindle-clamp-design.FCStd` | Design workspace (master sketches, layout exploration) |
| `parts/spindle/` | Purchased spindle model (JGY-80) and reference images |
| `parts/spindle-clamp-base/` | Clamp base part (recess for spindle clearance) |
| `parts/spindle-clamp-jaw/` | Clamp jaw part |
| `exports/` | `.step`, `.stl` committed after significant changes |

## Top-down design (spindle clamp)

Master sketches for the clamp live in `spindle-clamp.FCStd` inside a `Master sketches` group and a dedicated `Body_master` (`PartDesign::Body`). Sketches use **that Body's origin planes**, not the `Assembly` object's origin planes. Child parts (`spindle-clamp-base`, `spindle-clamp-jaw`) consume geometry via `SubShapeBinder` pointing at sketches inside `Body_master`.

This avoids a circular document dependency (assembly → part → assembly) that blocks Assembly **Insert**. See `doqs/docs/decisions/2026-06-24_freecad-master-sketches-body.md` and `doqs/docs/architecture.md` (Top-down design and master sketches).

Binary `.FCStd` / `.stl` use Git LFS (see root `.gitattributes`).
