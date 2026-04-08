# Game Rules Path Rules

- Keep game rules centralized and treat them as the source of truth.
- Do not scatter constants or legality checks across UI or presentation code.
- Keep turn order, scoring, win state, and rule transitions explicit.
- If a rule change affects behavior, require a targeted regression pass.

