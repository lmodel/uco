---
type: Dataset
id: https://w3id.org/lmodel/uco/knowledge/datasets/test-data
genre: reference
title: Test data and tests
description: "The schema's tests: 228 valid examples under `tests/data/valid/`, 28 of them from UCO's own examples and 200 minimal ones written from the schema, 19 counter-examples, one per kind of constraint, the check that holds each fault of UCO's failing examples to the validator, and the tests of the watch, the copy and the adapt copy against nine released neighbours."
resource: tests
references:
  - https://w3id.org/lmodel/uco/knowledge/datasets/uco-linkml-schema
sources:
  - id: tests
    resource: tests
    title: the test files and the data folders
  - id: test_data.py
    resource: tests/test_data.py
    title: KINDS and UNSTATED
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: NEIGHBOURS, SHARED_KEYS and SHARED_CLASSES
generated:
  by: process:ktl-librarian
  at: "2026-10-31T10:47:15Z"
status: draft
---

# Test data and tests

`tests/data/valid/` holds 228 examples, at least one for each of the 221 classes a concept may name as its type. `scripts/uco_examples.py` writes them: 28 from nodes of UCO's own passing examples, and 200 minimal ones from the schema where no example holds the class. `tests/data/invalid/` holds 19 counter-examples, one per kind of constraint, each opening with a `# Fails at:` line.[^tests]

`tests/test_data.py` holds every example to the validator and to the generated JSON Schema file. Its `KINDS` table pairs each kind of constraint with its counter-example. Its `UNSTATED` table lists each fault of UCO's failing examples that LinkML does not state, with the reason. Every other fault must fail the validator at the slot UCO's report names.[^test_data.py]

`tests/test_upstream.py` holds the copy and the schema header to the watch's pins, `tests/test_watch.py` runs the watch against stubbed answers, and `tests/test_schema_is_generated.py` reruns the two scripts with `--check`. `tests/test_schema_rules.py` holds the adapt copy apart from LOKF and nine released neighbours' copies in `tests/neighbours/`, each pinned by its SHA-256, and lists the names it shares with them.[^test_schema_rules.py]

[^tests]: tests, the test files and the data folders
[^test_data.py]: tests/test_data.py, KINDS and UNSTATED
[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS, SHARED_KEYS and SHARED_CLASSES
