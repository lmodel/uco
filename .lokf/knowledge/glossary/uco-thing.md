---
type: GlossaryTerm
id: https://w3id.org/lmodel/uco/knowledge/glossary/uco-thing
genre: reference
title: UcoThing
description: "In UCO, the top class of every individual: objects, facets, threads and thread items. The schema renders it as `UcoThing`, which carries the `type` designator."
resource: src/uco/schema/uco_core.yaml
definedBy:
  - https://w3id.org/lmodel/uco/knowledge/datasets/uco-linkml-schema
sources:
  - id: uco_core.yaml
    resource: src/uco/schema/uco_core.yaml
    title: UcoThing
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# UcoThing

In the Unified Cyber Ontology, `UcoThing` is the top class of every individual. Its two main subclasses are `UcoObject` and `UcoInherentCharacterizationThing`, the parent of facets. The schema renders it as `UcoThing`, which carries `type`, the slot whose value names an object's class.[^uco_core.yaml]

[^uco_core.yaml]: src/uco/schema/uco_core.yaml, UcoThing
