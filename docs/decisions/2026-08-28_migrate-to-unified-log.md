# 2026-08-28 — Migrate to unified activity log

- **Date:** 2026-08-28
- **Status:** Accepted
- **Supersedes:** Item 16 of [ADR-002 — Adopt refaqt-agents](2026-08-28_adopt-refaqt-agents.md)

## Context

ADR-002 (2026-08-28) retained DOQS narrative paths `docs/dev-log/` and `docs/prompts-log/` instead of
migrating to refaqt-agents `docs/log/`. Refaqt is standardizing on the unified activity log pattern
adopted in [aqtuator](https://github.com/refaqt/aqtuator) (PR #12,
`docs/decisions/2026-08-27_unify-agent-kit-via-refaqt-agents.md`).

Qarve also accumulated duplicate agent guidance across `AGENTS.md`, `.cursor/rules/*.mdc`, and
repo-local skills after the initial refaqt-agents install.

## Decision

1. Migrate `docs/dev-log/` → `docs/log/` with mandatory **Role(s):** on every entry.
2. Retire `docs/prompts-log/` entirely; fold substantive prompts-log content into log entries where
   not already captured elsewhere. Do not add a replacement “after every task” logging rule.
3. Slim `AGENTS.md` to a thin discovery stub; move repo-specific rule bodies to
   `.agents-local/rules/`.
4. Slim `.cursor/rules/*.mdc` to pointer-only adapters (plus globs where needed).
5. Remove prompts-log skill, rule, and Claude symlink.

## Consequences

- Qarve aligns with refaqt-agents living-docs and the shared `log` skill.
- Session logging is discretionary (when work is worth recording), same as aqtuator.
- ADR-002 items 13 and 16 are partially superseded: prompts-log is removed; paths use `docs/log/`.
- `doqs/docs/architecture.md` may still reference legacy paths until updated separately in the doqs repo.
