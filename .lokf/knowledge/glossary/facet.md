---
type: GlossaryTerm
id: https://w3id.org/lmodel/uco/knowledge/glossary/facet
genre: reference
title: Facet
description: In UCO, a group of properties that describe one aspect of an object, such as a file's name and size. The schema renders each facet as a value inside its object's `hasFacet` list.
resource: src/uco/schema/uco_core.yaml
definedBy:
  - https://w3id.org/lmodel/uco/knowledge/datasets/uco-linkml-schema
sources:
  - id: uco_core.yaml
    resource: src/uco/schema/uco_core.yaml
    title: Facet and hasFacet
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# Facet

In the Unified Cyber Ontology, a facet groups the properties of one inherent aspect of an object: a `FileFacet` holds a file's name and size, for example. An object lists its facets with `hasFacet`. The schema renders each facet as a value inside that list, named by its `type`, without an IRI of its own.[^uco_core.yaml]

[^uco_core.yaml]: src/uco/schema/uco_core.yaml, Facet and hasFacet
