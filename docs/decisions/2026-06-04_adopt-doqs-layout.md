# ADR-001 — Adopt DOQS modular layout

- **Date:** 2026-06-04
- **Status:** Accepted

## Context

The Qarve machine must be documented in a Git-friendly, agent-friendly way with reusable modules, OKH publishing, and long-lived physical builds.

## Decision

Adopt the DOQS architecture: identical module folders, SysML in `architecture/`, narrative docs in `docs/` subfolders, validators in `doqs/`, lockfiles in `builds/`.

## Consequences

- Agents must follow DOQS paths (not a flat `docs/mistakes.md` only).
- `doqs/` is a Git submodule pointing at `github.com/refaqt/doqs`; scripts stay path-stable.
- Full CERN-OHL licence text and GitHub org URLs remain to be finalized.
