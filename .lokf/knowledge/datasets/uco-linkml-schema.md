---
type: Dataset
id: https://w3id.org/lmodel/uco/knowledge/datasets/uco-linkml-schema
genre: reference
title: UCO LinkML schema
description: "The LinkML schema of the Unified Cyber Ontology (UCO) 1.5.0, `src/uco/schema/uco.yaml` (schema id `https://w3id.org/lmodel/uco`) with sixteen modules, one per UCO namespace and one for the Collections Ontology terms UCO uses: 425 classes, 771 slots, 53 enums and 14 types, all written by a converter. Its `lokf adapt` copy `.lokf/uco.yaml` is the bundle's domain schema."
resource: src/uco/schema/uco.yaml
derivedFrom:
  - https://w3id.org/lmodel/uco/knowledge/datasets/uco-copy
sources:
  - id: uco.yaml
    resource: src/uco/schema/uco.yaml
    title: the header, the comments and the document root
  - id: uco_to_linkml.py
    resource: scripts/uco_to_linkml.py
    title: the docstring's rules and the counts the script prints
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes and their roots
  - id: lokf-uco.yaml
    resource: .lokf/uco.yaml
    title: the adapt copy's header and notes
  - id: lokf-justfile
    resource: .lokf/justfile
    title: the schema := line
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# UCO LinkML schema

`src/uco/schema/uco.yaml` is the umbrella schema `uco`, id `https://w3id.org/lmodel/uco`, version 1.5.0, under the Apache License 2.0. Its `source` is UCO's 1.5.0 release. It imports sixteen modules in their import order and adds one class of its own, `UcoDocument`, whose `graph` lists UCO's things.[^uco.yaml]

`scripts/uco_to_linkml.py` writes every module from UCO's Turtle files, and nobody edits them by hand. The modules are `uco_core`, `uco_action`, `uco_analysis`, `uco_configuration`, `uco_identity`, `uco_location`, `uco_marking`, `uco_observable`, `uco_pattern`, `uco_role`, `uco_time`, `uco_tool`, `uco_types`, `uco_victim`, `uco_vocabulary` and `uco_co`. Each keeps the id of the old uco-* repository it replaces, such as `https://w3id.org/lmodel/uco-core`. Together they hold 425 classes, 771 slots, 53 enums and 14 types.[^uco_to_linkml.py]

## Domain schema

`project.justfile` runs `lokf adapt` with the roots `UcoObject`, `UcoType`, `Thread` and `ThreadItem`, the classes that carry an IRI, and writes `.lokf/uco.yaml`. `just lokf-adapt-check` fails when the copy is stale.[^project.justfile] The copy folds the modules into one file, imports `linkml:types` and `lokf`, and renames the names LOKF also defines, such as `Person` to `UcoPerson`.[^lokf-uco.yaml] The sidecar's justfile names it on its `schema :=` line, so `just lokf-validate` and `just lokf-check-refs` read it.[^lokf-justfile]

[^uco.yaml]: src/uco/schema/uco.yaml, the header, the comments and UcoDocument
[^uco_to_linkml.py]: scripts/uco_to_linkml.py, the docstring and the counts it prints
[^project.justfile]: project.justfile, lokf_adapt_roots, lokf-adapt and lokf-adapt-check
[^lokf-uco.yaml]: .lokf/uco.yaml, the header comment and the notes
[^lokf-justfile]: .lokf/justfile, the schema := line
