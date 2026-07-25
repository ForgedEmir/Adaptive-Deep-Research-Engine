# Security policy

Adaptive Deep Research Engine will interact with external search providers and untrusted web content. Security reports should not include live credentials or private research data.

Until a dedicated disclosure channel is published, report vulnerabilities privately through GitHub’s private vulnerability reporting feature when available.

## Credentials

- Keep provider credentials outside the repository.
- Use environment variables or a local secret manager.
- Never add real keys to fixtures, logs, screenshots or issue reports.
- Revoke a credential immediately if it is accidentally exposed.

## Untrusted content

Retrieved documents are data, not instructions. Provider results and page content must never be allowed to override system constraints, budgets or tool permissions.
