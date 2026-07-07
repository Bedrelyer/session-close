# Claude Code — session-close (no auto-prompt)

Reflection is **optional** and **inline by default**. Do not auto-ask whether to run session-close at turn end.

## Recommended: CLAUDE.md rule

Add to project `CLAUDE.md` or `~/.claude/CLAUDE.md`:

```markdown
When the user says 收尾 / wrap up / /session-close:
- Run session-close skill
- Default inline mode: Q1/Q2 in reasoning, ≤3-line digest, single turn
- Use 反思讨论 for interactive mode (full bullets + wait for user)
```

## Stop hook — not recommended

Previous prompt-hook examples that asked "want to run session-close?" at turn end caused an **extra conversation round**. Do not use them.

If you need a hook for logging only, return `{}` without `followup_message`.

## Install

```bash
./install.sh claude
# or project: cp -r skill layout to .claude/skills/session-close/
```
