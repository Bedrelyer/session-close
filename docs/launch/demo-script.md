# 30-Second Demo Script

Record a screen capture for README or social posts.

## Setup (before recording)

1. Open a project with some recent AI work (multi-file change ideal)
2. Ensure session-close is installed: `./install.sh cursor`
3. Clear or hide sensitive content

## Script (30 seconds)

| Time | Action | Narration (optional) |
|------|--------|----------------------|
| 0–5s | Show Cursor chat with completed task | "I just finished a feature with the AI." |
| 5–10s | Type `@session-close` or "wrap up" | "Instead of closing the tab, I run session-close." |
| 10–20s | Show agent response: digest + handoff path | "One turn — short digest in chat." |
| 20–25s | Open `.session-close/handoffs/*.md` in editor | "Full Q1/Q2, Now/Next, and a resume prompt." |
| 25–30s | Show INDEX.md or update-log.md | "Everything is indexed and auditable." |

## Export

- Save as `docs/demo.gif` (recommended ≤5 MB for GitHub README)
- Or attach to GitHub Release v0.5.0

## README embed (after GIF exists)

```markdown
![session-close demo](./docs/demo.gif)
```

Add below the one-line install block in README.md.
