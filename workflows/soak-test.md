# Soak Test

## Purpose

- Run a longer-running stability check for a risky path.

## Trigger

- Use when a path needs time-based or endurance testing.

## Primary lane

- `qa-regression`
- `qa-lead`
- `integration`

## Inputs

- Target path
- Duration
- Stability risks

## Steps

1. Define the soak target.
2. Run the test for the chosen duration.
3. Record failures or drift.
4. Hand back the soak result.

## Outputs

- Duration
- Results
- Failures

## Exit criteria

- The stability risk is known.

## Template

- `templates/soak-test.md`

