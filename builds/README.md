# Physical machine builds

Each subdirectory is one real machine instance (serial, prototype, or customer build). `build.toml` pins the machine repo version and, when sub-assemblies exist, each module version and parametric model — like `Cargo.lock` for hardware.

## New build

1. Copy `example-baseline.toml` to `<your-id>/build.toml`.
2. Set `[base]` to the qarve repo and tag. Add `[[module]]` entries when sub-assemblies exist under `modules/`.
3. Run `python doqs/scripts/validate_build.py`.
4. Add photos and `notes.md` for non-standard modifications.

External forks may list themselves in root `known-consumers.toml` for the reverse usage graph.
