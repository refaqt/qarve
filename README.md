# Qarve

Open-source modular CNC milling machine — text-first, Git-friendly, [DOQS](https://github.com/refaqt/doqs) documentation system.

Every folder in this repository is a **module** with the same first-level layout (`bom/`, `cad/`, `architecture/`, `docs/`, `manufacturing/`, `modules/`). The project root is the top-level module.

## Quick start

1. Clone with submodules: `git clone --recurse-submodules https://github.com/refaqt/qarve.git`
2. Install https://git-lfs.com/ and run `git lfs install` before pulling CAD binaries.
3. Read `docs/onboarding.md` for tooling, validation, and agent workflow.
4. Open `architecture/machine.sysml` for system requirements and composition.

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
| `modules/`      | Sub-assemblies (each a full module)                  |
| `builds/`       | Physical machine lockfiles                           |
| `graph/`        | Generated reverse-usage graph                        |
| `doqs/`         | Shared tools, templates, schemas                     |
| `firmware/`     | Motion controller and related software               |
| `docs/`         | Narrative: dev-log, mistakes, decisions, prompts-log |

## License

Hardware documentation and designs: [CERN-OHL-S-2.0](LICENSE). See each module's `okh.toml` for manifest metadata.
