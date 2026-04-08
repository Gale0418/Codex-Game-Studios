# Workflow Catalog

## Discovery flow

- Purpose: figure out where the project is and what is missing.
- Inputs: repo structure, docs, tests, production artifacts, source layout.
- Outputs: stage, gaps, relevant files, recommended split.

## Command discovery flow

- Purpose: help the user choose the right front-door command.
- Inputs: user intent, current state, available commands.
- Outputs: recommended command, reason, next step.

## Setup and adoption flow

- Purpose: establish the project baseline or adopt an existing repo.
- Inputs: engine choice, repo shape, current documentation.
- Outputs: setup checklist, adoption notes, risks.

## Art and UX flow

- Purpose: define art direction, asset requirements, and UX decisions.
- Inputs: visual targets, asset references, interaction goals.
- Outputs: art bible, asset spec, UX design, UX review.

## Asset audit flow

- Purpose: check asset readiness, drift, and scope gaps.
- Inputs: asset list, style targets, content scope, build state.
- Outputs: audit scope, gaps, action items, follow-up ownership.

## Systems mapping flow

- Purpose: turn a concept into systems and dependencies.
- Inputs: concept docs, gameplay ideas, current code, existing architecture notes.
- Outputs: systems list, dependency map, MVP order, risks.

## Design and story planning flow

- Purpose: move from idea to system shape, then epics, then stories.
- Inputs: concept notes, constraints, goals, deadlines.
- Outputs: design directions, architecture plan, epics, stories, ordering.
- Front-door aliases: `/design-system`, `/design-systems`.

## Architecture decision flow

- Purpose: capture an explicit decision when multiple technical paths are viable.
- Inputs: problem statement, constraints, alternatives, risks.
- Outputs: decision, tradeoffs, follow-up items.

## Architecture and control flow

- Purpose: review technical plans and formalize the routing manifest.
- Inputs: architecture notes, control requirements, routing intent.
- Outputs: architecture review, control manifest, route notes.

## Skill and lifecycle flows

- Purpose: validate command contracts, prototype ideas, or onboard a project.
- Inputs: skill changes, hypothesis, repo context, localization needs.
- Outputs: test result, improvement note, onboarding summary, prototype validation.

## QA planning flow

- Purpose: define what must be verified before handoff.
- Inputs: scope, risk, acceptance criteria, release readiness.
- Outputs: test matrix, gate criteria, execution order.

## QA and evidence flow

- Purpose: prepare tests, review evidence, and stabilize flaky checks.
- Inputs: failing tests, environment needs, evidence, endurance risks.
- Outputs: setup steps, helper notes, flakiness analysis, soak results.

## Bug and playtest flow

- Purpose: normalize bug reports and playtest evidence into usable handoffs.
- Inputs: bug details, playtest notes, repro steps, observed failures.
- Outputs: bug report, playtest report, test evidence review, next action.

## Release and hotfix flow

- Purpose: prepare release readiness or patch an urgent issue.
- Inputs: final diff, blockers, incident notes, verification state.
- Outputs: release checklist, hotfix plan, verification notes.

## Production health flow

- Purpose: track sprint progress, tech debt, and post-release learning.
- Inputs: sprint notes, operational status, debt list, playtest feedback.
- Outputs: sprint status, debt plan, retrospective, playtest report.

## Narrative continuity flow

- Purpose: keep narrative direction, tone, and content consistent.
- Inputs: story text, tone targets, content notes, narrative scope.
- Outputs: narrative review, consistency notes, action items.

## Team implementation flow

- Purpose: split a broad feature into parallel lanes.
- Inputs: request scope, target files, constraints, risk level.
- Outputs: lane assignments, patch plan, merged diff, verification notes.

## Team QA flow

- Purpose: verify changes and catch regressions before handoff.
- Inputs: changed files, bug report, acceptance criteria, QA checklist.
- Outputs: repro steps, test results, remaining failures, go/no-go advice.

## Release flow

- Purpose: prepare a large change for shipping.
- Inputs: final diff, QA results, notes on residual risk.
- Outputs: ship readiness, changelog summary, launch blockers, follow-up items.

## Reverse-document flow

- Purpose: reconstruct missing design or technical docs from code.
- Inputs: source files, runtime behavior, existing docs.
- Outputs: draft doc, gap list, unclear assumptions, validation needs.

## Review flows

- Purpose: review a change before or after implementation.
- Inputs: diff, relevant source files, acceptance criteria, risk notes.
- Outputs: findings, risks, gate decision, follow-up items.

## Delivery flows

- Purpose: sequence a feature, milestone, or release into a shippable path.
- Inputs: scope, blockers, target date, verification status.
- Outputs: plan, dependencies, blockers, next gate.

## Specialist team flows

- Purpose: run a focused lane for UI, QA, release, polish, audio, level, or combat work.
- Inputs: affected files, player impact, constraints, verification needs.
- Outputs: lane decisions, patch notes, verification notes, residual risk.
