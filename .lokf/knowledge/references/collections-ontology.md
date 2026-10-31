---
type: Reference
id: https://w3id.org/lmodel/uco/knowledge/references/collections-ontology
genre: reference
title: The Collections Ontology (CO)
description: The Collections Ontology (CO) 2.0, <http://purl.org/co/>, whose bag, list and item classes UCO's threads build on. Its files state no licence, so the schema's `uco_co` module renders the terms UCO's files use with descriptions of its own.
resource: https://github.com/collections-ontology/collections-ontology
sources:
  - id: notice
    resource: NOTICE
    title: The Collections Ontology
  - id: co.ttl
    resource: src/uco/schema/upstream/ontology/co/co.ttl
    title: UCO's shapes over CO
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# The Collections Ontology (CO)

The Collections Ontology, version 2.0, by Paolo Ciccarese and Silvio Peroni, defines bags, sets and lists of items, at <http://purl.org/co/>. Its OWL file and repository state no licence, so the schema copies none of its text.[^notice]

UCO's `co.ttl` adds SHACL shapes over CO's terms, and UCO's thread is a CO bag whose items are CO items.[^co.ttl] The `uco_co` module renders the CO classes and properties UCO's files use, with CO's IRIs under the prefix `coll`, and describes them in its own words.

[^notice]: NOTICE, The Collections Ontology
[^co.ttl]: src/uco/schema/upstream/ontology/co/co.ttl, UCO's shapes over CO
