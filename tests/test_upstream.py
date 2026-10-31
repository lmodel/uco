"""Checks that the schema renders the UCO release its copy pins.

src/uco/schema/upstream/ holds the ontology files, the licence and the
examples that scripts/check_upstream_release.py pins. These tests read the
copy offline and hold it, and the schema header, to the pins.
"""

import importlib.util
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent.parent
COPY = ROOT / "src" / "uco" / "schema" / "upstream"
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"


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
