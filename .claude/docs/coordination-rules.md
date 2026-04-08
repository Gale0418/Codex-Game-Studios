# Coordination Rules Mirror

This mirror exists to provide the `.claude`-style entry point used by the original studio pack.

## Source of truth

- `references/control-plane.md`
- `references/approval-protocol.md`
- `references/studio-hierarchy.md`
- `references/orchestration.md`

## Core rules

- Follow `Question -> Options -> Decision -> Draft -> Approval` before broad or risky writes.
- Do not start a parallel implementation wave until the route reaches `Decision`.
- Escalate specialist conflict to the relevant lead; escalate cross-domain conflict to producer plus the relevant directors.
- Close finished subagents immediately after handoff so the slot can be reused.
