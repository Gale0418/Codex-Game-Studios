# Hotfix

## Purpose

- Patch a production issue with the smallest safe change.

## Trigger

- Use when something broken needs immediate repair.

## Primary lane

- `release-manager`
- `qa-regression`
- `integration`

## Inputs

- Incident report
- Failing path
- Risk notes

## Steps

1. Narrow the problem to the smallest fix.
2. Patch only the urgent issue.
3. Verify the fix with the shortest useful check.
4. Hand back the hotfix summary.

## Outputs

- Incident
- Patch
- Verification

## Exit criteria

- The urgent issue is fixed and verified.

## Template

- `templates/hotfix.md`

