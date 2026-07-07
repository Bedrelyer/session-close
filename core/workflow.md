End substantial AI sessions with two canonical questions, graded by depth.

## Detect Platform

Infer the host tool from invocation style or context; **workflow logic is identical** across tools.

| Signal | Platform |
|--------|----------|
| `@session-close` | Cursor |
| `/session-close` | Claude Code or Codex |
| User says 收尾 without `@`/`/` | Any — run this skill |

## Canonical Questions (verbatim)

1. **What should I have asked you?**
2. **What am I missing?**

Never paraphrase these in the reflection output headers.

## Step 0 — Match Trigger & Depth

### Language triggers

Match the user's closing intent in any language. See [triggers.md](triggers.md) for the full phrase table.

If the user mixes languages, any matched phrase activates this skill.

### Depth override keywords

User can force a tier in the trigger phrase:

| Override | Tier |
|----------|------|
| `skip`, `跳过`, `スキップ`, `omitir` | L0 |
| `glance`, `轻量`, `軽量`, `ligero`, `léger` | L1 |
| `standard`, `标准`, `標準`, `estándar` | L2 |
| `deep`, `深度`, `深い`, `profundo`, `profond` | L3 |
| `critical`, `关键`, `重要`, `crítico`, `critique` | L4 |

Without override, auto-detect tier from session signals (below).

### Reflection depth tiers

| Tier | Name | Auto-detect signals | Gather | Q1/Q2 | User gate | Handoff | Memory |
|------|------|---------------------|--------|-------|-----------|---------|--------|
| **L0** | Skip | User cancels; or 1 exchange, no deliverable | — | — | — | — | — |
| **L1** | Glance | < 15 min feel; no file edits; conceptual Q&A | goal only | 1–2 bullets each | optional | no | no |
| **L2** | Standard | some edits or 3+ turns; single feature/fix | git status, files touched | 3 bullets each, evidence-based | yes | yes | if insight |
| **L3** | Deep | multi-file; arch/API choice; debugging marathon | full gather (see Phase 1) | 3–5 bullets + severity | required | yes | yes |
| **L4** | Critical | prod/deploy/security/money/data-loss stakes | full gather + risk scan | 5 bullets + verify actions | required + confirm Now | yes + resume prompt | yes + rules |

**Escalation rule**: when unsure between two tiers, pick the higher one for L3/L4 signals (security, deploy, irreversible ops).

**De-escalation rule**: user says `glance` / `轻量` / `L1` always wins over auto-detect.

Announce chosen tier at start: `Session close — L2 Standard (auto-detected)`.

## Phase 1 — Gather

Scale to tier. Skip entirely at L0; minimal at L1.

**L2+** run in parallel:
- `git status` and `git diff --stat`
- `git log --oneline -5`
- files modified/discussed this session
- open TODOs and explicit deferrals
- stated goal vs accomplished

**L3/L4** additionally note: unverified assumptions, tests not run, docs not updated.

Ground all reflection in this evidence. No generic "maybe add tests" without tying to a specific file or change.

## Phase 2 — Orient (Two Questions)

Answer in order. Do not merge into one summary.

### Q1 — What should I have asked you?

Process/prompting gaps. Per bullet:
- the question (copy-paste ready)
- why it wasn't asked
- rework it would have prevented

### Q2 — What am I missing?

Content/blind-spot gaps. Per bullet:
- what is missing (specific)
- severity: `blocker` / `risk` / `suggestion`
- one-line verify action

**Tier output counts**: L1 → 1–2 each; L2 → 3 each; L3 → 3–5 each; L4 → 5 each with at least one `blocker` or `risk`.

Present in the user's conversation language, but keep the Q1/Q2 headers in English canonical form.

## Phase 2.5 — User Gate

Required at L2+. Use this shell (localize the prompt line, keep headers):

```markdown
## Session Reflection (L{n} {Name})

### Q1 — What should I have asked you?
- ...

### Q2 — What am I missing?
- ...

Which points land? What did I miss saying?
```

Wait for user response before Phase 3 at L2+; at L4, also confirm Now items before acting.

## Phase 3 — Decide (Now vs Next)

Sort findings + user additions:
- **Now** — finishable in ~5 min (tiny fix, note, stash)
- **Next** — next session entry with a concrete first command or question

Every incomplete item → Now or Next. Nothing silent.

## Phase 4 — Act

Scale to tier.

| Action | L1 | L2 | L3 | L4 |
|--------|----|----|----|-----|
| Handoff file | — | yes | yes | yes |
| Update memory file (probe order below) | — | if insight | yes | yes |
| Update `NOTES.md` | — | if exists | yes | yes |
| Update `.session-close/INDEX.md` | — | yes | yes | yes |
| Suggest git commit/stash | — | note only | note | note |

### Handoff path (all platforms)

Write to **project root**:

`.session-close/handoffs/YYYYMMDD-HHMM-<slug>.md`

Use [templates/handoff.md](templates/handoff.md). Create `.session-close/handoffs/` if missing.

At L2+, append a one-line entry to `.session-close/INDEX.md` (date, slug, tier, context tags).

### Memory file probe order

Update the **first existing** file; at L3/L4 create `AGENTS.md` at project root if none exist:

1. `AGENTS.md` (Codex + universal)
2. `CLAUDE.md` (Claude Code)
3. `.cursor/rules/*.mdc` or `.cursor/rules/` (Cursor — append to most relevant rule file)
4. `NOTES.md` (if exists)

Only add durable lessons — not session narrative.

**Git**: never commit unless the user explicitly asks.

## Closing Report

```markdown
## Session Close Complete — L{n} {Name}

**Tier**: {auto|override} — {one-line reason}
**Handoff**: {path or "none"}
**Memory**: {files updated or "none"}
**Now**: ...
**Next**: ...
```

## Anti-patterns

- Same-model self-reflection loop → anchor every bullet to gather evidence
- Running L3 ritual on a one-line question → de-escalate to L1
- Skipping user gate on L3/L4
- Committing without explicit user request
- Writing handoffs to tool-specific paths (`.cursor/session-handoffs/`) — use `.session-close/handoffs/` only

## Additional Resources

- Full multilingual triggers: [triggers.md](triggers.md)
- Handoff template: [templates/handoff.md](templates/handoff.md)
- Worked examples by tier: [examples.md](examples.md)
- Cross-platform install and hooks: see repo `PORTABILITY.md`
