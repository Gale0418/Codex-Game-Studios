# Hook Map

## Session start

- Initialize current stage, active role, and open risks.
- Load the minimum relevant references.
- Use `runtime/session-lifecycle.md` as the checklist for the active session.
- Use `runtime/dispatch-manifest.md` to confirm the route before splitting.
- Use `runtime/execution-policy.md` to confirm allowed and denied actions before any tool call.
- Load `references/codex-first.md` when the session is still in the shortest-entry phase.

## Pre-tool

- Check whether the requested action stays inside the current lane.
- Stop and escalate if the action is risky or broad.
- Record the intended file set before broad multi-file edits.

## Post-tool

- Record what changed and whether verification is needed.
- Mark any unresolved assumption.
- Write a short audit note when the change affects routing, hooks, or shared indexes.

## Compact

- Summarize active context into a short handoff note.
- Preserve only the current state, not the entire conversation.
- Save the checkpoint before opening the next wave or subagent batch.

## Stop

- Finalize the session log.
- Record blockers, residual risks, and next steps.
- Write the final state back into `production/` if the task is large enough to need a handoff.
- Cross-check the note against `production/state-schema.md`.
- Write the command inventory or routing updates into the shared indexes before closing.
- If the wave changed the command inventory or routing surface, sync `commands/index.md`, `runtime/dispatch-manifest.md`, `references/workflow-playbooks.md`, `references/workflow-catalog.md`, `references/template-index.md`, and `scripts/validate_studio.sh` before closing.
- Close finished subagents before the stop step completes.

## Subagent log

- Record each agent’s role, output shape, and handoff status.
- Keep one concise entry per wave or major turn.
