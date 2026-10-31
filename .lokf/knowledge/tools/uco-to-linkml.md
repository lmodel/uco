---
type: Tool
id: https://w3id.org/lmodel/uco/knowledge/tools/uco-to-linkml
genre: reference
title: The UCO converter (uco_to_linkml.py)
description: "`scripts/uco_to_linkml.py`, the converter that writes every module of the schema from UCO's Turtle files: classes from OWL classes, slots from SHACL shapes and properties, enums from UCO's vocabularies, each keeping its UCO name and IRI. `--check` fails on a hand edit."
resource: scripts/uco_to_linkml.py
references:
  - https://w3id.org/lmodel/uco/knowledge/datasets/uco-linkml-schema
sources:
  - id: uco_to_linkml.py
    resource: scripts/uco_to_linkml.py
    title: the docstring and main
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# The UCO converter

`scripts/uco_to_linkml.py` reads the Turtle files under `src/uco/schema/upstream/ontology/` with rdflib and writes the sixteen modules and the umbrella into `src/uco/schema/`. Its docstring gives each rule it applies, and it prints a note for each part of the ontology it leaves out, renames or moves.[^uco_to_linkml.py]

Run it with `uv run python scripts/uco_to_linkml.py` after a change to the script or to the copy. With `--check`, it writes to a temporary folder and exits 1 when the output differs from the committed modules, which `tests/test_schema_is_generated.py` runs.

[^uco_to_linkml.py]: scripts/uco_to_linkml.py, the docstring and main
