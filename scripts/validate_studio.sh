#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

fail() {
  printf 'VALIDATION_FAIL: %s\n' "$1" >&2
  exit 1
}

workflow_names=(
  art-bible
  architecture-decision
  architecture-review
  asset-spec
  asset-audit
  adopt
  balance-check
  brainstorm
  bug-intake
  bug-report
  bug-triage
  consistency-check
  content-audit
  changelog
  code-review
  create-architecture
  create-control-manifest
  create-epics
  create-stories
  design-review
  design-system
  design-systems
  dev-story
  gate-check
  help
  hotfix
  launch-checklist
  map-systems
  milestone-review
  onboard
  estimate
  regression-suite
  soak-test
  qa-plan
  release-checklist
  patch-notes
  perf-profile
  playtest-report
  project-stage-detect
  prototype
  propagate-design-change
  retrospective
  quick-design
  scope-check
  smoke-check
  reverse-document
  setup-engine
  review-all-gdds
  skill-improve
  skill-test
  sprint-status
  story-done
  story-readiness
  sprint-plan
  start
  team-audio
  team-combat
  team-level
  team-polish
  team-qa
  team-release
  team-live-ops
  team-ui
  team-narrative
  tech-debt
  test-evidence-review
  test-flakiness
  test-helpers
  test-setup
  ux-design
  ux-review
  localize
)

command_names=(
  art-bible
  architecture-decision
  architecture-review
  asset-spec
  asset-audit
  adopt
  balance-check
  brainstorm
  bug-intake
  bug-report
  bug-triage
  consistency-check
  content-audit
  changelog
  code-review
  create-architecture
  create-control-manifest
  create-epics
  create-stories
  design-review
  design-system
  design-systems
  dev-story
  gate-check
  help
  hotfix
  launch-checklist
  map-systems
  milestone-review
  onboard
  estimate
  regression-suite
  soak-test
  qa-plan
  release-checklist
  patch-notes
  perf-profile
  playtest-report
  project-stage-detect
  prototype
  propagate-design-change
  retrospective
  quick-design
  scope-check
  smoke-check
  reverse-document
  setup-engine
  review-all-gdds
  skill-improve
  skill-test
  sprint-status
  story-done
  story-readiness
  sprint-plan
  start
  team-audio
  team-combat
  team-level
  team-polish
  team-qa
  team-release
  team-live-ops
  team-ui
  team-narrative
  tech-debt
  test-evidence-review
  test-flakiness
  test-helpers
  test-setup
  ux-design
  ux-review
  localize
)

required_sections=(
  "Primary lane"
  Inputs
  Steps
  Outputs
  "Exit criteria"
  Template
)

for name in "${workflow_names[@]}"; do
  file="$ROOT/workflows/$name.md"
  [ -f "$file" ] || fail "missing workflow: $file"
  for section in "${required_sections[@]}"; do
    grep -q "^## ${section}$" "$file" || fail "missing section ${section} in $file"
  done
done

for name in "${command_names[@]}"; do
  file="$ROOT/commands/$name.md"
  [ -f "$file" ] || fail "missing command: $file"
done

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
  .claude/statusline.ps1
  scripts/validate_studio.cmd
  .github/workflows/validate-studio.yml
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

legacy_refs=$(grep -RIn '/Volumes/MyGame/codex-game-studios/' \
  "$ROOT/commands" \
  "$ROOT/references" \
  "$ROOT/workflows" \
  "$ROOT/README.md" \
  "$ROOT/SKILL.md" \
  "$ROOT/AGENTS.md" \
  || true)

if [ -n "$legacy_refs" ]; then
  printf '%s\n' "$legacy_refs" >&2
  fail "legacy absolute links found; use relative paths"
fi

refs=$(grep -RhoE 'templates/[A-Za-z0-9._-]+' \
  "$ROOT/SKILL.md" \
  "$ROOT/AGENTS.md" \
  "$ROOT/references"/*.md \
  "$ROOT/workflows"/*.md \
  "$ROOT/commands"/*.md \
  | sort -u)

while IFS= read -r ref; do
  [ -z "$ref" ] && continue
  [ -f "$ROOT/$ref" ] || fail "missing template reference: $ref"
done <<EOF
$refs
EOF

printf 'VALIDATION_OK\n'
