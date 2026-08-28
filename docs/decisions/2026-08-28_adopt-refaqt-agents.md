# ADR-002 — Adopt refaqt-agents shared kit

- **Date:** 2026-08-28
- **Status:** Accepted

## Context

Qarve already had machine-local `.cursor/rules/` and skills copied or adapted from a generic bootstrap. Refaqt is standardizing cross-repo agent guidance in [refaqt-agents](https://github.com/refaqt/refaqt-agents), mounted at `.agents/` (see [aqtuator](https://github.com/refaqt/aqtuator) as reference).

## Decision

- Add `.agents/` Git submodule for shared rules and process skills.
- Keep Qarve/DOQS-specific behaviour in `.agents-local/` (patterns, prompts-log, DOQS skill symlinks) and scoped `.cursor/rules/` (doqs-workflow, freecad, sysml-okh, prompts-log).
- Restructure root `AGENTS.md` as the single entry point; add `CLAUDE.md` importing it for Claude Code.
- Add `.claude/skills/` symlinks mirroring shared and local skills.
- Retain DOQS narrative paths (`docs/dev-log/`, `docs/prompts-log/`) — do not migrate to refaqt-agents `docs/log/`.

## Consequences

- Generic workflow updates flow from refaqt-agents (bump submodule pointer); Qarve-only rules stay in this repo.
- `.cursor/skills/` is removed; skills load from `.agents/` and `.agents-local/` paths listed in `AGENTS.md`.
- `docs/skills.md` becomes a pointer to `.agents-local/skills/patterns/SKILL.md`.
- `doqs/docs/agent-guide.md` may be updated separately to document the three-layer model.
