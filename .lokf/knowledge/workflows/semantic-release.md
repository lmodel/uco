---
type: Service
id: https://w3id.org/lmodel/uco/knowledge/workflows/semantic-release
genre: reference
title: Semantic release (semantic-release.yml)
description: "The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request into main, its plan job checks that the commits, the changelog and the title would release; on a push to main, its release job in the release Environment tags vX.Y.Z, publishes the GitHub release and dispatches Knowledge Release."
resource: .github/workflows/semantic-release.yml
sources:
  - id: semantic-release.yml
    resource: .github/workflows/semantic-release.yml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# Semantic release (semantic-release.yml)

`.github/workflows/semantic-release.yml` is the workflow named "Semantic release". It runs on a pull request into `main` and on a push to `main`.[^semantic-release.yml] Its `plan` job runs on the pull request, read-only, within 10 minutes. Its `release` job runs on the push, in the `release` Environment, within 20 minutes. Both install semantic-release from `.github/release/package-lock.json` with `npm ci --ignore-scripts`. The release job tags `vX.Y.Z`, commits the promoted changelog, publishes the GitHub release, and dispatches Knowledge Release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.

[^semantic-release.yml]: .github/workflows/semantic-release.yml, the header comment, the on key and the jobs
