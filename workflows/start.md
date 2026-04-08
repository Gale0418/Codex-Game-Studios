# Start

## Purpose

- Turn an unclear request into the next safe command.

## Use when

- The task state is unclear.
- The repo needs a quick diagnosis.

## Primary lane

- `intake-scan`
- `control-plane`
- `workflow-catalog`

## Inputs

- Repo structure
- Stage note
- User intent

## Steps

1. Read the smallest relevant files.
2. Classify the request as discovery, planning, design, build, verify, or ship.
3. If the project stage is unclear, go to `/project-stage-detect`.
4. If the user is new or needs a clean setup path, go to `/onboard`.
5. If the task is broad or risky, ask before splitting.
6. Otherwise hand off to the smallest next workflow.

## Outputs

- Project state
- Suggested next command
- Split yes/no
- Wave goal if the task opens subagents

## Exit criteria

- The next workflow is obvious.

## Default Path

- `/start` -> `/project-stage-detect` -> `/onboard`
- When the task needs subagents, name the wave goal before opening the next lane.

## Template

- `templates/start-response.md`
