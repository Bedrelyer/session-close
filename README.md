# session-close

三端通用 Agent Skill：用两个经典问题结束 AI 会话，并做分级反思与 handoff。

支持 **Cursor**、**Claude Code**、**OpenAI Codex**。

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

触发词支持中/英/日/韩/西/法/德，详见安装后的 `triggers.md`。

## 统一路径（三端相同）

| 用途 | 路径 |
|------|------|
| Handoff | `.session-close/handoffs/YYYYMMDD-HHMM-<slug>.md` |
| 索引 | `.session-close/INDEX.md` |
| 记忆 | `AGENTS.md` → `CLAUDE.md` → `.cursor/rules/` → `NOTES.md` |

## 快速安装

```bash
git clone https://github.com/Bedrelyer/session-close.git
cd session-close
chmod +x install.sh
```

| 工具 | 命令 | 调用方式 |
|------|------|----------|
| Cursor | `./install.sh cursor` | `@session-close` 或「收尾」 |
| Claude Code | `./install.sh claude` | `/session-close` 或「收尾」 |
| Codex | `./install.sh codex` | `/session-close` 或按 description 发现 |
| 全部 | `./install.sh all` | — |

### Cursor 可选 Stop Hook

`install.sh cursor` 会复制 hook 脚本。将 `platforms/cursor/hooks/hooks.json.example` 中的 `stop` 条目合并到 `~/.cursor/hooks.json`。

### Codex 额外步骤

1. 合并 `platforms/codex/config.toml.snippet` 到 `~/.codex/config.toml`
2. 可选：将 `platforms/codex/AGENTS.md.snippet` 追加到 `~/.codex/AGENTS.md`

### Claude Code 可选 Hook

见 [platforms/claude-code/hooks.md](platforms/claude-code/hooks.md)。

## 使用示例

```
@session-close          # Cursor
/session-close          # Claude Code / Codex
收尾
deep close auth refactor
L4 critical close 准备上线
轻量收尾
```

## 仓库结构

```
core/                 # 工具无关工作流（单一来源）
platforms/
  cursor/             # Cursor 路径 + stop hook
  claude-code/        # Claude Code 路径 + hooks 文档
  codex/              # Codex 路径 + config/AGENTS 片段
install.sh            # 合并 core + platform → 各端 skills 目录
PORTABILITY.md        # 三端对照与迁移说明
```

## 无 Skill 时的最小 Prompt

任意聊天工具可粘贴：

```text
请按 session-close 流程收尾（L2）：
1. What should I have asked you?
2. What am I missing?
Handoff 写入 .session-close/handoffs/
```

## License

MIT
