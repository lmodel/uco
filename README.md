<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# uco

Unified Cyber Ontology (UCO) 1.5.0 (LinkML)

> **Two ways in.** This README is one; the other is a docent, a museum's name
> for a guide. Install
> [`ktl-docent`](https://github.com/noelmcloughlin/knowledge-trust-ladder) into
> whatever agent you already use, by a route from
> [the install page](https://w3id.org/ktl/docs/install/), and ask it anything
> about this project. It answers from `.lokf/knowledge/`,
> the checked part of what the project knows, and says how far each answer has
> been trusted (still a draft, checked by automation only, or confirmed by a
> named person). It opens the source for exact values, and records what it
> could not answer so the gap gets filled. The same docent serves a person at a
> prompt, an agent reading this file, or a chatbot that can load a skill.
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt`
> says how to weigh it.

## Documentation Website

[https://lmodel.github.io/uco](https://lmodel.github.io/uco)

## What it models

The schema renders the [Unified Cyber Ontology (UCO)](https://unifiedcyberontology.org/) at release [1.5.0](https://github.com/ucoProject/UCO/releases/tag/1.5.0) as one module for each of UCO's fifteen namespaces and the umbrella `uco.yaml`. The Collections Ontology (CO) terms UCO uses come from [lmodel/collections](https://github.com/lmodel/collections).

* **Core** (`uco_core`): UcoThing and UcoObject, facets, relationships, annotations, bundles and other compilations, events and external references.
* **Observable** (`uco_observable`): observable objects such as files, accounts, devices, processes, network connections and messages, and the facets that describe them.
* **Action**, **Analysis**, **Pattern** (`uco_action`, `uco_analysis`, `uco_pattern`): actions and their lifecycles, analyses and patterns.
* **Identity**, **Location**, **Role**, **Victim** (`uco_identity`, `uco_location`, `uco_role`, `uco_victim`): people and organisations, places, and the roles they play.
* **Tool**, **Configuration** (`uco_tool`, `uco_configuration`): tools and their configurations.
* **Marking** (`uco_marking`): data markings, such as licence and terms-of-use statements.
* **Types**, **Time**, **Vocabulary** (`uco_types`, `uco_time`, `uco_vocabulary`): dictionaries, hashes and threads, UCO's datatypes, and its 44 open vocabularies as enums.
* **Collections** (`collections/collections`): lmodel/collections' schema at release [v0.1.0](https://github.com/lmodel/collections/releases/tag/v0.1.0), copied unchanged. It renders CO 2.0's collection, set, bag, list and item classes, under CO's names and IRIs, and UCO's threads build on its bag and item.

`scripts/uco_to_linkml.py` writes every module from a copy of UCO's Turtle files in [src/uco/schema/upstream/](src/uco/schema/upstream). Every class, property and vocabulary keeps its UCO name and Internationalized Resource Identifier (IRI) under UCO's own prefixes, such as `uco-core:UcoObject`. Each class's slots come from its SHACL shapes and its parents'. The schema's `version` is 1.5.0, and release tags number the schema's own versions. A weekly workflow opens an issue when UCO releases or tags a newer version, or when the copy differs.

Data in the schema's form keeps UCO's keys, gives each object its IRI as `id` and its class as `type`, and holds facets inside the object they describe. `scripts/uco_examples.py` writes UCO's own examples that way into [tests/data/valid/](tests/data/valid).

The schema replaces the sixteen uco-* repositories, which modelled UCO 1.1.0 by hand. Each UCO module keeps its old repository's identifier, such as `https://w3id.org/lmodel/uco-core`, and the umbrella's identifier, `https://w3id.org/lmodel/uco`, takes uco-master's place. The CO terms of uco-co are lmodel/collections' now.

## Influences

None beyond UCO 1.5.0 and lmodel/collections, whose schema it imports for CO's terms. Its converter follows [lmodel/spdx](https://github.com/lmodel/spdx)'s, and its release asset and governance files follow [lmodel/slsa](https://github.com/lmodel/slsa).

## Mappings

None: each element is UCO's or CO's own term under its own IRI, and no element names a term of another vocabulary.

## Not modelled here

The converter leaves out what LinkML cannot state, and prints a note for each:

* SHACL shapes of severity Info or Warning, which are advice;
* SPARQL constraints, `sh:not` and `sh:xone`, and shapes on a property's objects;
* UCO's rule that `hasFacet` is inverse functional, so that a facet belongs to one object only;
* shapes over a path of more than one property;
* UCO's rule that a UcoThing is never a blank node, since a facet here is a value inside its object.

UCO's `owl.ttl`, which holds shapes over OWL itself, is not rendered. `tests/test_data.py` holds each fault of UCO's own failing examples to the validator, and lists the faults LinkML cannot state with the reason. [docs/about.md](docs/about.md) says where the schema's form differs from UCO's JSON-LD.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the converter, the examples writer and the upstream watch
* [src/uco/schema/](src/uco/schema): the LinkML modules, as the converter writes them (do not edit them), and UCO's files in [upstream/](src/uco/schema/upstream)
* [src/uco/datamodel/](src/uco/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle, written in the Linked Open Knowledge Format (LOKF). Its domain schema is `.lokf/uco.yaml`, which `lokf adapt` writes from `src/uco/schema/uco.yaml`. Change the converter, never the copy. A release carries the copy as `schema-<tag>-uco.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

`just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. The copy roots the four classes with an IRI on `Concept`: UcoObject, UcoType, Thread and ThreadItem. A concept may name any of the 221 classes at or under them as its `type`, and [tests/data/valid/](tests/data/valid) holds an example of each. In Obsidian, add the ones a bundle uses to the KTL Registrar and KTL Curator plugins' *Known LOKF types* setting, for example:

```text
UcoObject, Identity, UcoPerson, UcoOrganization, UcoRole, Location, Tool, AnalyticTool, ConfiguredTool, DefensiveTool, MaliciousTool, Software, ConfiguredSoftware, File, Device, Computer, Account, DigitalAccount, Action, Observation, Event, Relationship, Annotation, Bundle, Grouping, Technique
```

In the copy, LOKF's `id` and `type` replace the schema's own, so an inlined facet names its class as `type: FileFacet` rather than by a compact URI (CURIE). Facets and UCO's other value classes stay inside the concept that holds them.

A host imports the copy beside `lokf.yaml`, and LinkML merges the two into one namespace, where the last definition of a name wins silently. So the copy renames each name LOKF also defines and keeps its UCO IRI: the classes `Organization`, `Person` and `Role` become `UcoOrganization`, `UcoPerson` and `UcoRole`, and 17 keys take a `uco_` prefix, such as `uco_name` and `uco_description`.

Other names are UCO's and also a neighbour copy's, under another IRI there. The classes `Action`, `Address`, `Facet`, `Hash`, `Location`, `Observation` and `Profile` are oscal's too, and `Annotation`, `Bundle`, `DictionaryEntry`, `File`, `Hash`, `Relationship` and `Tool` are spdx's, so a host cannot import this copy beside oscal's or spdx's until one copy renames them. Sixteen keys are oscal's too, seventeen spdx's, three slsa's (`dependencies`, `subject`, `value`) and two in-toto's (`subject`, `value`). [lokf #169](https://github.com/nicholsn/lokf/issues/169) asks `adapt` for a `--beside` option to rename them. `tests/test_schema_rules.py` lists every shared name, checks the copy against LOKF and nine released neighbours, and fails on a new one.

The copy holds lmodel/collections' module, so it holds every class and key of collections' own copy, `schema-v0.1.0-collections.yaml`, under the same IRIs. A host imports this copy in place of both.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)).

UCO's files in [src/uco/schema/upstream/](src/uco/schema/upstream) are the UCO Community's, under the Apache License 2.0, and the descriptions of UCO's terms are its texts. The copy of lmodel/collections' schema in [src/uco/schema/collections/](src/uco/schema/collections) is under the Apache License 2.0, and its descriptions of CO's terms are lmodel/collections' own words: see [NOTICE](NOTICE). The knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), as its `index.md` declares.

This is not an official UCO release, and its use implies no endorsement by the UCO Community.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
