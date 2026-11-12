# ADR — Keep the layout models under cad/assemblies/

- **Date:** 2026-11-12
- **Status:** Accepted

## Context

`cad/architecture/` held six hand-drawn layout models: the machine layout and
the axis configuration studies. They hold sketches, datums and binders. They
are not parts that an assembly inserts.

The newer doqs (`validate_cad.py`, rule 5, "A Part on top") requires that every
`PartDesign::Body` in a part document sits inside an `App::Part` container. The
only exceptions are documents under `cad/assemblies/` and documents that hold an
Assembly. These are top-down documents whose master sketches live in a Body
(`doqs/docs/decisions/2026-06-24_freecad-master-sketches-body.md`). Our six
layout models are the same kind of document, but their folder put them in the
part rules. CI failed on all six.

## Decision

Move the folder as a whole to `cad/assemblies/architecture/`. Keep the file
names.

- The fingerprints stay valid. They record the file name and its checksum, not
  the folder.
- Keeping the names avoids a clash with `cad/assemblies/machine/machine.FCStd`
  and avoids editing fingerprints by hand.
- The `.FCStd` files themselves are not changed (hard rule 1).

## Consequences

- The layout models get the assembly rules, which fit how they are drawn.
- The folder holds six documents, not one assembly per folder like the rest of
  `cad/assemblies/`.
- `machine.FCStd` has five SubShapeBinders. If any of them links to a file
  outside its own document, the relative path is now one folder deeper. Open
  `machine.FCStd` once in FreeCAD after this move and check that the binders
  still resolve.
- Log entries that named `cad/architecture/` now name the new folder.
