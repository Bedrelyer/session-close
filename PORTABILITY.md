# Portability Guide

Cross-platform reference for session-close across Cursor, Claude Code, and Codex.

## Three-tool comparison

| Concern | Cursor | Claude Code | Codex |
|---------|--------|-------------|-------|
| Personal skill path | `~/.cursor/skills/session-close/` | `~/.claude/skills/session-close/` | `~/.agents/skills/session-close/` |
| Project skill path | `.cursor/skills/session-close/` | `.claude/skills/session-close/` | `.agents/skills/session-close/` |
| Invoke | `@session-close` | `/session-close` | `/session-close` |
| Reflection default | **inline** (1 turn) | **inline** | **inline** |
| Handoff (all) | `.session-close/handoffs/` | `.session-close/handoffs/` | `.session-close/handoffs/` |
| Update log (all) | `.session-close/update-log.md` | same | same |
| Memory probe | AGENTS.md → CLAUDE.md → .cursor/rules → NOTES.md | AGENTS.md → CLAUDE.md → NOTES.md | AGENTS.md → NOTES.md |
| Auto end-of-turn prompt | **disabled** (noop hook) | not recommended | not recommended |
| Install | `./install.sh cursor` | `./install.sh claude` | `./install.sh codex` |

## Reflection modes (all platforms)

| Mode | Triggers | Turns | User sees |
|------|----------|-------|-----------|
| inline | `收尾`, `@session-close` (default) | 1 | ≤3-line digest |
| off | `不反思`, `no reflection` | 1 | none |
| interactive | `反思讨论`, `review reflection` | 2+ | full Q1/Q2 + wait |

Full Q1/Q2 always written to handoff file at L2+ (inline/interactive). Never auto-run without explicit user invocation.

## Workflow

From `core/workflow.md`:

- L0–L4 depth tiers
- Gather → Orient (internal in inline) → [User gate if interactive] → Now/Next → Act
- Handoff to `.session-close/handoffs/`
- **Update log**: append every Phase 4 file change to `.session-close/update-log.md`

## Hook policy

| Tool | Behavior |
|------|----------|
| Cursor | `session-close-stop.py` returns `{}` always — no `followup_message` |
| Claude Code | Do not auto-prompt at turn end; user invokes `/session-close` |
| Codex | AGENTS.md snippet documents explicit invoke only |

## Fallback without skill

```text
收尾（inline L2）：在思考中回答 Q1/Q2，用户只见 digest，handoff 写 .session-close/handoffs/
```

## Re-install after git pull

```bash
cd session-close && git pull && ./install.sh cursor
```
