# session-close

**English** | [简体中文](./README.zh-CN.md)

> End every AI session with two questions. Handoff docs, reflection tiers, cross-platform.

Cross-platform Agent Skill that closes AI coding sessions with two canonical reflection questions and structured handoff documents.

Works with **Cursor**, **Claude Code**, and **OpenAI Codex**.

**Runs only when you explicitly invoke it** (`@session-close` / `/session-close` / `wrap up` / `收尾`). Does not auto-start an extra conversation round.

**Current version**: 0.5.0 · See [CHANGELOG.md](CHANGELOG.md) for full history.

## One-line install

```bash
git clone https://github.com/Bedrelyer/session-close.git && cd session-close && ./install.sh cursor
```

## Before vs After

| | End chat normally | session-close |
|---|-------------------|---------------|
| Context | Stays in chat history; re-explain next time | Written to `.session-close/handoffs/` |
| Reflection | None | Two canonical questions (Q1 / Q2) |
| Resume | Manual copy-paste | Ready-to-paste Resume Prompt |
| Audit trail | None | INDEX + update-log |

## The two questions

1. **What should I have asked you?**
2. **What am I missing?**

> *I end every AI coding session with these two questions. This skill automates that into a handoff file your next session can resume from — one turn, no extra chat round.*

## What is a Handoff?

A **handoff** is a Markdown file written to your project when session-close finishes. It captures what you discussed, what was done, and where to pick up next — so the **next conversation** (or a different agent / tool) can continue without re-explaining context.

Typical sections:

| Section | Purpose |
|---------|---------|
| Goal / Accomplished / Deferred | Target, done items, deferred items and why |
| Q1 / Q2 | **Full** answers to the two questions (inline mode shows a ≤3-line digest in chat; full text lives here) |
| Now / Next | Current state and concrete next actions |
| Resume Prompt | Copy-paste prompt for the next session |
| Files Touched | Files involved this session |

Path: `.session-close/handoffs/YYYYMMDD-HHMM-<slug>.md` (e.g. `20260707-1430-handler-fix.md`).  
Index: `.session-close/INDEX.md`.

## Reflection modes

| Mode | Trigger examples | Turns | User sees |
|------|------------------|-------|-----------|
| **inline** (default) | `wrap up`, `@session-close`, `收尾` | 1 | ≤3-line digest; full Q1/Q2 in handoff file |
| **off** | `no reflection`, `收尾 不反思` | 1 | No reflection; handoff + Now/Next only |
| **interactive** | `review reflection`, `收尾 反思讨论` | 2+ | Full Q1/Q2 in chat + waits for confirmation |

In **inline** mode, Q1/Q2 are answered in reasoning — no extra conversation turn.

## Depth tiers

| Tier | Name | When |
|------|------|------|
| L0 | Skip | Trivial / skip |
| L1 | Glance | Quick Q&A |
| L2 | Standard | Regular dev (default) |
| L3 | Deep | Multi-file / architecture |
| L4 | Critical | Ship / security / irreversible |

## Unified paths (all platforms)

| Purpose | Path |
|---------|------|
| Handoff | `.session-close/handoffs/YYYYMMDD-HHMM-<slug>.md` |
| Index | `.session-close/INDEX.md` |
| Update log | `.session-close/update-log.md` (one entry per Phase 4 write/update) |
| Memory | `AGENTS.md` → `CLAUDE.md` → `.cursor/rules/` → `NOTES.md` |

## Quick install

```bash
git clone https://github.com/Bedrelyer/session-close.git
cd session-close
chmod +x install.sh
```

| Tool | Command | Invoke |
|------|---------|--------|
| Cursor | `./install.sh cursor` | `@session-close` or `wrap up` / `收尾` |
| Claude Code | `./install.sh claude` | `/session-close` or `wrap up` / `收尾` |
| Codex | `./install.sh codex` | `/session-close` |
| All | `./install.sh all` | — |

### Cursor stop hook

Registered but **noop** (no auto follow-up). Invoke `@session-close` explicitly.

### Codex extra steps

1. Merge `platforms/codex/config.toml.snippet` into `~/.codex/config.toml`
2. Optional: `platforms/codex/AGENTS.md.snippet` → `~/.codex/AGENTS.md`

## Usage examples

```
wrap up                   # inline: single-turn digest + handoff
wrap up no reflection     # off: skip Q1/Q2
review reflection         # interactive: full Q1/Q2 + wait for you
@session-close
收尾                       # Chinese trigger also works
deep close auth refactor
L4 critical close ready to ship
```

## Version history

| Version | Date | Highlights |
|---------|------|------------|
| **0.5.0** | 2026-07-07 | English default README + zh-CN switcher; launch docs |
| **0.4.0** | 2026-07-07 | Mandatory update log for every Phase 4 file change |
| **0.3.0** | 2026-07-07 | Reflection modes inline / off / interactive; noop stop hook |
| **0.2.0** | 2026-07-06 | Cross-platform `core/` + `platforms/`; unified handoff path |
| **0.1.0** | 2026-07-06 | Initial Cursor skill; L0–L4 tiers; two-question workflow |

Full entries in [CHANGELOG.md](CHANGELOG.md).

## Links

- [PORTABILITY.md](PORTABILITY.md) — cross-platform install and path reference
- [Issues](https://github.com/Bedrelyer/session-close/issues) — feedback and feature requests

> Maintenance note: keep [README.md](./README.md) and [README.zh-CN.md](./README.zh-CN.md) in sync when editing.

## License

MIT
