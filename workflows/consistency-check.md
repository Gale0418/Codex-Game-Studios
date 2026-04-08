# Consistency Check

## Purpose

- Check whether related docs or systems stay consistent with each other.

## Trigger

- Use when multiple artifacts might drift apart.

## Primary lane

- `workflow-catalog`
- `integration`
- `docs-release`

## Inputs

- Related files
- Source of truth
- Target scope

## Steps

1. Find the inconsistent items.
2. Narrow the scope to the real conflicts.
3. Note the correct source of truth.
4. Hand back the correction list.

## Outputs

- Inconsistencies
- Scope
- Recommendation

## Exit criteria

- The mismatch is named and actionable.

## Template

- `templates/consistency-check.md`

