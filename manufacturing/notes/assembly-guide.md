# Machine assembly guide

> Scaffold — expand with step-by-step assembly, torque specs, and safety notes.

## Prerequisites

- Sub-module assembly guides under `modules/*/manufacturing/notes/` (when sub-assemblies exist)
- Build lockfile if assembling a specific serial (`builds/<id>/build.toml`)

## Overview

1. Sub-assemblies per their local guides (when `modules/` is populated).
2. Spindle clamp (`cad/assemblies/spindle-clamp/`):
   - Manufactured parts: `spindle-clamp-base` (base plate with recess for spindle clearance), `spindle-clamp-jaw` (clamping jaw), `spindle-clamp-flex` (flex part).
   - Top-down layout: master sketches in `Body_master` inside the assembly file; parts bind to those sketches (see `cad/README.md`).
   - Open the assembly in FreeCAD 1.1+ Assembly workbench; insert base and jaw parts, then add clamp joints.
3. Spindle stack: see `cad/assemblies/spindle-assembly/` (spindle model in `cad/parts/spindle/`).
4. Final machine integration at this level.
