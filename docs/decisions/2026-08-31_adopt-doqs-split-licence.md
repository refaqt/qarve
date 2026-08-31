# ADR — Adopt DOQS split-licence layout

- **Date:** 2026-08-31
- **Status:** Accepted

## Context

ADR-001 adopted the DOQS modular layout and left the full CERN-OHL licence text
as a placeholder in the root `LICENSE` file. DOQS now specifies a **content-type
split** at each Git repository root, not a single blanket licence:

| Content | Directories | Licence |
| --- | --- | --- |
| Hardware | `cad/`, `architecture/`, `manufacturing/`, `bom/`, `builds/`, `modules/` | CERN-OHL-S v2.0 |
| Firmware & software | `firmware/`, `software/`, `simulation/` | GPL-3.0 |
| Media & documentation | `docs/`, `measurement/` | CC BY-SA 4.0 |

Templates and validators live in `doqs/scripts/apply_licenses.py` and
`doqs/scripts/validate_licenses.py`.

## Decision

Qarve follows that layout:

- Root `LICENSE` is an overview mapping directories to licences.
- Full legal texts live in `LICENSES/`.
- `TRADEMARKS.md` reserves the organisation and project names/logos.
- Each mapped first-level directory that exists carries a short `LICENSE` stub.
- Root `okh.toml` keeps `license = "CERN-OHL-S-2.0"` (OKH describes the hardware
  project) with a comment pointing at the split.
- README has a Licence section naming all three licences.

Tooling submodules (`doqs/`, `.agents/`) and generated `graph/` are outside the
mapping and do not get directory stubs.

## Consequences

- New first-level content directories need `python doqs/scripts/apply_licenses.py`
  before `validate_all.py` will pass.
- `apply_licenses.py` must not be pointed at `.agents/` or `doqs/`.
- This closes the “full CERN-OHL text still to be finalized” item from ADR-001
  (`docs/decisions/2026-06-04_adopt-doqs-layout.md`).
