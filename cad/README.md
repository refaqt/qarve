# Top-level CAD

- **FreeCAD:** v1.1+ with built-in Assembly workbench.
- **Relative paths:** `Edit → Preferences → General → Document → Use relative paths when saving external links`.

## Paths

| Path | Purpose |
|------|---------|
| `assemblies/machine.FCStd` | Top assembly (links into `modules/*/cad/`) |
| `exports/` | `.step`, `.stl` committed after significant changes |

Binary `.FCStd` / `.stl` use Git LFS (see root `.gitattributes`).
