# Gate Check

## Purpose

- Decide whether the current stage can advance.

## Trigger

- Use when a milestone or phase needs a pass/fail verdict.

## Primary lane

- `qa-regression`
- `architecture`
- `docs-release`

## Inputs

- Gate evidence
- Relevant diff or stage output
- Acceptance criteria
- Residual risk notes

## Steps

1. Compare the evidence against the gate criteria.
2. Mark blockers, partial passes, and unknowns.
3. Decide pass or fail and name the next action.
4. Keep the verdict short and explicit.

## Outputs

- Verdict
- Blockers
- Gate evidence

## Exit criteria

- The gate can be acted on without follow-up interpretation.

## Template

- `templates/gate-check-report.md`
