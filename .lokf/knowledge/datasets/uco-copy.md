---
type: Dataset
id: https://w3id.org/lmodel/uco/knowledge/datasets/uco-copy
genre: reference
title: The UCO 1.5.0 copy
description: "UCO's own files at release 1.5.0, 79 files copied into `src/uco/schema/upstream/` under UCO's paths: the seventeen Turtle files of the ontology, UCO's LICENSE, and the passing and failing examples with the SHACL reports on the failing ones. Each is matched to commit `7ebb3957e9e9` by git object hash."
resource: src/uco/schema/upstream
derivedFrom:
  - https://w3id.org/lmodel/uco/knowledge/references/unified-cyber-ontology
sources:
  - id: upstream
    resource: src/uco/schema/upstream
    title: the copied files
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: PINNED_TAG, PINNED_COMMIT and PINNED_BLOBS
  - id: notice
    resource: NOTICE
    title: The Unified Cyber Ontology
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# The UCO 1.5.0 copy

`src/uco/schema/upstream/` holds 79 files from ucoProject/UCO at the tag `1.5.0`, commit `7ebb3957e9e9a2e1bb9c66cd1ede8c912a726344`, under the paths UCO gives them:[^upstream]

- the seventeen Turtle files: one per namespace under `ontology/uco/`, the master ontology `uco.ttl`, and `ontology/co/co.ttl`;
- UCO's `LICENSE`, the Apache License 2.0;
- 42 example files from `tests/examples/`, the passing and failing JSON-LD examples, and the 19 SHACL reports on the failing ones.

`scripts/check_upstream_release.py` pins each file's git object hash, and `tests/test_upstream.py` holds the copy to the pins offline.[^check_upstream_release.py] NOTICE credits the copy, and says that UCO's LICENSE carries no copyright line and that UCO ships no NOTICE file of its own.[^notice] The converter reads the Turtle files, the examples script reads the passing examples, and `tests/test_data.py` reads the failing ones with their reports. Nothing changes the copy.

[^upstream]: src/uco/schema/upstream, the copied files
[^check_upstream_release.py]: scripts/check_upstream_release.py, PINNED_TAG, PINNED_COMMIT and PINNED_BLOBS
[^notice]: NOTICE, The Unified Cyber Ontology
