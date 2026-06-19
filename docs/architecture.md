# Architecture overview (Qarve)

**Qarve** is the top-level DOQS machine module in this repository. It is currently a **single module** at the repo root; `modules/` is reserved for future sub-assemblies.

The **canonical** DOQS specification (modularity, versioning, interfaces, OKH, builds, FreeCAD params, agent workflow) lives in the **`doqs/` submodule**:

→ **[doqs/docs/architecture.md](../doqs/docs/architecture.md)** (from [github.com/refaqt/doqs](https://github.com/refaqt/doqs))

Also in the submodule:

| Doc | Topic |
|-----|--------|
| [doqs/docs/readiness-levels.md](../doqs/docs/readiness-levels.md) | OTRL / ODRL for `okh.toml` |
| [doqs/docs/naming.md](../doqs/docs/naming.md) | Naming conventions (draft) |
| [doqs/docs/agent-guide.md](../doqs/docs/agent-guide.md) | `.cursor` rules vs `doqs/` for agents |

## This repo (summary)

| Path | Role |
|------|------|
| `architecture/machine.sysml` | Machine composition and system requirements |
| `modules/` | Reserved for sub-assemblies (see [modules/README.md](../modules/README.md)) |
| `builds/` | Physical machine lockfiles |
| `graph/usage-graph.json` | Reverse usage (generated) |
| `doqs/` | Git submodule — tools + spec |

For multi-module composition and future extraction to separate repos, see `doqs/docs/architecture.md`.

## Authoritative model

Requirements and interfaces: **`architecture/*.sysml`** and, when present, **`modules/*/architecture/*.sysml`** — not this markdown file.
