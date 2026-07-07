## Platform: Codex

| Item | Value |
|------|-------|
| Invoke | `/session-close` or skill auto-discovery via description |
| Personal install | `~/.agents/skills/session-close/` |
| Project install | `.agents/skills/session-close/` |
| Register skill | Add `platforms/codex/config.toml.snippet` to `~/.codex/config.toml` |
| Handoff | `.session-close/handoffs/` (project root) |
| Memory probe | `AGENTS.md` → `NOTES.md` |
| Auto-prompt | No native stop hook — append `platforms/codex/AGENTS.md.snippet` to `~/.codex/AGENTS.md` |
