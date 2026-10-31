# Change Log

## 2026-10-31

* **Changed**: The Unified Cyber Ontology (UCO), its footnote's address in angle brackets, as Markdown linters ask.
* **Added**: Knowledge sources map, the librarian's scrape map, from the repository's tree.
* **Added**: UCO LinkML schema, from `src/uco/schema/uco.yaml`.
* **Added**: The UCO 1.5.0 copy, from `src/uco/schema/upstream`.
* **Added**: Generated artefacts, from `project`.
* **Added**: Test data and tests, from `tests`.
* **Added**: The UCO converter (uco_to_linkml.py), from `scripts/uco_to_linkml.py`.
* **Added**: The examples writer (uco_examples.py), from `scripts/uco_examples.py`.
* **Added**: The upstream watch script (check_upstream_release.py), from `scripts/check_upstream_release.py`.
* **Added**: The Unified Cyber Ontology (UCO), from <https://github.com/ucoProject/UCO/releases/tag/1.5.0>.
* **Added**: The Collections Ontology (CO), from <https://github.com/collections-ontology/collections-ontology>.
* **Added**: Scope, influences and mappings, from `README.md`.
* **Added**: Element names and the shared namespace, from `src/uco/schema/uco.yaml`.
* **Added**: The schema's form and UCO's JSON-LD, from `docs/about.md`.
* **Added**: UcoThing, from `src/uco/schema/uco_core.yaml`.
* **Added**: UcoObject, from `src/uco/schema/uco_core.yaml`.
* **Added**: Facet, from `src/uco/schema/uco_core.yaml`.
* **Added**: ObservableObject, from `src/uco/schema/uco_observable.yaml`.
* **Added**: Open vocabulary, from `src/uco/schema/uco_vocabulary.yaml`.
* **Added**: Regenerate and test after a change, from `CONTRIBUTING.md`.
* **Added**: Cut a release, from `CONTRIBUTING.md`.
* **Added**: Update the upstream pins, from `scripts/check_upstream_release.py`.
* **Added**: Validate data against the schema, from `docs/index.md`.
* **Added**: Security policy, from `SECURITY.md`.
* **Added**: AI covenant, from `AI_COVENANT.md`.
* **Added**: License and attribution, from `NOTICE`.
* **Added**: Documentation site, from `website`.
* **Added**: Build and test (main.yaml), from `.github/workflows/main.yaml`.
* **Added**: Lint & docs (lint-and-docs.yaml), from `.github/workflows/lint-and-docs.yaml`.
* **Added**: Semantic release (semantic-release.yml), from `.github/workflows/semantic-release.yml`.
* **Added**: Upstream watch (upstream-watch.yaml), from `.github/workflows/upstream-watch.yaml`.
* **Added**: Knowledge Librarian (knowledge-librarian.yaml), from `.github/workflows/knowledge-librarian.yaml`.
* **Added**: Knowledge Registrar (knowledge-registrar.yaml), from `.github/workflows/knowledge-registrar.yaml`.
* **Added**: Knowledge Release (knowledge-release.yaml), from `.github/workflows/knowledge-release.yaml`.
* **Added**: Knowledge sync (knowledge-sync.yaml), from `.github/workflows/knowledge-sync.yaml`.
* **Added**: Knowledge website (knowledge-website.yaml), from `.github/workflows/knowledge-website.yaml`.
* **Removal**: Example Service A, the sidecar's placeholder, now that real concepts stand in its place.
* **Removal**: Example Service B, the sidecar's placeholder, now that real concepts stand in its place.
* **Question**: Security policy, whether the ruleset on main that SECURITY.md names is in force; the repository did not exist yet to read it from.
* **Initialization**: Scaffolded the LOKF bundle for uco with placeholder
  services. Real concepts to follow.
