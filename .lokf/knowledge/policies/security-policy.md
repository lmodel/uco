---
type: Policy
id: https://w3id.org/lmodel/uco/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the ruleset on `main`, and the two repository settings that are not yet in force.
resource: SECURITY.md
sources:
  - id: security.md
    resource: SECURITY.md
    title: every section
  - id: dependabot.yml
    resource: .github/dependabot.yml
    title: the five update entries
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# Security policy

`SECURITY.md` asks for a vulnerability to be reported through GitHub's private vulnerability reporting, not in a public issue. It says that one person maintains the repository, so a first reply takes days and there is no bounty, and that only the latest release receives fixes.[^security.md]

The repository releases the schema, the Python models generated from it, and the adapt copy as a release asset; nothing is published to PyPI. The converter and the examples writer parse the copied files with rdflib, which fetches no remote context, and write only the schema and the examples. Its table of surfaces names each workflow and what holds it: the pull request checks run read-only, the release job runs only on a push to `main` in the `release` Environment, the website's deploy job alone holds the Pages scopes, and the upstream watch writes only issues.

Every workflow declares `permissions: {}` at the top, pins its actions to commit hashes and runs harden-runner in audit mode. Dependabot keeps the pins, both uv locks and the two npm locks current, each monthly.[^dependabot.yml] The policy says that a ruleset on `main` blocks deletion and force-pushes and keeps the history linear, and names two settings not yet in force: required reviewers on the `release` Environment, and secret scanning with push protection.

[^security.md]: SECURITY.md, every section
[^dependabot.yml]: .github/dependabot.yml, the five update entries

## Open questions

- 2026-10-31, process:ktl-librarian: SECURITY.md names a ruleset on main that blocks deletion and force-pushes and keeps the history linear, but lmodel/uco did not exist on 2026-10-31, so no ruleset could be read. Is it in force now?
