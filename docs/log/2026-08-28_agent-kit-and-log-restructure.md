# 2026-08-28 — Agent kit and log restructure

**Role(s):** engineering

## What happened

- Completed refaqt-agents ADR follow-through: slimmed `AGENTS.md` to a thin discovery stub;
  moved repo-specific rules to `.agents-local/rules/`.
- Slimmed `.cursor/rules/*.mdc` to pointer-only adapters (plus globs where needed).
- Migrated `docs/dev-log/` → `docs/log/` with mandatory **Role(s):** on every entry.
- Retired `docs/prompts-log/`; folded substantive prompts-log content into log entries
  (FEM workflow, x-axis Params pattern, spindle-clamp trade-offs, guide-rail FEM fix).
- Removed prompts-log skill, rule, and `.claude/skills/prompts-log` symlink.
- Added ADR superseding ADR-002 item 16:
  `docs/decisions/2026-08-28_migrate-to-unified-log.md`.

Reference: [aqtuator PR #12](https://github.com/refaqt/aqtuator/pull/12) and
`docs/decisions/2026-08-27_unify-agent-kit-via-refaqt-agents.md` in aqtuator.

## Decisions

- Qarve uses unified `docs/log/` per refaqt-agents; no prompts-log.
- Session logging uses the shared `log` skill when work is worth recording.

## Next Steps

- [ ] Bump `doqs/docs/agent-guide.md` separately if DOQS spec still references dev-log/prompts-log paths.
