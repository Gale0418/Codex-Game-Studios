# Acceptance Gates

- The change must match the source of truth in the repo.
- Any touched gameplay or AI rule must be verified with a targeted pass.
- Any persistence or restore path must be checked after reload or state reset.
- Any UI change must be checked on desktop and narrow viewport if relevant.
- Any multi-file task must either have one integration pass or a clear reason it is not needed.
- The final summary must list residual risk, not just the happy path.
- If the task is ambiguous, the chosen interpretation must be stated.

