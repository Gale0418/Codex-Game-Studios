# Dispatch Manifest

## Canonical source

- `references/command-registry.md` is the source of truth.
- This file is a short routing view.

## Routing principle

- Route by task shape first.
- Use the light path for tiny local fixes.
- Use the full path for broad or risky work.

## Routing map

| Group | Examples | Output |
| --- | --- | --- |
| Discovery | `/start`, `/help`, `/project-stage-detect`, `/onboard`, `/adopt` | state, next step |
| Planning | `/brainstorm`, `/estimate`, `/scope-check`, `/sprint-plan`, `/setup-engine` | plan, risks |
| Design | `/quick-design`, `/ux-design`, `/art-bible`, `/design-review`, `/design-system` | direction, constraints |
| Build | `/dev-story`, `/prototype`, `/bug-report`, `/code-review` | patch plan, findings |
| Verify | `/qa-plan`, `/smoke-check`, `/regression-suite`, `/gate-check` | coverage, verdict |
| Ship | `/release-checklist`, `/patch-notes`, `/team-release`, `/retrospective` | readiness, handoff |

## Handoff

- Every lane returns `findings`, `risks`, `files`, and `recommended_next_step`.
- The command file chooses the route.
- The workflow file explains the steps.
