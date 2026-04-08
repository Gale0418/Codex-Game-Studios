# Test Flakiness

## Purpose

- Investigate flaky tests and identify the cause pattern.

## Trigger

- Use when tests fail intermittently.

## Primary lane

- `qa-regression`
- `integration`
- `docs-release`

## Inputs

- Flaky tests
- Recent runs
- Environment notes

## Steps

1. Identify the flaky set.
2. Look for timing or environment causes.
3. Recommend the next stabilization step.
4. Hand back the flakiness note.

## Outputs

- Flaky tests
- Causes
- Next step

## Exit criteria

- The flake source is understood or narrowed.

## Template

- `templates/test-flakiness.md`

