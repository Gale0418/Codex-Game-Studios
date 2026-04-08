# Workflow Entry Contract

## Purpose

- Give every named workflow the same usable shape so it can be routed, executed, and verified without guesswork.

## Required shape

- `Purpose`: what this workflow is for.
- `Goal`: the target state the current wave is trying to reach.
- `Trigger`: when to choose it.
- `Primary lane`: who owns the first pass.
- `Inputs`: what files, state, or facts matter.
- `Steps`: the smallest safe execution path.
- `Outputs`: what the workflow should hand back.
- `Exit criteria`: what proves it is ready to close.
- `Template`: which report shell to use when writing the result.

## Writing rules

- Keep each entry concrete and short enough to scan quickly.
- State the goal before the steps when the workflow opens subagents.
- Name the lane owner before the helper lanes.
- Include verification when the workflow can change gameplay, AI, UI, persistence, release, or docs.
- If the workflow is broad, make the split point obvious before implementation starts.
- If the workflow is narrow, prefer one lane and one verification pass.

## Default handoff fields

- `findings`
- `risks`
- `files`
- `recommended_next_step`
