# Team QA

## Purpose

- Run a regression-heavy verification lane.

## Trigger

- Use after gameplay, AI, persistence, or UI changes.

## Primary lane

- `qa-regression`
- `integration`
- `docs-release`

## Inputs

- Changed files
- Acceptance criteria
- Repro paths
- Risk notes

## Steps

1. Reproduce the affected behavior.
2. Check the nearby regressions.
3. Consolidate any overlap that needs integration.
4. Report what still fails and what is safe.

## Outputs

- Repro steps
- Coverage notes
- Residual failures

## Exit criteria

- The task can be shipped or blocked with a clear reason.

## Template

- `templates/team-qa-plan.md`
