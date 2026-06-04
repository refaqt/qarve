# X-axis CAD

Spreadsheet alias names must match `cad/params/default.csv` (and model overrides).

## Workflow

1. `python cad/resolve_params.py <model>` → writes `cad/params.csv` (gitignored)
2. Open `cad/assemblies/x-axis.FCStd` in FreeCAD and run `cad/sync_params.py`
