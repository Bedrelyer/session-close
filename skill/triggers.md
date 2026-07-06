# Multilingual Trigger Phrases

Any phrase below activates `session-close`. Partial matches and mixed-language messages count.

## English (en)

| Intent | Phrases |
|--------|---------|
| Close session | `wrap up`, `wrap-up`, `end session`, `close session`, `close out`, `let's finish`, `session close`, `done for today` |
| Two questions | `two questions`, `ask the two questions`, `end with two questions` |
| Depth override | `skip close`, `glance close`, `standard close`, `deep close`, `critical close` |

## Chinese — Simplified (zh-CN)

| Intent | Phrases |
|--------|---------|
| Close session | `结束对话`, `收尾`, `收尾一下`, `结束会话`, `关闭会话`, `今天就到这`, `会话收尾` |
| Two questions | `两个问题`, `问两个问题`, `用两个问题结束` |
| Depth override | `跳过收尾`, `轻量收尾`, `标准收尾`, `深度收尾`, `关键收尾` |

## Chinese — Traditional (zh-TW)

| Intent | Phrases |
|--------|---------|
| Close session | `結束對話`, `收尾`, `結束會話`, `關閉會話`, `會話收尾` |
| Two questions | `兩個問題`, `問兩個問題` |
| Depth override | `跳過收尾`, `輕量收尾`, `深度收尾`, `關鍵收尾` |

## Japanese (ja)

| Intent | Phrases |
|--------|---------|
| Close session | `セッション終了`, `終わり`, `締めくくり`, `今日はここまで` |
| Two questions | `二つの質問`, `2つの質問` |
| Depth override | `スキップ`, `軽量`, `標準`, `深い`, `重要` |

## Korean (ko)

| Intent | Phrases |
|--------|---------|
| Close session | `세션 마무리`, `세션 종료`, `마무리`, `오늘은 여기까지` |
| Two questions | `두 가지 질문`, `두 질문` |
| Depth override | `건너뛰기`, `가볍게`, `표준`, `깊게`, `중요` |

## Spanish (es)

| Intent | Phrases |
|--------|---------|
| Close session | `cerrar sesión`, `terminar sesión`, `finalizar`, `por hoy` |
| Two questions | `dos preguntas`, `las dos preguntas` |
| Depth override | `omitir`, `ligero`, `estándar`, `profundo`, `crítico` |

## French (fr)

| Intent | Phrases |
|--------|---------|
| Close session | `fin de session`, `clôturer`, `on s'arrête là`, `terminer la session` |
| Two questions | `deux questions`, `les deux questions` |
| Depth override | `passer`, `léger`, `standard`, `profond`, `critique` |

## German (de)

| Intent | Phrases |
|--------|---------|
| Close session | `Sitzung beenden`, `Session beenden`, `abschließen`, `für heute fertig` |
| Two questions | `zwei Fragen`, `die zwei Fragen` |
| Depth override | `überspringen`, `kurz`, `standard`, `tief`, `kritisch` |

## Matching Rules

1. **Case-insensitive** for Latin scripts.
2. **Substring match** — `let's wrap up the auth work` matches `wrap up`.
3. **Skill invocation** — `@session-close`, `/session-close`, or `session-close` alone always activates at L2 unless depth override present.
4. **Focus suffix** — text after the trigger becomes reflection focus (e.g. `收尾 auth模块` → focus on auth).
5. **Explicit tier** — `L0`–`L4` or `L1`/`L2`/`L3`/`L4` in the message overrides keyword detection.

## Depth Detection Priority

1. Explicit tier token (`L3`, `深度收尾`, `deep close`)
2. Depth override keyword (table in SKILL.md)
3. Auto-detect from session signals
4. Default to **L2** when triggered but signals are ambiguous
