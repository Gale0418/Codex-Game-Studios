# Codex First Map

## Fast Entry

- Read the target workspace `AGENTS.md` only when that workspace provides one.
- Read `SKILL.md`.
- Read this file.
- Choose one route and stop expanding until that workflow needs more context:
  - vague state or unknown repo posture -> `workflows/start.md`, `workflows/help.md`, `workflows/project-stage-detect.md`, or `workflows/onboard.md`
  - a direct user command -> open the matching workflow from `references/command-registry.md`
- Open `references/command-registry.md` only when you need exact command routing or aliases.

## Full Studio Audit

- Use this wider pass only for broad, risky, release, migration, or refactor work.
- Add these docs when the task needs them:
  - `references/command-registry.md`
  - `runtime/dispatch-manifest.md`
  - `runtime/execution-policy.md`
  - `runtime/session-lifecycle.md`
  - `runtime/hook-map.md`
  - `production/stage.txt`
  - `production/active.md`
  - `production/state-schema.md`

## Optional next

- `commands/index.md` for a browsable command list
- `scripts/validate_studio.sh` or `scripts/validate_studio.cmd` for validation
- `references/agent-roster.md` for role selection
- `references/project-skeleton.md` for a game-project layout
- `templates/agent-handoff.md` for subagent handoffs
- `templates/wave-plan.md` for wave goals and close conditions

## Human-only or optional for Codex-first use

- `templates/*`
- `examples/*`
- `.claude/docs/*`
- `.claude/rules/*`
- `production/history.md`
- `production/review-mode.txt`
