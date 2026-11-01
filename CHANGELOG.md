# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

## [0.2.0] - 2026-11-01

### Changed

- **The schema imports lmodel/collections v0.1.0 for the Collections Ontology (CO) terms UCO uses, in place of its own `uco_co` module.** Every CO term keeps its IRI, CO's `index` is now `co_index`, and the schema gains CO's `Collection`, `Set` and inverse slots. Threads keep UCO's rules: a thread names its items by IRI, and an item's content stays optional.

## [0.1.0] - 2026-10-31

### Added

- **A LinkML rendering of the Unified Cyber Ontology (UCO) 1.5.0**, written by `scripts/uco_to_linkml.py` from UCO's own Turtle files: one module per UCO namespace, one for the Collections Ontology terms UCO uses, and an umbrella. Every class, property and vocabulary keeps its UCO name and IRI, and each class's slots come from its SHACL shapes and its parents'.
- **A copy of UCO 1.5.0's ontology files, licence and examples, and a weekly upstream watch** that reports a new release or tag, a changed or dropped file and a changed licence.
- **Examples and counter-examples.** Each class a concept may name as its type has a valid example, written from UCO's own examples where they hold the class and from the schema where not. A counter-example breaks each kind of constraint, and a test holds each fault UCO's own failing examples name to the validator, or lists why LinkML cannot state it.
- **`.lokf/uco.yaml`, the schema's `lokf adapt` copy, rooted on the classes with an IRI**: UcoObject, UcoType, Thread and ThreadItem. The knowledge release attaches it as `schema-<tag>-uco.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.59.0 templates with the lokf floor at 0.9.0, and a knowledge website.
- **`.github/release/package-lock.json`, which pins semantic-release and every package it pulls in.** The release job installs from it with `npm ci`, and Dependabot keeps it current.

### Changed

- **One repository and one schema replace the sixteen uco-* repositories**, which modelled UCO 1.1.0 by hand. Each module keeps its old repository's identifier, such as `https://w3id.org/lmodel/uco-core`, and the umbrella `https://w3id.org/lmodel/uco` takes uco-master's place.
