# Examples by Reflection Tier

## L1 Glance — conceptual Q&A (zh-CN trigger)

**Trigger**: `轻量收尾，帮我确认一下刚才的解释`

**Auto-detect**: single concept question, no file edits → L1 (user override confirms).

**Gather**: goal = explain WebSocket handshake; accomplished = explained.

**Reflection**:

### Q1 — What should I have asked you?
- "Does my server use `wss://` or `ws://`?" — I assumed local dev without asking — would have tailored the TLS section.

### Q2 — What am I missing?
- Production reverse-proxy timeout defaults — **suggestion** — verify: check nginx `proxy_read_timeout` docs.

**Act**: no handoff. Verbal close only.

---

## L2 Standard — single feature fix (en trigger)

**Trigger**: `wrap up`

**Auto-detect**: 4 turns, 2 files edited, tests not mentioned → L2.

**Gather**: `git diff --stat` shows `handler.py` + `test_handler.py` (test not created).

**Reflection** (3 bullets each, abbreviated):

**Q1**
- "Should new handler be backward-compatible with v1 clients?" — assumed greenfield.
- "What's the error contract for malformed payloads?" — never defined.
- "Run existing test suite before editing?" — skipped.

**Q2**
- No test file for new branch — **risk** — verify: `pytest tests/test_handler.py -k malformed`
- Docstring still references old API name — **suggestion** — verify: read `handler.py` L12–20
- Rate limit behavior unchanged but payload size grew — **risk** — verify: check middleware config

**User gate**: user confirms test gap + API name stale.

**Act**: write `.session-close/handoffs/20260706-1400-handler-fix.md`. No commit (user didn't ask).

---

## L3 Deep — multi-file refactor (ja + override)

**Trigger**: `セッション終了 深度 config refactor`

**Tier**: L3 (explicit `深度` override).

**Gather**: 6 files, config schema change, migration script added, no integration test run.

**Q1** (4 bullets with evidence):
- "Which env vars must stay backward-compatible?" — `config.py` removed `LEGACY_PORT` without deprecation note.
- "Who consumes `TrainingConfig` outside training/?" — only searched `training/` dir.
- ...

**Q2** (4 bullets):
- Migration script has no dry-run flag — **risk** — verify: read `scripts/migrate_config.py`
- ...

**Act**: handoff + add bullet to `AGENTS.md` about config migration checklist.

---

## L4 Critical — production deploy (mixed en/zh)

**Trigger**: `critical close 准备上线 norm stats 脚本`

**Tier**: L4 (deploy stakes + explicit override).

**Gather** + risk scan: uncommitted changes, script writes to shared NFS path, no rollback documented.

**Q1** (5 bullets): includes "What happens if stats file already exists?" — never asked.

**Q2** (5 bullets): at least two `blocker`/`risk`:
- Overwrite behavior on existing `norm_stats.json` — **blocker** — verify: run script with `--dry-run` or read overwrite branch
- No backup step before write — **risk** — verify: confirm backup path in ops runbook

**User gate**: user confirms overwrite is blocker; agrees to add dry-run before Now.

**Now**: document dry-run requirement in handoff; do NOT run deploy commands.

**Act**: handoff with full Resume Prompt + update `AGENTS.md` deploy checklist.

---

## L0 Skip

**Trigger**: `跳过收尾，我只是问个语法问题`

**Action**: acknowledge, no ritual. "L0 Skip — no reflection run."
