# Execution Policy

## Allow

- `git status`
- `git diff`
- `git log`
- `git branch`
- `rg`
- `sed`
- `pytest`
- `bash scripts/validate_studio.sh`
- `cmd /c scripts\\validate_studio.cmd`

## Deny

- `rm -rf`
- `git reset --hard`
- `git push --force`
- direct secret access
- writing outside the current repo without explicit approval

## Hook model

- `SessionStart`: load `SKILL.md`, `AGENTS.md`, `references/codex-first.md`, stage state, and the smallest usable reference set.
- `PreToolUse`: confirm the action stays inside the current lane and escalate broad or risky steps.
- `PostToolUse`: record changed files, verification status, and unresolved assumptions.
- `PreCompact`: reduce the session to stage, lane, risk, checkpoint, and next step.
- `Stop`: finalize the session log, close finished agents, and write handoff notes to `production/` when needed.
- `SubagentStart`: log the agent role, lane, wave goal, and expected handoff shape.

## Audit trail

- Record the active stage and lane before edits.
- Record changed files after edits.
- Record verification evidence before claiming completion.
- Record residual risk when the work touches AI logic, persistence, UI state, or release surfaces.
- Record the wave checkpoint before opening the next batch of subagents.
