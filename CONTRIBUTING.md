# Contributing

## Contributor agreement and copyright

The rules for all Refaqt repositories are in the
[Refaqt contributor manual](https://github.com/refaqt/.github/blob/main/CONTRIBUTING.md). In short:

- On your first pull request, you accept the
  [Refaqt Contributor Licence Agreement](https://github.com/refaqt/.github/blob/main/CLA.md)
  by posting one sentence as a comment. The check "Contributor agreement" tells you how. You do
  this once for all Refaqt repositories.
- You keep your copyright. Refaqt (BE 0804.145.539) gets a licence to use and license your work.
- Mark anything that you did not make yourself, and keep its own licence and notice.
- New text files that we made start with an `SPDX-FileCopyrightText` and an
  `SPDX-License-Identifier` line. The manual shows how.

## Principles

- **Text-first:** Prefer CSV, SysML, TOML, and Markdown over opaque binaries.
- **Never edit generated files:** Root `bom/bom.csv`, module `cad/params.csv`, `graph/usage-graph.json` (regenerate with scripts).
Requirements live in SysML under `architecture/` — not duplicate requirement docs. Graphical editing: double-click `syson.bat` (see `doqs/docs/syson.md`).
- **Geometry in FreeCAD:** Agents must not edit `.FCStd` files; change parameters via `cad/params/` and `sync_params.py`.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short description>
```

Types include: `feat`, `fix`, `docs`, `cad`, `arch`, `okh`, `firmware`, `chore`, `refactor`, `interface`, `model`, `build`, `params`.

## Before opening a PR

1. Run `python doqs/scripts/validate_all.py` from the repository root.
2. If a first-level content directory was added, run `python doqs/scripts/apply_licenses.py` first.
3. Update log / ADR / mistakes entries in `docs/` when applicable.
4. Regenerate aggregated BOM and usage graph if manifests or lockfiles changed.

## Branches

- `main` — next major version development
- `release/vN.x` — long-term support for deployed machines (see architecture doc)

## Modules

To add a sub-assembly, create `modules/<name>/` with the standard DOQS module layout (see `doqs/docs/architecture.md`) and register it in the root `okh.toml` via `[[hasComponent]]`.
