# Approval Protocol

## Required control loop

1. `Question`: restate the task and identify the uncertainty or risk.
2. `Options`: present the lowest-risk path and one clear alternative.
3. `Decision`: wait for the chosen direction before broad execution.
4. `Draft`: prepare the narrowest safe change or plan for review.
5. `Approval`: do not treat the draft as final until the user or gate owner signs off.
6. If the task will use subagents, name the wave goal, owner, helper, and integrator before the first write.

## Write gate

- Do not start broad multi-file writes until the direction is explicit.
- Do not treat exploratory analysis as permission to rewrite architecture.
- Use the light path for tiny safe fixes; use the full approval loop for broad, risky, or cross-domain work.
- Record assumptions as assumptions until they are approved decisions.
- Close finished agents immediately and start the next wave only after the checkpoint is written.

## Sign-off rules

- User sign-off is required for broad or user-visible behavior changes.
- Lead or gate sign-off is required before release or milestone closure.
- If approval is missing, stop at draft or recommendation rather than claiming completion.
