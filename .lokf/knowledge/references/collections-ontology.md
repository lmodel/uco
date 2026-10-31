---
type: Reference
id: https://w3id.org/lmodel/uco/knowledge/references/collections-ontology
genre: reference
title: The Collections Ontology (CO)
description: The Collections Ontology (CO) 2.0, <http://purl.org/co/>, whose bag, list and item classes UCO's threads build on. The schema imports lmodel/collections' rendering of it, which keeps CO's IRIs, and NOTICE gives CO's licence position.
resource: https://github.com/collections-ontology/collections-ontology
sources:
  - id: notice
    resource: NOTICE
    title: lmodel/collections and the Collections Ontology
  - id: co.ttl
    resource: src/uco/schema/upstream/ontology/co/co.ttl
    title: UCO's shapes over CO
  - id: collections.yaml
    resource: src/uco/schema/collections/collections.yaml
    title: the header
generated:
  by: process:ktl-librarian
  at: "2026-10-31T23:09:51Z"
status: draft
---

# The Collections Ontology (CO)

The Collections Ontology, version 2.0, by Paolo Ciccarese and Silvio Peroni, defines bags, sets and lists of items, at <http://purl.org/co/>. Its repository states no licence of its own. NOTICE says that the Google Code archive gives the Apache License 2.0 for the project's code, CO's OWL file among it, and CC BY 3.0 for its other content, such as its wiki.[^notice]

UCO's `co.ttl` adds SHACL shapes over CO's terms, and UCO's thread is a CO bag whose items are CO items.[^co.ttl] The schema imports lmodel/collections' module for CO's terms. That module keeps CO's IRIs under the prefix `coll` and describes the terms in lmodel/collections' own words.[^collections.yaml]

[^notice]: NOTICE, lmodel/collections and the Collections Ontology
[^co.ttl]: src/uco/schema/upstream/ontology/co/co.ttl, UCO's shapes over CO
[^collections.yaml]: src/uco/schema/collections/collections.yaml, the header
