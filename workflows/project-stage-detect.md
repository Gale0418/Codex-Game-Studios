# Project Stage Detect

## Purpose

- Determine the current project stage and identify missing artifacts.

## Trigger

- Use when the task needs stage, gap, or readiness assessment.

## Primary lane

- `intake-scan`
- `qa-regression`
- `docs-release`

## Inputs

- Stage notes
- Production state
- Relevant docs
- Existing tests or validation evidence

## Steps

1. Inspect the current stage and active note.
2. List what is present, missing, and stale.
3. Decide whether the task is ready for a heavier workflow.
4. If the stage is still unclear, point back to `/start`.
5. If the user is new or the repo is still being adopted, point to `/onboard`.
6. If ready, name the next gate and the next workflow.
7. Record the handoff path.

## Outputs

- Stage report
- Gap list
- Next steps
- Wave goal if the next step needs subagents

## Exit criteria

- The current stage and the next gate are both explicit.

## Default Use

- Prefer this workflow immediately after `/start`.
- Use it before picking any design, implementation, or release workflow.

## Template

- `templates/project-stage-report.md`
