# Team UI

## Purpose

- Run a focused UI lane with design, implementation, and verification.

## Trigger

- Use when layout, interaction, or responsiveness is a major concern.

## Primary lane

- `ui-ux`
- `implementation`
- `qa-regression`

## Inputs

- Affected views
- Breakpoints
- Interaction risks
- Visual constraints

## Steps

1. Confirm which surfaces and breakpoints are in scope.
2. Separate layout, interaction, and polish work.
3. Keep state and copy concerns out of the view lane unless needed.
4. Verify the result on wide and narrow layouts.

## Outputs

- Layout decisions
- Patch summary
- Viewport verification

## Exit criteria

- The UI works on desktop and narrow viewport without layout regressions.

## Template

- `templates/team-ui-plan.md`
