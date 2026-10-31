---
type: Playbook
id: https://w3id.org/lmodel/uco/knowledge/playbooks/release
genre: how-to
title: Cut a release
description: "How a release is made: Conventional Commits on `main`, an `## [Unreleased]` changelog section, the `v0.0.0` baseline tag that keeps the first release at 0.1.0, and `semantic-release.yml`, which tags the release and dispatches Knowledge Release to attach `schema-<tag>-uco.yaml` once `KNOWLEDGE_RELEASE_ENABLED` is true."
resource: CONTRIBUTING.md
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Releasing (maintainers)
  - id: releaserc.json
    resource: .releaserc.json
    title: the release rules
  - id: changelog.md
    resource: CHANGELOG.md
    title: the baseline paragraph
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# Cut a release

1. Write `## [Unreleased]` in `CHANGELOG.md` as you go; the release job refuses an empty one.[^contributing.md]
2. Type each commit as Conventional Commits say. Only `feat:`, `fix:`, `security:` and a breaking change release, and `.releaserc.json` makes a breaking change a minor release below 1.0.0.[^releaserc.json]
3. Before the first releasing merge, push the signed `v0.0.0` tag on `main`, so that the first release is 0.1.0.[^changelog.md]
4. Merge the pull request. `semantic-release.yml` promotes the changelog section, tags `vX.Y.Z`, publishes the GitHub release, and dispatches Knowledge Release once `KNOWLEDGE_RELEASE_ENABLED` is `true`, which attaches the bundle and `schema-<tag>-uco.yaml`.

[^contributing.md]: CONTRIBUTING.md, Releasing (maintainers)
[^releaserc.json]: .releaserc.json, the release rules
[^changelog.md]: CHANGELOG.md, the baseline paragraph
