# 2026-06-04 — Repository bootstrap

## Goal

Initialize the Qarve repository per `doqs_architecture.md` and portable Cursor agent kit.

## Work Done

- Root and example modules (`frame`, `x-axis`) with OKH, SysML, BOM, CAD param scripts.
- Embedded `doqs/` validators, templates, schemas.
- Example build lockfile `builds/serial-0042/`.
- `.cursor` rules and skills adapted for DOQS.

## Decisions Made

- See `docs/decisions/2026-06-04_adopt-doqs-layout.md`.

## Open Questions

- [ ] Confirm GitHub org/repo URLs and licence text.
- [ ] Extract `doqs/` to standalone repo vs keep embedded.
- [ ] Initial module set beyond frame + x-axis.

## Next Steps

- [ ] Add FreeCAD assemblies and LFS-tracked binaries.
- [ ] Wire CI to run validators on push.
