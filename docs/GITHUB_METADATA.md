# GitHub Repository Metadata

Apply these in **GitHub → Settings → General** for [Bedrelyer/session-close](https://github.com/Bedrelyer/session-close).

## Description

```
End every AI session with two questions — handoff docs, reflection tiers, Cursor/Claude/Codex skill
```

## Topics

Add all of the following:

- `cursor-skills`
- `cursor`
- `agent-skills`
- `claude-code`
- `codex`
- `ai-workflow`
- `handoff`
- `session-management`

## Social Preview

1. Go to **Settings → General → Social preview**
2. Upload [`social-preview.png`](./social-preview.png) (1200×630)

## Optional: gh CLI

If `gh` is authenticated:

```bash
gh repo edit Bedrelyer/session-close \
  --description "End every AI session with two questions — handoff docs, reflection tiers, Cursor/Claude/Codex skill" \
  --add-topic cursor-skills --add-topic cursor --add-topic agent-skills \
  --add-topic claude-code --add-topic codex --add-topic ai-workflow \
  --add-topic handoff --add-topic session-management
```

Social preview must still be uploaded manually in the GitHub UI.
