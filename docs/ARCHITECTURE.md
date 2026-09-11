# Grid Carbon Intelligence architecture

## Purpose

Choose lower-carbon workload windows while respecting duration and deadline constraints.

## Current flow

`carbon signal → feasible windows → optimization → avoided-emissions report`

## Design rule

Keep domain assumptions at the boundary, keep core utilities deterministic, and keep evaluation separate from training or inference code. Every future model should be compared with the current baseline under the same split and metric definitions.

## Review checklist

- Input units, timestamps, and provenance are documented.
- Training and evaluation information are separated.
- Edge cases have tests.
- Uncertainty or failure behavior is explicit.
- The README states intended use and non-goals.
