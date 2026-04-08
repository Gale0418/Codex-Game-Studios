# Example Workflows

## Feature flow

1. `intake-scan` classifies the request and lists the files involved.
2. `architecture` compares options and picks one direction.
3. `implementation` changes the smallest safe slice.
4. `qa-regression` checks the new behavior and nearby regressions.
5. `docs-release` summarizes the final change.

## Planning flow

1. `help` or `start` chooses the right entry point.
2. `brainstorm` or `design-system` shapes the solution space.
3. `create-architecture` and `create-epics` split the work.
4. `create-stories` and `dev-story` carry the change into execution.
5. `qa-plan` names the verification path.

## Art and release flow

1. `art-bible` and `asset-spec` define production boundaries.
2. `ux-design` and `ux-review` settle the interface.
3. `smoke-check` and `regression-suite` verify the risky paths.
4. `release-checklist` or `hotfix` handles shipping pressure.

## Skill flow

1. `skill-test` checks the contract shape.
2. `skill-improve` applies the smallest useful refinement.
3. `onboard` or `prototype` closes the loop when context or validation is needed.

## Bug flow

1. `intake-scan` narrows the reproduction path.
2. `qa-regression` reproduces the bug and confirms the source.
3. `implementation` patches the bug with a narrow diff.
4. `integration` resolves any overlap if multiple files changed.
5. `qa-regression` reruns the repro and confirms the fix.

## AI or balance flow

1. `intake-scan` finds the rule source and the AI entry points.
2. `game-rules` checks legality, turn order, and scoring.
3. `ai-behavior` checks heuristics, move choice, and fallback behavior.
4. `qa-regression` runs targeted play checks.

## UI flow

1. `intake-scan` identifies the affected views and breakpoints.
2. `ui-ux` checks layout, spacing, and interaction risk.
3. `implementation` makes the targeted change.
4. `qa-regression` checks desktop and narrow viewport behavior.

## Release flow

1. `intake-scan` collects the final diff, blockers, and residual risk.
2. `release-manager` checks ship readiness and release notes.
3. `qa-lead` confirms the gate evidence.
4. `docs-release` writes the handoff summary and final notes.

## Control manifest flow

1. `control-plane` and `intake-scan` define the routing problem and active lanes.
2. `architecture` and `docs-release` shape the manifest and the handoff text.
3. `integration` consolidates the manifest updates across files.
4. `qa-regression` checks that the route and the contract still agree.

## QA evidence flow

1. `intake-scan` normalizes the bug or test request.
2. `qa-regression` reproduces or interprets the evidence.
3. `integration` or `release-manager` resolves any overlap in the fix path.
4. `docs-release` summarizes the final result.

## Reporting flow

1. `producer` captures sprint state, retrospectives, or status updates.
2. `architecture` or `qa-lead` checks blockers and follow-up actions.
3. `docs-release` turns the notes into a short, scannable report.
4. `integration` updates any shared artifacts if the report changes policy.

## Narrative flow

1. `narrative-director` and `writer` inspect tone, continuity, and content structure.
2. `intake-scan` lists the affected files or content areas.
3. `docs-release` returns the narrative notes and remaining risks.
