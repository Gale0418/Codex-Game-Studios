# Help

## Purpose

- Route to the best next command.

## Canonical source

- Full registry: `references/command-registry.md`

## Use when

- The user asks what to do next.
- The user asks which command fits best.

## Primary lane

- `control-plane`
- `workflow-catalog`
- `intake-scan`

## Inputs

- User request
- Current repo state
- Available commands

## Steps

1. Identify the task shape.
2. Pick the shortest safe command.
3. Give one reason.
4. Hand back one next step.

## Outputs

- Recommended command
- Short reason
- Next step

## Exit criteria

- The user can pick a command without guessing.

## Quick chooser

- Unknown start: `/start`
- Need command name: `/help`
- Need project stage: `/project-stage-detect`
- Need onboarding: `/onboard`
- Need setup baseline: `/setup-engine`
- Need design direction: `/quick-design` or `/design-review`
- Need bug report: `/bug-report`
- Need verification: `/qa-plan`, `/smoke-check`, or `/team-qa`
- Need release readiness: `/release-checklist` or `/team-release`
- Need recap: `/retrospective`

## Template

- `templates/help-response.md`
