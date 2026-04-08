# Balance Check

## Purpose

- Review tuning for fairness, pacing, and player feel.

## Trigger

- Use when numbers, difficulty, or pacing changed.

## Primary lane

- `game-designer`
- `economy-designer`
- `qa-regression`

## Inputs

- Tuning values
- Player feel notes
- Comparable targets
- Regression risk

## Steps

1. Identify which tuning values moved.
2. Check whether the new values still fit the intended experience.
3. Flag the smallest safe adjustment if the feel drifted.
4. Hand back the tuning risks and verification needs.

## Outputs

- Observations
- Balance risks
- Suggested adjustments

## Exit criteria

- The tuning decision is clear enough to implement or reject.

## Template

- `templates/balance-check-report.md`
