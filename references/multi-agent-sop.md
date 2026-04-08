# Multi-Agent SOP

## Default model

- Small task: `1+0+0`
- Default task: `1+1+1`
- Medium task: `1+1+1` with a second wave if needed
- Broad task: `2+1+1` split into waves
- Maximum task: `6-slot wave` only after control-plane approval

## Roles

- `owner`: drives the lane
- `helper`: adds one narrow supporting pass
- `integrator`: closes the changeset
- `monitor`: rotates between agents to check scope, handoff quality, and checkpoint hygiene

## Wave rule

1. Write the wave goal before opening agents.
2. Open only the agents needed for that wave.
3. Assign one agent as the monitor for that wave.
4. The monitor checks scope drift, handoff quality, and whether finished agents were closed.
5. Close finished agents immediately.
6. Save a short checkpoint before the next wave.
7. Reopen fresh agents only when the next wave starts.

## Required outputs

- `wave goal`
- `findings`
- `risks`
- `files`
- `recommended_next_step`
- `checkpoint`
- `monitor_notes`

## Read order

- `SKILL.md`
- `references/codex-first.md`
- `AGENTS.md`
- `references/orchestration.md`
- `templates/wave-plan.md`
- `templates/agent-handoff.md`
