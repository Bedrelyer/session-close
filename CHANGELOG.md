# Changelog

All notable changes to the **session-close** skill repository.

## [Unreleased]

### Added

- Mandatory update log: every Phase 4 file create/update appends to `.session-close/update-log.md`
- Template `core/templates/update-log-entry.md`

## [0.3.0] — 2026-07-07

### Changed

- Reflection modes: **inline** (default), **off**, **interactive**
- Q1/Q2 answered in reasoning for inline mode; single-turn digest in chat
- Cursor stop hook disabled (`followup_message` noop)

## [0.2.0] — 2026-07-06

### Changed

- Cross-platform layout: `core/` + `platforms/{cursor,claude-code,codex}/`
- Unified handoff path `.session-close/handoffs/`
- `install.sh` for Cursor / Claude Code / Codex

## [0.1.0] — 2026-07-06

### Added

- Initial Cursor skill with L0–L4 depth tiers
- Two canonical questions workflow
- Multilingual triggers
