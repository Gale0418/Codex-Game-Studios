# Runtime Guardrails

## Approval rules

- Ask before creating, overwriting, or deleting files when the task is broad or ambiguous.
- Ask before any multi-file change that could alter behavior outside the user’s requested scope.
- Ask before writing reports or artifacts that the user has not explicitly requested.

## File boundaries

- Keep each agent inside its assigned lane.
- Do not edit unrelated files just because they are nearby.
- Prefer the smallest file set that can safely solve the task.

## Dangerous operations

- Do not suggest destructive commands.
- Treat force-push, hard reset, bulk delete, and secret access as blocked unless the user explicitly asks and it is safe.
- If a task depends on a risky action, raise it as a decision point before proceeding.

## Verification rule

- If a task touches gameplay, AI, persistence, UI state, or release flow, require a verification step before handoff.
- If a result cannot be verified automatically, mark it as `MANUAL CHECK NEEDED`.

