# Performance Profile

## Purpose

- Identify performance bottlenecks and expensive paths.

## Trigger

- Use when the game feels slow, heavy, or unstable.

## Primary lane

- `performance-analyst`
- `engine-programmer`
- `qa-regression`

## Inputs

- Slow paths
- Hot code or render paths
- Target hardware or browser
- Observed symptoms

## Steps

1. Find the most likely expensive path.
2. Distinguish measurement from guesswork.
3. Pinpoint the smallest useful optimization target.
4. Note what still needs a deeper profile pass.

## Outputs

- Measurements
- Bottlenecks
- Action items

## Exit criteria

- The bottleneck and next optimization step are both named.

## Template

- `templates/perf-profile-report.md`
