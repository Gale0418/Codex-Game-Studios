# Session Lifecycle

## Start

- Read `SKILL.md`.
- Read `AGENTS.md`.
- Read `production/stage.txt` and `production/active.md`.
- Load only the references needed for the current lane.
- Record the active stage, lane, and open risks before making changes.
- Read `runtime/execution-policy.md` before the first tool call.

## Before tool use

- Check whether the action stays inside the current lane.
- Ask before broad, risky, or cross-domain changes.
- Record a short assumption if you proceed with an unresolved detail.

## After tool use

- Record changed files and verification status.
- Note any unresolved assumption or follow-up needed.
- Update the active note if the stage or lane changed.
- Add a short audit line when routing, hooks, or shared indexes changed.
- If the current lane is done, close finished agents immediately and save a short checkpoint before starting the next wave.

## Compact

- Save the current stage, lane, risks, and next step into a short handoff note.
- Preserve only the active thread state, not the full discussion.
- Reopen a fresh agent only when a new lane or wave is needed.

## Stop

- Finalize the session log.
- Record blockers, residual risk, and the next verified step.
- Close the subagent thread once its output is captured.
- Reopen with a fresh agent only when a new lane or wave is needed.
- If a new command or workflow was added, update the shared indexes and validation script before the session closes.

## Log fields

- `session_id`
- `role`
- `lane`
- `scope`
- `files`
- `verification`
- `residual_risk`
- `next_step`
