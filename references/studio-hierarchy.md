# Studio Hierarchy

## Core chain

- `producer`: owns scope, scheduling, cross-team coordination, and final handoff.
- `creative-director`: owns vision, design direction, and major creative tradeoffs.
- `technical-director`: owns architecture, technical risk, and cross-system coherence.
- `department-leads`: own their domain and arbitrate conflicts within it.
- `specialists`: implement focused tasks inside a single lane.

## Default starting point

- Start with `producer`, `creative-director`, and `technical-director` for broad work.
- Add one domain lead only when the lane is clear.
- Add at most one helper for the same lane.
- Add specialists only after the lane owner is known.
- Keep one integrator per changeset.
- When the engine is known, the engine-specific specialist should usually support the lane owner instead of replacing them.

## Escalation rules

- Specialist disagreements escalate to their lead.
- Helper disagreements escalate to the lane owner first, then to the lead only if the lane owner cannot settle it.
- Cross-domain disagreements escalate to producer plus the relevant directors.
- Scope cuts and milestone decisions belong to producer with director input.
- Technical feasibility disputes belong to technical-director.
- Design direction disputes belong to creative-director.

## Ownership rules

- A role should only decide within its domain.
- A role may advise outside its domain, but not override the owner.
- Multi-file or multi-domain changes need a named integrator.
- The default answer for a vague request should be one owner, one helper, and one integrator.
- If a request needs more than one helper, split the lane or escalate back to producer so the changeset does not lose a single source of truth.

## Cross-domain notifications

- When design intent changes, notify implementation, QA, and release planning.
- When architecture changes, notify the relevant implementers and QA.
- When UI or accessibility constraints change, notify UI, implementation, and QA.
- When persistence or save format changes, notify implementation, QA, and release planning.

## Anti-patterns

- Do not bypass the hierarchy just because a specialist can edit the file.
- Do not let one lane silently modify another lane's responsibilities.
- Do not treat assumptions as decisions.
- Do not let a task grow so large that it loses clear ownership.
- Do not stack helpers until the lane becomes a committee.
