# Dispatch Manifest

## Canonical source

- `references/command-registry.md` is the source of truth.
- This file is a derived routing summary, not a shortened example list.

## Routing principle

- Route by task shape first.
- Use the light path for tiny local fixes.
- Use the full path for broad or risky work.

## Routing map

### Discovery

- Commands: 
- Typical output: state, next step

### Planning

- Commands: 
- Typical output: plan, risks

### Design

- Commands: 
- Typical output: direction, constraints

### Build

- Commands: 
- Typical output: patch plan, findings

### Verify

- Commands: 
- Typical output: coverage, verdict

### Ship

- Commands: 
- Typical output: readiness, handoff

## Handoff

- Every lane returns `findings`, `risks`, `files`, and `recommended_next_step`.
- The command file chooses the route.
- The workflow file explains the steps.
