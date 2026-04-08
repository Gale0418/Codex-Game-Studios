# Command Registry

## Canonical source

- This file is the source of truth for command categories, aliases, and routing.
- Update this file first when adding, renaming, or re-routing a command.
- Derived views should reference this file instead of inventing their own taxonomy:
  - `commands/index.md`
  - `runtime/dispatch-manifest.md`
  - `workflows/help.md`

## Routing rules

- Use `Discovery` when the state is unclear or the user needs the right starting point.
- Use `Planning` when the task needs decomposition, sequencing, or setup decisions.
- Use `Design` when player-facing intent, content shape, or UX needs to be defined.
- Use `Build` when the work is implementation, review, or a small safe slice.
- Use `Verify` when the work needs checks, regressions, evidence, or gate decisions.
- Use `Ship` when release readiness, handoff, or post-cycle closure is the main concern.
- Aliases share the same routing intent and workflow contract.

## Discovery

| Command | Aliases | Workflow | Routing |
| --- | --- | --- | --- |
| `/start` | - | `workflows/start.md` | `intake-scan`, `control-plane`, `workflow-catalog`; use when the request is vague or the state is unknown |
| `/help` | - | `workflows/help.md` | `control-plane`, `workflow-catalog`, `intake-scan`; use when the user wants the right command |
| `/project-stage-detect` | - | `workflows/project-stage-detect.md` | `intake-scan`, `qa-regression`, `docs-release`; use when the project stage or readiness is unclear |
| `/onboard` | - | `workflows/onboard.md` | `intake-scan`, `control-plane`, `docs-release`; use when adopting a repo or starting fresh |
| `/adopt` | - | `workflows/adopt.md` | `intake-scan`, `control-plane`, `docs-release`; use when absorbing an existing workspace or codebase |

## Planning

| Command | Aliases | Workflow | Routing |
| --- | --- | --- | --- |
| `/brainstorm` | - | `workflows/brainstorm.md` | `game-designer`, `creative-director`, `systems-designer`; use when shaping ideas and candidate directions |
| `/estimate` | - | `workflows/estimate.md` | `producer`, `architecture`, `implementation`; use when estimating scope, effort, or risk |
| `/scope-check` | - | `workflows/scope-check.md` | `control-plane`, `architecture`, `producer`; use when deciding whether the scope is still healthy |
| `/sprint-plan` | - | `workflows/sprint-plan.md` | `producer`, `architecture`, `implementation`; use when turning goals into sequenced work |
| `/create-epics` | - | `workflows/create-epics.md` | `producer`, `architecture`, `game-designer`; use when breaking a plan into epics |
| `/create-stories` | - | `workflows/create-stories.md` | `producer`, `implementation`, `qa-regression`; use when turning epics into story-sized work |
| `/create-architecture` | - | `workflows/create-architecture.md` | `architecture`, `technical-director`, `integration`; use when the solution needs a technical shape |
| `/create-control-manifest` | - | `workflows/create-control-manifest.md` | `control-plane`, `workflow-catalog`, `technical-director`; use when routing rules need to be written down |
| `/map-systems` | - | `workflows/map-systems.md` | `architecture`, `game-rules`, `persistence`, `ui-ux`; use when a concept needs system decomposition |
| `/setup-engine` | - | `workflows/setup-engine.md` | `control-plane`, `architecture`, `docs-release`; use when the technical baseline or stack setup must be clarified |
| `/architecture-decision` | - | `workflows/architecture-decision.md` | `architecture`, `technical-director`, `docs-release`; use when one technical direction needs to be chosen |
| `/architecture-review` | - | `workflows/architecture-review.md` | `architecture`, `technical-director`, `qa-regression`; use when a plan needs a technical review before implementation |

## Design

| Command | Aliases | Workflow | Routing |
| --- | --- | --- | --- |
| `/quick-design` | - | `workflows/quick-design.md` | `creative-director`, `game-designer`, `ui-ux`; use when a fast design direction is needed |
| `/review-all-gdds` | - | `workflows/review-all-gdds.md` | `creative-director`, `game-designer`, `docs-release`; use when reviewing multiple GDDs or a wider design set |
| `/propagate-design-change` | - | `workflows/propagate-design-change.md` | `producer`, `architecture`, `game-designer`; use when a design change needs to fan out safely |
| `/art-bible` | - | `workflows/art-bible.md` | `art-director`, `technical-artist`, `ux-designer`; use when visual style targets need to be defined |
| `/asset-spec` | - | `workflows/asset-spec.md` | `art-director`, `technical-artist`, `production`; use when asset requirements need to be pinned down |
| `/asset-audit` | - | `workflows/asset-audit.md` | `art-director`, `technical-artist`, `docs-release`; use when existing assets need a gap check |
| `/ux-design` | - | `workflows/ux-design.md` | `ui-ux`, `creative-director`, `implementation`; use when UI or flow design is needed |
| `/ux-review` | - | `workflows/ux-review.md` | `ui-ux`, `qa-regression`, `docs-release`; use when reviewing the player-facing interface |
| `/design-system` | `/design-systems` | `workflows/design-system.md` | `architecture`, `game-rules`, `ui-ux`; use when the underlying systems and boundaries need shaping |
| `/content-audit` | - | `workflows/content-audit.md` | `narrative-director`, `writer`, `docs-release`; use when narrative or content consistency needs a pass |
| `/localize` | - | `workflows/localize.md` | `localization-lead`, `writer`, `ui-ux`; use when multi-language readiness matters |
| `/reverse-document` | - | `workflows/reverse-document.md` | `intake-scan`, `architecture`, `docs-release`; use when reconstructing docs from the current state |
| `/design-review` | - | `workflows/design-review.md` | `game-designer`, `systems-designer`, `creative-director`; use when a design needs a pre-implementation review |

## Build

| Command | Aliases | Workflow | Routing |
| --- | --- | --- | --- |
| `/dev-story` | - | `workflows/dev-story.md` | `implementation`, `integration`, `qa-regression`; use when turning a story into a safe patch plan |
| `/prototype` | - | `workflows/prototype.md` | `prototyper`, `game-designer`, `implementation`; use when a hypothesis needs a small proof of concept |
| `/code-review` | - | `workflows/code-review.md` | `qa-regression`, `architecture`, `docs-release`; use when implementation needs bug and regression review |
| `/bug-intake` | - | `workflows/bug-intake.md` | `qa-regression`, `integration`, `docs-release`; use when a bug needs initial capture and sorting |
| `/bug-report` | - | `workflows/bug-report.md` | `qa-regression`, `integration`, `docs-release`; use when a bug needs a reproducible report |
| `/bug-triage` | - | `workflows/bug-triage.md` | `qa-lead`, `producer`, `integration`; use when a bug needs prioritization and ownership |
| `/consistency-check` | - | `workflows/consistency-check.md` | `docs-release`, `integration`, `qa-regression`; use when the change set needs a consistency pass |
| `/tech-debt` | - | `workflows/tech-debt.md` | `architecture`, `producer`, `integration`; use when debt needs to be named and sequenced |
| `/team-ui` | - | `workflows/team-ui.md` | `ui-ux`, `implementation`, `qa-regression`; use when a UI-heavy slice needs a dedicated lane |
| `/team-polish` | - | `workflows/team-polish.md` | `ui-ux`, `implementation`, `qa-regression`; use when the work is polish-first |
| `/team-audio` | - | `workflows/team-audio.md` | `sound-designer`, `audio-director`, `implementation`; use when audio needs a dedicated lane |
| `/team-level` | - | `workflows/team-level.md` | `level-designer`, `game-designer`, `implementation`; use when a level slice needs dedicated handling |
| `/team-combat` | - | `workflows/team-combat.md` | `game-rules`, `ai-behavior`, `implementation`; use when combat or rules tuning needs a focused lane |
| `/team-narrative` | - | `workflows/team-narrative.md` | `narrative-director`, `writer`, `docs-release`; use when narrative content needs a dedicated lane |
| `/team-live-ops` | - | `workflows/team-live-ops.md` | `live-ops-designer`, `producer`, `qa-regression`; use when live content or ops cadence changes |

## Verify

| Command | Aliases | Workflow | Routing |
| --- | --- | --- | --- |
| `/qa-plan` | - | `workflows/qa-plan.md` | `qa-lead`, `qa-regression`, `docs-release`; use when the test matrix or gate needs planning |
| `/smoke-check` | - | `workflows/smoke-check.md` | `qa-regression`, `integration`, `docs-release`; use for a quick sanity check |
| `/regression-suite` | - | `workflows/regression-suite.md` | `qa-lead`, `qa-regression`, `integration`; use for a deeper regression pass |
| `/soak-test` | - | `workflows/soak-test.md` | `qa-regression`, `qa-lead`, `integration`; use when time-based stability matters |
| `/test-setup` | - | `workflows/test-setup.md` | `qa-regression`, `integration`, `docs-release`; use when test infrastructure or fixtures need setup |
| `/test-helpers` | - | `workflows/test-helpers.md` | `qa-regression`, `integration`, `docs-release`; use when shared test helpers need to be built or fixed |
| `/test-flakiness` | - | `workflows/test-flakiness.md` | `qa-regression`, `integration`, `docs-release`; use when flaky tests need diagnosis or mitigation |
| `/test-evidence-review` | - | `workflows/test-evidence-review.md` | `qa-lead`, `qa-regression`, `docs-release`; use when evidence needs a final review |
| `/playtest-report` | - | `workflows/playtest-report.md` | `qa-regression`, `game-designer`, `docs-release`; use when playtest observations need consolidation |
| `/balance-check` | - | `workflows/balance-check.md` | `game-designer`, `qa-regression`, `docs-release`; use when tuning balance or difficulty |
| `/perf-profile` | - | `workflows/perf-profile.md` | `qa-regression`, `architecture`, `docs-release`; use when performance needs profiling |
| `/story-readiness` | - | `workflows/story-readiness.md` | `producer`, `qa-regression`, `implementation`; use when deciding if a story is ready to start |
| `/story-done` | - | `workflows/story-done.md` | `qa-regression`, `integration`, `docs-release`; use when deciding if a story is finished |
| `/gate-check` | - | `workflows/gate-check.md` | `qa-regression`, `architecture`, `docs-release`; use when a pass/fail gate decision is needed |
| `/team-qa` | - | `workflows/team-qa.md` | `qa-regression`, `integration`, `docs-release`; use when the task needs a regression-heavy verification lane |

## Ship

| Command | Aliases | Workflow | Routing |
| --- | --- | --- | --- |
| `/release-checklist` | - | `workflows/release-checklist.md` | `release-manager`, `qa-lead`, `producer`; use when readiness needs to be checked before shipping |
| `/launch-checklist` | - | `workflows/launch-checklist.md` | `release-manager`, `qa-lead`, `producer`; use when launch prep needs a final pass |
| `/patch-notes` | - | `workflows/patch-notes.md` | `community-manager`, `docs-release`, `producer`; use when a release note needs drafting |
| `/changelog` | - | `workflows/changelog.md` | `docs-release`, `producer`, `integration`; use when the change log needs to be updated |
| `/milestone-review` | - | `workflows/milestone-review.md` | `producer`, `qa-lead`, `technical-director`; use when a milestone needs a ship or cut decision |
| `/sprint-status` | - | `workflows/sprint-status.md` | `producer`, `architecture`, `implementation`; use when the sprint needs a status update |
| `/hotfix` | - | `workflows/hotfix.md` | `release-manager`, `qa-regression`, `integration`; use when an urgent fix must ship safely |
| `/skill-test` | - | `workflows/skill-test.md` | `qa-regression`, `docs-release`, `integration`; use when a skill or workflow contract needs validation |
| `/skill-improve` | - | `workflows/skill-improve.md` | `docs-release`, `integration`, `qa-regression`; use when a skill or workflow needs refinement |
| `/team-release` | - | `workflows/team-release.md` | `release-manager`, `qa-lead`, `devops-engineer`, `producer`; use when release readiness is the main concern |
| `/retrospective` | - | `workflows/retrospective.md` | `producer`, `qa-lead`, `docs-release`; use when capturing lessons after a sprint or release |
