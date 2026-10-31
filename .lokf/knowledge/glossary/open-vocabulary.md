---
type: GlossaryTerm
id: https://w3id.org/lmodel/uco/knowledge/glossary/open-vocabulary
genre: reference
title: Open vocabulary
description: In UCO, a list of suggested string values for a property, such as the hash names MD5 and SHA256. The schema renders each as an enum, and a property that takes one also takes any string.
resource: src/uco/schema/uco_vocabulary.yaml
definedBy:
  - https://w3id.org/lmodel/uco/knowledge/datasets/uco-linkml-schema
sources:
  - id: uco_vocabulary.yaml
    resource: src/uco/schema/uco_vocabulary.yaml
    title: the enums
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# Open vocabulary

In the Unified Cyber Ontology, a vocabulary lists the values a property suggests, such as the hash names `MD5` and `SHA256`. Since UCO 1.4.0 the lists are open: a value outside one is advice, not an error. The schema renders each vocabulary as an enum, and a property that takes one accepts the enum's values or any string.[^uco_vocabulary.yaml]

[^uco_vocabulary.yaml]: src/uco/schema/uco_vocabulary.yaml, the enums
