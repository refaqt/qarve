# Changelog

All notable releases of this repository are documented here.

## [Unreleased]

### Added

- Initial DOQS repository scaffold (modular layout, validators, agent rules).
- Embedded `doqs/` tooling via Git submodule (scripts, templates, schemas).
- Spindle CAD: `cad/assemblies/spindle-assembly/`, `cad/assemblies/spindle-clamp/`, and related parts under `cad/parts/`.
- ADR-002: single top-level module (`docs/decisions/2026-06-19_single-top-level-module.md`).

### Changed

- Single top-level module: removed example `modules/frame` and `modules/x-axis` scaffolds; `modules/` reserved for future sub-assemblies.
