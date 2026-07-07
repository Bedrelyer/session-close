# Examples by Reflection Tier and Mode

## L1 Glance — inline (zh-CN trigger)

**Trigger**: `轻量收尾，帮我确认一下刚才的解释`

**Mode**: inline (default). **Tier**: L1.

**Gather**: goal = explain WebSocket handshake; accomplished = explained.

**Internal Q1/Q2** (in reasoning only): 1–2 bullets each.

**User-visible digest**:
- Q1: Should have asked wss vs ws upfront.
- Q2: Production proxy timeout defaults unchecked — suggestion.

**Act**: no handoff. Single turn. No user gate.

---

## L2 Standard — inline (en trigger)

**Trigger**: `wrap up`

**Mode**: inline. **Tier**: L2 (4 turns, 2 files edited).

**Gather**: `git diff --stat` shows `handler.py` + `test_handler.py` (test not created).

**User-visible** (single turn):

```markdown
## Session Close Complete — L2 Standard (inline)

**Reflection**:
- Q1: Should have confirmed backward-compat and error contract before editing.
- Q2: Missing tests for malformed payloads — risk.

**Handoff**: `.session-close/handoffs/20260706-1400-handler-fix.md`
**Update log**: `.session-close/update-log.md` (3 entries: handoff create, INDEX append, no memory)
**Now**: —
**Next**: `pytest tests/test_handler.py -k malformed`
```

**Handoff file** contains full 3-bullet Q1 and Q2. No user gate. No second turn.

---

## L2 — off (zh-CN)

**Trigger**: `收尾 不反思`

**Mode**: off. **Tier**: L2.

**Phase 2**: skipped.

**User-visible**:

```markdown
## Session Close Complete — L2 Standard (off)

**Reflection**: skipped (off mode)
**Handoff**: `.session-close/handoffs/20260706-1500-handler-fix.md`
**Update log**: `.session-close/update-log.md` (2 entries: handoff create, INDEX append)
**Now**: —
**Next**: run pytest on handler tests
```

Handoff has Goal/Accomplished/Now/Next only — no Q1/Q2 section.

---

## L2 — interactive (zh-CN)

**Trigger**: `收尾 反思讨论`

**Mode**: interactive. **Tier**: L2.

**Turn 1**: full Q1/Q2 bullets in chat + "Which points land?"

**Turn 2** (after user confirms test gap): Now/Next + handoff + closing report.

---

## L3 Deep — inline (ja + override)

**Trigger**: `セッション終了 深度 config refactor`

**Mode**: inline. **Tier**: L3.

**Gather**: 6 files, config schema change, migration script added.

**User-visible**: ≤3-line digest + handoff path. Full Q1/Q2 in handoff + `AGENTS.md` bullet.

Single turn. No user gate.

---

## L4 Critical — interactive (mixed en/zh)

**Trigger**: `critical close 反思讨论 准备上线 norm stats 脚本`

**Mode**: interactive. **Tier**: L4.

**Turn 1**: 5 bullets each Q1/Q2 with blocker/risk + user gate.

**Turn 2**: user confirms overwrite blocker → Now documents dry-run in handoff; no deploy commands.

---

## L0 Skip

**Trigger**: `跳过收尾，我只是问个语法问题`

**Action**: acknowledge, no ritual. "L0 Skip — no reflection run."
