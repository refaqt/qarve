# 2026-06-23 — Spindle clamp design

**Role(s):** engineering

## Goal

Design a spindle clamp sub-assembly (base + jaw) around the JGY-80 spindle model, using top-down master sketches in FreeCAD.

## Work Done

- Iterated spindle clamp layout in `cad/assemblies/spindle-clamp/` (design workspace was later removed after width reduction).
- Added recess in `spindle-clamp-base` for spindle clearance.
- Fixed `spindle-clamp-base` Binder link error (part failed to appear in Assembly Insert).
- Adopted DOQS pattern: master sketches in `Body_master` with Body origin planes (not Assembly origin planes) to break assembly ↔ part document cycle.
- Reduced clamp width; accepted increased height as a trade-off (harder to manufacture on Qarve).
- Explored `spindle-clamp-flex` as an alternative and rejected it: either clamping force must be too high (thick collar) or rigidity is questionable (thin collar).

## Decisions Made

- Top-down driving geometry stays in the assembly file's `Body_master`; parts consume via `SubShapeBinder`.
- Purchased spindle remains reference geometry in `cad/parts/spindle/spindle.FCStd`.
- Width-reduced clamp geometry is preferred over the flex variant.

## Open Questions

- [ ] Torque specs and fastener sizes for clamp screws
- [ ] Export `.step` / `.stl` for manufactured parts after geometry freeze

## Next Steps

- [ ] Integrate spindle clamp into `spindle-assembly` stack
- [ ] Add BOM entries when part list is finalized
