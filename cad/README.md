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
| `parts/spindle-clamp-base/` | Clamp base part |
| `parts/spindle-clamp-jaw/` | Clamp jaw part |
| `exports/` | `.step`, `.stl` committed after significant changes |

Binary `.FCStd` / `.stl` use Git LFS (see root `.gitattributes`).
