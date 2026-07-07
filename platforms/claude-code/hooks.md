# Claude Code — optional session-close reminder hook

Codex has no built-in equivalent to Cursor's `stop` hook with `followup_message`. Claude Code supports hooks via settings — see [Claude Code hooks docs](https://code.claude.com/docs/en/hooks).

## Option A: Stop hook (after each agent turn)

Add to your Claude Code hooks configuration (path varies by version; often `~/.claude/settings.json` or project `.claude/settings.json`):

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "If this session involved substantive code changes or multi-step work, and the user has NOT already said wrap up / 收尾 / skip / 跳过, ask whether to run /session-close for the two-question ritual (What should I have asked you? What am I missing?). If trivial Q&A only, do nothing extra."
          }
        ]
      }
    ]
  }
}
```

Adjust to match your Claude Code version's hook schema.

## Option B: SessionEnd hook (when chat closes)

Fire-and-forget logging only — cannot auto-continue the conversation. Use for analytics, not for prompting session-close.

## Option C: CLAUDE.md rule (simplest)

Add to project `CLAUDE.md` or `~/.claude/CLAUDE.md`:

```markdown
After substantive work, if the user has not closed the session, suggest running `/session-close` before they leave.
```

## Cursor hook script

For a full Python stop hook with transcript detection, copy from this repo:

`platforms/cursor/hooks/session-close-stop.py` (Cursor-specific stdin/stdout contract).
