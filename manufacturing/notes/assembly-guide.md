# Machine assembly guide

> Scaffold — expand with step-by-step assembly, torque specs, and safety notes.

## Prerequisites

- Sub-module assembly guides under `modules/*/manufacturing/notes/` (when sub-assemblies exist)
- Build lockfile if assembling a specific serial (`builds/<id>/build.toml`)

## Overview

1. Sub-assemblies per their local guides (when `modules/` is populated).
2. Spindle clamp: see `cad/assemblies/spindle-clamp/` (parts in `cad/parts/spindle-clamp-base/`, `cad/parts/spindle-clamp-jaw/`).
3. Spindle stack: see `cad/assemblies/spindle-assembly/` (spindle model in `cad/parts/spindle/`).
4. Final machine integration at this level.
