# Changelog

## Purpose

- Maintain a running summary of shipped changes.

## Trigger

- Use when a release history record is needed.

## Primary lane

- `docs-release`
- `release-manager`

## Inputs

- Shipped changes
- Release version
- Categorized notes
- Residual risk

## Steps

1. Record only the durable summary of the release.
2. Keep the entry grouped by category.
3. Preserve the shipping context in a readable form.
4. Avoid duplicating the patch notes word for word.

## Outputs

- Unreleased entries
- Categorized changes

## Exit criteria

- The release history can survive future edits without confusion.

## Template

- `templates/changelog.md`
