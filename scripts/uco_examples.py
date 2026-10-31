#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["linkml-runtime>=1.12", "pyyaml>=6", "rdflib>=7"]
# ///
"""Write a valid example for each class a concept may name as its type.

A knowledge-bundle concept may name as its type any class that carries the
identifier ``id``: UcoObject, UcoType, Thread and ThreadItem, and every class
under them. For each such class, ``tests/data/valid/`` holds:

- the richest node of that class in each of UCO's ``*_PASS.json`` examples,
  copied under ``src/uco/schema/upstream/``, written in the schema's form
  (``Class-uco-<example>.yaml``);
- where no example has one, a minimal instance written from the schema: an
  IRI, the type and each required slot (``Class-001.yaml``).

The schema's form differs from UCO's JSON-LD in four ways. Keys are the
schema's slot names, not CURIEs. ``type`` names one class, the most specific
of a node's types. A facet or other value object sits inside the object that
holds it, without its IRI. A reference to an object is its IRI. A node that
cannot be written so is skipped, with the reason on standard error: two
types that name no one class, a class the schema does not have, or a blank
node where the schema needs an IRI.

Usage::

    uv run python scripts/uco_examples.py [--check]

``--check`` compares with ``tests/data/valid/`` instead of writing, and exits
1 when they differ. tests/test_data.py uses the ``Reader`` class to read
UCO's XFAIL examples the same way.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

import yaml
from linkml_runtime.utils.schemaview import SchemaView
from rdflib import BNode, Graph, Literal
from rdflib.namespace import RDF, XSD

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "src" / "uco" / "schema" / "uco.yaml"
EXAMPLES = ROOT / "src" / "uco" / "schema" / "upstream" / "tests" / "examples"
OUT = ROOT / "tests" / "data" / "valid"
KB = "http://example.org/kb/"

INTEGERS = {
    XSD.integer,
    XSD.int,
    XSD.long,
    XSD.short,
    XSD.byte,
    XSD.nonNegativeInteger,
    XSD.positiveInteger,
    XSD.unsignedInt,
    XSD.unsignedShort,
    XSD.unsignedLong,
}
NUMBERS = {XSD.decimal, XSD.double, XSD.float}

# A value for each kind of literal a minimal instance needs, by the LinkML
# type it ends at.
SAMPLES = {
    "string": "example",
    "integer": 1,
    "boolean": True,
    "decimal": 1.5,
    "float": 1.5,
    "double": 1.5,
    "datetime": "2026-01-01T00:00:00Z",
    "date": "2026-01-01",
    "uri": "http://example.org/",
    "uriorcurie": "http://example.org/",
    "uco_hex_binary": "00ff",
    "uco_base64_binary": "AA==",
    "uco_duration": "P1D",
}


class Skip(Exception):
    """A node the schema's form cannot hold."""


def kebab(name: str) -> str:
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", name).lower()


def sort_key(value) -> str:
    return json.dumps(value, sort_keys=True)


class Reader:
    """Reads UCO's JSON-LD into the schema's form."""

    def __init__(self, schema: Path = SCHEMA) -> None:
        self.view = SchemaView(str(schema))
        self.classes = self.view.all_classes()
        self.class_by_iri = {self.view.get_uri(c, expand=True): c for c in self.classes}
        self.slot_by_iri = {
            self.view.get_uri(s, expand=True): name
            for name, s in self.view.all_slots().items()
        }
        self._induced: dict[str, dict] = {}
        self._ancestors: dict[str, list[str]] = {}
        self.dropped: set[str] = set()

    def ancestors(self, cls: str) -> list[str]:
        if cls not in self._ancestors:
            self._ancestors[cls] = self.view.class_ancestors(cls)
        return self._ancestors[cls]

    def induced(self, cls: str) -> dict:
        if cls not in self._induced:
            self._induced[cls] = {s.name: s for s in self.view.class_induced_slots(cls)}
        return self._induced[cls]

    def has_id(self, cls: str) -> bool:
        return any("id" in (self.classes[a].slots or []) for a in self.ancestors(cls))

    def concept_types(self) -> list[str]:
        """The classes a concept may name as its type: those with an IRI."""
        return sorted(c for c in self.classes if self.has_id(c))

    def type_of(self, g: Graph, node) -> str:
        names = []
        for t in g.objects(node, RDF.type):
            name = self.class_by_iri.get(str(t))
            if name is None:
                raise Skip(f"it is typed {t}, which the schema does not define")
            names.append(name)
        if not names:
            raise Skip("it has no type")
        most = [n for n in set(names) if all(m in self.ancestors(n) for m in names)]
        if len(most) != 1:
            raise Skip(f"its types {sorted(set(names))} name no one class")
        return most[0]

    def instance(
        self,
        g: Graph,
        node,
        strict: bool = True,
        depth: int = 0,
        expected: str | None = None,
    ) -> dict:
        """One node in the schema's form. With strict off, as for UCO's XFAIL
        examples, what the schema cannot hold is kept so a validator can
        report it: a key the class does not have, a type the schema does not
        define in a slot whose range is known, and a missing IRI."""
        if depth > 8:
            raise Skip("its values nest more than eight deep")
        try:
            cls = self.type_of(g, node)
            type_value = self.view.get_uri(cls, expand=False)
        except Skip:
            if strict or expected is None:
                raise
            cls = expected
            type_value = min((str(t) for t in g.objects(node, RDF.type)), default=None)
        slots = self.induced(cls)
        out: dict = {}
        if "id" in slots:
            if isinstance(node, BNode):
                if strict:
                    raise Skip("it is a blank node, where the schema needs an IRI")
            else:
                out["id"] = str(node)
        if "type" in slots and type_value is not None:
            out["type"] = type_value
        values: dict[str, list] = defaultdict(list)
        for p, o in g.predicate_objects(node):
            if p == RDF.type:
                continue
            name = self.slot_by_iri.get(str(p))
            if name is None:
                # An annotation such as rdfs:comment, or a key whose prefix the
                # example's context leaves undeclared.
                self.dropped.add(str(p))
                continue
            if name not in slots:
                if strict:
                    raise Skip(f"it has {name}, which {cls} does not have")
                values[name].append(
                    str(o) if not isinstance(o, Literal) else self.literal(o)
                )
                continue
            values[name].append(self.value(g, o, slots[name], strict, depth))
        for name in sorted(values):
            vals = sorted(values[name], key=sort_key)
            multivalued = name in slots and slots[name].multivalued
            out[name] = vals if multivalued or len(vals) > 1 else vals[0]
        return out

    def literal(self, o: Literal):
        if o.datatype in INTEGERS:
            return int(o)
        if o.datatype in NUMBERS:
            return float(o)
        if o.datatype == XSD.boolean:
            return str(o).strip().lower() in ("true", "1")
        return str(o)

    def value(self, g: Graph, o, slot, strict: bool, depth: int):
        if isinstance(o, Literal):
            return self.literal(o)
        rng = slot.range
        if rng in self.classes:
            inline = slot.inlined if slot.inlined is not None else not self.has_id(rng)
            if inline:
                return self.instance(g, o, strict, depth + 1, expected=rng)
            if isinstance(o, BNode):
                raise Skip(
                    f"its {slot.name} is a blank node, where the schema needs an IRI"
                )
        return str(o)

    # -- minimal instances ------------------------------------------------------

    def sample(self, slot):
        """A value for a required slot that its constraints accept."""
        if slot.equals_string is not None:
            return slot.equals_string
        if slot.has_member is not None and slot.has_member.equals_string is not None:
            return [slot.has_member.equals_string]
        ranges = (
            [a.range for a in slot.any_of] if slot.any_of else [slot.range or "string"]
        )
        rng = ranges[0]
        if rng in self.classes:
            inline = slot.inlined if slot.inlined is not None else not self.has_id(rng)
            value = (
                self.minimal(rng, inline=inline) if inline else f"{KB}{kebab(rng)}-001"
            )
        elif rng in self.view.all_enums():
            value = next(iter(self.view.get_enum(rng).permissible_values))
        else:
            name = rng
            while name not in SAMPLES:
                name = self.view.get_type(name).typeof
            value = SAMPLES[name]
            if slot.minimum_value is not None and isinstance(value, int):
                value = max(value, int(slot.minimum_value))
        return [value] if slot.multivalued else value

    def minimal(self, cls: str, inline: bool = False) -> dict:
        slots = self.induced(cls)
        out: dict = {}
        if "id" in slots and not inline:
            out["id"] = f"{KB}{kebab(cls)}-001"
        if "type" in slots:
            out["type"] = self.view.get_uri(cls, expand=False)
        for name, slot in sorted(slots.items()):
            if name in ("id", "type") or not slot.required:
                continue
            out[name] = self.sample(slot)
        return out


def read(path: Path) -> Graph:
    """One of UCO's JSON-LD examples as a graph. An example names its prefixes
    in an inline context; a context given by address would be fetched, so it
    is refused."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data.get("@context"), dict):
        raise SystemExit(f"{path.name}: the context is not inline")
    return Graph().parse(data=json.dumps(data), format="json-ld")


def build(reader: Reader) -> tuple[dict[str, dict], list[str]]:
    """Every example file by name, and a note for each node left out."""
    concept = set(reader.concept_types())
    files: dict[str, dict] = {}
    notes: list[str] = []
    covered: set[str] = set()
    sources = sorted(EXAMPLES.glob("*_PASS.json")) + sorted(
        EXAMPLES.glob("technique/*_PASS.json")
    )
    for path in sources:
        g = read(path)
        reader.dropped = set()
        best: dict[str, tuple[int, str, dict]] = {}
        for node in sorted(set(g.subjects(RDF.type, None)), key=str):
            try:
                cls = reader.type_of(g, node)
                if cls not in concept:
                    continue
                inst = reader.instance(g, node)
            except Skip as reason:
                notes.append(f"{path.name}: left out {node}, since {reason}")
                continue
            size = len(sort_key(inst))
            if cls not in best or size > best[cls][0]:
                best[cls] = (size, str(node), inst)
        for key in sorted(reader.dropped):
            notes.append(
                f"{path.name}: dropped {key}, which the schema has no slot for"
            )
        stem = path.name.removesuffix("_PASS.json").replace("_", "-")
        for cls, (_, node, inst) in sorted(best.items()):
            files[f"{cls}-uco-{stem}.yaml"] = {
                "_comment": f"{node} in UCO's {path.name}.",
                **inst,
            }
            covered.add(cls)
    for cls in sorted(concept - covered):
        files[f"{cls}-001.yaml"] = {
            "_comment": "A minimal instance written from the schema: no UCO example has one.",
            **reader.minimal(cls),
        }
    return files, notes


class _Dumper(yaml.SafeDumper):
    def increase_indent(
        self, flow=False, indentless=False
    ):  # lists sit indented under their key
        return super().increase_indent(flow, False)


def dump(instance: dict) -> str:
    body = {k: v for k, v in instance.items() if k != "_comment"}
    text = yaml.dump(
        body,
        Dumper=_Dumper,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=100,
    )
    return f"# {instance['_comment']}\n{text}"


def write_all(files: dict[str, dict], out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    for name, instance in files.items():
        (out / name).write_text(dump(instance), encoding="utf-8")


def check(files: dict[str, dict], out: Path) -> int:
    """Compare a fresh writing with the folder; 0 when they agree."""
    with tempfile.TemporaryDirectory() as tmp:
        fresh = Path(tmp)
        write_all(files, fresh)
        status = 0
        present = {p.name for p in out.glob("*.yaml")}
        for name in sorted(present - set(files)):
            print(f"not written by the script: {out / name}")
            status = 1
        for name in sorted(files):
            new = (fresh / name).read_text(encoding="utf-8")
            old = (
                (out / name).read_text(encoding="utf-8")
                if (out / name).exists()
                else ""
            )
            if new != old:
                status = 1
                diff = difflib.unified_diff(
                    old.splitlines(),
                    new.splitlines(),
                    name,
                    "rewritten",
                    lineterm="",
                    n=1,
                )
                print("\n".join(list(diff)[:30]))
        return status


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="compare with tests/data/valid/ instead of writing",
    )
    args = parser.parse_args(argv)
    files, notes = build(Reader())
    for note in notes:
        print(f"note: {note}", file=sys.stderr)
    if args.check:
        return check(files, OUT)
    for stale in OUT.glob("*.yaml"):
        if stale.name not in files:
            stale.unlink()
    write_all(files, OUT)
    taken = sum(1 for name in files if "-uco-" in name)
    print(
        f"{len(files)} examples: {taken} from UCO's examples, {len(files) - taken} minimal",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
