# Qarve

Open-source modular CNC milling machine — text-first, Git-friendly, [DOQS](https://github.com/refaqt/doqs) documentation system.

The repository root is the **top-level DOQS module**. Sub-assemblies will live under `modules/` when added; none exist yet.

## Quick start

1. Clone with submodules: `git clone --recurse-submodules https://github.com/refaqt/qarve.git`
2. If you cloned without `--recurse-submodules`, run `git submodule update --init --recursive` so validators find `doqs/` at the repo root (not a sibling folder).
3. Install https://git-lfs.com/ and run `git lfs install` before pulling CAD binaries.
4. Read `docs/onboarding.md` for tooling, validation, and agent workflow.
5. Open `architecture/machine.sysml` for system requirements and composition.

## Validation

From the repository root:

```powershell
python doqs/scripts/validate_okh.py
python doqs/scripts/validate_build.py
python doqs/scripts/build_graph.py
python doqs/scripts/check_links.py
```

## Layout

| Path            | Role                                                 |
| --------------- | ---------------------------------------------------- |
| `architecture/` | Top-level SysML (requirements, interfaces)           |
| `cad/`          | Machine assembly FreeCAD + exports                   |
| `modules/`      | Reserved for future sub-assemblies (empty today)     |
| `builds/`       | Physical machine lockfiles                           |
| `graph/`        | Generated reverse-usage graph                        |
| `doqs/`         | Git submodule — shared tools, templates, schemas     |
| `firmware/`     | Motion controller and related software               |
| `docs/`         | Narrative: dev-log, mistakes, decisions, prompts-log |

## License

Hardware documentation and designs: [CERN-OHL-S-2.0](LICENSE). See `okh.toml` for manifest metadata.
