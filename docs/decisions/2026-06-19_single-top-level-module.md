# ADR-002 — Single top-level module (defer sub-assemblies)

- **Date:** 2026-06-19
- **Status:** Accepted

## Context

Qarve was bootstrapped with example sub-modules (`modules/frame`, `modules/x-axis`) to demonstrate DOQS multi-module composition. Early development is simpler as one repository and one top-level module. Hardware sub-modules may later live under `modules/` and optionally be extracted to separate repositories.

The `doqs/` Git submodule (shared tools and specification) remains unchanged.

## Decision

- Operate Qarve as a **single top-level DOQS module** at the repository root.
- Remove example scaffolds under `modules/frame` and `modules/x-axis`.
- Keep `modules/` (and `modules/adapters/`) as placeholders for future sub-assemblies.
- Root `okh.toml` has no `[[hasComponent]]` entries until real sub-modules are added.
- Build lockfiles pin `[base]` only until sub-modules exist.

## Consequences

- `architecture/machine.sysml` holds machine-level requirements only; no sub-module imports until added.
- Agents and docs should not assume active sub-modules under `modules/`.
- Adding the first sub-assembly follows `modules/README.md` and `doqs/docs/architecture.md`.
- Extraction to separate repos remains a future option (DOQS Mode B); not implemented now.
