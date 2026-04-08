# Six-Slot Operating Model

## Why this exists

- The runtime can only keep a small number of subagents active at once.
- This model turns that limit into a predictable studio rotation.
- The goal is to feel heavyweight by using waves, not by keeping everything open forever.

## Default 6-slot layout

1. `intake-scan` - scope, files, problem shape, initial split
2. `architecture` - approach selection, risks, and tradeoffs
3. `implementation-a` - first narrow implementation lane
4. `implementation-b` - second narrow implementation lane
5. `qa-regression` - repro, verify, and check nearby fallout
6. `integration-release` - merge, consolidate, and hand off

## Wave plan

- Write the wave goal first so each slot knows what it is solving.
- Wave 0: control-plane decision and task classification
- Wave 1: intake + architecture
- Wave 2: implementation lanes
- Wave 3: QA + integration
- Wave 4: docs + release polish if needed

## Rotation rules

- Close finished agents before starting the next wave.
- Reuse slots for the next specialist instead of trying to keep everything alive.
- If a lane is blocked, swap in a domain specialist rather than expanding the active set.
- Keep only one integrator per changeset.
- Write a short checkpoint after every wave so the next wave can restart cleanly.

## When to split implementation lanes

- Split by domain when the task touches AI, UI, persistence, or rules at the same time.
- Split by file family when there is a clean ownership boundary.
- Split by risk when one branch is experimental and the other is straightforward.

## Output expectation

Every wave should produce:

- `findings`
- `risks`
- `files`
- `recommended_next_step`
