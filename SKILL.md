---
name: codex-game-studios
description: Use for Codex-first game project work that needs routing, parallel agents, QA, or release checks.
---

# Codex Game Studio

Use this skill for Codex-first game-dev work that needs routing, parallel agents, or explicit verification.

## Default path

README -> /start -> /project-stage-detect -> /onboard

## Install note

If this skill was installed from GitHub, start with `/start` after Codex reloads skills.
If the workspace already contains `AGENTS.md`, read it first and then follow the shortest safe entry.

## Rules

- Read `AGENTS.md` first when it exists.
- Read `references/codex-first.md` next when you need the shortest safe entry map.
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

## Refs

- `references/codex-first.md` for the shortest reading order.
- `references/multi-agent-sop.md` for the default wave model.
- `commands/` for the front door.
- `workflows/` for the steps.
- `references/command-registry.md` for the command source of truth.
- `templates/agent-handoff.md` and `templates/wave-plan.md` for wave targets and close conditions.
