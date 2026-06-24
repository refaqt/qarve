# Changelog

All notable releases of this repository are documented here.

## [Unreleased]

### Added

- Initial DOQS repository scaffold (modular layout, validators, agent rules).
- Embedded `doqs/` tooling via Git submodule (scripts, templates, schemas).
- Spindle CAD: `cad/assemblies/spindle-assembly/`, `cad/assemblies/spindle-clamp/`, and related parts under `cad/parts/`.
- ADR-002: single top-level module (`docs/decisions/2026-06-19_single-top-level-module.md`).
- Spindle clamp sub-assembly: top-down design with `spindle-clamp-base` and `spindle-clamp-jaw` parts; recess in clamp base for spindle clearance.
- `[[part]]` entries in `okh.toml` for spindle-clamp manufactured parts.

### Changed

- Single top-level module: removed example `modules/frame` and `modules/x-axis` scaffolds; `modules/` reserved for future sub-assemblies.
- Spindle clamp assembly: master sketches moved to `Body_master` per DOQS ADR (fixes Assembly Insert / Binder cycle); see `doqs/docs/decisions/2026-06-24_freecad-master-sketches-body.md`.
- `doqs/` submodule bumped to `71d6216` (FreeCAD master-sketches Body ADR and architecture docs).
