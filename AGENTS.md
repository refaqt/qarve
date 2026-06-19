# Agent instructions (Qarve / DOQS)

## Logging rule

After completing any task, append an entry to `docs/prompts-log/YYYY-MM.md` (current year-month).

Format:

---

### HH:MM — Short task title

**Prompt:** "..."

**Actions:**

- ...

**Files changed:**

- `path/to/file` — created / modified / deleted

**Outcome:** One sentence.
---

## Hard rules

1. **Never edit `.FCStd` files** — geometry changes happen in FreeCAD manually.
2. **Requirements live in SysML** (`architecture/`) — do not duplicate as standalone requirement docs.
3. **Run validators** after OKH or build changes: `python doqs/scripts/validate_okh.py` (and siblings).
4. **Read** `docs/mistakes/README.md` and recent `docs/mistakes/*.md` at task start.
5. **Prefer** CSV/TOML/SysML output; validate before commit.

## Pointed tasks

Example: *"Look at `bom/bom.csv` (when present) and draft `[[part]]` entries using `doqs/templates/okh-module-with-parts.toml`."*

See `.cursor/rules/` for full workflow.
