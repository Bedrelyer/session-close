#!/usr/bin/env python3
"""Cursor stop hook — intentionally noop.

Auto-prompt via followup_message was disabled to avoid an extra conversation
turn. Users must explicitly invoke session-close (@session-close or 收尾).

This script remains registered so hooks.json needs no change; it always
returns {} and never injects followup_message.
"""

from __future__ import annotations

import json
import sys


def _noop() -> None:
    print("{}")
    sys.stdout.flush()


def main() -> int:
    try:
        json.load(sys.stdin)
    except json.JSONDecodeError:
        pass
    _noop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
