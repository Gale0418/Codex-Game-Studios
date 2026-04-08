# Runtime Policies

## Allow

- `git status`
- `git diff`
- `git log`
- `git branch`
- `rg`
- `sed`
- `pytest`
- `bash scripts/validate_studio.sh`
- `cmd /c scripts\\validate_studio.cmd`

## Deny

- `rm -rf`
- `git reset --hard`
- `git push --force`
- direct secret access
- writing outside the repo without explicit approval

## Notes

- Escalate any action that can delete work or leak secrets.
- Prefer explicit verification over assumed success.
- Treat broad multi-file changes as review points before handoff.
- Log session start, tool use, compact, and stop events in the active note when the task is broad.
