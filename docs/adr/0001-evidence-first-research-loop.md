# ADR 0001: Use an evidence-first research loop

- Status: Accepted
- Date: 2026-07-22

## Context

A multi-provider research engine can be organised around provider results, generated prose or evidence requirements. Provider-first aggregation is easy to implement but makes it difficult to explain why more searching is needed. Prose-first synthesis can hide unsupported claims behind fluent output.

Changing the central research state after provider adapters and evaluation datasets exist would be expensive. Future contributors also need to understand why Adaptive Deep Research Engine does not simply merge result lists.

## Decision

The canonical state of a Research Run will be expressed in terms of Claims, Evidence, Evidence Links, Contradictions and Evidence Gaps.

Search providers supply candidate Documents. The planner selects further searches from unresolved Evidence Gaps. Narrative synthesis occurs after the evidence state is available and cannot silently upgrade unresolved Claims.

## Consequences

### Positive

- Search decisions can be traced to explicit information needs.
- Provider quality can be evaluated independently from report fluency.
- Contradictions and unknowns remain representable.
- Stopping decisions can be tested against the research state.

### Negative

- The first vertical slice requires more modelling than a result-merging wrapper.
- Evidence extraction errors become a distinct failure mode.
- Confidence cannot be reduced to a single opaque model score.
