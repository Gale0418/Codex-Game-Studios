# Governance Map

## Control plane

- `Question -> Options -> Decision -> Draft -> Approval`
- `control-plane` owns scope, risk framing, and the first route choice.
- `workflow-catalog` maps the task to the correct command and workflow.

## Default first response

- Use `/start` when the request is vague.
- Use `/project-stage-detect` when the repo state matters more than the command choice.
- Use `/help` only when the task is already understood but the best command is unclear.
- Stop at the control plane before splitting broad or risky work.

## Vertical delegation

- `producer` owns scope, schedule, and final handoff.
- `creative-director` owns vision, content direction, and creative tradeoffs.
- `technical-director` owns architecture, technical risk, and integration health.
- `department-leads` arbitrate their domain.
- `specialists` execute inside one lane and escalate conflicts upward.

## Horizontal consultation

- Design changes notify implementation, QA, docs, and release.
- Architecture changes notify implementers, QA, and release planning.
- UI or accessibility changes notify UI, implementation, and QA.
- Persistence or save-format changes notify implementation, QA, and release.

## Escalation paths

- Specialist conflict -> department lead
- Cross-domain conflict -> producer + relevant directors
- Technical feasibility conflict -> technical-director
- Design direction conflict -> creative-director
- Ship / milestone decision -> producer + gate owner

## Engine matrix

- `engine-agnostic` is the default path.
- `godot` routes through Godot specialists and sub-specialists.
- `unity` routes through Unity specialists and sub-specialists.
- `unreal` routes through Unreal specialists and sub-specialists, including `ue-*` aliases.

## Runtime governance

- `SessionStart`, `PreToolUse`, `PostToolUse`, `PreCompact`, `Stop`, and `SubagentStart` are the expected lifecycle checkpoints.
- `runtime/execution-policy.md` owns allow / deny and audit expectations.
- `production/` owns active stage state, handoff state, and history.
