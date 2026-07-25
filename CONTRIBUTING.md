# Contributing to Adaptive Deep Research Engine

Adaptive Deep Research Engine is in its foundation phase. Contributions should keep claims, evidence and evaluation separate from presentation.

## Branch workflow

1. Start from `develop`.
2. Create a short-lived `feat/*`, `fix/*`, `test/*` or `docs/*` branch.
3. Add or update tests before production behaviour changes.
4. Open a pull request into `develop`.
5. Record the verification commands and their real output.

`main` is reserved for accepted, demonstrable milestones.

## Commit format

Use Conventional Commits:

```text
feat(scope): short description
fix(scope): short description
test(scope): short description
docs(scope): short description
```

## Non-negotiable constraints

- Never remove a budget, timeout or stopping condition silently.
- Never commit API keys, tokens or provider responses containing secrets.
- Do not describe planned behaviour as implemented behaviour.
- A citation must support the associated claim, not merely mention the topic.
- Provider integrations must preserve raw references for traceability.
