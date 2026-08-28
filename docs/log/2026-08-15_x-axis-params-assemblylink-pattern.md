# 2026-08-15 — X-axis Params and AssemblyLink pattern

**Role(s):** engineering, cad

## What happened

Diagnosed broken `linear-guide-x` joints in `x-axis.FCStd`: `Joint005` Distance
expressions could not read `x_axis_position` from linked `x-axis_Params` — Joint005
showed Invalid in the parent assembly.

Root causes:

- Wrong cross-document expression syntax for spreadsheet aliases.
- `AssemblyLink::synchronizeJoints` copies Distance float values into the parent but
  does **not** bring the child's Params `App::Link` into the parent document.

Proposed cycle-free topology (matches DOQS skeleton/params guidance and FreeCAD
master-spreadsheet DAG pattern):

- Params live in a dedicated leaf document (`x-axis_Params.FCStd`).
- Each consumer gets `LinkMake` to the Params spreadsheet.
- Machine-level Distance constraints on the x-axis assembly are owned by `x-axis`,
  not duplicated inside linked children.

## Decisions

- Do not drive child joints from parent-linked spreadsheets via AssemblyLink sync;
  use explicit Params links in each document that needs them.

## Next Steps

- [ ] Apply the Params → LinkMake → consumer pattern across x-axis sub-assemblies.
- [ ] Capture param aliases in `cad/params/` CSV when values stabilize.
