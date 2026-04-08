# Control Plane

## When to use the full studio flow

- Use the full flow for broad tasks, ambiguous tasks, or tasks that touch 2 or more subsystems.
- Use the full flow when the task affects gameplay rules, AI behavior, persistence, UI state, or release readiness.
- Use the full flow when independent review or parallel verification would reduce risk.
- When the full flow is chosen, define the wave goal, the lane owner, and the handoff shape before opening the first subagent wave.

## When to stay light

- Use a lighter path for single-file fixes, tiny content edits, or obvious low-risk changes.
- Do not spin up extra agents when one clear pass is enough.
- Use `references/codex-first.md` to keep the light path short and predictable.

## Decision loop

1. Inspect the repo and relevant instructions.
2. Ask the user for direction if the task is ambiguous.
3. Present the lowest-risk path plus one clear alternative.
4. Wait for the decision.
5. Split work only after the direction is clear.
6. If the task needs waves, close finished agents before opening the next wave and record a short checkpoint.

## Approval protocol

- Follow `Question -> Options -> Decision -> Draft -> Approval`.
- Do not treat exploratory work as permission for broad writes.
- For broad or risky changes, stop at draft until approval is explicit.
- Use `references/approval-protocol.md` when the task touches user-visible behavior, architecture, or release readiness.

## Approval gate

- Never treat a draft as final without verification.
- Never write broad changes without an explicit handoff plan.
- Keep user-visible assumptions labeled as assumptions.
