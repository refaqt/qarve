"""Write the geometry fingerprint for every FreeCAD document in this repository.

Run it from the repository root, after you save a model in FreeCAD:

    python cad/fingerprint_models.py

Qarve draws its geometry by hand in the FreeCAD window. There is no build script
to rebuild a part from parameters, so the usual DOQS route --
`FreeCADCmd cad/build_model.py` -- does not apply here. This script measures the
saved file instead. See `docs/decisions/2026-09-22_fingerprints-for-hand-drawn-models.md`.

It never saves a `.FCStd`. Each document is opened in its own FreeCAD process,
measured, and closed. Nothing is written except the fingerprint files.

Options:

    --freecad PATH   the FreeCADCmd program, when it is not in the usual place
    --only PATH      one document, instead of all of them
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

#: How the FreeCAD side hands its result back to the side that started it.
MARKER = "REPORT "

#: Where FreeCAD puts its command-line program on each platform.
FREECAD_CANDIDATES = (
    r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe",
    r"C:\Program Files\FreeCAD 1.0\bin\freecadcmd.exe",
    "/usr/bin/FreeCADCmd",
    "/usr/local/bin/FreeCADCmd",
    "/Applications/FreeCAD.app/Contents/Resources/bin/FreeCADCmd",
)


def repo_root():
    return Path(__file__).resolve().parent.parent


def doqs_scripts():
    scripts = repo_root() / "doqs" / "scripts"
    if not (scripts / "cad_rules.py").is_file():
        raise SystemExit(
            "doqs/scripts is empty. Run: bash setup-tooling.sh"
        )
    return scripts


# ---------------------------------------------------------------- inside FreeCAD

def measure_one(root, target):
    """Measure one saved document. Runs inside FreeCAD. Never saves."""
    import FreeCAD

    sys.path.insert(0, str(root / "doqs" / "scripts"))
    import cad_fingerprint
    import cad_rules

    report = {"file": str(target.relative_to(root)), "written": False, "drifts": []}
    doc = FreeCAD.openDocument(str(target))

    # FreeCAD marks a document as touched while it loads an external link, even
    # though no geometry changed. The flag would record `saved: false`, which
    # DOQS rejects, so it is cleared. Nothing in this process ever writes the
    # .FCStd, so the measurements below are exactly what the committed file
    # holds.
    stored = cad_rules.normalise(cad_fingerprint.measure(doc, params={}))["objects"]
    doc.purgeTouched()

    payload = cad_fingerprint.measure(doc, params={})
    report["objects"] = len(payload["objects"])
    report["errors"] = payload["errors"]
    if cad_rules.measured_nothing(payload):
        report["errors"].append("nothing was measured")
    elif payload["saved"]:
        cad_rules.write_fingerprint(cad_rules.fingerprint_path(target), payload)
        report["written"] = True

    # A separate question, reported and not acted on: does this document still
    # agree with itself? Refreshing it moves geometry when the saved file no
    # longer matches its own sketches and joints. Only a person can fix that, in
    # FreeCAD.
    #
    # This needs a second, clean open. FreeCAD only refreshes what it has marked
    # as changed, and the flag was cleared above, so refreshing this copy would
    # do nothing at all and every document would look healthy. Every document is
    # closed first, linked parts included, so the second open reads them all from
    # disk again. Nothing here saves, so what is dropped is only in memory.
    #
    # Refreshing can raise: an assembly with a broken joint reference throws out
    # of FreeCAD's own code. That must not cost this document its measurement,
    # which is already written by now, so the whole check is guarded and a
    # failure is reported as a question nobody could answer.
    try:
        for name in list(FreeCAD.listDocuments()):
            FreeCAD.closeDocument(name)
        fresh = FreeCAD.openDocument(str(target))
        fresh.recompute()
        rebuilt = cad_rules.normalise(
            cad_fingerprint.measure(fresh, params={})
        )["objects"]
        report["drifts"] = sorted(
            name for name in set(stored) | set(rebuilt)
            if stored.get(name) != rebuilt.get(name)
        )
    except Exception as err:
        report["drift_check_failed"] = f"{type(err).__name__}: {err}"
    return report


# ---------------------------------------------------------------- outside FreeCAD

def find_freecad(given):
    if given:
        return given
    for name in ("FreeCADCmd", "freecadcmd"):
        found = shutil.which(name)
        if found:
            return found
    for candidate in FREECAD_CANDIDATES:
        if Path(candidate).is_file():
            return candidate
    raise SystemExit(
        "FreeCAD was not found. Install FreeCAD 1.1, or pass --freecad with the "
        "path to FreeCADCmd."
    )


def documents(root, only):
    sys.path.insert(0, str(doqs_scripts()))
    from cad_rules import cad_documents

    if only:
        return [Path(only).resolve()]
    return cad_documents(root)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--freecad", default=os.environ.get("QARVE_FREECAD"))
    parser.add_argument("--only", default=None)
    args = parser.parse_args(argv)

    root = repo_root()
    freecad = find_freecad(args.freecad)
    targets = documents(root, args.only)
    print(f"{len(targets)} FreeCAD documents")

    written, failed, drifting, unchecked = 0, [], [], []
    for index, target in enumerate(targets, 1):
        env = dict(os.environ, QARVE_ROOT=str(root), QARVE_FCSTD=str(target))
        proc = subprocess.run(
            [freecad, str(Path(__file__).resolve())], env=env, cwd=str(root),
            capture_output=True, text=True, timeout=1800,
        )
        # FreeCAD writes its progress bar with carriage returns and no newline,
        # so the report can start halfway along a line instead of at the front of
        # one. Normalise the carriage returns and cut from the marker, or a slow
        # document looks like a failed one.
        stdout = proc.stdout.replace("\r", "\n")
        line = next(
            (l[l.index(MARKER):] for l in stdout.splitlines() if MARKER in l), None
        )
        rel = target.relative_to(root)
        if line is None:
            failed.append(str(rel))
            print(f"{index:3d}/{len(targets)} FAIL {rel}")
            print((proc.stdout + proc.stderr)[-500:])
            continue
        report = json.loads(line[len(MARKER):])
        if report["written"]:
            written += 1
        else:
            failed.append(str(rel))
        if report["drifts"]:
            drifting.append((str(rel), ", ".join(report["drifts"][:6])))
        elif report.get("drift_check_failed"):
            unchecked.append((str(rel), report["drift_check_failed"]))
        state = "ok  " if report["written"] else "FAIL"
        print(f"{index:3d}/{len(targets)} {state} {rel} "
              f"objects={report.get('objects')} errors={len(report.get('errors') or [])}")

    print(f"\n{written} fingerprints written, {len(failed)} documents failed")
    if drifting:
        print(
            "\nThese documents no longer agree with their own sketches and joints.\n"
            "The fingerprint records what the saved file holds, which is correct.\n"
            "Open each one in FreeCAD, refresh it, check the result, and save:"
        )
        for rel, detail in drifting:
            print(f"  {rel} - {detail}")
    if unchecked:
        print(
            "\nThese documents were measured, but FreeCAD could not refresh them,\n"
            "so nobody knows whether they still agree with themselves. A broken\n"
            "link inside an assembly is the usual cause. Open each one and look:"
        )
        for rel, detail in unchecked:
            print(f"  {rel} - {detail}")
    return 1 if failed else 0


# This file runs in two places, and the environment variable says which. The
# usual `__name__ == "__main__"` test cannot be used: FreeCADCmd imports a script
# under the file's own name, so the guard would never be true and the macro would
# do nothing at all.
if os.environ.get("QARVE_FCSTD"):
    print(MARKER + json.dumps(measure_one(
        Path(os.environ["QARVE_ROOT"]).resolve(),
        Path(os.environ["QARVE_FCSTD"]).resolve(),
    )))
elif __name__ == "__main__":
    raise SystemExit(main())
