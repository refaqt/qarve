# 2026-08-11 — FEM CalculiX assembly material/mesh workflow

**Role(s):** engineering, simulation

## What happened

Investigated CalculiX `femelement_table` errors on `cad/models/test-fem` with an
Assembly-linked multi-material model (`Assembly_model.FCStd` → BooleanFragments
CompSolid → CompoundFilter → Analysis).

- Reproduced a material coverage gap (2706 mesh volumes vs 2430 assigned). Gmsh
  Solid1/2/3 groups sum correctly when counted manually.
- Confirmed FreeCAD binary solid-node search undercounts CompSolid interface C3D10
  elements; assigning material via empty-reference workaround restores full
  coverage (2706/2706).
- Ran CalculiX on a temp copy: ccx exit 0, `.frd` produced.
- After the material fix, a remaining group-data ERROR in the report is expected
  noise — geometry fallback succeeded and full assignment was verified.

## Decisions

- Keep Assembly.FCStd link intact; fix material assignment in the FEM mesh pipeline
  rather than flattening the assembly prematurely.

## Next Steps

- [ ] Document the empty-reference material workaround in the FreeCAD skill if it
  recurs on other CompSolid assemblies.
