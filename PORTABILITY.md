# Portability Guide

Cross-platform reference for session-close across Cursor, Claude Code, and Codex.

## Three-tool comparison

| Concern | Cursor | Claude Code | Codex |
|---------|--------|-------------|-------|
| Personal skill path | `~/.cursor/skills/session-close/` | `~/.claude/skills/session-close/` | `~/.agents/skills/session-close/` |
| Project skill path | `.cursor/skills/session-close/` | `.claude/skills/session-close/` | `.agents/skills/session-close/` |
| Invoke | `@session-close` | `/session-close` | `/session-close` |
| Skill format | `SKILL.md` + YAML frontmatter | Same | Same |
| Handoff (all) | `.session-close/handoffs/` | `.session-close/handoffs/` | `.session-close/handoffs/` |
| Memory probe | AGENTS.md → CLAUDE.md → .cursor/rules → NOTES.md | AGENTS.md → CLAUDE.md → NOTES.md | AGENTS.md → NOTES.md |
| Auto end-of-turn prompt | `stop` hook (Python) | Hook or CLAUDE.md rule | AGENTS.md snippet only |
| Install | `./install.sh cursor` | `./install.sh claude` | `./install.sh codex` |

## Workflow is identical

All platforms run the same core workflow from `core/workflow.md`:

- L0–L4 depth tiers
- Two canonical questions (verbatim English headers)
- Gather → Orient → User gate → Now/Next → Act
- Handoff to `.session-close/handoffs/`

Only the **Platform** section at the top of each installed `SKILL.md` differs.

## Memory file probe (Phase 4)

Update the first existing file in this order:

1. `AGENTS.md` — Codex native; universal team conventions
2. `CLAUDE.md` — Claude Code project memory
3. `.cursor/rules/*.mdc` — Cursor rules (append to most relevant file)
4. `NOTES.md` — scratchpad / teaching workspaces

At L3/L4, if none exist, create `AGENTS.md` at project root with the lesson bullet.

## Handoff index

At L2+, append to `.session-close/INDEX.md`:

```markdown
- 2026-07-06 14:00 handler-fix — L2 — tags: auth, websocket
```

## Migration from Cursor-only layout

If you used the old `.cursor/session-handoffs/` path:

```bash
mkdir -p .session-close/handoffs
mv .cursor/session-handoffs/* .session-close/handoffs/ 2>/dev/null || true
```

Old handoffs remain readable; new sessions write only to `.session-close/handoffs/`.

## Fallback without any skill installed

Paste into any AI chat:

```text
End this session with session-close (L2 Standard):

Answer in order:
### Q1 — What should I have asked you?
### Q2 — What am I missing?

Then: Now / Next list. If substantive, write handoff to .session-close/handoffs/YYYYMMDD-HHMM-<slug>.md
```

## Hook limitations

| Tool | Native auto-prompt | Workaround |
|------|-------------------|------------|
| Cursor | Yes — `platforms/cursor/hooks/session-close-stop.py` | — |
| Claude Code | Partial — hook schema varies by version | `hooks.md` prompt hook or CLAUDE.md rule |
| Codex | No stop + followup_message | `AGENTS.md.snippet` in `~/.codex/AGENTS.md` |

## Re-install after git pull

```bash
cd session-close
git pull
./install.sh cursor   # or claude / codex / all
```

This regenerates a single-file `SKILL.md` per platform from `core/` + `platforms/`.
