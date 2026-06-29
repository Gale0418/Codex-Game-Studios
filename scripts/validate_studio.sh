#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

fail() {
  printf 'VALIDATION_FAIL: %s\n' "$1" >&2
  exit 1
}

python "$ROOT/scripts/generate_dispatch_manifest.py" --root "$ROOT" --check ||   fail "command-registry.md derived docs or workflow contracts are out of sync"

required_files=(
  references/workflow-entry-contract.md
  references/command-entry-contract.md
  references/approval-protocol.md
  references/governance-map.md
  runtime/dispatch-manifest.md
  runtime/session-lifecycle.md
  runtime/execution-policy.md
  production/state-schema.md
  commands/index.md
  .claude/settings.json
  .claude/settings.macos.json
  .claude/settings.windows.json
  .claude/statusline.sh
  .claude/statusline.cmd
  .claude/statusline.ps1
  .github/workflows/validate-studio.yml
  .claude/docs/coordination-rules.md
  .claude/docs/agent-coordination-map.md
  .claude/docs/workflow-catalog.yaml
  .claude/hooks/README.md
  .claude/hooks/session-start.sh
  .claude/hooks/pre-tool-use.sh
  .claude/hooks/post-tool-use.sh
  .claude/hooks/pre-compact.sh
  .claude/hooks/stop.sh
  .claude/hooks/subagent-start.sh
  .claude/hooks/session-start.ps1
  .claude/hooks/pre-tool-use.ps1
  .claude/hooks/post-tool-use.ps1
  .claude/hooks/pre-compact.ps1
  .claude/hooks/stop.ps1
  .claude/hooks/subagent-start.ps1
  .claude/hooks/session-start.cmd
  .claude/hooks/pre-tool-use.cmd
  .claude/hooks/post-tool-use.cmd
  .claude/hooks/pre-compact.cmd
  .claude/hooks/stop.cmd
  .claude/hooks/subagent-start.cmd
  scripts/validate_studio.cmd
)

for rel in "${required_files[@]}"; do
  file="$ROOT/$rel"
  [ -f "$file" ] || fail "missing required file: $file"
done

path_rule_files=(
  references/path-rules/src.md
  references/path-rules/design.md
  references/path-rules/game-rules.md
  references/path-rules/ui-ux.md
  references/path-rules/qa-regression.md
  references/path-rules/tests.md
  references/path-rules/docs.md
  references/path-rules/persistence.md
  references/path-rules/release.md
  references/path-rules/runtime-production.md
  references/path-rules/assets.md
)

claude_rule_files=(
  .claude/rules/assets.md
  .claude/rules/design.md
  .claude/rules/docs.md
  .claude/rules/game-rules.md
  .claude/rules/persistence.md
  .claude/rules/qa-regression.md
  .claude/rules/release.md
  .claude/rules/runtime-production.md
  .claude/rules/src.md
  .claude/rules/tests.md
  .claude/rules/ui-ux.md
)

for rel in "${path_rule_files[@]}"; do
  file="$ROOT/$rel"
  [ -f "$file" ] || fail "missing path rule file: $file"
done

for rel in "${claude_rule_files[@]}"; do
  file="$ROOT/$rel"
  [ -f "$file" ] || fail "missing .claude rule file: $file"
done

legacy_inputs=(
  "$ROOT/commands"
  "$ROOT/references"
  "$ROOT/workflows"
  "$ROOT/README.md"
  "$ROOT/SKILL.md"
)
if [ -f "$ROOT/AGENTS.md" ]; then
  legacy_inputs+=("$ROOT/AGENTS.md")
fi
legacy_refs=$(grep -RIn '/Volumes/MyGame/codex-game-studios/' "${legacy_inputs[@]}" || true)

if [ -n "$legacy_refs" ]; then
  printf '%s
' "$legacy_refs" >&2
  fail "legacy absolute links found; use relative paths"
fi

template_inputs=(
  "$ROOT/SKILL.md"
  "$ROOT/references"/*.md
  "$ROOT/workflows"/*.md
  "$ROOT/commands"/*.md
)
if [ -f "$ROOT/AGENTS.md" ]; then
  template_inputs+=("$ROOT/AGENTS.md")
fi
refs=$(grep -RhoE 'templates/[A-Za-z0-9._-]+' "${template_inputs[@]}" | sort -u)

while IFS= read -r ref; do
  [ -z "$ref" ] && continue
  [ -f "$ROOT/$ref" ] || fail "missing template reference: $ref"
done <<EOF
$refs
EOF

printf 'VALIDATION_OK\n'
