"""Checks that the schema renders the UCO release its copy pins.

src/uco/schema/upstream/ holds the ontology files, the licence and the
examples that scripts/check_upstream_release.py pins. These tests read the
copy offline and hold it, and the schema header, to the pins.
"""

import importlib.util
import subprocess
from pathlib import Path

import yaml
from rdflib import Graph, URIRef

ROOT = Path(__file__).parent.parent
SCHEMA_DIR = ROOT / "src" / "uco" / "schema"
COPY = SCHEMA_DIR / "upstream"
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
MODULES = sorted(SCHEMA_DIR.glob("uco*.yaml"))


def _watch():
    spec = importlib.util.spec_from_file_location("watch_pins", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


WATCH = _watch()


def test_the_copy_is_the_pinned_files():
    """Every copied file is the blob the watch pins, and nothing else is there."""
    held = {
        p.relative_to(COPY).as_posix(): WATCH._blob_sha(p)
        for p in COPY.rglob("*")
        if p.is_file()
    }
    assert held == WATCH.PINNED_BLOBS


def test_the_watch_hashes_files_as_git_does():
    """The watch's hash is git's object hash, so it matches the trees API."""
    licence = COPY / "LICENSE"
    git = subprocess.run(
        ["git", "hash-object", str(licence)],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    assert WATCH._blob_sha(licence) == git == WATCH.PINNED_BLOBS["LICENSE"]


def test_the_copy_holds_every_namespace_of_the_master_ontology():
    """uco.ttl imports fifteen UCO namespaces, the Collections Ontology's
    supplement and the OWL shapes; the copy holds each file but the last,
    which the schema does not render."""
    master = (COPY / "ontology" / "uco" / "master" / "uco.ttl").read_text()
    imported = {
        line.split("/")[-2]
        for line in master.splitlines()
        if line.startswith("# imports: ")
    }
    held = {p.stem for p in (COPY / "ontology" / "uco").glob("*/*.ttl")} - {"uco"}
    held |= {p.stem for p in (COPY / "ontology" / "co").glob("*.ttl")}
    assert imported - held == {"owl"}
    assert held <= imported


def test_the_header_names_the_pinned_release():
    """Every module's version and source are the release the watch pins."""
    assert MODULES
    for module in MODULES:
        header = yaml.safe_load(module.read_text())
        assert header["version"] == WATCH.PINNED_TAG, module.name
        assert header["source"] == WATCH.PINNED_SOURCE, module.name
        assert header["license"] == WATCH.PINNED_LICENSE, module.name


def _iris(node, prefixes, out):
    """Every class_uri, slot_uri and enum_uri in a module, expanded."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in ("class_uri", "slot_uri", "enum_uri") and isinstance(value, str):
                prefix, _, local = value.partition(":")
                out.add(prefixes.get(prefix, prefix + ":") + local)
            else:
                _iris(value, prefixes, out)
    elif isinstance(node, list):
        for value in node:
            _iris(value, prefixes, out)
    return out


def test_every_iri_names_a_term_in_ucos_files():
    """Each class, slot and enum IRI from UCO's or CO's namespaces names a
    term the copied ontology files name, so no IRI is invented. The schema
    states no mappings, so none can name a term that does not exist."""
    graph = Graph()
    for path in sorted((COPY / "ontology").glob("*/*/*.ttl")) + [
        COPY / "ontology" / "co" / "co.ttl"
    ]:
        graph.parse(path)
    terms = {str(t) for triple in graph for t in triple if isinstance(t, URIRef)}
    for module in MODULES:
        doc = yaml.safe_load(module.read_text())
        assert not any(key.endswith("_mappings") for key in _keys(doc)), module.name
        for iri in _iris(doc, doc["prefixes"], set()):
            if iri.startswith(
                ("https://ontology.unifiedcyberontology.org/", "http://purl.org/co/")
            ):
                assert iri in terms, (module.name, iri)


def _keys(node):
    if isinstance(node, dict):
        for key, value in node.items():
            yield key
            yield from _keys(value)
    elif isinstance(node, list):
        for value in node:
            yield from _keys(value)
