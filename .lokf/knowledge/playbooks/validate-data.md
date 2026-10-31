---
type: Playbook
id: https://w3id.org/lmodel/uco/knowledge/playbooks/validate-data
genre: how-to
title: Validate data against the schema
description: How to validate UCO data in the schema's form with `linkml-validate`, one object against its class or a whole document as a `UcoDocument`, and why the validator, not the generated Python models, is the check that applies every constraint.
resource: docs/index.md
sources:
  - id: index.md
    resource: docs/index.md
    title: Validate data
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# Validate data against the schema

1. Write the data in the schema's form: each object gives its IRI as `id` and its class as `type`, and holds its facets in `hasFacet`.[^index.md]
2. Validate one object against its class with `uv run linkml-validate -s src/uco/schema/uco.yaml -C File file.yaml`, or a whole document against `UcoDocument`.
3. Trust the validator's verdict. The generated Python and Pydantic models apply fewer of the constraints, and the JSON Schema in `project/jsonschema/` holds the same ones for a tool without LinkML.

[^index.md]: docs/index.md, Validate data
