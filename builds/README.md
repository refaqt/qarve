# Physical machine builds

Each subdirectory is one real machine instance (serial, prototype, or customer build). `build.toml` pins exact module versions and parametric models — like `Cargo.lock` for hardware.

## New build

1. Copy `example-baseline.toml` to `<your-id>/build.toml`.
2. Pin versions and models for every module in the composition.
3. Run `python doqs/scripts/validate_build.py`.
4. Add photos and `notes.md` for non-standard modifications.

External forks may list themselves in root `known-consumers.toml` for the reverse usage graph.
