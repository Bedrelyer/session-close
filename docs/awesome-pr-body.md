# awesome-cursor-skills PR

Use this when opening a PR to [spencerpauly/awesome-cursor-skills](https://github.com/spencerpauly/awesome-cursor-skills).

## PR title

```
Add session-close — two-question session handoff skill
```

## PR body

```markdown
## Summary

Adds [session-close](https://github.com/Bedrelyer/session-close) — a cross-platform Agent Skill that ends AI coding sessions with two reflection questions and writes structured handoff documents to the project.

## Why include it

- Solves a common pain point: context loss between AI sessions
- Works on Cursor, Claude Code, and Codex (single install script)
- Inline reflection mode: one turn, no extra chat round
- Produces auditable artifacts: handoff files, INDEX, update log

## Install

```bash
git clone https://github.com/Bedrelyer/session-close.git && cd session-close && ./install.sh cursor
```

Invoke with `@session-close`, `wrap up`, or `收尾`.

## List entry

Add under **Workflow / Session / Productivity** (or equivalent):

```markdown
- [session-close](https://github.com/Bedrelyer/session-close) — End AI sessions with two reflection questions; generates handoff docs and update logs. Cursor, Claude Code, Codex.
```
```

## File to edit

Fork `spencerpauly/awesome-cursor-skills`, find the skills list section, add the line above, open PR.

## Checklist

- [ ] Forked awesome-cursor-skills
- [ ] Added one-line entry with link and description
- [ ] PR description includes install command
- [ ] Verified link resolves
