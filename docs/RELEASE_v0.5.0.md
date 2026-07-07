# Release v0.5.0

Create this release on GitHub: **Releases → Draft a new release → Choose tag `v0.5.0`**

## Release title

```
v0.5.0 — Bilingual README and international launch
```

## Release notes (paste into GitHub)

```markdown
## What's new

- **English default README** with [简体中文](./README.zh-CN.md) language switcher
- Before/After comparison table and one-line install
- Social preview asset (`docs/social-preview.png`)
- Launch templates for HN, Reddit, X (`docs/launch/`)
- Community submission guides (`docs/launch/directory-submissions.md`)
- awesome-cursor-skills PR template (`docs/awesome-pr-body.md`)

## Install

```bash
git clone https://github.com/Bedrelyer/session-close.git && cd session-close && ./install.sh cursor
```

Then invoke `@session-close` or say `wrap up`.

## Also in this release line

Includes all 0.4.0 features: mandatory update log (`.session-close/update-log.md`) for every Phase 4 file change.
```

## Post-release checklist

- [ ] Upload `docs/social-preview.png` to Settings → Social preview
- [ ] Set Description and Topics per `docs/GITHUB_METADATA.md`
- [ ] Open awesome-cursor-skills PR per `docs/awesome-pr-body.md`
- [ ] Submit to skills.sh and CursorDirectory per `docs/launch/directory-submissions.md`
- [ ] Post HN / Reddit / X using `docs/launch/` templates
