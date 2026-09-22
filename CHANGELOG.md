# Changelog

All notable releases of this repository are documented here.

## [Unreleased]

### Added

- Initial DOQS repository scaffold (modular layout, validators, agent rules).
- Embedded `doqs/` tooling via Git submodule (scripts, templates, schemas).
- Spindle CAD: `cad/assemblies/spindle-assembly/`, `cad/assemblies/spindle-clamp/`, and related parts under `cad/parts/`.
- ADR-002: single top-level module (`docs/decisions/2026-06-19_single-top-level-module.md`).
- Spindle clamp sub-assembly: top-down design with `spindle-clamp-base` and `spindle-clamp-jaw` parts; recess in clamp base for spindle clearance.
- Spindle clamp flex part: `cad/parts/spindle-clamp-flex/spindle-clamp-flex.FCStd`.
- `[[part]]` entries in `okh.toml` for spindle-clamp manufactured parts.
- Guide-rail adjustment FEM study: 5 mm POM layer under the rail compressed by screw preload to correct a bend in the guide (`simulation/guide-rail-adjustment/guide-rail-adjustment.FCStd`).
- A measurement file beside every FreeCAD model, so a change to the geometry can be read as text in a pull request.
- `cad/fingerprint_models.py` writes those measurement files. Run it after saving a model in FreeCAD.
- ADR: why this repository measures hand-drawn models instead of rebuilding them (`docs/decisions/2026-09-22_fingerprints-for-hand-drawn-models.md`).

### Changed

- Split-licence layout per current DOQS spec: CERN-OHL-S v2.0 (hardware), GPL-3.0 (firmware/software/simulation), CC BY-SA 4.0 (docs/media), with `LICENSES/` full texts, `TRADEMARKS.md`, and per-directory `LICENSE` stubs.
- `doqs/` submodule bumped to include the split-licence apply/validate scripts; licence scanner skips `.agents/` tooling submodule.
- CI and onboarding validation run `doqs/scripts/validate_all.py` (includes `validate_licenses`).
- Single top-level module: removed example `modules/frame` and `modules/x-axis` scaffolds; `modules/` reserved for future sub-assemblies.
- Spindle clamp assembly: master sketches moved to `Body_master` per DOQS ADR (fixes Assembly Insert / Binder cycle); see `doqs/docs/decisions/2026-06-24_freecad-master-sketches-body.md`.
- Spindle clamp geometry: reduced clamp width; removed obsolete `spindle-clamp-design.FCStd`.
- `doqs/` submodule bumped to `71d6216` (FreeCAD master-sketches Body ADR and architecture docs).
- The automatic checks, the README and the setup guide now use one command, `python doqs/doqs.py check`. It replaces the separate validation scripts, two of which had been renamed and no longer ran.
- The build server now fetches the real FreeCAD models instead of the small stubs Git LFS leaves behind. Without this, the model check compares each measurement against a stub.
- Every shell file is now stored with Unix line endings, not only the two that were named one by one. A shell script saved with Windows line endings fails to start.

### Removed

- The example machine record `builds/serial-0042/`. It described a machine that does not exist and pointed at a version tag that was never created. The blank example to copy from, `builds/example-baseline.toml`, is unchanged.
- `bom/aggregate_bom.py`. It was an old copy of a tool that lives in the `doqs/` submodule and had fallen behind it.
