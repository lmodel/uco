---
type: GlossaryTerm
id: https://w3id.org/lmodel/uco/knowledge/glossary/uco-object
genre: reference
title: UcoObject
description: In UCO, the base class of every object a graph names by IRI, such as a file, an account, a tool or an action. The schema renders it as `UcoObject`, one of the four classes its adapt copy roots on `Concept`.
resource: src/uco/schema/uco_core.yaml
definedBy:
  - https://w3id.org/lmodel/uco/knowledge/datasets/uco-linkml-schema
sources:
  - id: uco_core.yaml
    resource: src/uco/schema/uco_core.yaml
    title: UcoObject
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# UcoObject

In the Unified Cyber Ontology, a `UcoObject` represents a concept of the cyber domain, or one needed to describe it, and is the base class of every object a graph names by IRI: a file, an account, a tool, an identity, an action and the rest. The schema renders it as `UcoObject`, which carries the identifier `id`, and its adapt copy roots it on `Concept`.[^uco_core.yaml]

[^uco_core.yaml]: src/uco/schema/uco_core.yaml, UcoObject
