---
type: Service
id: https://w3id.org/lmodel/uco/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its uco-copy job runs `scripts/check_upstream_release.py` against ucoProject/UCO, and on a finding opens or updates the issue titled Upstream watch: the Unified Cyber Ontology has changed."
resource: .github/workflows/upstream-watch.yaml
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

`.github/workflows/upstream-watch.yaml` is the workflow named "Upstream watch". It runs every Monday at 07:00 UTC and by hand.[^upstream-watch.yaml] Its one job, `uco-copy`, checks the repository out with `persist-credentials: false` and runs `scripts/check_upstream_release.py` with the runner's own Python, within 10 minutes. On a finding, `.github/scripts/report-issue.sh` opens the issue titled "Upstream watch: the Unified Cyber Ontology has changed", or comments on the one already open. The job holds `contents: read` and `issues: write`.

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml, the header comment, the on key and the jobs
