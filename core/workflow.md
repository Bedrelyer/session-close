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

### Activation rule

Run this skill **only when the user explicitly invokes** session-close (`@session-close`, `/session-close`, or closing phrases in [triggers.md](triggers.md)). Do **not** auto-run reflection after substantive work unless explicitly asked.

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
| **L1** | Glance | < 15 min feel; no file edits; conceptual Q&A | goal only | 1–2 bullets each (internal) | — | no | no |
| **L2** | Standard | some edits or 3+ turns; single feature/fix | git status, files touched | 3 bullets each (internal) | interactive only | yes | if insight |
| **L3** | Deep | multi-file; arch/API choice; debugging marathon | full gather (see Phase 1) | 3–5 bullets + severity (internal) | interactive only | yes | yes |
| **L4** | Critical | prod/deploy/security/money/data-loss stakes | full gather + risk scan | 5 bullets + verify actions (internal) | interactive only | yes + resume prompt | yes + rules |

**Escalation rule**: when unsure between two tiers, pick the higher one for L3/L4 signals (security, deploy, irreversible ops).

**De-escalation rule**: user says `glance` / `轻量` / `L1` always wins over auto-detect.

Announce chosen tier at start: `Session close — L2 Standard (inline, auto-detected)`.

## Reflection Mode

Detect from trigger phrase. Priority: **off** > **interactive** > **inline** (default).

| Mode | Trigger examples | Behavior | Turns |
|------|------------------|----------|-------|
| **off** | `不反思`, `no reflection`, `close without reflection` | Skip Phase 2; handoff + Now/Next only | 1 |
| **inline** (default) | `收尾`, `@session-close`, `/session-close` | Q1/Q2 answered in **reasoning/thinking**; user sees ≤3-line digest only | 1 |
| **interactive** | `反思讨论`, `review reflection`, `讨论反思` | Full Q1/Q2 in chat; wait for user before Phase 3 | 2+ |

### inline mode rules

1. Answer Q1 and Q2 **completely inside reasoning/thinking** before the visible reply.
2. **Do not** paste full bullet lists in the user-visible message.
3. User-visible **Reflection digest**: at most one line per question, ≤3 lines total.
4. Write **full Q1/Q2** into the handoff file (L2+), not in chat.
5. **Do not** ask "Which points land?" or wait for user confirmation.
6. Complete Gather → Orient (internal) → Decide → Act in **one turn**.

### off mode rules

Skip Phase 2 entirely. Still run Phase 3–4 per tier (handoff at L2+).

### interactive mode rules

Show full Q1/Q2 bullets in chat, then Phase 2.5 user gate. Wait for user before Phase 3.

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

## Phase 2 — Orient (Two Questions, inline default)

**off mode**: skip this phase.

Answer Q1 then Q2 in order. Do not merge into one summary.

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

**Tier output counts** (for internal reasoning and handoff file): L1 → 1–2 each; L2 → 3 each; L3 → 3–5 each; L4 → 5 each with at least one `blocker` or `risk`.

**inline mode**: produce full bullets in reasoning/handoff only; user-visible digest ≤3 lines.

**interactive mode**: show full bullets in chat per tier counts.

Present digest in the user's conversation language; keep Q1/Q2 headers in English canonical form in handoff and interactive chat.

## Phase 2.5 — User Gate (interactive only)

**Do not run** in inline or off mode.

```markdown
## Session Reflection (L{n} {Name})

### Q1 — What should I have asked you?
- ...

### Q2 — What am I missing?
- ...

Which points land? What did I miss saying?
```

Wait for user response before Phase 3. At L4, also confirm Now items before acting.

## Phase 3 — Decide (Now vs Next)

Sort findings (+ user additions in interactive mode):
- **Now** — finishable in ~5 min (tiny fix, note, stash)
- **Next** — next session entry with a concrete first command or question

Every incomplete item → Now or Next. Nothing silent.

In **inline/off** mode, proceed without waiting for user input.

## Phase 4 — Act

Scale to tier.

| Action | L1 | L2 | L3 | L4 |
|--------|----|----|----|-----|
| Handoff file | — | yes | yes | yes |
| Full Q1/Q2 in handoff | — | yes (inline/interactive) | yes | yes |
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

Single-turn output for **inline** and **off** (no follow-up question):

```markdown
## Session Close Complete — L{n} {Name} ({reflection_mode})

**Tier**: {auto|override} — {one-line reason}
**Reflection**: {digest lines, or "skipped (off mode)"}
**Handoff**: {path or "none"}
**Memory**: {files updated or "none"}
**Now**: ...
**Next**: ...
```

## Anti-patterns

- Same-model self-reflection loop → anchor every bullet to gather evidence
- Running L3 ritual on a one-line question → de-escalate to L1
- Pasting full Q1/Q2 bullet lists in chat during **inline** mode
- Using `followup_message` or a second turn to run reflection
- Auto-running session-close without explicit user invocation
- Committing without explicit user request
- Writing handoffs to tool-specific paths (`.cursor/session-handoffs/`) — use `.session-close/handoffs/` only

## Additional Resources

- Full multilingual triggers: [triggers.md](triggers.md)
- Handoff template: [templates/handoff.md](templates/handoff.md)
- Worked examples by tier: [examples.md](examples.md)
- Cross-platform install and hooks: see repo `PORTABILITY.md`
