---
type: Dataset
id: https://w3id.org/lmodel/uco/knowledge/datasets/collections-module
genre: reference
title: lmodel/collections module
description: The schema module of lmodel/collections that renders the Collections Ontology (CO) 2.0, copied unchanged into `src/uco/schema/collections/` from collections v0.1.0, held to its git object hash by `tests/test_collections_import.py`, and imported by `uco_types` and the umbrella for the CO terms UCO's threads build on.
resource: src/uco/schema/collections/collections.yaml
license: Apache-2.0
derivedFrom:
  - https://w3id.org/lmodel/uco/knowledge/references/collections-ontology
sources:
  - id: test_collections_import.py
    resource: tests/test_collections_import.py
    title: the docstring, COLLECTIONS_COMMIT, PINNED_BLOBS and CO_TERMS_BEFORE
  - id: notice
    resource: NOTICE
    title: lmodel/collections and the Collections Ontology
  - id: uco_types.yaml
    resource: src/uco/schema/uco_types.yaml
    title: the imports and the slot_usage of Thread and ThreadItem
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: COLLECTIONS and test_the_copy_holds_collections_copy
generated:
  by: process:ktl-librarian
  at: "2026-10-31T23:09:51Z"
status: draft
---

# lmodel/collections module

`src/uco/schema/collections/collections.yaml` is lmodel/collections' only schema module at release v0.1.0, copied unchanged. `tests/test_collections_import.py` pins that release's commit, a55334d, and the file's git object hash, and fails when another file sits beside it. NOTICE puts the module under the Apache License 2.0 and says its descriptions are lmodel/collections' own words.[^test_collections_import.py][^notice]

The module renders CO 2.0 with CO's names and IRIs under the prefix `coll`. CO's `Item`, `size` and `index` are named `CoItem`, `co_size` and `co_index`. The same test checks that each CO class and slot the schema held before the import keeps its IRI, and that the vendored module declares it.[^test_collections_import.py]

`uco_types` and the umbrella import it. A thread is a CO bag and a thread item a CO item. Two rules differ from the module. `Thread` names its items by IRI, where the module holds a bag's items inside the bag, and `ThreadItem` keeps `itemContent` optional, where the module requires it.[^uco_types.yaml]

The adapt copy holds every class and key of collections' own released copy, `schema-v0.1.0-collections.yaml`, under the same IRIs, and `tests/test_schema_rules.py` checks it against that asset's SHA-256. A later collections release replaces the file whole, and the pins move with it.[^test_schema_rules.py]

[^test_collections_import.py]: tests/test_collections_import.py, the docstring, COLLECTIONS_COMMIT, PINNED_BLOBS and CO_TERMS_BEFORE
[^notice]: NOTICE, lmodel/collections and the Collections Ontology
[^uco_types.yaml]: src/uco/schema/uco_types.yaml, the imports and the slot_usage of Thread and ThreadItem
[^test_schema_rules.py]: tests/test_schema_rules.py, COLLECTIONS and test_the_copy_holds_collections_copy
