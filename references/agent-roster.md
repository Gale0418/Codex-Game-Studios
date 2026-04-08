# Agent Roster

## Engine tags

- `engine-agnostic` (default)
- `godot`
- `unity`
- `unreal`

Use an engine tag to scope decisions, file patterns, and tooling assumptions. Engine tags do not replace discipline roles below; they refine them.

## Default studio stack

- `control-plane` for the first route choice.
- `producer` for scope, schedule, and handoff.
- `creative-director` for vision and creative tradeoffs.
- `technical-director` for architecture and technical risk.
- `qa-lead` for verification and release gates.
- `release-manager` for shipping readiness.
- `engine-generalist` for the first implementation pass when the engine is not yet known.

Use this stack as the default answer when a task is broad but the project is still being adopted.
Use `references/codex-first.md` when a new session needs the shortest safe entry path.

## Role selection principle

- Pick one clear owner first.
- Add at most one helper for the same lane.
- Assign one integrator for the changeset.
- Add an engine-specific role only when the engine is known or the task genuinely depends on engine APIs, tooling, or asset pipeline behavior.
- When a lane opens subagents, name the wave goal, close finished agents immediately, and write a short checkpoint before the next wave.

If the task is still vague, start with `control-plane`, then route to one discipline owner, one helper, and one integrator.

## Control roles

- `control-plane`
- `workflow-catalog`
- `producer`
- `creative-director`
- `technical-director`
- `lead-programmer`
- `qa-lead`
- `release-manager`
- `localization-lead`

## Design roles

- `game-designer`
- `systems-designer`
- `level-designer`
- `economy-designer`
- `narrative-director`
- `writer`
- `world-builder`
- `ux-designer`

## Technical roles

- `gameplay-programmer`
- `engine-programmer`
- `ai-programmer`
- `network-programmer`
- `tools-programmer`
- `ui-programmer`
- `devops-engineer`
- `performance-analyst`
- `security-engineer`

## Engine leads

- `godot-specialist`
- `unity-specialist`
- `unreal-specialist`

## Engine sub-specialists

- `godot-gdscript-specialist`
- `godot-shader-specialist`
- `godot-gdextension-specialist`
- `unity-dots-specialist`
- `unity-shader-specialist`
- `unity-addressables-specialist`
- `unity-ui-specialist`
- `unreal-gas-specialist`
- `unreal-blueprint-specialist`
- `unreal-replication-specialist`
- `unreal-umg-specialist`

## Content roles

- `art-director`
- `technical-artist`
- `sound-designer`
- `audio-director`
- `community-manager`
- `analytics-engineer`
- `live-ops-designer`
- `prototyper`

## QA roles

- `qa-regression`
- `qa-tester`
- `accessibility-specialist`

## Release roles

- `docs-release`

## Default lane rule

- Prefer one discipline owner, one helper, and one integrator per lane.
- Keep specialist roles as helpers, not as the primary owner, unless the task is explicitly narrow.
- Add engine-specific roles only when the engine is known or the task needs engine-specific knowledge.
- If the engine is known, the engine-specific role should usually be the helper, not the owner, unless the work is engine-first by nature.

## Quick role selection cheat sheet

- Broad game feature: `producer` or `creative-director` or `technical-director` + `engine-generalist` + one integrator
- Engine-known feature: discipline owner + one engine lead + one integrator
- UI or UX pass: `ux-designer` or `ui-programmer` + `unity-ui-specialist` or `unreal-umg-specialist` as helper + integrator
- Systems or architecture pass: `technical-director` or `engine-programmer` + `godot-specialist` or `unity-specialist` or `unreal-specialist` as helper + integrator
- Content or narrative pass: `narrative-director` or `writer` + `world-builder` or `game-designer` as helper + integrator
- QA or release pass: `qa-lead` or `qa-regression` + one verification helper + `release-manager`

## Engine-specific roles (additive)

These roles are used when the project engine is known. Prefer one engine-specific lead per lane, and keep the discipline role as the primary ownership signal.

### Engine-agnostic core (recommended default)

- `engine-generalist`
- `build-release-engineer`

### Godot branch

- `godot-specialist`
- `godot-engine-programmer`
- `godot-tools-programmer`
- `godot-ui-programmer`
- `godot-technical-artist`
- `godot-build-release`

### Unity branch

- `unity-specialist`
- `unity-engine-programmer`
- `unity-tools-programmer`
- `unity-ui-programmer`
- `unity-technical-artist`
- `unity-build-release`

### Unreal branch

- `unreal-specialist`
- `unreal-engine-programmer`
- `unreal-tools-programmer`
- `unreal-ui-programmer`
- `unreal-technical-artist`
- `unreal-build-release`
- `ue-gas-specialist`
- `ue-blueprint-specialist`
- `ue-replication-specialist`
- `ue-umg-specialist`
