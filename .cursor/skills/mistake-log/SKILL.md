---
name: mistake-log
description: >-
  Logs incidents to docs/mistakes/ as dated files, escalates repeated failures,
  and promotes prevention rules. Use at task start, after bugs, failed approaches,
  rejected output, or convention misunderstandings in this repository.
---

# Mistake log (DOQS)

## What counts as a mistake

- A bug introduced and fixed in the same session.
- A wrong approach taken and abandoned.
- A misunderstanding of project conventions that caused rework.
- Any output the user rejected or asked to redo.

## Before starting work

1. Read `docs/mistakes/README.md` and recent `docs/mistakes/YYYY-MM-DD_*.md`.
2. State which prevention rules apply to the current task.

## After a mistake

1. Create `docs/mistakes/YYYY-MM-DD_short-topic.md` using `doqs/templates/mistake-entry.md`.
2. Update `docs/mistakes/README.md` if a new standing prevention rule should be listed.
3. If the same mistake happens twice, promote the rule into scoped `.cursor/rules/`.

## Continuous improvement

- Review `docs/mistakes/` and `docs/skills.md` after long sessions for patterns to promote.

## Entry format

Use `doqs/templates/mistake-entry.md` — one file per incident, not a single rolling `mistakes.md`.
