---
name: prompts-log
description: >-
  Appends completed agent task summaries to docs/prompts-log/YYYY-MM.md.
  Use after every repository task when AGENTS.md or prompts-log rule applies.
---

# Prompts log

## When

After completing any agent task on this repository (unless the user explicitly opts out).

## How

1. Open or create `docs/prompts-log/YYYY-MM.md` for the current month.
2. Append a new block separated by `---`.
3. Use the structure in `AGENTS.md`.

## Quality

- **Prompt:** Short paraphrase of the user request.
- **Actions:** Bullet list of what was done.
- **Files changed:** Paths with created/modified/deleted.
- **Outcome:** One sentence result.
