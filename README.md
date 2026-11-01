<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# uco

Unified Cyber Ontology (UCO) 1.5.0 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/uco](https://lmodel.github.io/uco)

## What it models

The schema renders the [Unified Cyber Ontology (UCO)](https://unifiedcyberontology.org/) at release [1.5.0](https://github.com/ucoProject/UCO/releases/tag/1.5.0) as one module for each of UCO's fifteen namespaces, such as `uco_core` and `uco_observable`, under the umbrella `uco.yaml`. The Collections Ontology (CO) terms UCO uses come from [lmodel/collections](https://github.com/lmodel/collections) at release [v0.1.0](https://github.com/lmodel/collections/releases/tag/v0.1.0), copied unchanged.

`scripts/uco_to_linkml.py` writes every module from a copy of UCO's Turtle files in [src/uco/schema/upstream/](src/uco/schema/upstream). Every class, property and vocabulary keeps its UCO name and Internationalized Resource Identifier (IRI) under UCO's own prefixes, such as `uco-core:UcoObject`. A weekly workflow opens an issue when UCO releases or tags a newer version, or when the copy differs.

Data in the schema's form keeps UCO's keys, gives each object its IRI as `id` and its class as `type`, and holds facets inside the object they describe. `scripts/uco_examples.py` writes UCO's own examples that way into [tests/data/valid/](tests/data/valid).

The schema replaces the sixteen uco-* repositories, which modelled UCO 1.1.0 by hand. Its identifier, `https://w3id.org/lmodel/uco`, takes uco-master's place.

## Mappings

None: each element is UCO's or CO's own term under its own IRI.

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

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/uco.yaml`, is the copy `just lokf-adapt` writes from `src/uco/schema/uco.yaml`, and `just lokf-adapt-check` says when it is stale. Change the converter, never the copy. A release carries the copy as `schema-<tag>-uco.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots the four classes with an IRI on `Concept`: UcoObject, UcoType, Thread and ThreadItem. A concept may name any of the 221 classes at or under them as its `type`, and [tests/data/valid/](tests/data/valid) holds an example of each. In Obsidian, add the ones a bundle uses to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins, for example:

```text
UcoObject, Identity, UcoPerson, UcoOrganization, UcoRole, Location, Tool, AnalyticTool, ConfiguredTool, DefensiveTool, MaliciousTool, Software, ConfiguredSoftware, File, Device, Computer, Account, DigitalAccount, Action, Observation, Event, Relationship, Annotation, Bundle, Grouping, Technique
```

In the copy, LOKF's `id` and `type` replace the schema's own, so an inlined facet names its class as `type: FileFacet` rather than by a compact URI (CURIE). Facets and UCO's other value classes stay inside the concept that holds them.

The copy renames each name LOKF also defines and keeps its UCO IRI: the classes `Organization`, `Person` and `Role` become `UcoOrganization`, `UcoPerson` and `UcoRole`, and 17 keys take a `uco_` prefix, such as `uco_name` and `uco_description`. Several classes are oscal's or spdx's too, such as `Hash`, so a host cannot import this copy beside oscal's or spdx's until one copy renames them. `tests/test_schema_rules.py` lists every shared class and key and fails on a new one, and [lokf #169](https://github.com/nicholsn/lokf/issues/169) asks `adapt` for a `--beside` option to rename them.

The copy holds lmodel/collections' module, so a host imports this copy in place of collections' own.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

UCO's files are the UCO Community's, under the Apache License 2.0, and the descriptions of UCO's terms are its texts. The descriptions of CO's terms are lmodel/collections' own words. [NOTICE](NOTICE) gives the details. This is not an official UCO release, and its use implies no endorsement by the UCO Community.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
