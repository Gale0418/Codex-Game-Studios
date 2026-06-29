# Dispatch Manifest

## Canonical source

- `references/command-registry.md` is the source of truth.
- This file is a derived routing summary generated from the registry.

## Fast Entry

- Read the target workspace `AGENTS.md` only when that workspace provides one.
- Then read `SKILL.md` and `references/codex-first.md`.
- Pick exactly one command lane and open the matching workflow before expanding into broader runtime docs.

## Full Studio Audit

- Use this heavier path for broad, risky, release, migration, or refactor work.
- Add `references/command-registry.md`, `runtime/execution-policy.md`, `runtime/session-lifecycle.md`, `runtime/hook-map.md`, `production/stage.txt`, and `production/active.md`.

## Routing map

### Discovery

- Commands: `/start`, `/help`, `/project-stage-detect`, `/onboard`, `/adopt`
- Workflows: `workflows/start.md`, `workflows/help.md`, `workflows/project-stage-detect.md`, `workflows/onboard.md`, `workflows/adopt.md`
- `/start` routes through `workflows/start.md`; `intake-scan`, `control-plane`, `workflow-catalog`; use when the request is vague or the state is unknown
- `/help` routes through `workflows/help.md`; `control-plane`, `workflow-catalog`, `intake-scan`; use when the user wants the right command
- `/project-stage-detect` routes through `workflows/project-stage-detect.md`; `intake-scan`, `qa-regression`, `docs-release`; use when the project stage or readiness is unclear
- `/onboard` routes through `workflows/onboard.md`; `intake-scan`, `control-plane`, `docs-release`; use when adopting a repo or starting fresh
- `/adopt` routes through `workflows/adopt.md`; `intake-scan`, `control-plane`, `docs-release`; use when absorbing an existing workspace or codebase

### Planning

- Commands: `/brainstorm`, `/estimate`, `/scope-check`, `/sprint-plan`, `/create-epics`, `/create-stories`, `/create-architecture`, `/create-control-manifest`, `/map-systems`, `/setup-engine`, `/architecture-decision`, `/architecture-review`
- Workflows: `workflows/brainstorm.md`, `workflows/estimate.md`, `workflows/scope-check.md`, `workflows/sprint-plan.md`, `workflows/create-epics.md`, `workflows/create-stories.md`, `workflows/create-architecture.md`, `workflows/create-control-manifest.md`, `workflows/map-systems.md`, `workflows/setup-engine.md`, `workflows/architecture-decision.md`, `workflows/architecture-review.md`
- `/brainstorm` routes through `workflows/brainstorm.md`; `game-designer`, `creative-director`, `systems-designer`; use when shaping ideas and candidate directions
- `/estimate` routes through `workflows/estimate.md`; `producer`, `architecture`, `implementation`; use when estimating scope, effort, or risk
- `/scope-check` routes through `workflows/scope-check.md`; `control-plane`, `architecture`, `producer`; use when deciding whether the scope is still healthy
- `/sprint-plan` routes through `workflows/sprint-plan.md`; `producer`, `architecture`, `implementation`; use when turning goals into sequenced work
- `/create-epics` routes through `workflows/create-epics.md`; `producer`, `architecture`, `game-designer`; use when breaking a plan into epics
- `/create-stories` routes through `workflows/create-stories.md`; `producer`, `implementation`, `qa-regression`; use when turning epics into story-sized work
- `/create-architecture` routes through `workflows/create-architecture.md`; `architecture`, `technical-director`, `integration`; use when the solution needs a technical shape
- `/create-control-manifest` routes through `workflows/create-control-manifest.md`; `control-plane`, `workflow-catalog`, `technical-director`; use when routing rules need to be written down
- `/map-systems` routes through `workflows/map-systems.md`; `architecture`, `game-rules`, `persistence`, `ui-ux`; use when a concept needs system decomposition
- `/setup-engine` routes through `workflows/setup-engine.md`; `control-plane`, `architecture`, `docs-release`; use when the technical baseline or stack setup must be clarified
- `/architecture-decision` routes through `workflows/architecture-decision.md`; `architecture`, `technical-director`, `docs-release`; use when one technical direction needs to be chosen
- `/architecture-review` routes through `workflows/architecture-review.md`; `architecture`, `technical-director`, `qa-regression`; use when a plan needs a technical review before implementation

### Design

- Commands: `/quick-design`, `/review-all-gdds`, `/propagate-design-change`, `/art-bible`, `/asset-spec`, `/asset-audit`, `/ux-design`, `/ux-review`, `/design-system`, `/content-audit`, `/localize`, `/reverse-document`, `/design-review`
- Workflows: `workflows/quick-design.md`, `workflows/review-all-gdds.md`, `workflows/propagate-design-change.md`, `workflows/art-bible.md`, `workflows/asset-spec.md`, `workflows/asset-audit.md`, `workflows/ux-design.md`, `workflows/ux-review.md`, `workflows/design-system.md`, `workflows/content-audit.md`, `workflows/localize.md`, `workflows/reverse-document.md`, `workflows/design-review.md`
- `/quick-design` routes through `workflows/quick-design.md`; `creative-director`, `game-designer`, `ui-ux`; use when a fast design direction is needed
- `/review-all-gdds` routes through `workflows/review-all-gdds.md`; `creative-director`, `game-designer`, `docs-release`; use when reviewing multiple GDDs or a wider design set
- `/propagate-design-change` routes through `workflows/propagate-design-change.md`; `producer`, `architecture`, `game-designer`; use when a design change needs to fan out safely
- `/art-bible` routes through `workflows/art-bible.md`; `art-director`, `technical-artist`, `ux-designer`; use when visual style targets need to be defined
- `/asset-spec` routes through `workflows/asset-spec.md`; `art-director`, `technical-artist`, `production`; use when asset requirements need to be pinned down
- `/asset-audit` routes through `workflows/asset-audit.md`; `art-director`, `technical-artist`, `docs-release`; use when existing assets need a gap check
- `/ux-design` routes through `workflows/ux-design.md`; `ui-ux`, `creative-director`, `implementation`; use when UI or flow design is needed
- `/ux-review` routes through `workflows/ux-review.md`; `ui-ux`, `qa-regression`, `docs-release`; use when reviewing the player-facing interface
- `/design-system` routes through `workflows/design-system.md`; aliases: /design-systems; `architecture`, `game-rules`, `ui-ux`; use when the underlying systems and boundaries need shaping
- `/content-audit` routes through `workflows/content-audit.md`; `narrative-director`, `writer`, `docs-release`; use when narrative or content consistency needs a pass
- `/localize` routes through `workflows/localize.md`; `localization-lead`, `writer`, `ui-ux`; use when multi-language readiness matters
- `/reverse-document` routes through `workflows/reverse-document.md`; `intake-scan`, `architecture`, `docs-release`; use when reconstructing docs from the current state
- `/design-review` routes through `workflows/design-review.md`; `game-designer`, `systems-designer`, `creative-director`; use when a design needs a pre-implementation review

### Build

- Commands: `/dev-story`, `/prototype`, `/code-review`, `/bug-intake`, `/bug-report`, `/bug-triage`, `/consistency-check`, `/tech-debt`, `/team-ui`, `/team-polish`, `/team-audio`, `/team-level`, `/team-combat`, `/team-narrative`, `/team-live-ops`
- Workflows: `workflows/dev-story.md`, `workflows/prototype.md`, `workflows/code-review.md`, `workflows/bug-intake.md`, `workflows/bug-report.md`, `workflows/bug-triage.md`, `workflows/consistency-check.md`, `workflows/tech-debt.md`, `workflows/team-ui.md`, `workflows/team-polish.md`, `workflows/team-audio.md`, `workflows/team-level.md`, `workflows/team-combat.md`, `workflows/team-narrative.md`, `workflows/team-live-ops.md`
- `/dev-story` routes through `workflows/dev-story.md`; `implementation`, `integration`, `qa-regression`; use when turning a story into a safe patch plan
- `/prototype` routes through `workflows/prototype.md`; `prototyper`, `game-designer`, `implementation`; use when a hypothesis needs a small proof of concept
- `/code-review` routes through `workflows/code-review.md`; `qa-regression`, `architecture`, `docs-release`; use when implementation needs bug and regression review
- `/bug-intake` routes through `workflows/bug-intake.md`; `qa-regression`, `integration`, `docs-release`; use when a bug needs initial capture and sorting
- `/bug-report` routes through `workflows/bug-report.md`; `qa-regression`, `integration`, `docs-release`; use when a bug needs a reproducible report
- `/bug-triage` routes through `workflows/bug-triage.md`; `qa-lead`, `producer`, `integration`; use when a bug needs prioritization and ownership
- `/consistency-check` routes through `workflows/consistency-check.md`; `docs-release`, `integration`, `qa-regression`; use when the change set needs a consistency pass
- `/tech-debt` routes through `workflows/tech-debt.md`; `architecture`, `producer`, `integration`; use when debt needs to be named and sequenced
- `/team-ui` routes through `workflows/team-ui.md`; `ui-ux`, `implementation`, `qa-regression`; use when a UI-heavy slice needs a dedicated lane
- `/team-polish` routes through `workflows/team-polish.md`; `ui-ux`, `implementation`, `qa-regression`; use when the work is polish-first
- `/team-audio` routes through `workflows/team-audio.md`; `sound-designer`, `audio-director`, `implementation`; use when audio needs a dedicated lane
- `/team-level` routes through `workflows/team-level.md`; `level-designer`, `game-designer`, `implementation`; use when a level slice needs dedicated handling
- `/team-combat` routes through `workflows/team-combat.md`; `game-rules`, `ai-behavior`, `implementation`; use when combat or rules tuning needs a focused lane
- `/team-narrative` routes through `workflows/team-narrative.md`; `narrative-director`, `writer`, `docs-release`; use when narrative content needs a dedicated lane
- `/team-live-ops` routes through `workflows/team-live-ops.md`; `live-ops-designer`, `producer`, `qa-regression`; use when live content or ops cadence changes

### Verify

- Commands: `/qa-plan`, `/smoke-check`, `/regression-suite`, `/soak-test`, `/test-setup`, `/test-helpers`, `/test-flakiness`, `/test-evidence-review`, `/playtest-report`, `/balance-check`, `/perf-profile`, `/story-readiness`, `/story-done`, `/gate-check`, `/team-qa`
- Workflows: `workflows/qa-plan.md`, `workflows/smoke-check.md`, `workflows/regression-suite.md`, `workflows/soak-test.md`, `workflows/test-setup.md`, `workflows/test-helpers.md`, `workflows/test-flakiness.md`, `workflows/test-evidence-review.md`, `workflows/playtest-report.md`, `workflows/balance-check.md`, `workflows/perf-profile.md`, `workflows/story-readiness.md`, `workflows/story-done.md`, `workflows/gate-check.md`, `workflows/team-qa.md`
- `/qa-plan` routes through `workflows/qa-plan.md`; `qa-lead`, `qa-regression`, `docs-release`; use when the test matrix or gate needs planning
- `/smoke-check` routes through `workflows/smoke-check.md`; `qa-regression`, `integration`, `docs-release`; use for a quick sanity check
- `/regression-suite` routes through `workflows/regression-suite.md`; `qa-lead`, `qa-regression`, `integration`; use for a deeper regression pass
- `/soak-test` routes through `workflows/soak-test.md`; `qa-regression`, `qa-lead`, `integration`; use when time-based stability matters
- `/test-setup` routes through `workflows/test-setup.md`; `qa-regression`, `integration`, `docs-release`; use when test infrastructure or fixtures need setup
- `/test-helpers` routes through `workflows/test-helpers.md`; `qa-regression`, `integration`, `docs-release`; use when shared test helpers need to be built or fixed
- `/test-flakiness` routes through `workflows/test-flakiness.md`; `qa-regression`, `integration`, `docs-release`; use when flaky tests need diagnosis or mitigation
- `/test-evidence-review` routes through `workflows/test-evidence-review.md`; `qa-lead`, `qa-regression`, `docs-release`; use when evidence needs a final review
- `/playtest-report` routes through `workflows/playtest-report.md`; `qa-regression`, `game-designer`, `docs-release`; use when playtest observations need consolidation
- `/balance-check` routes through `workflows/balance-check.md`; `game-designer`, `qa-regression`, `docs-release`; use when tuning balance or difficulty
- `/perf-profile` routes through `workflows/perf-profile.md`; `qa-regression`, `architecture`, `docs-release`; use when performance needs profiling
- `/story-readiness` routes through `workflows/story-readiness.md`; `producer`, `qa-regression`, `implementation`; use when deciding if a story is ready to start
- `/story-done` routes through `workflows/story-done.md`; `qa-regression`, `integration`, `docs-release`; use when deciding if a story is finished
- `/gate-check` routes through `workflows/gate-check.md`; `qa-regression`, `architecture`, `docs-release`; use when a pass/fail gate decision is needed
- `/team-qa` routes through `workflows/team-qa.md`; `qa-regression`, `integration`, `docs-release`; use when the task needs a regression-heavy verification lane

### Ship

- Commands: `/release-checklist`, `/launch-checklist`, `/patch-notes`, `/changelog`, `/milestone-review`, `/sprint-status`, `/hotfix`, `/skill-test`, `/skill-improve`, `/team-release`, `/retrospective`
- Workflows: `workflows/release-checklist.md`, `workflows/launch-checklist.md`, `workflows/patch-notes.md`, `workflows/changelog.md`, `workflows/milestone-review.md`, `workflows/sprint-status.md`, `workflows/hotfix.md`, `workflows/skill-test.md`, `workflows/skill-improve.md`, `workflows/team-release.md`, `workflows/retrospective.md`
- `/release-checklist` routes through `workflows/release-checklist.md`; `release-manager`, `qa-lead`, `producer`; use when readiness needs to be checked before shipping
- `/launch-checklist` routes through `workflows/launch-checklist.md`; `release-manager`, `qa-lead`, `producer`; use when launch prep needs a final pass
- `/patch-notes` routes through `workflows/patch-notes.md`; `community-manager`, `docs-release`, `producer`; use when a release note needs drafting
- `/changelog` routes through `workflows/changelog.md`; `docs-release`, `producer`, `integration`; use when the change log needs to be updated
- `/milestone-review` routes through `workflows/milestone-review.md`; `producer`, `qa-lead`, `technical-director`; use when a milestone needs a ship or cut decision
- `/sprint-status` routes through `workflows/sprint-status.md`; `producer`, `architecture`, `implementation`; use when the sprint needs a status update
- `/hotfix` routes through `workflows/hotfix.md`; `release-manager`, `qa-regression`, `integration`; use when an urgent fix must ship safely
- `/skill-test` routes through `workflows/skill-test.md`; `qa-regression`, `docs-release`, `integration`; use when a skill or workflow contract needs validation
- `/skill-improve` routes through `workflows/skill-improve.md`; `docs-release`, `integration`, `qa-regression`; use when a skill or workflow needs refinement
- `/team-release` routes through `workflows/team-release.md`; `release-manager`, `qa-lead`, `devops-engineer`, `producer`; use when release readiness is the main concern
- `/retrospective` routes through `workflows/retrospective.md`; `producer`, `qa-lead`, `docs-release`; use when capturing lessons after a sprint or release

## Handoff

- Every lane returns `findings`, `risks`, `files`, and `recommended_next_step`.
- The command file chooses the route.
- The workflow file explains the steps.
