# Modules

This directory is reserved for **sub-assemblies** — each a full DOQS module with the same layout as the repository root (`bom/`, `cad/`, `architecture/`, `docs/`, `manufacturing/`, `modules/`).

**Current state:** Qarve is a single top-level module. No sub-assemblies exist yet.

When you add the first sub-module:

1. Create `modules/<name>/` with the standard module layout.
2. Register it in the root `okh.toml` via `[[hasComponent]]`.
3. Import its SysML from `architecture/machine.sysml`.
4. Pin it in `builds/<id>/build.toml`.

Later, a sub-module can be extracted to its own repository and linked back as a Git submodule at the same path — see [doqs/docs/architecture.md](../doqs/docs/architecture.md).

Interface version bridges live under `modules/adapters/` by convention.
