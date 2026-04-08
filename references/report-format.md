# Report Format

Use this structure for subagent output:

```text
findings:
- ...

risks:
- ...

files:
- /absolute/path/to/file

recommended_next_step:
- ...

goal:
- ...

wave:
- ...

checkpoint:
- ...
```

Rules:

- Keep findings concrete.
- Name exact files when possible.
- Separate confirmed facts from assumptions.
- Mention verification status for any code change.
