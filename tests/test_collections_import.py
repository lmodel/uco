"""Checks the vendored copy of lmodel/collections' schema.

src/uco/schema/collections/ holds lmodel/collections' schema module, copied
unchanged. It renders the Collections Ontology (CO) 2.0 with CO's names and
IRIs. UCO's thread is a CO bag and its thread item a CO item, and the modules
whose UCO files import UCO's co.ttl import this module.
"""

import hashlib
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView

SCHEMA_DIR = Path(__file__).parent.parent / "src" / "uco" / "schema"
COPY = SCHEMA_DIR / "collections"

# The commit of the lmodel/collections release the copy equals, v0.1.0, and
# the git object hash of its module there, src/collections/schema/
# collections.yaml. Move them with the copy, from a later release of
# lmodel/collections.
COLLECTIONS_COMMIT = "a55334d11fdff610988c1c1776fcc3055295d74d"
PINNED_BLOBS = {
    "collections.yaml": "dacb48cf872558947109c26b34913e86415a11a0",
}

CO = "http://purl.org/co/"

# Every CO class and slot the schema held before it imported
# lmodel/collections, when its own uco_co module rendered them, with its IRI.
# The IRIs are unchanged. One name changed: CO's index is co_index, as
# lmodel/collections names it.
CO_TERMS_BEFORE = {
    "classes": {
        "Bag": CO + "Bag",
        "CoItem": CO + "Item",
        "List": CO + "List",
        "ListItem": CO + "ListItem",
    },
    "slots": {
        "co_size": CO + "size",
        "element": CO + "element",
        "firstItem": CO + "firstItem",
        "followedBy": CO + "followedBy",
        "co_index": CO + "index",
        "item": CO + "item",
        "itemContent": CO + "itemContent",
        "lastItem": CO + "lastItem",
        "nextItem": CO + "nextItem",
        "precededBy": CO + "precededBy",
        "previousItem": CO + "previousItem",
    },
}


def _blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def test_the_module_is_the_pinned_file():
    """The vendored module is byte for byte the pinned one."""
    found = {name: _blob_sha(COPY / name) for name in PINNED_BLOBS}
    assert found == PINNED_BLOBS


def test_the_copy_holds_only_the_pinned_module():
    """Nothing else sits beside the module, so nothing unpinned is imported."""
    assert sorted(p.name for p in COPY.iterdir()) == sorted(PINNED_BLOBS)


def test_no_module_of_its_own_renders_co():
    """The converter writes no CO module: the schema's CO terms are the
    vendored module's alone."""
    assert not (SCHEMA_DIR / "uco_co.yaml").exists()


def test_co_terms_keep_their_iris():
    """Each CO class and slot the schema held before keeps its IRI, and is
    declared by the vendored module."""
    view = SchemaView(str(SCHEMA_DIR / "uco.yaml"))
    source = "https://w3id.org/lmodel/collections"
    for name, iri in CO_TERMS_BEFORE["classes"].items():
        cls = view.get_class(name)
        assert cls is not None, name
        assert view.get_uri(cls, expand=True) == iri, name
        assert cls.from_schema == source, name
    for name, iri in CO_TERMS_BEFORE["slots"].items():
        slot = view.get_slot(name)
        assert slot is not None, name
        assert view.get_uri(slot, expand=True) == iri, name
        assert slot.from_schema == source, name


def test_threads_keep_what_uco_says():
    """UCO's thread names its items by IRI, where lmodel/collections inlines
    a bag's items, and a thread item need not wrap anything, where
    lmodel/collections requires an item's content."""
    view = SchemaView(str(SCHEMA_DIR / "uco.yaml"))
    for slot in ("item", "threadOriginItem", "threadTerminalItem"):
        induced = view.induced_slot(slot, "Thread")
        assert induced.range == "ThreadItem", slot
        assert not induced.inlined, slot
        assert not induced.inlined_as_list, slot
    content = view.induced_slot("itemContent", "ThreadItem")
    assert content.range == "UcoObject"
    assert not content.required
    assert view.induced_slot("itemContent", "CoItem").required
