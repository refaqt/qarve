# 2026-09-22 — The repository passes its own checks again

**Role(s):** engineering, software

## What happened

The automatic checks on every pull request had been failing. Three separate
problems were behind it, and none of them was about the machine design.

**The FreeCAD models had no measurements.** Every model needs a small
measurement file beside it, so that a change to the geometry can be read as text
in a pull request. All 44 models were missing theirs, so all 44 failed. They now
have them. How they are produced, and why this repository cannot use the usual
route, is in a separate decision note.

**The example machine record described a machine that does not exist.** It was
marked "Example Workshop" and "Scaffold", and it pointed at a version tag that
was never created. A machine record is meant to say what really went into one
real machine, so this one was removed. The blank example that people copy from
is still there.

**The build server called a tool that had been renamed.** The checking tools
were updated on 1 September, and three of them changed name. The build server
still used an old name, which now stops with an error instead of running. The
build server, the README and the setup guide now use one command,
`python doqs/doqs.py check`, which is also the command to run before you commit.

## Two things that need a person

**Three models no longer agree with their own sketches and joints.** When FreeCAD
refreshes them, parts move. The measurement files record what the saved files
hold, which is correct, but somebody should open these three in FreeCAD, refresh
them, check the result and save:

- `cad/architecture/linear-axis-configuration.FCStd` — one sketch moves 5 mm
- `cad/assemblies/linear-motor-z/linear-motor-z.FCStd` — the motor parts move
- `cad/assemblies/x-axis/x-axis.FCStd` — two guide blocks move 32 mm

This is most likely a side effect of the linear axis work on this branch: those
assemblies use the parts that changed.

**A fault in the shared tools was fixed in the shared tools.** Three models hold
a stress analysis, and the measuring tool could not read any of them. It treated
an analysis mesh as geometry and gave up on the whole document. That was fixed in
the shared tools repository, not here, so every machine project gets the fix:
[refaqt/doqs#34](https://github.com/refaqt/doqs/pull/34). That pull request still
needs to be merged. Once it is, `bash setup-tooling.sh` brings it into this
working copy. The measurements already in this repository were taken with the fix
in place and do not need redoing.

## Next Steps

- [ ] Open the three models listed above in FreeCAD, refresh them, check the result and save.
- [ ] Run `python cad/fingerprint_models.py` after saving them, then commit both the models and their measurements.
- [ ] Merge [refaqt/doqs#34](https://github.com/refaqt/doqs/pull/34), then run `bash setup-tooling.sh` here.

## Related

- [2026-09-22_fingerprints-for-hand-drawn-models.md](../decisions/2026-09-22_fingerprints-for-hand-drawn-models.md)
- [2026-09-22_linear-axis-seal-roller-clearance.md](2026-09-22_linear-axis-seal-roller-clearance.md)
