# Hooks Mirror

This directory mirrors the hook-oriented layout of the original studio pack.

## Files

- `session-start.sh`: mirrors the session-start lifecycle contract.
- `pre-tool-use.sh`: mirrors lane and risk checks before a tool call.
- `post-tool-use.sh`: mirrors audit logging after a tool call.
- `pre-compact.sh`: mirrors compact-time handoff capture.
- `stop.sh`: mirrors session finalization and production-state sync.
- `subagent-start.sh`: mirrors subagent audit logging.

## Source of truth

- `runtime/execution-policy.md`
- `runtime/hook-map.md`
- `runtime/session-lifecycle.md`
