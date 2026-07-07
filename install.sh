#!/usr/bin/env bash
# Install session-close skill for Cursor, Claude Code, or Codex.
# Usage: ./install.sh cursor|claude|codex|all

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SHARED_DESCRIPTION='Runs the two-question end-of-session ritual when explicitly invoked (@session-close, /session-close, 收尾). Default inline mode: Q1/Q2 in reasoning, single-turn digest; optional off (不反思) or interactive (反思讨论). Handoff to .session-close/handoffs/. Works in Cursor, Claude Code, and Codex.'

write_skill_md() {
  local platform_file="$1"
  local dest="$2"
  mkdir -p "$dest/templates"
  {
    echo "---"
    echo "name: session-close"
    echo "description: >-"
    echo "  $SHARED_DESCRIPTION"
    echo "disable-model-invocation: true"
    echo 'argument-hint: "[depth] [focus] — e.g. deep auth refactor, 轻量, L2"'
    echo "---"
    echo ""
    echo "# Session Close"
    echo ""
    cat "$platform_file"
    echo ""
    cat "$ROOT/core/workflow.md"
  } > "$dest/SKILL.md"
  cp "$ROOT/core/triggers.md" "$dest/triggers.md"
  cp "$ROOT/core/examples.md" "$dest/examples.md"
  cp "$ROOT/core/templates/handoff.md" "$dest/templates/handoff.md"
  echo "Installed skill → $dest"
}

install_cursor() {
  local dest="${HOME}/.cursor/skills/session-close"
  write_skill_md "$ROOT/platforms/cursor/platform.md" "$dest"
  mkdir -p "${HOME}/.cursor/hooks"
  cp "$ROOT/platforms/cursor/hooks/session-close-stop.py" "${HOME}/.cursor/hooks/"
  chmod +x "${HOME}/.cursor/hooks/session-close-stop.py"
  echo "Installed hook (noop) → ${HOME}/.cursor/hooks/session-close-stop.py"
  echo "  Hook does not auto-prompt; invoke @session-close explicitly."
}

install_claude() {
  local dest="${HOME}/.claude/skills/session-close"
  write_skill_md "$ROOT/platforms/claude-code/platform.md" "$dest"
  echo ""
  echo "Optional hooks: $ROOT/platforms/claude-code/hooks.md"
}

install_codex() {
  local dest="${HOME}/.agents/skills/session-close"
  write_skill_md "$ROOT/platforms/codex/platform.md" "$dest"
  echo ""
  echo "Register in ~/.codex/config.toml — see:"
  echo "  $ROOT/platforms/codex/config.toml.snippet"
  echo "Optional AGENTS.md rule — see:"
  echo "  $ROOT/platforms/codex/AGENTS.md.snippet"
}

usage() {
  echo "Usage: $0 cursor|claude|codex|all"
  exit 1
}

[[ $# -eq 1 ]] || usage

case "$1" in
  cursor) install_cursor ;;
  claude) install_claude ;;
  codex) install_codex ;;
  all)
    install_cursor
    echo "---"
    install_claude
    echo "---"
    install_codex
    ;;
  *) usage ;;
esac
