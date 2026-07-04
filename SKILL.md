---
name: codex-game-studios
description: Use for Codex-first game project work that needs routing, parallel agents, QA, or release checks.
---

# Codex Game Studio

Use this skill for Codex-first game-dev work that needs routing, parallel agents, or explicit verification.

## Fast Entry

`AGENTS.md` (if the target workspace provides it) -> `SKILL.md` -> `references/codex-first.md` -> one routed workflow

## Full Studio Audit

Use the heavier runtime, registry, and production docs only for broad, risky, release, migration, or refactor work.

## Install note

If this skill was installed from GitHub, start with `/start` after Codex reloads skills.
If the target workspace already contains `AGENTS.md`, read that workspace file first and then follow the shortest safe entry.

## Invocation

If the user asks how to use the skill, explain that they can either:
- give a task directly and let Codex infer the next safe workflow, or
- explicitly say `use codex-game-studios skill` to bias the session toward this studio flow.

## Rules

- Read the target workspace `AGENTS.md` first when it exists.
- Start with the Fast Entry path, then read `references/codex-first.md` to route into one workflow.
- Escalate to Full Studio Audit only when the task is broad, risky, release-focused, migration-heavy, or refactor-heavy.
- If the user does not know the right command, infer the next safe workflow and continue.
- Start with the smallest file set that answers the task.
- Classify the task as `intake`, `architecture`, `implementation`, `QA`, `docs`, or `release`.
- Ask before splitting broad or risky work.
- Use parallel agents only after the control plane is clear.
- Keep one owner per lane and one integrator per change.
- Rotate one monitor per wave so the studio can check its own handoff quality.
- Work in waves: spawn only the agents you need for the current lane, close finished agents immediately, and reopen new ones only when the next wave starts.
- Reclaim completed parallel agents before opening new ones if the slot limit is tight.
- Save a short checkpoint after each wave so the next wave can restart cleanly.
- Prefer narrow diffs over broad refactors.
- Validate with tests or `scripts/validate_studio.sh` / `scripts/validate_studio.cmd`.

## Language & Communication Protocol

When the user communicates in Traditional Chinese (zh-TW), Codex MUST maintain this language context across all studio workflows:

1. Generate all game design documents (GDD), dev notes, task plans, and comments in **Traditional Chinese (zh-TW)**.
2. Preserve standard Taiwanese game development terminology (e.g. `場景`, `著色器`, `Sprite Sheet 貼圖`, `影格`, `碰撞區`).

## Game Engine & Asset Workflows

When working with Godot 4.x or Unity game projects:

1. **Godot 4.x (GDScript)**: Check `scenes/*.tscn` and `scripts/*.gd`. Use headless tests (`godot --headless --quit-after 5`) for Verification.
2. **Sprite Sheet Asset Workflow**: For transparent sprite sheets or video keying, check `Background_remover` integration (`frames[].frameRect`, `extrude`, `padding`) before manual slice adjustments.

## Refs

- `references/codex-first.md` for the shortest reading order.
- `references/godot-node-architecture.md` for parsing and editing text-based Godot `.tscn` scene tree files.
- `references/ai-asset-pipeline.md` for ComfyUI / Sprite Sheet background removal and audio pipelines.
- `references/multi-agent-sop.md` for the default wave model.
- `commands/` for the front door.
- `workflows/` for the steps.
- `references/command-registry.md` for the command source of truth.
- `templates/agent-handoff.md` and `templates/wave-plan.md` for wave targets and close conditions.
