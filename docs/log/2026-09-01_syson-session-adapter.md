# 2026-09-01 — SysON session adapter

**Role(s):** engineering, software

## What happened

Added a DOQS launcher so Qarve SysML can be edited in Eclipse SysON without
manual upload/download. Docker Desktop is a one-time install; then
double-click `syson.bat` (control panel) or `python doqs/scripts/syson.py ui`.
Canonical files stay in `architecture/*.sysml`. SysON homepage Download
(JSON zip) is not used for git.

## Decisions

Keep SysON as a Docker web app with a persistent Postgres volume. Import and
export through SysON’s APIs from doqs, not a SysON fork.

## Open Questions

Round-trip fidelity of SysON textual export on Qarve’s models still needs a
live check after Docker is available.

## Next Steps

Use latest doqs (`bash setup-tooling.sh` or bump the submodule) and
double-click `syson.bat`.
