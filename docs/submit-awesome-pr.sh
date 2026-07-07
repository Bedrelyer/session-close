#!/usr/bin/env bash
# Submit session-close to awesome-cursor-skills (manual fork workflow).
# Requires: git, GitHub account with fork of spencerpauly/awesome-cursor-skills
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PATCH="$ROOT/docs/awesome-pr.patch"
WORKDIR="${TMPDIR:-/tmp}/awesome-cursor-skills-submit"

echo "=== awesome-cursor-skills PR submit helper ==="
echo
echo "1. Fork https://github.com/spencerpauly/awesome-cursor-skills on GitHub"
echo "2. Replace FORK below with your GitHub username (e.g. Bedrelyer)"
echo "3. Re-run: FORK=YourUser $0"
echo

FORK="${FORK:-}"
if [[ -z "$FORK" ]]; then
  exit 0
fi

rm -rf "$WORKDIR"
git clone --depth 1 "https://github.com/$FORK/awesome-cursor-skills.git" "$WORKDIR"
cd "$WORKDIR"
git checkout -b add-session-close
patch -p1 < "$PATCH"
git add README.md
git -c user.name="Bedrelyer" -c user.email="lyz1907@outlook.com" commit -m "Add session-close to Workflow section"
git push -u origin add-session-close

echo
echo "4. Open PR: https://github.com/spencerpauly/awesome-cursor-skills/compare/main...$FORK:add-session-close"
echo "5. Paste body from: $ROOT/docs/awesome-pr-body.md"
