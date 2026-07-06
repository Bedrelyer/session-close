# session-close

Cursor Agent Skill：用两个经典问题结束 AI 会话，并做分级反思与 handoff。

## 两个问题（原文）

1. **What should I have asked you?**
2. **What am I missing?**

## 反思分级

| Tier | 名称 | 场景 |
|------|------|------|
| L0 | Skip | 跳过 |
| L1 | Glance | 轻量问答 |
| L2 | Standard | 常规开发（默认） |
| L3 | Deep | 多文件 / 架构 |
| L4 | Critical | 上线 / 安全 / 不可逆 |

触发词支持中/英/日/韩/西/法/德，详见 `skill/triggers.md`。

## 安装

### Skill（个人，全项目可用）

```bash
mkdir -p ~/.cursor/skills
cp -r skill ~/.cursor/skills/session-close
```

### Stop Hook（可选，Agent 结束时提示收尾）

```bash
mkdir -p ~/.cursor/hooks
cp hooks/session-close-stop.py ~/.cursor/hooks/
chmod +x ~/.cursor/hooks/session-close-stop.py
```

合并 `hooks/hooks.json.example` 中的 `stop` 段落到 `~/.cursor/hooks.json`（若已有 hooks，只追加 `stop` 条目）。

## 使用

```
@session-close
收尾
deep close auth refactor
L4 critical close 准备上线
```

## 目录

```
skill/          # Cursor skill（SKILL.md + triggers + examples + template）
hooks/          # 可选 stop hook
```

## License

MIT
