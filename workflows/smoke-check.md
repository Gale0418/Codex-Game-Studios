# Smoke Check

## Purpose

- Run a fast sanity pass over the changed behavior.

## Trigger

- Use after a small patch or before deeper QA.

## Primary lane

- `qa-regression`
- `integration`
- `docs-release`

## Inputs

- Changed files
- Key behavior
- Known risks

## Steps

1. Run the shortest useful checks.
2. Confirm the core path still works.
3. Note any obvious regressions.
4. Hand back the smoke result.

## Outputs

- Smoke steps
- Result
- Notes

## Exit criteria

- The change is either safe to deepen or blocked.

## Template

- `templates/smoke-check.md`

