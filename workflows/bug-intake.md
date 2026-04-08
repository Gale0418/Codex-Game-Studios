# Bug Intake

## Purpose

- Capture a reproducible bug report and initial triage.

## Trigger

- Use when a player-facing issue needs to be stabilized.

## Primary lane

- `intake-scan`
- `qa-regression`
- `docs-release`

## Inputs

- Repro steps
- Expected behavior
- Actual behavior
- Environment details

## Steps

1. Normalize the report into a reproducible shape.
2. Separate symptom from likely cause.
3. Hand off the minimal repro path to QA or implementation.
4. Keep the triage note short and concrete.

## Outputs

- Repro steps
- Expected vs actual
- Notes

## Exit criteria

- Someone can reproduce or confidently close the report.

## Template

- `templates/bug-report.md`
