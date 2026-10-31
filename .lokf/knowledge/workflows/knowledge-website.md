---
type: Service
id: https://w3id.org/lmodel/uco/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: "The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true."
resource: .github/workflows/knowledge-website.yaml
sources:
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

`.github/workflows/knowledge-website.yaml` is the workflow named "Knowledge website", a copy of the ktl-website template. It runs on a push or a pull request that touches `website/`, `.lokf/`, the README, `docs/`, the changelog, `llms.txt`, `.linkml/`, a justfile, a `pyproject.toml` or a `uv.lock`, every Monday at 05:23 UTC and by hand.[^knowledge-website.yaml] Its `build` job, read-only, runs `npm ci --ignore-scripts` and `npm run build`, which syncs the pages, builds the site and checks every link, and uploads `website/dist`. Its `deploy` job holds `pages: write` and `id-token: write` in the `github-pages` Environment, and runs only once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`.

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the header comment, the on key and the jobs
