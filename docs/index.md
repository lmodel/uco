# uco

This project is a LinkML rendering of the [Unified Cyber Ontology (UCO)](https://unifiedcyberontology.org/) 1.5.0. The [schema pages](elements/index.md) describe each class, slot and vocabulary, under UCO's own names and IRIs.

## Validate data

Data in the schema's form is YAML or JSON. Each object gives its IRI as `id` and its class as `type`, by its compact URI (CURIE), and holds its facets in `hasFacet`:

```yaml
id: http://example.org/kb/file-1
type: uco-observable:File
hasFacet:
  - type: uco-observable:FileFacet
    fileName: report.pdf
    sizeInBytes: 2048
```

Validate one object against its class, or a whole document as a `UcoDocument`, whose `graph` lists UCO's things:

```bash
uv run linkml-validate -s src/uco/schema/uco.yaml -C File file.yaml
```

The validator applies every constraint the schema states. The generated Python and Pydantic models apply fewer. The JSON Schema in `project/jsonschema/` holds the same constraints for a tool without LinkML, and the tests hold every example to it.

## Read UCO's JSON-LD

`scripts/uco_examples.py` holds `Reader`, which turns a node of UCO's JSON-LD into the schema's form. It drops what the form has no key for, such as a facet's own IRI and an `rdfs:comment`, and refuses a node of two unrelated classes. [About](about.md) says where the schema's form differs from UCO's.
