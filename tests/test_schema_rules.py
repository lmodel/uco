"""Checks that the adapt copy can sit beside LOKF and the neighbours' copies.

`.lokf/uco.yaml` is the copy `lokf adapt` writes from the schema, and a host
imports it beside `lokf.yaml` and the copies other lmodel repositories
release. LinkML merges a host's imports into one namespace, where the last
definition of a name wins, and the JSON-LD context gives each key one IRI. So
a name the copy shares with another file must mean the same thing there, or
be listed here.
"""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
COPY = ROOT / ".lokf" / "uco.yaml"
LOKF = ROOT / ".lokf" / "lokf.yaml"
NEIGHBOUR_DIR = ROOT / "tests" / "neighbours"

# What a host may import beside this copy: LOKF's schema, pinned by the
# sidecar, and the adapt copies other lmodel repositories release. Each
# neighbour is the schema asset of a release, downloaded and checked against
# the release's .sha256 and its build-provenance attestation, and pinned here
# by that checksum.
NEIGHBOURS = {
    # lmodel/slsa v0.8.0, schema-v0.8.0-slsa.yaml
    "slsa.yaml": "16a3c50a4592dbeffeeee0e9d3d354efe71ae3efcc8eb272ed9b782117d8a024",
    # lmodel/github-actions v0.3.0, schema-v0.3.0-github-actions.yaml
    "github-actions.yaml": "52224e53939325f56d3470ed6ddd2041cdd53ae7cdb0ac72773829100798452e",
    # lmodel/oscal v0.1.2, schema-v0.1.2-oscal.yaml
    "oscal.yaml": "4eb56d7d1106463ed0a2255a29af14b8d619741acc29863d1e86eb3f8923c710",
    # lmodel/spdx v0.1.0, schema-v0.1.0-spdx.yaml
    "spdx.yaml": "3411cf5d19b1955f0362988c542984e4c817417c7b7b7892647aba1adf1ddd4a",
    # lmodel/nist-sp-800-218 v0.1.1, schema-v0.1.1-nist-sp-800-218.yaml
    "nist-sp-800-218.yaml": "479824cdd95e52226a35ff3a471b7ce93239635ccd5db7ac72a8143cdd1d8495",
    # lmodel/nist-sp-800-53 v0.1.0, schema-v0.1.0-nist-sp-800-53.yaml
    "nist-sp-800-53.yaml": "d32a989b5b855281cb45d707bf59cf52b125f05a09c54930e2b4d45c174c0d99",
    # lmodel/nist-sp-800-171 v0.1.0, schema-v0.1.0-nist-sp-800-171.yaml
    "nist-sp-800-171.yaml": "d204efa6653692da665f8604a8fb8bf445f04b37f41460a5ce2853a014b2982f",
    # lmodel/nist-csf-v2 v0.1.0, schema-v0.1.0-nist-csf-v2.yaml
    "nist-csf-v2.yaml": "5f6bba4c4721f65665c3a0a702ca6b15df5b488048fed454acfe4cc69f7ca9c7",
    # lmodel/in-toto v0.1.1, schema-v0.1.1-in-toto.yaml
    "in-toto.yaml": "feb2711d782643dfeb670648508540f29393c437aaceae5318849f62e8e14c6d",
}
# lmodel/collections v0.1.0, schema-v0.1.0-collections.yaml, the release
# whose module src/uco/schema/collections/ holds, checked the same way.
COLLECTIONS = {
    "collections.yaml": "11e3d604355eca5bba2e5ab4e21716566b9ac04d11b00ff4f097983c9c1c7d8a"
}
ELEMENT_KINDS = ("classes", "enums", "types", "subsets")

# Keys the copy shares with a neighbour, each under another IRI there. They
# are UCO's own property names, and `lokf adapt` renames only what lokf.yaml
# defines, so they stay until it can rename what a neighbour copy defines too
# (lokf #169). A host that imports this copy beside one of these neighbours
# projects each key under one vocabulary's IRI. A new overlap fails the test.
SHARED_KEYS = {name: set() for name in NEIGHBOURS}
SHARED_KEYS["in-toto.yaml"] = {"subject", "value"}
SHARED_KEYS["slsa.yaml"] = {"dependencies", "subject", "value"}
SHARED_KEYS["oscal.yaml"] = {
    "address", "country", "dependencies", "groups", "hashes", "number",
    "profile", "protocols", "remarks", "scheme", "state", "statement",
    "subject", "text", "value", "values",
}  # fmt: skip
SHARED_KEYS["spdx.yaml"] = {
    "comment", "contentType", "createdBy", "domain", "element", "endTime",
    "environment", "extension", "externalIdentifier", "hashValue", "key",
    "modifiedTime", "specVersion", "startTime", "statement", "subject", "value",
}  # fmt: skip

# Classes the copy and a neighbour both define, under UCO's names. The merged
# namespace keeps one class of each name, so a host cannot import this copy
# beside oscal's or spdx's until a copy renames them (lokf #169).
SHARED_CLASSES = {name: set() for name in NEIGHBOURS}
SHARED_CLASSES["oscal.yaml"] = {
    "Action", "Address", "Facet", "Hash", "Location", "Observation", "Profile",
}  # fmt: skip
SHARED_CLASSES["spdx.yaml"] = {
    "Annotation", "Bundle", "DictionaryEntry", "File", "Hash", "Relationship", "Tool",
}  # fmt: skip

# The classes `just lokf-adapt` re-roots on Concept: those that carry the
# identifier. Every class under them is a concept type too.
ROOTS = {"UcoObject", "UcoType", "Thread", "ThreadItem"}

# Every key whose value LinkML expands as a CURIE, and the mapping keys.
CURIE_KEYS = (
    "class_uri",
    "slot_uri",
    "enum_uri",
    "uri",
    "meaning",
    "mappings",
    "exact_mappings",
    "close_mappings",
    "related_mappings",
    "narrow_mappings",
    "broad_mappings",
)


def _names(path):
    """Each kind of element a schema file declares, and every slot and
    attribute name with the IRI it expands to."""
    doc = yaml.safe_load(path.read_text())
    prefixes = doc.get("prefixes") or {}

    def expand(curie):
        prefix, _, local = curie.partition(":")
        return prefixes[prefix] + local if prefix in prefixes else curie

    default = doc.get("default_prefix")
    elements = {kind: set(doc.get(kind) or {}) for kind in ELEMENT_KINDS}
    slots = {}
    owners = [doc.get("slots") or {}]
    owners += [
        (cls or {}).get("attributes") or {}
        for cls in (doc.get("classes") or {}).values()
    ]
    for owner in owners:
        for name, slot in owner.items():
            uri = (slot or {}).get("slot_uri") or f"{default}:{name}"
            slots.setdefault(name, set()).add(expand(uri))
    return elements, slots


def _curies(node):
    """Every value of a key that LinkML expands as a CURIE, anywhere in a
    parsed schema file."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in CURIE_KEYS and isinstance(value, (str, list)):
                yield from value if isinstance(value, list) else [value]
            else:
                yield from _curies(value)
    elif isinstance(node, list):
        for item in node:
            yield from _curies(item)


def test_neighbours_are_the_released_assets():
    """Each neighbour copy is byte for byte the asset its release published."""
    pinned = {**NEIGHBOURS, **COLLECTIONS}
    assert {p.name for p in NEIGHBOUR_DIR.iterdir()} == set(pinned)
    for name, sha256 in pinned.items():
        digest = hashlib.sha256((NEIGHBOUR_DIR / name).read_bytes()).hexdigest()
        assert digest == sha256, name


def test_names_apart_from_lokf():
    """No class, enum, type or subset name of the copy is LOKF's, and a slot
    name the two share carries LOKF's IRI: the copy renamed each name the
    two shared."""
    elements, slots = _names(COPY)
    their_elements, their_slots = _names(LOKF)
    for kind in ELEMENT_KINDS:
        assert not elements[kind] & their_elements[kind], kind
    for name in slots.keys() & their_slots.keys():
        assert slots[name] == their_slots[name], name


def test_names_apart_from_neighbours():
    """The only classes and keys the copy shares with a neighbour are the
    listed ones, and it shares no enum, type or subset name."""
    elements, slots = _names(COPY)
    for name in NEIGHBOURS:
        their_elements, their_slots = _names(NEIGHBOUR_DIR / name)
        assert (
            elements["classes"] & their_elements["classes"] == SHARED_CLASSES[name]
        ), name
        for kind in ("enums", "types", "subsets"):
            assert not elements[kind] & their_elements[kind], (name, kind)
        assert slots.keys() & their_slots.keys() == SHARED_KEYS[name], name


def test_the_copy_holds_collections_copy():
    """The copy holds lmodel/collections' module, so it holds every element
    and key of collections' own copy, each key with the same IRI, and a host
    imports this copy in place of both."""
    elements, slots = _names(COPY)
    their_elements, their_slots = _names(NEIGHBOUR_DIR / "collections.yaml")
    for kind in ELEMENT_KINDS:
        assert their_elements[kind] <= elements[kind], kind
    for name, iris in their_slots.items():
        assert slots.get(name) == iris, name


def test_copy_roots_the_concept_classes():
    """The copy re-roots exactly the classes with an IRI on Concept and imports
    nothing but the LinkML types and LOKF."""
    doc = yaml.safe_load(COPY.read_text())
    rooted = {
        name for name, cls in doc["classes"].items() if cls.get("is_a") == "Concept"
    }
    assert rooted == ROOTS
    assert doc["imports"] == ["linkml:types", "lokf"]


def test_curies_use_a_bound_prefix():
    """Every IRI the copy names is a CURIE whose prefix the copy binds. A full
    address that no prefix covers makes every `lokf convert --schema` over the
    copy warn that it has no namespace."""
    doc = yaml.safe_load(COPY.read_text())
    prefixes = doc.get("prefixes") or {}
    curies = list(_curies(doc))
    assert curies
    for curie in curies:
        prefix, sep, _ = curie.partition(":")
        assert sep and prefix in prefixes, curie


def test_no_prefix_is_bound_twice():
    """A prefix the copy binds means what lokf.yaml and each neighbour bind it
    to, so LinkML can merge the files in one composite."""
    ours = yaml.safe_load(COPY.read_text()).get("prefixes") or {}
    for other in (
        LOKF,
        *(NEIGHBOUR_DIR / name for name in {**NEIGHBOURS, **COLLECTIONS}),
    ):
        theirs = yaml.safe_load(other.read_text()).get("prefixes") or {}
        for prefix in ours.keys() & theirs.keys():
            assert ours[prefix] == theirs[prefix], (other.name, prefix)
