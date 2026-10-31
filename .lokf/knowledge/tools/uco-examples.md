---
type: Tool
id: https://w3id.org/lmodel/uco/knowledge/tools/uco-examples
genre: reference
title: The examples writer (uco_examples.py)
description: "`scripts/uco_examples.py`, which writes a valid example for each class a concept may name as its type: from nodes of UCO's own passing examples, turned from JSON-LD into the schema's form, and from the schema where no example holds the class. Its `Reader` also reads UCO's failing examples for the tests."
resource: scripts/uco_examples.py
references:
  - https://w3id.org/lmodel/uco/knowledge/datasets/test-data
sources:
  - id: uco_examples.py
    resource: scripts/uco_examples.py
    title: the docstring and Reader
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# The examples writer

`scripts/uco_examples.py` writes `tests/data/valid/`. For each class that carries an IRI, and each class under one, it takes the richest node of that class in each of UCO's passing examples. Where no example holds the class, it writes a minimal instance from the schema: an IRI, the type and each required slot.[^uco_examples.py]

Its `Reader` turns a node of UCO's JSON-LD into the schema's form. It reads only an example whose context is inline, so rdflib fetches nothing. It skips a node it cannot hold, such as one of two unrelated classes, and says why. `--check` compares with the committed examples instead of writing.

[^uco_examples.py]: scripts/uco_examples.py, the docstring and Reader
