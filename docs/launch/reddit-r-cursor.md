# Reddit r/cursor Post

## Title

```
[Tool] session-close – structured handoff docs when you end an AI session (Cursor / Claude / Codex)
```

## Body

```
I open-sourced a skill that closes AI coding sessions with two reflection questions and writes a handoff file to your project.

**The two questions:**
1. What should I have asked you?
2. What am I missing?

**What you get:**
- `.session-close/handoffs/YYYYMMDD-HHMM-slug.md` — full session summary + Q1/Q2 + resume prompt
- `.session-close/INDEX.md` — index of all handoffs
- `.session-close/update-log.md` — audit trail of file changes during close

**Platforms:** Cursor, Claude Code, Codex (one install script)

**Install:**
```bash
git clone https://github.com/Bedrelyer/session-close.git && cd session-close && ./install.sh cursor
```

Invoke: `@session-close` or "wrap up"

Inline mode = single turn, no extra chat round. Full Q1/Q2 answers go in the handoff file.

Repo: https://github.com/Bedrelyer/session-close

Happy to answer questions about the workflow or tiers (L0–L4 depth).
```

## Subreddits

- r/cursor (primary)
- r/ClaudeAI (secondary, mention Claude Code support)
- r/LocalLLaMA (optional, if discussing agent workflows)
