---
type: Explanation
id: https://w3id.org/lmodel/uco/knowledge/explanations/element-names
genre: explanation
title: Element names and the shared namespace
description: "How the schema names its elements: UCO's own names and IRIs under UCO's prefixes, a namespace prefix on 20 properties UCO defines in two namespaces, lmodel/collections' `CoItem`, `co_size` and `co_index` for CO terms, and the renames `lokf adapt` makes beside LOKF. It also lists the class and key names the adapt copy shares with lmodel/oscal, spdx, slsa and in-toto."
resource: src/uco/schema/uco.yaml
about:
  - https://w3id.org/lmodel/uco/knowledge/datasets/uco-linkml-schema
sources:
  - id: uco.yaml
    resource: src/uco/schema/uco.yaml
    title: the comments
  - id: collections.yaml
    resource: src/uco/schema/collections/collections.yaml
    title: the notes
  - id: linkmllint.yaml
    resource: .linkmllint.yaml
    title: the naming rule
  - id: readme.md
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: SHARED_KEYS and SHARED_CLASSES
generated:
  by: process:ktl-librarian
  at: "2026-10-31T23:10:24Z"
status: draft
---

# Element names and the shared namespace

Every class, property and vocabulary keeps its UCO local name, and its IRI as a compact URI under UCO's prefix for its namespace, such as `uco-core:UcoObject`. Where UCO defines one local name in more than one namespace, the namespace that comes first in the import order keeps it, and 20 others take their namespace as a prefix, such as `observable_endTime`. The umbrella's comments list them.[^uco.yaml] The Collections Ontology (CO) terms keep the names lmodel/collections gives them: CO's `Item`, `size` and `index` are `CoItem`, `co_size` and `co_index`, under CO's IRIs.[^collections.yaml] `.linkmllint.yaml` admits those names and UCO's upper-case acronyms, such as `MSISDNType`.[^linkmllint.yaml]

The adapt copy renames each name LOKF also defines and keeps its IRI: `Organization`, `Person` and `Role` become `UcoOrganization`, `UcoPerson` and `UcoRole`, and 17 keys take a `uco_` prefix.[^readme.md]

Some names are UCO's and a released neighbour's too. Seven classes are lmodel/oscal's, such as `Hash` and `Location`, and seven lmodel/spdx's, such as `File` and `Tool`, so a host cannot import this copy beside either until one copy renames them. `tests/test_schema_rules.py` lists every shared class and key, and fails on a new one.[^test_schema_rules.py]

[^uco.yaml]: src/uco/schema/uco.yaml, the comments
[^linkmllint.yaml]: .linkmllint.yaml, the naming rule
[^readme.md]: README.md, Knowledge Trust Ladder (KTL)
[^test_schema_rules.py]: tests/test_schema_rules.py, SHARED_KEYS and SHARED_CLASSES

[^collections.yaml]: src/uco/schema/collections/collections.yaml, the notes
