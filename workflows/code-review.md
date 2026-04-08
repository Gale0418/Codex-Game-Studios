# Code Review

## Purpose

- Review implementation for bugs, regressions, and missing tests.

## Trigger

- Use after a patch or before merge.

## Primary lane

- `qa-regression`
- `architecture`
- `docs-release`

## Inputs

- Diff
- Related source files
- Acceptance criteria
- Test evidence

## Steps

1. Read the diff in the context of the surrounding code.
2. Check for behavioral regressions and missing tests.
3. Separate hard findings from lower-risk concerns.
4. Recommend merge, rework, or follow-up verification.

## Outputs

- Findings
- Risks
- Verdict

## Exit criteria

- The review result is specific enough to act on immediately.

## Template

- `templates/code-review-report.md`
