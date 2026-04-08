# Team Combat

## Purpose

- Focus on rules, feel, and combat-related tuning.

## Trigger

- Use when combat or move resolution changes.

## Primary lane

- `game-designer`
- `gameplay-programmer`
- `qa-regression`

## Inputs

- Combat rules
- Move resolution
- Balance goals
- Regression risk

## Steps

1. Isolate the rule or move change.
2. Check legality, turn order, and win state impact.
3. Keep the implementation path small and observable.
4. Verify the feel and the rule result.

## Outputs

- Rules notes
- Feel notes
- Regression notes

## Exit criteria

- The combat rule works and still matches the intended feel.

## Template

- `templates/team-combat-plan.md`
