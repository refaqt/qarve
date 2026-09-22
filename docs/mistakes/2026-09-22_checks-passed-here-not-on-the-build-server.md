# 2026-09-22 — The checks passed on my machine and failed on the build server

## What happened

All 44 FreeCAD models got a measurement file, and every check passed locally,
including a rehearsal against the exact version of the checking tools the build
server uses. The work was pushed as passing. The build server then failed all 44
models at once, each with the same message: the model changed since its
measurement was written.

Nothing had changed. The models are stored with Git LFS, and the build server
was checking out a small text stub in place of each one. The check compares a
checksum of the model file against the checksum recorded in the measurement, so
it was comparing the measurement against a stub.

## Why it went wrong

Two habits met.

The rehearsal was careful about the wrong variable. It pinned the version of the
tools, because that had already caused one failure that day. It did not pin the
**contents of the working copy**, and that was the variable that differed: a
developer's copy has the real models, a fresh checkout does not unless it is
told to fetch them.

The error message also pointed away from the cause. "The model changed since its
measurement was written" describes the common case and reads as a statement of
fact. A stub is not a changed model, but the check cannot tell the difference
from a checksum alone.

## Prevention rule

1. **A check that reads a large binary file must be proved on a fresh checkout,
   not only on a working copy.** Anything stored with Git LFS is not there by
   default. In GitHub Actions this means `lfs: true` on the checkout step.
2. **"It passes here" is not a result.** Say which environment a check passed
   in, and name what is different about the one that matters.

## Related

- `.github/workflows/validate.yml`
- [2026-09-22_repository-passes-its-own-checks.md](../log/2026-09-22_repository-passes-its-own-checks.md)
