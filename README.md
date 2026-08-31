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
python doqs/scripts/validate_all.py
python doqs/scripts/build_graph.py
```

`validate_all.py` runs `validate_okh`, `validate_licenses`, `check_names`, `check_links`, and `validate_build`. After adding a first-level content directory, also run `python doqs/scripts/apply_licenses.py`.

## Layout

| Path              | Role                                                 |
| ----------------- | ---------------------------------------------------- |
| `LICENSE`         | Overview mapping directories to licences             |
| `LICENSES/`       | Full CERN-OHL-S, GPL-3.0, and CC BY-SA texts         |
| `TRADEMARKS.md`   | Reserved organisation and project marks              |
| `architecture/`   | Top-level SysML (requirements, interfaces)           |
| `cad/`            | Machine assembly FreeCAD + exports                   |
| `modules/`        | Reserved for future sub-assemblies (empty today)     |
| `builds/`         | Physical machine lockfiles                           |
| `graph/`          | Generated reverse-usage graph                        |
| `doqs/`           | Git submodule — shared tools, templates, schemas     |
| `.agents/`        | Git submodule — shared agent rules and skills        |
| `.agents-local/`  | Qarve-only agent rules and skills                    |
| `firmware/`       | Motion controller and related software               |
| `docs/`           | Narrative: log, mistakes, decisions                  |

## Agents

Cursor, Claude Code, and cloud agents: start at [`AGENTS.md`](AGENTS.md). Shared kit is in
[`.agents/`](.agents/); repo-specific rules and skills in [`.agents-local/`](.agents-local/).

## Licence

This repository uses different licences for different kinds of content:

- **Hardware** (`cad/`, `architecture/`, `manufacturing/`, `bom/`, `builds/`, `modules/`) —
  [CERN-OHL-S v2.0](LICENSES/CERN-OHL-S-2.0.txt)
- **Firmware & software** (`firmware/`, `software/`, `simulation/`) —
  [GPL-3.0](LICENSES/GPL-3.0.txt)
- **Media & documentation** (`docs/`, `measurement/`) —
  [CC BY-SA 4.0](LICENSES/CC-BY-SA-4.0.txt)

The Refaqt BV, BE 0804.145.539 name and logo, and the Qarve CNC Milling Machine name and logo, are
trademarks and are not covered by the above — see [TRADEMARKS.md](TRADEMARKS.md).

See [LICENSE](LICENSE) for the full overview and directory mapping.
