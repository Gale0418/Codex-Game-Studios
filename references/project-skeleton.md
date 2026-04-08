# Project Skeleton

Use this when a real game project is created under this studio.
Keep the tree small at the start, then grow only the folders you need.

## Recommended shape

```text
game-project/
  README.md
  src/
  assets/
  tests/
  design/
  docs/
  content/        # optional
  tools/          # optional
  build/          # generated output, not hand-edited
```

## What each folder is for

- `src/`: gameplay code, systems, UI glue, engine code, and anything that changes how the game runs.
- `assets/`: art, audio, animation, fonts, imported data, and level resources.
- `tests/`: smoke checks, regression checks, fixture tests, and bug repro coverage.
- `design/`: GDD notes, balance notes, level specs, UX flows, and feature decisions.
- `docs/`: setup steps, build notes, release notes, integration notes, and onboarding material.
- `content/`: story text, quests, dialogue, localization source, and other content-heavy data.
- `tools/`: importers, editor helpers, build helpers, and other non-runtime utilities.
- `build/`, `dist/`, `temp/`: generated output only. Do not treat these as source of truth.

## When to add files

- Add `src/` files as soon as there is behavior, rules, or UI logic to own.
- Add `assets/` files when the project references art, audio, or other runtime media.
- Add `tests/` files when a path becomes risky, repeatable, or expensive to verify by hand.
- Add `design/` files before implementation when the team still needs decisions, scope, or layouts.
- Add `docs/` files when setup, build, release, or onboarding steps need to be shared.

## Practical rules

- Keep game rules close to the systems that enforce them.
- Keep asset names predictable and grouped by feature or domain.
- Keep tests near the risk they cover, not buried in a generic bucket.
- Keep design docs short and current. If a decision is final, move the result into implementation or docs.
- Keep docs operational. If nobody uses the file to build, test, or ship the project, it is probably too vague.

## Minimal starter tree

```text
game-project/
  README.md
  src/
  assets/
  tests/
  design/
  docs/
```

