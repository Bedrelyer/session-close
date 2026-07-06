#!/usr/bin/env python3
"""Stop hook: suggest @session-close after substantive agent turns."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# User already closing or skipping — do not re-prompt
CLOSE_OR_SKIP = re.compile(
    r"(?:"
    r"wrap[\s-]?up|end session|close session|session close|two questions|"
    r"结束对话|收尾|跳过收尾|跳过|"
    r"セッション終了|세션\s*마무리|"
    r"cerrar sesi[oó]n|fin de session|cl[oô]turer|"
    r"Sitzung beenden|session-close|@session-close|"
    r"L0\s*Skip|Session Close Complete"
    r")",
    re.IGNORECASE,
)

# Substantive work signals in agent transcripts (jsonl or plain text)
SUBSTANTIVE = re.compile(
    r"(?:Write|StrReplace|EditNotebook|Delete|ApplyPatch|"
    r'"tool"\s*:\s*"(?:Write|StrReplace|EditNotebook|Delete|Shell)"|'
    r"tool_name.*?(?:Write|StrReplace|Shell))",
    re.IGNORECASE,
)

ALREADY_CLOSED = re.compile(
    r"Session Close Complete|session-close.*L[0-4]",
    re.IGNORECASE,
)

FOLLOWUP_ZH = (
    "Agent 本轮已结束。若本次有实质工作（改代码、多步任务、重要决策），"
    "请询问用户是否运行 @session-close 做两个经典问题的收尾反思：\n"
    "1. What should I have asked you?\n"
    "2. What am I missing?\n"
    "用户回复「收尾」则读取 session-close skill 并执行；"
    "回复「跳过」或 trivial 问答则简短确认，不再追问。"
)

FOLLOWUP_EN = (
    "This agent turn ended. If the session involved substantive work "
    "(code changes, multi-step tasks, or important decisions), "
    "ask the user whether to run @session-close for the two-question ritual:\n"
    "1. What should I have asked you?\n"
    "2. What am I missing?\n"
    "If they say wrap up / 收尾, load the session-close skill and run it. "
    "If they say skip / 跳过 or it was trivial Q&A, acknowledge briefly and stop."
)


def _noop() -> None:
    print("{}")
    sys.stdout.flush()


def _tail(text: str, n: int = 12000) -> str:
    return text[-n:] if len(text) > n else text


def _last_user_text(transcript: str) -> str:
    """Best-effort extract of the latest user message from transcript."""
    user_chunks: list[str] = []
    for line in transcript.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            if line.lower().startswith("user:"):
                user_chunks.append(line[5:].strip())
            continue
        role = obj.get("role") or obj.get("type") or ""
        if str(role).lower() in {"user", "human"}:
            content = obj.get("content") or obj.get("text") or ""
            if isinstance(content, list):
                parts = []
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "text":
                        parts.append(str(block.get("text", "")))
                    elif isinstance(block, str):
                        parts.append(block)
                content = " ".join(parts)
            user_chunks.append(str(content))
        elif "message" in obj and isinstance(obj["message"], dict):
            msg = obj["message"]
            if str(msg.get("role", "")).lower() == "user":
                user_chunks.append(str(msg.get("content", "")))
    return user_chunks[-1] if user_chunks else ""


def _pick_language(last_user: str) -> str:
    if re.search(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]", last_user):
        return "zh"
    return "en"


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        _noop()
        return 0

    status = payload.get("status", "")
    loop_count = int(payload.get("loop_count") or 0)

    if status != "completed":
        _noop()
        return 0

    if loop_count >= 1:
        _noop()
        return 0

    if payload.get("is_background_agent"):
        _noop()
        return 0

    composer_mode = payload.get("composer_mode")
    if composer_mode in {"ask", "edit"}:
        _noop()
        return 0

    transcript_path = payload.get("transcript_path")
    transcript = ""
    if isinstance(transcript_path, str) and transcript_path:
        path = Path(transcript_path)
        if path.is_file():
            transcript = path.read_text(encoding="utf-8", errors="ignore")

    if not transcript:
        _noop()
        return 0

    tail = _tail(transcript)
    last_user = _last_user_text(transcript)

    if ALREADY_CLOSED.search(tail):
        _noop()
        return 0

    if CLOSE_OR_SKIP.search(last_user):
        _noop()
        return 0

    if not SUBSTANTIVE.search(transcript):
        _noop()
        return 0

    lang = _pick_language(last_user)
    followup = FOLLOWUP_ZH if lang == "zh" else FOLLOWUP_EN
    print(json.dumps({"followup_message": followup}, ensure_ascii=False))
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
