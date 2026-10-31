---
type: Explanation
id: https://w3id.org/lmodel/uco/knowledge/explanations/scope-and-influences
genre: explanation
title: Scope, influences and mappings
description: "What the schema renders and what it leaves out: UCO 1.5.0's fifteen namespaces and the CO terms it uses, as a converter writes them, with lmodel/spdx's converter and lmodel/slsa's release and governance files as its influences. It maps to no other vocabulary, and leaves out SHACL advice, SPARQL constraints and what LinkML cannot state."
resource: README.md
about:
  - https://w3id.org/lmodel/uco/knowledge/datasets/uco-linkml-schema
sources:
  - id: readme.md
    resource: README.md
    title: What it models, Influences, Mappings and Not modelled here
  - id: changelog.md
    resource: CHANGELOG.md
    title: Unreleased
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# Scope, influences and mappings

The schema renders the Unified Cyber Ontology at release 1.5.0: its fifteen namespaces, as one module each, and the Collections Ontology terms UCO's files use. It replaces the sixteen uco-* repositories, which modelled UCO 1.1.0 by hand.[^readme.md][^changelog.md]

Its influences are few. The converter follows lmodel/spdx's, and the release asset and governance files follow lmodel/slsa. It names no term of another vocabulary, so it has no mappings.

It leaves out what LinkML cannot state: SHACL shapes of severity Info or Warning, SPARQL constraints, `sh:not` and `sh:xone`, shapes over a path of more than one property, and UCO's rule that a UcoThing is never a blank node. It does not render UCO's `owl.ttl`, which holds shapes over OWL itself.

[^readme.md]: README.md, What it models, Influences, Mappings and Not modelled here
[^changelog.md]: CHANGELOG.md, Unreleased
