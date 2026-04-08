# Game Patterns

## Rule centralization

- Keep board sizes, win conditions, and AI levels in one place.
- Avoid scattering the same rule across UI and worker code.

## State ownership

- Keep the authoritative state in one source.
- Mirror state only when the UI needs a derived view.

## Worker separation

- Put heavy AI or search logic in a worker when possible.
- Keep UI code focused on interaction and display.

## Risk hotspots

- Undo and redo.
- Save and restore.
- Turn order and move legality.
- Responsive board layout.
- Victory and tie handling.

