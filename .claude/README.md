# Claude Code agent kit (Qarve)

Claude Code reads [`CLAUDE.md`](../CLAUDE.md) at session start, which imports [`AGENTS.md`](../AGENTS.md). Do not duplicate instructions here.

## Skills

This folder symlinks skills so Claude auto-discovers them:

| Skill | Source |
| --- | --- |
| `mistake-log` | `.agents/skills/mistake-log` |
| `maintain-patterns` | `.agents/skills/maintain-patterns` |
| `log` | `.agents/skills/log` |
| `freecad` | `.agents/skills/freecad` |
| `doqs-naming` | `.agents/skills/doqs-naming` |

On Windows, if symlinks are unavailable, copy skill folders or junction-link per [`.agents/README.md`](../.agents/README.md).

## Cursor

Cursor uses `.cursor/rules/*.mdc` adapters pointing at the same `.agents/` and `.agents-local/` paths.
