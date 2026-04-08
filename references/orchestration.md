# Orchestration

## Role map

- `intake`: classify the request and isolate the smallest useful scope.
- `architecture`: compare approaches, data flow, and risk.
- `implementation`: make the change in the narrowest safe slice.
- `QA`: reproduce, verify, and check for regressions.
- `docs`: update usage notes or developer-facing guidance.
- `release`: prepare the final handoff and list residual risk.

## One-page role selection principle

1. Classify the request with `intake`.
2. Choose one owner for the lane.
3. Add at most one helper for that lane.
4. Assign one integrator for the changeset.
5. Add an engine-specific role only when the engine is known or the work depends on engine behavior.
6. Escalate to `architecture`, `QA`, or `release` only when the task needs independent review, not just because more people are available.
7. Reuse slots wave by wave so finished agents can close and new waves can take over.

## When to split into subagents

- Use 1 agent for tiny, local fixes.
- Use 3 agents for medium tasks: intake, implementation, QA.
- Use 4 to 6 agents for broad tasks: intake, architecture, implementation, QA, docs, release.
- Use the 6-slot wave when the task spans more than one domain or needs independent verification.
- Split earlier if the task touches game rules, AI behavior, persistence, UI state, or assets.
- Keep one integrator per changeset and do not let multiple lanes edit the same file unless the split is explicit.

## Parallel ownership

- Give each agent one lane only.
- Do not duplicate the same analysis across agents unless you need an independent validation pass.
- Prefer source files, logs, and observable behavior over guesswork.
- Close an agent as soon as its handoff is complete so the slot can be reused for the next wave.
- Never keep a finished agent alive just because the task is still ongoing elsewhere.
- When the slot limit gets tight, close finished agents first, then open the next wave.
- Do not launch a broad implementation wave until the approval protocol reaches `Decision`.

## Required handoff fields

Each agent should return:

- `findings`
- `risks`
- `files`
- `recommended_next_step`

## Wave rule

- Write the wave goal before opening the first slot of a new wave.
- Prefer a first wave for intake and architecture, a second wave for implementation, and a third wave for QA and release.
- If a task is still ambiguous after intake, pause before launch and route through the control plane again.
- Reuse slots wave by wave instead of holding finished agents open.
- End each wave with a short checkpoint so the next wave can resume cleanly.
