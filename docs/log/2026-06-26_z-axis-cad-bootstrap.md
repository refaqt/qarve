# 2026-06-26 — Z-axis CAD bootstrap

**Role(s):** engineering, cad

## What happened

- Extended spindle assembly work and began the z-slide assembly stack in FreeCAD.
- Added CAD parts and assemblies: z-axis assembly, guide-block, guide-rail-z,
  linear-motor forcer/magnets (`.FCStd` plus `.stp` sources where applicable).
- Committed alongside the guide-rail adjustment FEM setup in
  `simulation/guide-rail-adjustment/`.
- Bumped `doqs/` submodule pointer; excluded regenerable FreeCAD extract artifacts
  (`fcstd-extract/`, `*.zip`) via `.gitignore`.

## Next Steps

- [ ] Continue z-axis assembly integration and parametric joints.
- [ ] Register new parts in `okh.toml` when geometry stabilizes.
