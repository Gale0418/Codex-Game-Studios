# Skill Test

## Purpose

- Test whether a skill or workflow behaves as intended.

## Trigger

- Use after changing a skill or workflow contract.

## Primary lane

- `qa-regression`
- `docs-release`
- `integration`

## Inputs

- Skill or workflow change
- Test cases
- Expected shape

## Steps

1. Run the relevant checks.
2. Compare the output shape to the contract.
3. Note any drift or missing behavior.
4. Hand back the test result.

## Outputs

- Test cases
- Result
- Notes

## Exit criteria

- The skill change is validated or blocked.

## Template

- `templates/skill-test.md`

