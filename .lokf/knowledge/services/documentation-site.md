---
type: Service
id: https://w3id.org/lmodel/uco/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: "The Astro Starlight site in `website/`, for <https://lmodel.github.io/uco>: the README as its home page, the pages of `docs/`, a page per schema element, a page per concept of this bundle with its trust label, the bundle's exports, and redirects from the retired sites' element pages, built and published by Knowledge website."
resource: website
sources:
  - id: site.config.mjs
    resource: website/site.config.mjs
    title: REPO, SITE, BASE, DOCS and REDIRECTS
  - id: website-readme.md
    resource: website/README.md
    title: the build
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# Documentation site

`website/` is an Astro Starlight site from the ktl-website template, for `https://lmodel.github.io/uco`. `npm run build` syncs the README, the pages of `docs/`, the schema's element pages and the bundle into it, builds it and checks every link.[^website-readme.md]

Its `REDIRECTS` keep old addresses working. `/elements/` and each element page of the retired mkdocs site go to the schema pages, and `/about` to the docs' about page. The element pages of the sixteen retired uco-* sites whose names changed go to their successors, and the rest to the schema index.[^site.config.mjs] The `Knowledge website` workflow publishes it.

[^site.config.mjs]: website/site.config.mjs, REPO, SITE, BASE, DOCS and REDIRECTS
[^website-readme.md]: website/README.md, the build
