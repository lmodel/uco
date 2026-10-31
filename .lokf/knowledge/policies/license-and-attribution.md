---
type: Policy
id: https://w3id.org/lmodel/uco/knowledge/policies/license-and-attribution
genre: reference
title: License and attribution
description: "The repository's licences: Apache 2.0 for the schema and the code, the UCO Community's Apache 2.0 for the copy of UCO's files and the descriptions taken from it, Apache 2.0 for the copy of lmodel/collections' module, MIT for the copier template's scaffolding, Apache 2.0 for the KTL templates, and CC BY 4.0 for the knowledge bundle."
resource: NOTICE
sources:
  - id: notice
    resource: NOTICE
    title: every section
  - id: license
    resource: LICENSE
    title: the licence text
  - id: readme.md
    resource: README.md
    title: License
generated:
  by: process:ktl-librarian
  at: "2026-10-31T23:09:51Z"
status: draft
---

# License and attribution

The schema and the code are under the Apache License 2.0.[^license] `NOTICE` lists the third-party work the repository carries:[^notice]

- **UCO.** The copy of UCO 1.5.0's files and the description of each UCO term in the schema are the UCO Community's, under the Apache License 2.0. UCO's LICENSE carries no copyright line.
- **lmodel/collections and the Collections Ontology.** The copy of lmodel/collections' module is under the Apache License 2.0, and its descriptions of CO's terms are its own words. CO's repository states no licence; the Google Code archive gives Apache 2.0 for CO's code and CC BY 3.0 for its other content.
- **linkml-project-copier**, under the MIT License, for the justfile, configuration and documentation scaffolding.
- **The KTL templates**, under the Apache License 2.0, for the sidecar's scripts, its workflows and the website.

The README says that the knowledge bundle is under CC BY 4.0, as its `index.md` declares, and that the schema is not an official UCO release.[^readme.md]

[^license]: LICENSE, the licence text
[^notice]: NOTICE, every section
[^readme.md]: README.md, License
