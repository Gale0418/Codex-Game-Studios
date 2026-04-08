# Regression Suite

## Purpose

- Run a broader regression pass for a risky change.

## Trigger

- Use when a change could affect nearby behavior.

## Primary lane

- `qa-lead`
- `qa-regression`
- `integration`

## Inputs

- Risk areas
- Test list
- Acceptance criteria

## Steps

1. Pick the most likely failure paths.
2. Run the broader regression set.
3. Record failures and coverage gaps.
4. Hand back the regression verdict.

## Outputs

- Coverage
- Results
- Failures

## Exit criteria

- The regression surface is understood.

## Template

- `templates/regression-suite.md`

