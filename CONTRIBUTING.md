# Contributing

## Principles

- **Text-first:** Prefer CSV, SysML, TOML, and Markdown over opaque binaries.
- **Never edit generated files:** Root `bom/bom.csv`, module `cad/params.csv`, `graph/usage-graph.json` (regenerate with scripts).
- **Requirements live in SysML** under `architecture/` — not duplicate requirement docs.
- **Geometry in FreeCAD:** Agents must not edit `.FCStd` files; change parameters via `cad/params/` and `sync_params.py`.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short description>
```

Types include: `feat`, `fix`, `docs`, `cad`, `arch`, `okh`, `firmware`, `chore`, `refactor`, `interface`, `model`, `build`, `params`.

## Before opening a PR

1. Run validators under `doqs/scripts/`.
2. Update dev-log / ADR / mistakes entries in `docs/` when applicable.
3. Regenerate aggregated BOM and usage graph if manifests or lockfiles changed.

## Branches

- `main` — next major version development
- `release/vN.x` — long-term support for deployed machines (see architecture doc)

## Modules

To add a sub-assembly, create `modules/<name>/` with the standard DOQS module layout (see `doqs/docs/architecture.md`) and register it in the root `okh.toml` via `[[hasComponent]]`.
