# Team Release

## Purpose

- Prepare a large change for shipping.

## Trigger

- Use when release readiness is the main concern.

## Primary lane

- `release-manager`
- `qa-lead`
- `devops-engineer`
- `producer`

## Inputs

- Final diff
- QA evidence
- Launch blockers
- Rollback notes
- Release notes draft

## Steps

1. Check readiness against the launch criteria.
2. Confirm the changelog, patch notes, and release notes boundaries.
3. Surface blockers early and separate shipping blockers from follow-up work.
4. Hand off the shipping decision and follow-up list.

## Outputs

- Release readiness
- Changelog summary
- Blockers

## Exit criteria

- The release path is explicit, the blockers are named, and the final handoff is clear.

## Template

- `templates/team-release-plan.md`
