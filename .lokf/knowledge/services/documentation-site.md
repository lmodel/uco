---
type: Service
id: https://w3id.org/lmodel/uco/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: "The Hugo site in `website/`, for <https://lmodel.github.io/uco>: the README as its home page, the pages of `docs/`, a page per schema element, a page per concept of this bundle with its trust label, the bundle's exports, and redirects from the retired sites' element pages, built and published by Knowledge website."
resource: website
sources:
  - id: site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
  - id: website-readme.md
    resource: website/README.md
    title: the build
  - id: prepare.sh
    resource: website/scripts/prepare.sh
    title: the schema's pages
  - id: content.gotmpl
    resource: website/content/_content.gotmpl
    title: the redirects
  - id: readme.md
    resource: README.md
    title: the uco-* repositories the schema replaces
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:10:24Z"
status: draft
---

# Documentation site

`website/` is a Hugo site from the ktl-website template, for `https://lmodel.github.io/uco/`. `website/scripts/build.sh` builds it into `dist/` with Hugo and Pagefind, which come from PyPI through uv, adds the search index and checks every link between its pages.[^website-readme.md] Before Hugo runs, `website/scripts/prepare.sh` runs `lokf export` on the bundle and LinkML's `gen-doc` on `src/uco/schema/uco.yaml`, and writes the output into `website/generated/`, which is never committed.[^prepare.sh]

The redirects in `website/site.toml` keep old addresses working. `/about` goes to the docs' about page, and each `/schema/<name>/` address to that element's page.[^site.toml] `/elements/` and each element page whose name the schema keeps go to the schema pages with no setting.[^content.gotmpl] The schema replaces the sixteen uco-* repositories.[^readme.md] Their element pages whose names changed go to their successors, and the rest to the schema index.[^site.toml] The `Knowledge website` workflow publishes it.

[^site.toml]: website/site.toml, the site's address, title and redirects
[^website-readme.md]: website/README.md, the build
[^prepare.sh]: website/scripts/prepare.sh, the schema's pages
[^content.gotmpl]: website/content/_content.gotmpl, the redirects
[^readme.md]: README.md, the uco-* repositories the schema replaces
