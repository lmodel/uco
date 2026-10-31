---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/uco/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: uco Knowledge Bundle
description: Unified Cyber Ontology (UCO) 1.5.0 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/uco/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# uco Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for uco. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The Astro Starlight site in `website/`, for <https://lmodel.github.io/uco>: the README as its home page, the pages of `docs/`, a page per schema element, a page per concept of this bundle with its trust label, the bundle's exports, and redirects from the retired sites' element pages, built and published by Knowledge website.

# Playbooks

* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose.
* [Regenerate and test after a change](playbooks/regenerate-and-test.md) - How to change the schema and check it: `uv sync --group dev`, change the converter or the copy, run the converter and the examples writer, then `just gen-project`, `just gen-doc`, `just lokf-adapt`, `just lint` and `just test`, and the pre-commit hooks before a pull request.
* [Cut a release](playbooks/release.md) - How a release is made: Conventional Commits on `main`, an `## [Unreleased]` changelog section, the `v0.0.0` baseline tag that keeps the first release at 0.1.0, and `semantic-release.yml`, which tags the release and dispatches Knowledge Release to attach `schema-<tag>-uco.yaml` once `KNOWLEDGE_RELEASE_ENABLED` is true.
* [Update the upstream pins](playbooks/update-upstream-pins.md) - What to do when the weekly upstream watch reports a newer UCO release or tag, a moved tag, a changed or dropped copied file, a changed licence, or a check that could not finish: replace the copy whole from one release, move the pins, rerun the converter and the examples writer, and run the tests.
* [Validate data against the schema](playbooks/validate-data.md) - How to validate UCO data in the schema's form with `linkml-validate`, one object against its class or a whole document as a `UcoDocument`, and why the validator, not the generated Python models, is the check that applies every constraint.

# Datasets

* [UCO LinkML schema](datasets/uco-linkml-schema.md) - The LinkML schema of the Unified Cyber Ontology (UCO) 1.5.0, `src/uco/schema/uco.yaml` (schema id `https://w3id.org/lmodel/uco`) with fifteen modules, one per UCO namespace, written by a converter, and lmodel/collections' module for the Collections Ontology terms UCO uses. Its `lokf adapt` copy `.lokf/uco.yaml` is the bundle's domain schema.
* [The UCO 1.5.0 copy](datasets/uco-copy.md) - UCO's own files at release 1.5.0, 79 files copied into `src/uco/schema/upstream/` under UCO's paths: the seventeen Turtle files of the ontology, UCO's LICENSE, and the passing and failing examples with the SHACL reports on the failing ones. Each is matched to commit `7ebb3957e9e9` by git object hash.
* [Generated artefacts](datasets/generated-artefacts.md) - What the LinkML generators and `lokf adapt` write from the schema: `project/` (JSON Schema, OWL, SHACL, ShEx, JSON-LD, GraphQL, protobuf, SQL, TypeScript, Excel and 427 Java classes), the Python dataclasses and Pydantic models in `src/uco/datamodel/`, `docs/schema/`, and `.lokf/uco.yaml`. None is edited by hand.
* [Test data and tests](datasets/test-data.md) - The schema's tests: 228 valid examples under `tests/data/valid/`, 28 of them from UCO's own examples and 200 minimal ones written from the schema, 19 counter-examples, one per kind of constraint, the check that holds each fault of UCO's failing examples to the validator, and the tests of the watch, the copy and the adapt copy against nine released neighbours.
* [lmodel/collections module](datasets/collections-module.md) - The schema module of lmodel/collections that renders the Collections Ontology (CO) 2.0, copied unchanged into `src/uco/schema/collections/` from collections v0.1.0, held to its git object hash by `tests/test_collections_import.py`, and imported by `uco_types` and the umbrella for the CO terms UCO's threads build on.

# Tools

* [The UCO converter (uco_to_linkml.py)](tools/uco-to-linkml.md) - `scripts/uco_to_linkml.py`, the converter that writes every module of the schema from UCO's Turtle files: classes from OWL classes, slots from SHACL shapes and properties, enums from UCO's vocabularies, each keeping its UCO name and IRI. `--check` fails on a hand edit.
* [The examples writer (uco_examples.py)](tools/uco-examples.md) - `scripts/uco_examples.py`, which writes a valid example for each class a concept may name as its type: from nodes of UCO's own passing examples, turned from JSON-LD into the schema's form, and from the schema where no example holds the class. Its `Reader` also reads UCO's failing examples for the tests.
* [The upstream watch script (check_upstream_release.py)](tools/check-upstream-release.md) - `scripts/check_upstream_release.py`, the standard-library script the upstream watch runs: it asks the GitHub API about ucoProject/UCO and reports a newer release or tag, a moved tag, a changed or dropped copied file, a changed licence and a check that could not finish.

# References

* [The Unified Cyber Ontology (UCO)](references/unified-cyber-ontology.md) - The Unified Cyber Ontology (UCO), release 1.5.0 of July 24, 2026, at <https://github.com/ucoProject/UCO>: a community ontology for cyber-domain information in OWL and SHACL, in fifteen namespaces, which the schema renders.
* [The Collections Ontology (CO)](references/collections-ontology.md) - The Collections Ontology (CO) 2.0, <http://purl.org/co/>, whose bag, list and item classes UCO's threads build on. The schema imports lmodel/collections' rendering of it, which keeps CO's IRIs, and NOTICE gives CO's licence position.

# Explanations

* [Scope, influences and mappings](explanations/scope-and-influences.md) - What the schema renders and what it leaves out: UCO 1.5.0's fifteen namespaces, as a converter writes them, with lmodel/collections' schema imported for the CO terms, and lmodel/spdx's converter and lmodel/slsa's release and governance files as its influences. It maps to no other vocabulary, and leaves out SHACL advice, SPARQL constraints and what LinkML cannot state.
* [Element names and the shared namespace](explanations/element-names.md) - How the schema names its elements: UCO's own names and IRIs under UCO's prefixes, a namespace prefix on 20 properties UCO defines in two namespaces, lmodel/collections' `CoItem`, `co_size` and `co_index` for CO terms, and the renames `lokf adapt` makes beside LOKF. It also lists the class and key names the adapt copy shares with lmodel/oscal, spdx, slsa and in-toto.
* [The schema's form and UCO's JSON-LD](explanations/data-form.md) - Where data in the schema's form differs from UCO's JSON-LD: keys are slot names, `type` names one class, facets and other value objects sit inside their object without an IRI, a reference is an IRI, vocabularies are open, and a literal carries no datatype.

# Glossary

* [UcoThing](glossary/uco-thing.md) - In UCO, the top class of every individual: objects, facets, threads and thread items. The schema renders it as `UcoThing`, which carries the `type` designator.
* [UcoObject](glossary/uco-object.md) - In UCO, the base class of every object a graph names by IRI, such as a file, an account, a tool or an action. The schema renders it as `UcoObject`, one of the four classes its adapt copy roots on `Concept`.
* [Facet](glossary/facet.md) - In UCO, a group of properties that describe one aspect of an object, such as a file's name and size. The schema renders each facet as a value inside its object's `hasFacet` list.
* [ObservableObject](glossary/observable-object.md) - In UCO, an object of the digital domain that can be observed, such as a file, a device, an account or a network connection. The schema renders it as `ObservableObject`, with 95 direct subclasses.
* [Open vocabulary](glossary/open-vocabulary.md) - In UCO, a list of suggested string values for a property, such as the hash names MD5 and SHA256. The schema renders each as an enum, and a property that takes one also takes any string.

# Policies

* [Security policy](policies/security-policy.md) - How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the ruleset on `main`, and the two repository settings that are not yet in force.
* [AI covenant](policies/ai-covenant.md) - The repository's rules for work done with artificial intelligence (AI): you own what you submit, the schema is the converter's output and a rule cites the part of UCO's files it reads, the copy of UCO's files is never edited, and every element keeps UCO's IRI.
* [License and attribution](policies/license-and-attribution.md) - The repository's licences: Apache 2.0 for the schema and the code, the UCO Community's Apache 2.0 for the copy of UCO's files and the descriptions taken from it, Apache 2.0 for the copy of lmodel/collections' module, MIT for the copier template's scaffolding, Apache 2.0 for the KTL templates, and CC BY 4.0 for the knowledge bundle.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow, `.github/workflows/main.yaml`: on a push to main and on every pull request, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`, the check that `.lokf/uco.yaml` is current.
* [Lint & docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on a push to main, every pull request, a Monday 06:00 UTC schedule and by hand, four jobs run ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), and markdownlint, lychee and codespell over the Markdown.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request into main, its plan job checks that the commits, the changelog and the title would release; on a push to main, its release job in the release Environment tags vX.Y.Z, publishes the GitHub release and dispatches Knowledge Release.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its uco-copy job runs `scripts/check_upstream_release.py` against ucoProject/UCO, and on a finding opens or updates the issue titled Upstream watch: the Unified Cyber Ontology has changed.
* [Knowledge Librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: every Monday at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is true, it runs an agent with the ktl-librarian skill (pinned by `TRUST_LADDER_SKILLS_REF` at v0.59.0) in a read-only job and opens a review pull request from a separate job that runs no agent.
* [Knowledge Registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: the gate on the knowledge bundle, run on pull requests that touch `.lokf/` or `knowledge_bundle/`, every Monday at 06:00 UTC and by hand; it validates the bundle and its relation targets against the domain schema, runs the conventions script, and checks that each new confirmation by a person is backed by an approval or a signed commit.
* [Knowledge Release (knowledge-release.yaml)](workflows/knowledge-release.md) - The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: dispatched with a release's tag, or started by a published release once `KNOWLEDGE_RELEASE_ENABLED` is true, it attaches the bundle zip, the domain schema as `schema-<tag>-uco.yaml` with its checksum, and the Copilot skills to the release, when the bundle or the schema changed or `force` is set.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: every Monday at 04:10 UTC and by hand, it moves the sidecar's copies and the skills pin to the newest Knowledge Trust Ladder release through one pull request, opened with the `KNOWLEDGE_SYNC_TOKEN` secret, and holds the workflow changes for a person to approve.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true.
