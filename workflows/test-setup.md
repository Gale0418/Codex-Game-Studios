# Test Setup

## Purpose

- Prepare the test environment or test fixtures needed for a change.

## Trigger

- Use when tests need setup work before they can run.

## Primary lane

- `qa-lead`
- `qa-regression`
- `integration`

## Inputs

- Test target
- Dependencies
- Setup constraints

## Steps

1. Identify the needed setup.
2. List the dependencies or fixtures.
3. Call out anything brittle.
4. Hand back the setup notes.

## Outputs

- Setup
- Dependencies
- Notes

## Exit criteria

- The test environment can be prepared deterministically.

## Template

- `templates/test-setup.md`

