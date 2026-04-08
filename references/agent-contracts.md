# Agent Contracts

## Core roles

- `control-plane`: decide whether the request should stay light or move into the full studio flow.
- `workflow-catalog`: match the request to the correct named workflow and expected output shape.
- `intake-scan`: classify the task, identify scope, and list relevant files.
- `architecture`: compare approaches, data flow, and risk.
- `producer`: own scope, sequencing, cross-team coordination, and final handoff.
- `creative-director`: own vision, design direction, tone, and creative tradeoffs.
- `technical-director`: own architecture, technical risk, integration health, and feasibility calls.
- `art-director`: define visual style targets and asset boundaries.
- `technical-artist`: translate art direction into production constraints.
- `game-designer`: own player-facing design intent, goals, and acceptance criteria.
- `systems-designer`: own systems decomposition, progression loops, and economy structure.
- `economy-designer`: own currencies, sinks/sources, inflation risk, and reward pacing.
- `level-designer`: own spatial flow, pacing, encounter layout, and play routes.
- `game-rules`: isolate rules, win conditions, balance, and state transitions.
- `ai-behavior`: isolate move selection, heuristics, and worker behavior.
- `ui-ux`: isolate layout, interaction, responsiveness, and polish.
- `persistence`: isolate save data, undo, history, and restore behavior.
- `narrative-director`: own story direction, content consistency, and tone.
- `writer`: draft and revise content or narrative material.
- `prototyper`: build and validate small proof-of-concept slices.
- `live-ops-designer`: own live content cadence and operational changes.
- `sound-designer`: own SFX goals, moment-to-moment feedback, and mix intent.
- `audio-director`: own audio direction, style consistency, and audio risk for shipping.
- `community-manager`: own public-facing messaging, player comms cadence, and community risk.
- `analytics-engineer`: own event instrumentation, metrics definitions, and data quality checks.
- `localization-lead`: own language coverage and localization readiness.
- `implementation`: make the change in the smallest safe slice.
- `integration`: merge the lanes, resolve conflicts, and consolidate the final diff.
- `qa-regression`: verify behavior, reproduce bugs, and check for regressions.
- `qa-lead`: own the verification plan and gate decision.
- `qa-tester`: run manual checks, exploratory passes, and device/viewport coverage.
- `accessibility-specialist`: own accessibility checks and a11y risk assessment.
- `docs-release`: summarize the result and call out remaining risk.
- `release-manager`: own the shipping path and final release handoff.

## Engine-specific roles

Use these when the engine is known or when the lane is blocked on engine internals. Keep the discipline owner as primary, and treat the engine specialist as an additive constraint owner.

- `godot-specialist`: engine lead for Godot.
- `godot-gdscript-specialist`: GDScript implementation and runtime behavior.
- `godot-shader-specialist`: Godot shader/material pipeline guidance.
- `godot-gdextension-specialist`: native extension and binding guidance.
- `godot-engine-programmer`: engine-level Godot code and performance.
- `godot-tools-programmer`: editor tooling and pipelines in Godot context.
- `godot-ui-programmer`: UI implementation in Godot context.
- `godot-technical-artist`: art pipeline constraints in Godot context.
- `godot-build-release`: build, export, and release constraints for Godot.

- `unity-specialist`: engine lead for Unity.
- `unity-dots-specialist`: DOTS/ECS guidance and performance constraints.
- `unity-shader-specialist`: shader/material pipeline guidance in Unity.
- `unity-addressables-specialist`: addressables/content delivery constraints.
- `unity-ui-specialist`: Unity UI systems constraints and patterns.
- `unity-engine-programmer`: engine-level Unity code and performance.
- `unity-tools-programmer`: editor tooling and pipelines in Unity context.
- `unity-ui-programmer`: UI implementation in Unity context.
- `unity-technical-artist`: art pipeline constraints in Unity context.
- `unity-build-release`: build, packaging, and release constraints for Unity.

- `unreal-specialist`: engine lead for Unreal.
- `unreal-gas-specialist`: GAS integration and gameplay ability constraints.
- `unreal-blueprint-specialist`: Blueprint architecture and performance guidance.
- `unreal-replication-specialist`: networking/replication constraints and pitfalls.
- `unreal-umg-specialist`: UMG/UI constraints and patterns.
- `ue-gas-specialist`: alias for `unreal-gas-specialist`.
- `ue-blueprint-specialist`: alias for `unreal-blueprint-specialist`.
- `ue-replication-specialist`: alias for `unreal-replication-specialist`.
- `ue-umg-specialist`: alias for `unreal-umg-specialist`.
- `unreal-engine-programmer`: engine-level Unreal code and performance.
- `unreal-tools-programmer`: editor tooling and pipelines in Unreal context.
- `unreal-ui-programmer`: UI implementation in Unreal context.
- `unreal-technical-artist`: art pipeline constraints in Unreal context.
- `unreal-build-release`: build, packaging, and release constraints for Unreal.

## Dispatch rules

- Use `intake-scan` first for ambiguous or broad tasks.
- Use `architecture` whenever there is a tradeoff or more than one plausible implementation.
- Use `producer` when the task needs prioritization, scheduling, multi-team routing, or a single accountable plan.
- Use `creative-director` when the task changes tone, vision, or player-facing creative direction.
- Use `technical-director` when feasibility is unclear, risk is high, or integration/architecture coherence is at stake.
- Use `art-director` when the change affects visual direction or asset style.
- Use `technical-artist` when art constraints need to be translated into production-ready requirements.
- Use `art-director` and `technical-artist` for `architecture-review`, `asset-audit`, and `create-control-manifest` when the output needs production-ready shape.
- Use `game-designer` when the task changes player goals, rules intent, onboarding, UX intent, or acceptance criteria.
- Use `systems-designer` when the task touches progression loops, meta systems, or cross-system boundaries.
- Use `economy-designer` when the task touches currencies, rewards, rates, pricing, or inflation risk.
- Use `level-designer` when the task touches pacing, layout, encounter structure, or traversal flow.
- Use `game-rules` when the change can affect scoring, turns, legality, or win state.
- Use `ai-behavior` when the change affects any move decision or opponent response.
- Use `ui-ux` when the change affects player-facing layout or interaction.
- Use `persistence` when data survives reloads, undo, or session changes.
- Use `narrative-director` and `writer` when content, lore, or text consistency matters.
- Use `narrative-director` and `writer` for `team-narrative`, `playtest-report`, and content-heavy retrospective notes.
- Use `prototyper` when the task needs a small proof-of-concept or hypothesis check.
- Use `live-ops-designer` when the change affects live content cadence or operational events.
- Use `sound-designer` when the task touches feedback timing, SFX direction, or mix intent.
- Use `audio-director` when audio direction consistency matters or when release risk includes audio quality.
- Use `community-manager` when the output is player-facing messaging, patch comms, or incident comms.
- Use `analytics-engineer` when the change needs event instrumentation, metric definition, or data validation.
- Use `localization-lead` when the task affects multi-language readiness or string coverage.
- Use `qa-regression` and `qa-lead` for `bug-report`, `test-setup`, `test-evidence-review`, `soak-test`, and `playtest-report`.
- Use `qa-tester` when manual verification is required (viewport/device checks, exploratory passes, or human judgment).
- Use `accessibility-specialist` when the UI or interaction could affect accessibility, input modes, or readability.
- Use `producer` and `docs-release` for `sprint-status`, `retrospective`, and `create-control-manifest`.
- Use `integration` when multiple lanes produce overlapping files.
- Use `qa-regression` for any gameplay, AI, or persistence change.
- Use `qa-regression` for smoke checks and regression-suite passes too.
- Use `docs-release` for final handoff on large tasks.
- Use `release-manager` for release-checklist and hotfix decisions.

## Wave discipline

- When a task uses subagents, name the wave goal before opening slots.
- Keep one owner, one helper, and one integrator per lane unless the task is explicitly broader.
- Close finished agents immediately, write a short checkpoint, and reopen fresh agents only for the next wave.

## Engine routing rules

- If the engine is unknown, default to `engine-agnostic` assumptions and avoid engine-specific rewrites.
- If the engine is known:
- Route engine-specific constraints through the engine lead (`godot-specialist`, `unity-specialist`, `unreal-specialist`).
- Route subdomain questions through the matching sub-specialist (shaders, UI, replication, GAS, addressables, extensions).
- Prefer one engine specialist per wave; do not split multiple engine specialists into the same wave unless the lane is explicitly engine-internal.

## Handoff fields

Every role returns:

- `findings`
- `risks`
- `files`
- `recommended_next_step`

Role-specific additions:

- `intake-scan`: `scope`, `relevant_files`, `recommended_split`
- `architecture`: `options`, `tradeoffs`, `recommended_direction`
- `producer`: `scope_lock`, `priorities`, `owners`, `timeline`, `status_summary`
- `creative-director`: `vision_guardrails`, `tone_notes`, `acceptance_notes`, `risk_to_player_experience`
- `technical-director`: `risk_register`, `integration_risks`, `feasibility_notes`, `non_goals`
- `game-designer`: `design_intent`, `success_criteria`, `player_impact`, `edge_cases`
- `systems-designer`: `systems_map`, `dependencies`, `tuning_knobs`, `mvp_cutline`
- `economy-designer`: `economy_assumptions`, `sources_sinks`, `rate_table`, `inflation_risk`
- `level-designer`: `pacing_notes`, `layout_constraints`, `encounter_notes`, `playtest_questions`
- `implementation`: `patch_plan`, `changed_files`, `verification_status`
- `integration`: `merge_conflicts`, `consolidation_notes`, `final_diff_risk`
- `qa-regression`: `repro_steps`, `test_results`, `residual_failures`
- `qa-tester`: `manual_checks`, `device_matrix`, `exploratory_notes`, `screenshots_or_recordings`
- `accessibility-specialist`: `a11y_checks`, `input_modes`, `contrast_readability`, `a11y_risks`
- `sound-designer`: `audio_goals`, `assets_touched`, `mix_notes`, `verification_notes`
- `audio-director`: `direction_notes`, `quality_risk`, `ship_blockers`, `followups`
- `community-manager`: `player_message`, `release_comms`, `incident_comms`, `community_risks`
- `analytics-engineer`: `events`, `metrics`, `dashboards`, `data_quality_notes`
- `docs-release`: `user_facing_changes`, `ship_readiness`, `remaining_risk`
- `godot-specialist`: `engine_assumptions`, `engine_constraints`, `files`, `build_or_export_notes`
- `unity-specialist`: `engine_assumptions`, `engine_constraints`, `files`, `build_or_package_notes`
- `unreal-specialist`: `engine_assumptions`, `engine_constraints`, `files`, `build_or_package_notes`

## Engine specialist handoff additions

These fields apply to engine sub-specialists too:

- `engine_version` (if known)
- `performance_constraints`
- `tooling_constraints`
- `migration_risk`
