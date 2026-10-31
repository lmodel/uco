---
type: Explanation
id: https://w3id.org/lmodel/uco/knowledge/explanations/data-form
genre: explanation
title: The schema's form and UCO's JSON-LD
description: "Where data in the schema's form differs from UCO's JSON-LD: keys are slot names, `type` names one class, facets and other value objects sit inside their object without an IRI, a reference is an IRI, vocabularies are open, and a literal carries no datatype."
resource: docs/about.md
about:
  - https://w3id.org/lmodel/uco/knowledge/datasets/uco-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: The data's form and The schema's shape
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# The schema's form and UCO's JSON-LD

In the schema's form, a key is UCO's local name for the property, not its compact URI, and `type` names the most specific class of a node. A node UCO types with two unrelated classes has no form here.[^about.md]

A facet, a hash, a dictionary and UCO's other value classes sit inside the object that holds them, without an IRI of their own. Only an object, a thread, a thread item and a UcoType instance has an IRI, as `id`. A slot ranged over an object holds that object's IRI as a string.

UCO 1.4.0 made its vocabularies suggestions, so a property such as `hashMethod` takes a vocabulary value or any string. A value carries no datatype IRI. Where UCO forbids a property on a class with `sh:maxCount 0`, the class has `none_of` its slot.

[^about.md]: docs/about.md, The data's form and The schema's shape
