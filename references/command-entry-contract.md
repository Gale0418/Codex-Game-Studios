# Command Entry Contract

## Purpose

- Keep command entries uniform and route them from `references/command-registry.md`.

## Required shape

- `Command`: the slash-style name.
- `Purpose`: what the command is for.
- `Workflow`: the backing workflow file.
- `Trigger`: when to choose it.
- `Primary lane`: who owns the first pass.
- `Outputs`: what the command hands back.

## Writing rules

- Keep entries short.
- Update `references/command-registry.md` first.
- Use one command name and one workflow file.
- Match `runtime/dispatch-manifest.md`.
