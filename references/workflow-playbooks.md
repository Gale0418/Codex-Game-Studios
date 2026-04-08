# Workflow Playbooks

## Shared contract

- `commands/` is the front door.
- Every entry file follows `references/workflow-entry-contract.md`.
- Every broad workflow should state its primary lane, helper lanes, outputs, and exit criteria.
- Use `runtime/dispatch-manifest.md` when choosing the first workflow.
- When a workflow opens subagents, pair it with `templates/agent-handoff.md` and `templates/wave-plan.md` so the wave goal and close condition stay visible.

## Entry files

- `workflows/quick-design.md`
- `workflows/review-all-gdds.md`
- `workflows/propagate-design-change.md`
- `workflows/story-readiness.md`
- `workflows/story-done.md`
- `workflows/estimate.md`
- `workflows/prototype.md`
- `workflows/onboard.md`
- `workflows/localize.md`
- `workflows/skill-test.md`
- `workflows/skill-improve.md`
- `workflows/architecture-decision.md`
- `workflows/architecture-review.md`
- `workflows/create-control-manifest.md`
- `workflows/art-bible.md`
- `workflows/asset-audit.md`
- `workflows/asset-spec.md`
- `workflows/content-audit.md`
- `workflows/bug-report.md`
- `workflows/bug-triage.md`
- `workflows/consistency-check.md`
- `workflows/hotfix.md`
- `workflows/release-checklist.md`
- `workflows/regression-suite.md`
- `workflows/soak-test.md`
- `workflows/scope-check.md`
- `workflows/smoke-check.md`
- `workflows/test-evidence-review.md`
- `workflows/test-flakiness.md`
- `workflows/test-helpers.md`
- `workflows/test-setup.md`
- `workflows/team-live-ops.md`
- `workflows/playtest-report.md`
- `workflows/retrospective.md`
- `workflows/sprint-status.md`
- `workflows/tech-debt.md`
- `workflows/ux-design.md`
- `workflows/ux-review.md`
- `workflows/help.md`
- `workflows/setup-engine.md`
- `workflows/adopt.md`
- `workflows/brainstorm.md`
- `workflows/design-system.md`
- `workflows/design-systems.md`
- `workflows/create-architecture.md`
- `workflows/create-epics.md`
- `workflows/create-stories.md`
- `workflows/dev-story.md`
- `workflows/qa-plan.md`
- `workflows/start.md`
- `workflows/project-stage-detect.md`
- `workflows/map-systems.md`
- `workflows/gate-check.md`
- `workflows/team-ui.md`
- `workflows/team-qa.md`
- `workflows/team-release.md`
- `workflows/reverse-document.md`
- `workflows/design-review.md`
- `workflows/code-review.md`
- `workflows/balance-check.md`
- `workflows/perf-profile.md`
- `workflows/bug-intake.md`
- `workflows/sprint-plan.md`
- `workflows/milestone-review.md`
- `workflows/launch-checklist.md`
- `workflows/patch-notes.md`
- `workflows/changelog.md`
- `workflows/team-polish.md`
- `workflows/team-audio.md`
- `workflows/team-level.md`
- `workflows/team-combat.md`

## Discovery and routing

- `quick-design.md`: produce a fast design direction.
- `review-all-gdds.md`: review the full design document set.
- `propagate-design-change.md`: push a design change through affected areas.
- `story-readiness.md`: check whether a story is ready.
- `story-done.md`: confirm a story is done.
- `estimate.md`: estimate scope, effort, or complexity.
- `prototype.md`: build a lightweight prototype.
- `onboard.md`: bring a person, repo, or project into the flow.
- `localize.md`: prepare strings or content for localization.
- `skill-test.md`: test a skill or workflow contract.
- `skill-improve.md`: improve a skill after testing.
- `architecture-decision.md`: capture a technical decision with tradeoffs.
- `architecture-review.md`: review an architecture before implementation.
- `create-control-manifest.md`: formalize the control and routing manifest.
- `art-bible.md`: define the visual style targets and asset boundaries.
- `asset-audit.md`: audit the asset set for gaps or drift.
- `asset-spec.md`: define the assets, formats, and constraints.
- `ux-design.md`: design interaction and layout behavior.
- `ux-review.md`: review UI clarity and usability.
- `content-audit.md`: review content for gaps and contradictions.
- `bug-report.md`: normalize a bug report into a clean handoff.
- `bug-triage.md`: assign priority and ownership to a bug.
- `consistency-check.md`: find mismatches across related artifacts.
- `scope-check.md`: check whether a task boundary is safe.
- `help.md`: choose the right next entry point.
- `setup-engine.md`: establish the technical baseline.
- `adopt.md`: bring an existing project into the studio flow.
- `start.md`: route a vague request into a working mode.
- `project-stage-detect.md`: determine stage and missing artifacts.
- `map-systems.md`: decompose a concept into systems and dependencies.
- `gate-check.md`: decide whether a stage can advance.

## Design and planning

- `brainstorm.md`: generate candidate directions before committing.
- `design-system.md`: shape the game systems and boundaries.
- `design-systems.md`: alias command for the same systems-shaping workflow.
- `create-architecture.md`: produce an architecture plan.
- `create-epics.md`: turn a broad scope into epics.
- `create-stories.md`: convert epics into stories.
- `dev-story.md`: execute one story with a small patch.
- `qa-plan.md`: prepare the verification plan.

## Reviews

- `design-review.md`: review the design before implementation.
- `code-review.md`: review implementation for bugs and regressions.
- `balance-check.md`: review fairness, pacing, and feel.
- `perf-profile.md`: identify bottlenecks and expensive paths.
- `playtest-report.md`: summarize playtest observations and issues.
- `retrospective.md`: capture lessons learned and action items.
- `sprint-status.md`: report sprint progress, blockers, and next steps.
- `tech-debt.md`: track debt, impact, and cleanup direction.
- `reverse-document.md`: reconstruct missing docs from code.
- `smoke-check.md`: run a fast sanity pass.
- `regression-suite.md`: run a broader regression pass.
- `soak-test.md`: run a time-based stability test.
- `test-evidence-review.md`: assess evidence before a test verdict.
- `test-flakiness.md`: isolate and mitigate flaky tests.
- `test-helpers.md`: prepare helper scaffolding for tests.
- `test-setup.md`: prepare the test environment.

## Planning and delivery

- `bug-intake.md`: capture a reproducible bug report.
- `sprint-plan.md`: turn scope into a short plan.
- `milestone-review.md`: decide whether a milestone can ship.
- `release-checklist.md`: confirm release readiness with a focused checklist.
- `launch-checklist.md`: confirm launch readiness.
- `patch-notes.md`: summarize what changed in a release.
- `changelog.md`: maintain the release history.
- `hotfix.md`: patch a production issue with the smallest safe change.

## Team lanes

- `team-ui.md`: focus on layout, interaction, and responsiveness.
- `team-qa.md`: focus on regression-heavy verification.
- `team-release.md`: focus on release readiness and blockers.
- `team-polish.md`: focus on hardening and cleanup.
- `team-audio.md`: focus on sound design and feedback.
- `team-level.md`: focus on layout, pacing, and spatial flow.
- `team-combat.md`: focus on rules, feel, and combat tuning.
- `team-live-ops.md`: focus on live-ops updates and operational content.

## Workflow selection

- Use the shortest entry that can still answer the task.
- Use the team lanes when the work spans more than one file or discipline.
- Use the review and delivery flows when the main output is a decision, gate, or handoff rather than a code patch.
- After a lane reports back, close it before starting the next wave.
- After a lane reports back, close it before starting the next wave and write a short checkpoint.
