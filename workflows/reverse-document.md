# Reverse Document

## Purpose

- Reconstruct design or technical docs from code.

## Trigger

- Use when implementation exists but documentation is missing.

## Primary lane

- `intake-scan`
- `architecture`
- `docs-release`

## Inputs

- Source files
- Runtime behavior
- Existing docs
- Validation gaps

## Steps

1. Read the implementation as if it were the spec.
2. Reconstruct the missing design or technical intent.
3. Call out assumptions and unclear edges.
4. Note what still needs validation before shipping the doc.

## Outputs

- Draft doc
- Assumptions
- Validation needs

## Exit criteria

- A reader can understand the system without reading the code first.

## Template

- `templates/reverse-document.md`
