---
type: Dataset
id: https://w3id.org/lmodel/uco/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What the LinkML generators and `lokf adapt` write from the schema: `project/` (JSON Schema, OWL, SHACL, ShEx, JSON-LD, GraphQL, protobuf, SQL, TypeScript, Excel and 425 Java classes), the Python dataclasses and Pydantic models in `src/uco/datamodel/`, `docs/schema/`, and `.lokf/uco.yaml`. None is edited by hand."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/uco/knowledge/datasets/uco-linkml-schema
sources:
  - id: justfile
    resource: justfile
    title: the gen-project, gen-python and gen-doc recipes
  - id: generators.yaml
    resource: .linkml/generators.yaml
    title: the generator_args
  - id: project
    resource: project
    title: the folders
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# Generated artefacts

`just gen-project` runs LinkML's generators over the umbrella schema with the settings in `.linkml/generators.yaml`, moves the Python dataclasses into `src/uco/datamodel/`, writes the Pydantic models beside them, and runs `gen-java`.[^justfile] The JSON Schema generator lists each range's subclasses, so data of a real class validates against the file.[^generators.yaml]

`project/` holds the output: JSON Schema, OWL, SHACL, ShEx, the JSON-LD context and document, GraphQL, protobuf, SQL, TypeScript, an Excel workbook, a prefix map and a Java class per schema class.[^project] `just gen-doc` writes `docs/schema/uco.yaml`, the merged schema, and the element pages under `docs/elements/`, which git ignores. `just lokf-adapt` writes `.lokf/uco.yaml`. A schema change reruns all three, and the pre-commit hooks leave the output alone.

[^justfile]: justfile, the gen-project, gen-python and gen-doc recipes
[^generators.yaml]: .linkml/generators.yaml, the generator_args
[^project]: project, the folders
