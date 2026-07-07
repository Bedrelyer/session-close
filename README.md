# session-close

三端通用 Agent Skill：用两个经典问题结束 AI 会话，并做分级反思与 handoff。

支持 **Cursor**、**Claude Code**、**OpenAI Codex**。

**仅在你显式调用时运行**（`@session-close` / `/session-close` / `收尾`），不会自动多开一轮对话。

## 两个问题（原文）

1. **What should I have asked you?**
2. **What am I missing?**

## 反思模式

| 模式 | 触发示例 | 对话轮次 | 用户可见 |
|------|----------|----------|----------|
| **inline**（默认） | `收尾`, `@session-close` | 1 | ≤3 行 digest；完整 Q1/Q2 在 handoff |
| **off** | `收尾 不反思`, `no reflection` | 1 | 无反思，仅 handoff + Now/Next |
| **interactive** | `收尾 反思讨论`, `review reflection` | 2+ | 完整 Q1/Q2 + 等待确认 |

inline 模式下 Q1/Q2 在**思考过程**中完成，不占用额外对话轮次。

## 反思分级

| Tier | 名称 | 场景 |
|------|------|------|
| L0 | Skip | 跳过 |
| L1 | Glance | 轻量问答 |
| L2 | Standard | 常规开发（默认） |
| L3 | Deep | 多文件 / 架构 |
| L4 | Critical | 上线 / 安全 / 不可逆 |

## 统一路径（三端相同）

| 用途 | 路径 |
|------|------|
| Handoff | `.session-close/handoffs/YYYYMMDD-HHMM-<slug>.md` |
| 索引 | `.session-close/INDEX.md` |
| 更新日志 | `.session-close/update-log.md`（每次写入/更新必记一条） |
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
| Codex | `./install.sh codex` | `/session-close` |
| 全部 | `./install.sh all` | — |

### Cursor Stop Hook

已注册但 **noop**（不自动追问），避免额外对话轮。用户需显式调用 session-close。

### Codex 额外步骤

1. 合并 `platforms/codex/config.toml.snippet` 到 `~/.codex/config.toml`
2. 可选：`platforms/codex/AGENTS.md.snippet` → `~/.codex/AGENTS.md`

## 使用示例

```
收尾                      # inline：单轮 digest + handoff
收尾 不反思                # off：无 Q1/Q2
收尾 反思讨论              # interactive：完整反思 + 等你确认
@session-close
deep close auth refactor
L4 critical close 准备上线
```

## License

MIT
