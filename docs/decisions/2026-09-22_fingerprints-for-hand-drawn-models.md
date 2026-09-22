# ADR — Measure hand-drawn FreeCAD models instead of rebuilding them

- **Date:** 2026-09-22
- **Status:** Accepted

## Context

Every FreeCAD document in this repository needs a small measurement file beside
it, called a fingerprint. The automatic checks refuse a model without one. The
measurement records the size, the position and the volume of each object, so a
change to the geometry shows up as readable text in a pull request instead of
hiding inside a binary file.

DOQS writes that file as a side effect of rebuilding a part from its parameters:

```powershell
FreeCADCmd cad/build_model.py
```

Qarve does not work that way. The geometry is drawn by hand in the FreeCAD
window, and hard rule 1 in the agent guide says it stays that way. There is no
build script that could produce these 44 documents, and writing 44 of them by
hand would be a large piece of work that changes how the machine is designed.

Without a decision, the repository could never pass its own checks.

## Decision

Measure the saved file instead of rebuilding it.

`cad/fingerprint_models.py` opens each document in its own FreeCAD process,
measures what the file holds, and writes the fingerprint beside it. It never
saves a `.FCStd`. Geometry keeps changing only in the FreeCAD window, by hand.

Two details matter.

**The measurement describes the saved file, not a refreshed version of it.**
FreeCAD marks a document as changed while it loads a linked part, even when no
geometry moved. The script clears that flag so the measurement counts as coming
from the saved file, which is exactly what it is.

**A document that no longer agrees with itself is reported, not corrected.**
After measuring, the script refreshes the document in memory and compares. If
the geometry moves, the saved file no longer matches its own sketches and
joints. The script names those documents at the end of its run. Only a person
can fix that, in FreeCAD.

## Consequences

- After you save a model in FreeCAD, run `python cad/fingerprint_models.py`
  before you commit. The checks fail if the measurement and the model disagree.
- The measurement is tied to the exact bytes of the `.FCStd`. Saving the model
  again always means writing the fingerprint again.
- If Qarve ever adds parametric parts with a build script, those parts use the
  DOQS route and this script leaves them alone: it writes the same file in the
  same place.
- The script needs FreeCAD 1.1 on the computer that runs it. The build server
  only reads the committed files and does not need FreeCAD.
