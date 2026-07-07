# session-close

**[English](./README.md)** | 简体中文

> 用两个经典问题结束 AI 会话。会话交接文档、分级反思、三端通用。

三端通用 Agent Skill：用两个经典问题结束 AI 会话，并做分级反思与会话交接（handoff）。

支持 **Cursor**、**Claude Code**、**OpenAI Codex**。

**仅在你显式调用时运行**（`@session-close` / `/session-close` / `收尾`），不会自动多开一轮对话。

**当前版本**：0.5.0 · 完整变更见 [CHANGELOG.md](CHANGELOG.md)

## 一键安装

```bash
git clone https://github.com/Bedrelyer/session-close.git && cd session-close && ./install.sh cursor
```

## 普通结束 vs session-close

| | 普通结束对话 | session-close |
|---|-------------|---------------|
| 上下文 | 留在聊天记录里，新会话需重述 | 写入 `.session-close/handoffs/` 文件 |
| 反思 | 无结构化回顾 | 两个经典问题（Q1/Q2） |
| 续接 | 手动复制粘贴 | Resume Prompt 可直接粘贴 |
| 审计 | 无 | INDEX + update-log 可追溯 |

## 什么是 Handoff？

**Handoff**（会话交接文档）是一次 session-close 结束时写入项目的 Markdown 文件，用来把「这次聊了什么、做到了什么、下次从哪继续」固定下来，方便**下一次对话**（或换 Agent / 换工具）直接接上，不必从头复述背景。

典型内容包括：

| 区块 | 作用 |
|------|------|
| Goal / Accomplished / Deferred | 目标、已完成、暂缓及原因 |
| Q1 / Q2 | 两个经典问题的**完整**回答（inline 模式下聊天里只显示 digest，全文在这里） |
| Now / Next | 当前状态与下一步可执行动作 |
| Resume Prompt | 可复制粘贴的续聊提示词 |
| Files Touched | 本次涉及的文件 |

文件路径：`.session-close/handoffs/YYYYMMDD-HHMM-<slug>.md`（例如 `20260707-1430-handler-fix.md`）。  
索引汇总在 `.session-close/INDEX.md`。

## 两个问题（原文）

1. **What should I have asked you?**
2. **What am I missing?**

## 反思模式

| 模式 | 触发示例 | 对话轮次 | 用户可见 |
|------|----------|----------|----------|
| **inline**（默认） | `收尾`, `@session-close` | 1 | ≤3 行 digest；完整 Q1/Q2 在交接文档 |
| **off** | `收尾 不反思`, `no reflection` | 1 | 无反思，仅交接文档 + Now/Next |
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
| 会话交接（Handoff） | `.session-close/handoffs/YYYYMMDD-HHMM-<slug>.md` |
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
收尾                      # inline：单轮 digest + 交接文档
收尾 不反思                # off：无 Q1/Q2
收尾 反思讨论              # interactive：完整反思 + 等你确认
@session-close
deep close auth refactor
L4 critical close 准备上线
```

## 版本记录

| 版本 | 日期 | 要点 |
|------|------|------|
| **0.5.0** | 2026-07-07 | 英文默认 README + 中文 README.zh-CN.md；国际传播素材 |
| **0.4.0** | 2026-07-07 | Phase 4 每次文件变更必记 `.session-close/update-log.md`；新增日志行模板 |
| **0.3.0** | 2026-07-07 | 反思模式 inline / off / interactive；inline 默认单轮；Stop hook 改为 noop |
| **0.2.0** | 2026-07-06 | 三端结构 `core/` + `platforms/`；统一 handoff 路径；`install.sh` |
| **0.1.0** | 2026-07-06 | 初始 Cursor skill；L0–L4 分级；两问工作流；多语言触发词 |

详细条目见 [CHANGELOG.md](CHANGELOG.md)。

## 相关链接

- [PORTABILITY.md](PORTABILITY.md) — 三端安装与路径对照
- [Issues](https://github.com/Bedrelyer/session-close/issues) — 反馈与功能请求

> 维护提示：更新 README 时请同步 [README.md](./README.md) 与本文档。

## License

MIT
