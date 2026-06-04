# X-Axis module

Linear motion axis (example module scaffold). See `okh.toml` for OKH metadata and `architecture/x-axis.sysml` for requirements and interfaces.

## Parametric models

```powershell
python cad/resolve_params.py default
python cad/resolve_params.py 500mm
```

Then sync into FreeCAD: `cad/sync_params.py` (inside FreeCAD runtime).
