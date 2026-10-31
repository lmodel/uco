#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6", "rdflib>=7"]
# ///
"""Render the Unified Cyber Ontology's OWL and SHACL in Turtle as LinkML modules.

The script reads UCO's files, copied under ``src/uco/schema/upstream/``, and
writes into ``src/uco/schema/`` one LinkML module per UCO namespace, one for
the Collections Ontology (CO) terms UCO uses, and the umbrella ``uco.yaml``.
Every YAML file in that folder is its output: change the script, or the copy,
and run it again.

Usage::

    uv run python scripts/uco_to_linkml.py [--upstream DIR] [-d OUTPUT_DIR] [--check]

``--check`` writes to a temporary folder and exits 1 when the result differs
from what the output folder holds, so a test can tell a hand edit from a
regeneration. Either way, the script prints a note on standard error for each
part of the ontology it leaves out, renames or moves.

The rules, each applied the same way to every element:

- Names and IRIs are UCO's. An ``owl:Class`` is a class, an ``owl:*Property``
  a top-level slot, and an ``rdfs:Datatype`` with an ``owl:oneOf`` list an
  enum. Each keeps its local name, and its IRI as a CURIE under UCO's own
  prefix for its namespace (``uco-core:UcoObject``). A property a shape names
  but no file declares (``uco-observable:eventID``) is a slot too.
- A local name UCO defines in more than one namespace keeps its bare form in
  the namespace that comes first in the modules' import order (the umbrella
  imports them in that order); each other one takes its namespace and an
  underscore as a prefix (``observable_endTime``).
- The Collections Ontology (CO) terms UCO's files name keep CO's IRIs, under
  Bioregistry's prefix ``coll``. One whose local name UCO also defines takes
  ``Co`` or ``co_`` (``CoItem``). CO states no licence, so their descriptions
  are this project's own, and each CO property with a domain in CO's own
  ontology is a slot of that class.
- ``rdfs:subClassOf`` gives ``is_a``. Where a class has more than one parent,
  a parent that is an ancestor of another is dropped; ``is_a`` is the UCO
  parent with the most ancestors, a tie going to the class's own namespace,
  and each other parent is a mixin.
- A class's SHACL property shapes, and those of the shapes that target it,
  give its slots. ``sh:class`` or ``sh:datatype`` is the range, ``sh:or`` over
  datatypes a union, and ``sh:in`` the vocabulary enum with the same values.
  ``sh:minCount 1`` is ``required``, ``sh:maxCount 1`` a single value and
  ``sh:maxCount 0`` a slot the class has ``none_of``. ``sh:hasValue`` on a
  literal is ``equals_string``, or ``has_member`` on a multivalued slot. A
  shape that targets the subjects of a property constrains the slot wherever
  it is used. With no range from a shape, the property's ``rdfs:range`` gives
  it: a union of a vocabulary and ``xsd:string`` is the vocabulary's enum or
  any string, as UCO 1.4.0 made its vocabularies open, and a datatype
  restriction adds its bounds. A ``sh:datatype`` that names a class
  (``uco-pattern:PatternExpression``) types a string.
- SHACL applies a class's shapes to its subclasses too, so each class's slot
  is the conjunction of its own shapes and its parents'. The slot carries
  what every class agrees on, and a class has ``slot_usage`` where its
  conjunction differs. LinkML reads a false boolean in a ``slot_usage`` as
  unset, so a class that holds one value of a slot its parent holds many of
  keeps the list and holds at most one item.
- A property no class shape names is a slot of its ``rdfs:domain``, or of its
  super-property's; with neither, it is a slot no class lists.
- A shape of severity ``sh:Info`` or ``sh:Warning`` is advice, not a
  constraint, and is left out; so are SPARQL constraints, ``sh:not``,
  ``sh:xone``, paths of more than one property, and deactivated shapes.
- Every UcoThing has an IRI. The identifier ``id`` is a slot of
  ``UcoObject``, of each other class directly under ``UcoThing`` except
  ``UcoInherentCharacterizationThing`` (``Thread`` and ``ThreadItem``), and of
  ``UcoType``, whose instances are classes. A slot ranged over a class with
  the identifier holds an IRI; one ranged over a class without it, such as a
  facet, holds the object inlined.
- ``type``, the ``rdf:type`` designator, is a slot of ``UcoThing`` and
  ``UcoType``. Its value is the class's CURIE, so an inlined facet says which
  facet it is and RDF written from the data types each object.
- Each module imports the modules its UCO file imports. An element a module
  needs from one it does not import is declared in it instead, keeping its
  IRI, and a disjointness goes on the class whose module sees both.
- XSD datatypes become LinkML types: the built-in ones where they match,
  else a ``uco_`` type in the core module with XSD's bounds or pattern. The
  CO module, which imports no other, bounds its integers on the slot.
"""

from __future__ import annotations

import argparse
import difflib
import sys
import tempfile
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from rdflib import BNode, Graph, Literal, URIRef
from rdflib.collection import Collection
from rdflib.namespace import OWL, RDF, RDFS, SH, XSD

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_UPSTREAM = ROOT / "src" / "uco" / "schema" / "upstream"
DEFAULT_OUT = ROOT / "src" / "uco" / "schema"

UCO_ROOT = "https://ontology.unifiedcyberontology.org/"
UCO_NS = UCO_ROOT + "uco/"
CO_NS = "http://purl.org/co/"
SCHEMA_ID = "https://w3id.org/lmodel/uco"
OWN_PREFIX = "uco_linkml"
OWN_NS = SCHEMA_ID + "/"
UMBRELLA = "uco"
CO = "co"
# Bioregistry's prefix for the Collections Ontology; UCO's files write co.
CO_PREFIX = "coll"
CORE = "core"
LICENSE = "Apache-2.0"
RELEASES = "https://github.com/ucoProject/UCO/releases/tag/"
SITE = "https://lmodel.github.io/uco"

# What the converter adds, each in the core module except the document.
ID_SLOT = "id"
TYPE_SLOT = "type"
DOCUMENT = "UcoDocument"
GRAPH_SLOT = "graph"

# The classes of the core namespace the identifier rule names.
UCO_THING = "UcoThing"
UCO_OBJECT = "UcoObject"
UCO_TYPE = "UcoType"
UCO_ICT = "UcoInherentCharacterizationThing"

# XSD datatypes LinkML's own types render as they are.
BUILTIN = {
    XSD.string: "string",
    XSD.dateTime: "datetime",
    XSD.integer: "integer",
    XSD.boolean: "boolean",
    XSD.decimal: "decimal",
    XSD.anyURI: "uri",
}

# The other XSD datatypes UCO uses, each a type in the core module. Each names
# its base as well as its typeof, because the SQL generator reads the base from
# the type itself (linkml 1.12.1). The bounds and patterns are XSD's.
XSD_TYPES = {
    XSD.unsignedInt: (
        "uco_unsigned_int",
        {
            "typeof": "integer",
            "base": "int",
            "description": "XSD's unsignedInt: an integer from 0 to 4294967295.",
            "minimum_value": 0,
            "maximum_value": 4294967295,
        },
    ),
    XSD.unsignedShort: (
        "uco_unsigned_short",
        {
            "typeof": "integer",
            "base": "int",
            "description": "XSD's unsignedShort: an integer from 0 to 65535.",
            "minimum_value": 0,
            "maximum_value": 65535,
        },
    ),
    XSD.byte: (
        "uco_byte",
        {
            "typeof": "integer",
            "base": "int",
            "description": "XSD's byte: an integer from -128 to 127.",
            "minimum_value": -128,
            "maximum_value": 127,
        },
    ),
    XSD.nonNegativeInteger: (
        "uco_non_negative_integer",
        {
            "typeof": "integer",
            "base": "int",
            "description": "XSD's nonNegativeInteger: an integer of zero or more.",
            "minimum_value": 0,
        },
    ),
    XSD.positiveInteger: (
        "uco_positive_integer",
        {
            "typeof": "integer",
            "base": "int",
            "description": "XSD's positiveInteger: an integer of one or more.",
            "minimum_value": 1,
        },
    ),
    XSD.hexBinary: (
        "uco_hex_binary",
        {
            "typeof": "string",
            "base": "str",
            "description": "XSD's hexBinary: binary data as pairs of hexadecimal digits.",
            "pattern": r"^([0-9a-fA-F]{2})*$",
        },
    ),
    XSD.base64Binary: (
        "uco_base64_binary",
        {
            "typeof": "string",
            "base": "str",
            "description": "XSD's base64Binary: binary data in the Base64 alphabet, padded with =.",
            "pattern": r"^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$",
        },
    ),
    XSD.duration: (
        "uco_duration",
        {
            "typeof": "string",
            "base": "str",
            "description": "XSD's duration: a length of time such as P1DT2H, in ISO 8601's form.",
            "pattern": r"^-?P(?!$)(\d+Y)?(\d+M)?(\d+D)?(T(?!$)(\d+H)?(\d+M)?(\d+(\.\d+)?S)?)?$",
        },
    ),
}

# Integer datatypes the CO module renders as bounds on a slot, since it
# imports no module that declares the types above.
CO_BOUNDS = {XSD.positiveInteger: 1, XSD.nonNegativeInteger: 0}

# The datatype facets a restriction may carry, as LinkML's bound keys.
FACETS = {XSD.minInclusive: "minimum_value", XSD.maxInclusive: "maximum_value"}

# CO states no licence, so the CO terms carry descriptions written here.
CO_DESCRIPTIONS = {
    "Bag": "A collection that may hold one element more than once, in no order.",
    "Item": "An entry of a collection, which wraps one element of the collection's content.",
    "List": "A collection whose items come in order, one after another.",
    "ListItem": "An item of a list, which has a place in the list's order.",
    "item": "An item of the collection.",
    "itemContent": "The element that the item wraps.",
    "index": "The place of the item in its list, counting from 1.",
    "size": "How many items the collection holds.",
    "firstItem": "The first item of the list.",
    "lastItem": "The last item of the list.",
    "nextItem": "The item that comes straight after this one.",
    "previousItem": "The item that comes straight before this one.",
    "followedBy": "An item that comes somewhere after this one.",
    "precededBy": "An item that comes somewhere before this one.",
}

# The domains CO 2.0's own ontology gives the CO properties UCO's files use,
# as the CO classes rendered here: CO's Collection, which UCO's files do not
# name, is Bag. Each is a slot of its domain, beside any class a UCO shape
# gives it to. CO gives nextItem, previousItem and precededBy no domain.
# item stays on the classes UCO's shapes give it to, List and Thread: a list
# holds its items inline and a thread names them by IRI, and LinkML cannot
# undo on Thread an inlining its parent Bag states.
CO_DOMAINS = {
    "size": "Bag",
    "itemContent": "Item",
    "index": "ListItem",
    "firstItem": "List",
    "lastItem": "List",
    "followedBy": "ListItem",
}

# What a property shape may say that the converter reads, or knows to pass.
SHAPE_KEYS = {
    SH.path,
    SH["class"],
    SH.datatype,
    SH.minCount,
    SH.maxCount,
    SH["in"],
    SH["or"],
    SH.hasValue,
    SH.nodeKind,
    SH.message,
    SH.description,
    SH.severity,
    SH.deactivated,
    SH.targetSubjectsOf,
    RDFS.comment,
    RDF.type,
}

# What a node shape may say beside its property shapes and its target that
# the converter knows to pass.
NODE_KEYS = {
    RDF.type,
    RDFS.label,
    RDFS.comment,
    RDFS.subClassOf,
    RDFS.seeAlso,
    RDFS.isDefinedBy,
    SH.property,
    SH.targetClass,
    SH.message,
    SH.severity,
    SH.description,
    OWL.disjointWith,
}


# The LinkML default of each key a field states even when false; a slot
# definition leaves the default unwritten.
DEFAULTS = {"required": False, "multivalued": False}

# The order in which a slot or slot_usage states its keys.
KEY_ORDER = (
    "range",
    "any_of",
    "required",
    "multivalued",
    "minimum_cardinality",
    "maximum_cardinality",
    "inlined",
    "inlined_as_list",
    "equals_string",
    "has_member",
    "minimum_value",
    "maximum_value",
)


def ordered(f: dict) -> dict:
    return {
        k: f[k]
        for k in sorted(
            f, key=lambda k: KEY_ORDER.index(k) if k in KEY_ORDER else len(KEY_ORDER)
        )
    }


@dataclass(frozen=True)
class Constraint:
    """What SHACL says about one property on one class, before rendering.
    ``range`` holds LinkML names, more than one for a union."""

    range: tuple[str, ...] | None = None
    min: int = 0
    max: int | None = None
    has_value: str | None = None
    bounds: tuple[tuple[str, int], ...] = ()
    absent: bool = False


@dataclass
class Element:
    """One schema element and the module it is declared in."""

    kind: str  # class, slot, enum or type
    name: str
    module: str
    iri: URIRef | None = None
    data: dict = field(default_factory=dict)


def toposort(deps: dict[str, set[str]]) -> list[str]:
    """Order the modules so that each comes after the modules it imports; a
    tie goes in alphabetical order, one module at a time."""
    order: list[str] = []
    pending = {k: set(v) for k, v in deps.items()}
    while pending:
        ready = sorted(k for k, v in pending.items() if not v)
        if not ready:
            raise SystemExit(f"import cycle among modules: {sorted(pending)}")
        order.append(ready[0])
        del pending[ready[0]]
        for v in pending.values():
            v.discard(ready[0])
    return order


def text(value) -> str:
    return " ".join(str(value).split())


class Converter:
    def __init__(self, upstream: Path) -> None:
        self.report: list[str] = []
        self.literal_classes: set[URIRef] = set()
        onto = upstream / "ontology"
        self.files: dict[str, Graph] = {}
        for path in sorted((onto / "uco").glob("*/*.ttl")):
            self.files[path.parent.name] = Graph().parse(path, format="turtle")
        self.files[CO] = Graph().parse(onto / CO / "co.ttl", format="turtle")
        self.master = self.files.pop("master")
        self.g = Graph()
        for graph in self.files.values():
            self.g += graph
        self.namespaces = sorted(ns for ns in self.files if ns != CO)
        self._read_version()
        self._read_imports()
        self._collect()
        self._name()
        self._structure()
        self._read_shapes()
        self._effective()

    # -- the ontology as a whole ----------------------------------------------

    def _read_version(self) -> None:
        ontology = next(self.master.subjects(RDF.type, OWL.Ontology))
        self.version = str(self.master.value(ontology, OWL.versionInfo))
        for ns, graph in self.files.items():
            onto = next(graph.subjects(RDF.type, OWL.Ontology))
            iri = str(graph.value(onto, OWL.versionIRI))
            if not iri.endswith("/" + self.version):
                raise SystemExit(f"{ns}'s version IRI {iri} is not UCO {self.version}")
        self.source = RELEASES + self.version

    def _ontology_module(self, iri) -> str | None:
        s = str(iri)
        if s.startswith(UCO_NS):
            ns = s[len(UCO_NS) :].split("/")[0]
            return ns if ns in self.files else None
        if s.startswith(UCO_ROOT + "co/") or s == UCO_ROOT + "co":
            return CO
        return None

    def _read_imports(self) -> None:
        self.imports: dict[str, set[str]] = {}
        for ns, graph in self.files.items():
            onto = next(graph.subjects(RDF.type, OWL.Ontology))
            self.imports[ns] = set()
            for target in graph.objects(onto, OWL.imports):
                module = self._ontology_module(target)
                if module:
                    self.imports[ns].add(module)
                else:
                    self.report.append(
                        f"{ns}.ttl imports {target}, which is not rendered"
                    )
        master = next(self.master.subjects(RDF.type, OWL.Ontology))
        for target in self.master.objects(master, OWL.imports):
            if self._ontology_module(target) is None:
                self.report.append(f"uco.ttl imports {target}, which is not rendered")
        self.order = toposort(self.imports)
        self.closure = {m: self._closure(m) for m in self.files}

    def _closure(self, module: str) -> set[str]:
        out: set[str] = set()
        stack = [module]
        while stack:
            for dep in self.imports[stack.pop()]:
                if dep not in out:
                    out.add(dep)
                    stack.append(dep)
        return out

    def visible(self, frm: str, to: str) -> bool:
        return frm == to or to in self.closure[frm]

    # -- what the files declare ---------------------------------------------------

    def ns_of(self, iri) -> str | None:
        s = str(iri)
        if s.startswith(UCO_NS):
            ns = s[len(UCO_NS) :].split("/")[0]
            return ns if ns in self.namespaces else None
        if s.startswith(CO_NS):
            return CO
        return None

    def local(self, iri) -> str:
        s = str(iri)
        if s.startswith(CO_NS):
            return s[len(CO_NS) :]
        return s.rsplit("/", 1)[-1]

    def curie(self, iri) -> str:
        ns = self.ns_of(iri)
        return f"{CO_PREFIX if ns == CO else 'uco-' + ns}:{self.local(iri)}"

    def _collect(self) -> None:
        g = self.g
        self.classes = {
            c
            for c in g.subjects(RDF.type, OWL.Class)
            if isinstance(c, URIRef) and self.ns_of(c) not in (None, CO)
        }
        named = set(g.subjects(RDFS.subClassOf, None)) | set(
            g.objects(None, RDFS.subClassOf)
        )
        named |= set(g.objects(None, SH.targetClass)) | set(
            g.objects(None, SH["class"])
        )
        named |= set(g.objects(None, OWL.disjointWith))
        self.classes |= {
            c for c in named if isinstance(c, URIRef) and self.ns_of(c) == CO
        }
        self.properties = {
            p
            for kind in (
                OWL.ObjectProperty,
                OWL.DatatypeProperty,
                OWL.AnnotationProperty,
            )
            for p in g.subjects(RDF.type, kind)
            if isinstance(p, URIRef) and self.ns_of(p) not in (None, CO)
        }
        self.properties |= {
            p
            for p in g.objects(None, SH.path)
            if isinstance(p, URIRef) and self.ns_of(p) == CO
        }
        # A property a shape names but no file declares, such as
        # uco-observable:eventID, is a slot too.
        self.undeclared = {
            p
            for p in g.objects(None, SH.path)
            if isinstance(p, URIRef)
            and self.ns_of(p) not in (None, CO)
            and p not in self.properties
        }
        for p in sorted(self.undeclared, key=str):
            self.report.append(
                f"{self.curie(p)} is a slot, although UCO names it in a shape without declaring it"
            )
        self.properties |= self.undeclared
        self.enums: dict[URIRef, list[str]] = {}
        self.datatypes: set[URIRef] = set()
        for d in g.subjects(RDF.type, RDFS.Datatype):
            if not isinstance(d, URIRef) or self.ns_of(d) in (None, CO):
                continue
            equivalent = g.value(d, OWL.equivalentClass)
            members = g.value(equivalent, OWL.oneOf) if equivalent is not None else None
            if members is not None:
                values = [str(v) for v in Collection(g, members)]
                if len(set(values)) != len(values):
                    raise SystemExit(f"{self.curie(d)} lists a value twice")
                self.enums[d] = values
            else:
                self.datatypes.add(d)
        for p in sorted(
            {
                o
                for s in g.subjects(SH.path, None)
                for o in self._path_members(g.value(s, SH.path))
            }
            - self.properties
            - {RDFS.subClassOf, RDF.type},
            key=str,
        ):
            self.report.append(
                f"left out, {p}: used only inside a path of more than one property"
            )

    def _path_members(self, path) -> set[URIRef]:
        """The properties a path of more than one property names."""
        if not isinstance(path, BNode):
            return set()
        out: set[URIRef] = set()
        try:
            members = list(Collection(self.g, path))
        except Exception:  # not an RDF list: an inverse or repetition path
            members = list(self.g.objects(path, None))
        for m in members:
            if isinstance(m, URIRef):
                out.add(m)
            else:
                out |= self._path_members(m)
        return out

    # -- names ------------------------------------------------------------------------

    def _name(self) -> None:
        position = {m: i for i, m in enumerate(self.order)}
        self.class_name: dict[URIRef, str] = {}
        uco_class_names = {self.local(c) for c in self.classes if self.ns_of(c) != CO}
        enum_names = {self.local(e) for e in self.enums}
        type_names = {self.local(t) for t in self.datatypes}
        for c in sorted(self.classes, key=str):
            name = self.local(c)
            if (
                self.ns_of(c) == CO
                and name in uco_class_names | enum_names | type_names
            ):
                name = "Co" + name
                self.report.append(
                    f"renamed, {self.curie(c)}: {name}, since UCO also has a {self.local(c)}"
                )
            self.class_name[c] = name
        by_local: dict[str, list[URIRef]] = defaultdict(list)
        for p in self.properties:
            by_local[self.local(p)].append(p)
        self.slot_name: dict[URIRef, str] = {}
        self.renamed_slots: list[str] = []
        for local, props in sorted(by_local.items()):
            uco = sorted(
                (p for p in props if self.ns_of(p) != CO),
                key=lambda p: position[self.ns_of(p)],
            )
            for i, p in enumerate(uco):
                self.slot_name[p] = local if i == 0 else f"{self.ns_of(p)}_{local}"
                if i:
                    self.renamed_slots.append(self.slot_name[p])
                    self.report.append(
                        f"renamed, {self.curie(p)}: {self.slot_name[p]}, since uco-{self.ns_of(uco[0])} also has a {local}"
                    )
            for p in (p for p in props if self.ns_of(p) == CO):
                self.slot_name[p] = f"co_{local}" if uco else local
                if uco:
                    self.report.append(
                        f"renamed, {self.curie(p)}: co_{local}, since UCO also has a {local}"
                    )
        self.enum_name = {e: self.local(e) for e in self.enums}
        self.type_name = {t: self.local(t) for t in self.datatypes}
        elements = (
            list(self.class_name.values())
            + list(self.enum_name.values())
            + list(self.type_name.values())
            + [name for name, _ in XSD_TYPES.values()]
            + [DOCUMENT]
        )
        clashes = {n for n in elements if elements.count(n) > 1}
        if clashes:
            raise SystemExit(f"two elements share a name: {sorted(clashes)}")
        slots = list(self.slot_name.values()) + [ID_SLOT, TYPE_SLOT, GRAPH_SLOT]
        clashes = {n for n in slots if slots.count(n) > 1}
        if clashes:
            raise SystemExit(f"two slots share a name: {sorted(clashes)}")

    # -- the class tree -----------------------------------------------------------

    def core(self, local: str) -> URIRef:
        return URIRef(f"{UCO_NS}core/{local}")

    def _raw_parents(self, c) -> list[URIRef]:
        return [p for p in self.g.objects(c, RDFS.subClassOf) if p in self.classes]

    def _raw_ancestors(self, c) -> set[URIRef]:
        out: set[URIRef] = set()
        stack = [c]
        while stack:
            for p in self._raw_parents(stack.pop()):
                if p not in out:
                    out.add(p)
                    stack.append(p)
        return out

    def _structure(self) -> None:
        """is_a and mixins of every class, and which classes carry the
        identifier and the designator."""
        self.is_a: dict[URIRef, URIRef | None] = {}
        self.mixins: dict[URIRef, list[URIRef]] = {}
        for c in sorted(self.classes, key=str):
            parents = self._raw_parents(c)
            kept = [
                p
                for p in parents
                if not any(p in self._raw_ancestors(q) for q in parents if q != p)
            ]
            for p in sorted(set(parents) - set(kept), key=str):
                self.report.append(
                    f"left out, {self.curie(c)} rdfs:subClassOf {self.curie(p)}: an ancestor of another parent"
                )
            if not kept:
                self.is_a[c], self.mixins[c] = None, []
                continue
            kept.sort(
                key=lambda p: (
                    self.ns_of(p) == CO,
                    -len(self._raw_ancestors(p)),
                    self.ns_of(p) != self.ns_of(c),
                    self.curie(p),
                )
            )
            self.is_a[c], self.mixins[c] = kept[0], sorted(kept[1:], key=self.curie)
        thing, obj, ict, uco_type = (
            self.core(n) for n in (UCO_THING, UCO_OBJECT, UCO_ICT, UCO_TYPE)
        )
        self.id_classes = {obj, uco_type} | {
            c
            for c in self.classes
            if thing in self._raw_parents(c) and c not in (obj, ict)
        }
        self.type_classes = {thing, uco_type}

    def ancestors(self, c) -> list[URIRef]:
        """Every ancestor through is_a and mixins, nearest first."""
        out: list[URIRef] = []
        queue = [p for p in [self.is_a[c], *self.mixins[c]] if p is not None]
        while queue:
            p = queue.pop(0)
            if p not in out:
                out.append(p)
                queue += [q for q in [self.is_a[p], *self.mixins[p]] if q is not None]
        return out

    def has_id(self, c) -> bool:
        return c in self.id_classes or any(
            a in self.id_classes for a in self.ancestors(c)
        )

    # -- shapes ---------------------------------------------------------------------

    def _read_shape(self, owner: str, shape) -> tuple[URIRef, dict] | None:
        """One property shape as (property, raw constraint), or None when the
        shape is left out."""
        g = self.g
        path = g.value(shape, SH.path)
        where = f"{owner}.{self.local(path) if isinstance(path, URIRef) else 'path'}"
        if g.value(shape, SH.deactivated) == Literal(True):
            self.report.append(f"left out, a deactivated shape on {where}")
            return None
        if not isinstance(path, URIRef):
            self.report.append(
                f"left out, a shape on {owner} whose path has more than one property"
            )
            return None
        if path not in self.properties:
            self.report.append(
                f"left out, a shape on {owner} over {path}, which is not a rendered property"
            )
            return None
        severity = g.value(shape, SH.severity)
        if severity in (SH.Info, SH.Warning):
            self.report.append(
                f"left out, advice of severity {g.qname(severity)} on {where}"
            )
            return None
        for predicate in sorted(set(g.predicates(shape)) - SHAPE_KEYS, key=str):
            self.report.append(
                f"left out, the {g.qname(predicate)} constraint on {where}"
            )
        raw: dict = {}
        for key, predicate in (
            ("class", SH["class"]),
            ("datatype", SH.datatype),
            ("has_value", SH.hasValue),
        ):
            value = g.value(shape, predicate)
            if value is not None:
                raw[key] = value
        for key, predicate in (("min", SH.minCount), ("max", SH.maxCount)):
            value = g.value(shape, predicate)
            if value is not None:
                raw[key] = int(value)
        if raw.get("max") == 0:
            # sh:maxCount 0 forbids the property; the slot keeps its shape.
            del raw["max"]
            raw["absent"] = True
        members = g.value(shape, SH["in"])
        if members is not None:
            raw["in"] = [str(v) for v in Collection(g, members)]
        alternatives = g.value(shape, SH["or"])
        if alternatives is not None:
            types = [g.value(alt, SH.datatype) for alt in Collection(g, alternatives)]
            if all(t is not None for t in types):
                raw["or"] = types
            else:
                self.report.append(
                    f"left out, an sh:or that is not a union of datatypes on {where}"
                )
        return path, raw

    def _read_shapes(self) -> None:
        g = self.g
        # Constraints on a property wherever it is used, from the shapes that
        # target its subjects.
        self.wide: dict[URIRef, dict] = defaultdict(dict)
        for shape in sorted(set(g.subjects(SH.targetSubjectsOf, None)), key=str):
            target = g.value(shape, SH.targetSubjectsOf)
            path = g.value(shape, SH.path)
            if path == target and (shape, SH["class"], None) in g:
                read = self._read_shape(f"subjects of {self.curie(target)}", shape)
                if read:
                    self.wide[read[0]] = self._merge(
                        self.wide[read[0]], read[1], str(shape)
                    )
            elif (
                path is None
                and (shape, SH["class"], None) in g
                and (shape, SH.property, None) not in g
            ):
                self.report.append(
                    f"left out, {self.curie(target)}'s subjects shape: its subjects are "
                    f"{self.curie(g.value(shape, SH['class']))}"
                )
            elif path == target:
                read = self._read_shape(f"subjects of {self.curie(target)}", shape)
                if read:
                    self.wide[read[0]] = self._merge(
                        self.wide[read[0]], read[1], str(shape)
                    )
            elif path is None and (shape, SH.property, None) in g:
                # A node shape on the subjects: its property shapes over the
                # property itself constrain it, and the rest is left out.
                for predicate in sorted(
                    set(g.predicates(shape)) - NODE_KEYS - {SH.targetSubjectsOf},
                    key=str,
                ):
                    self.report.append(
                        f"left out, the {g.qname(predicate)} constraint on the subjects of {self.curie(target)}"
                    )
                for inner in g.objects(shape, SH.property):
                    if g.value(inner, SH.path) != target:
                        self.report.append(
                            f"left out, a shape over another path on the subjects of {self.curie(target)}"
                        )
                        continue
                    read = self._read_shape(f"subjects of {self.curie(target)}", inner)
                    if read:
                        self.wide[read[0]] = self._merge(
                            self.wide[read[0]], read[1], str(shape)
                        )
            else:
                self.report.append(
                    f"left out, the shape {self.local(shape)} on the subjects of {self.curie(target)}"
                )
        # Each class's own shapes.
        self.own: dict[URIRef, dict[URIRef, dict]] = {}
        for c in sorted(self.classes, key=str):
            owner = self.class_name[c]
            shapes = [c] if (c, RDF.type, SH.NodeShape) in g else []
            shapes += sorted(
                (s for s in g.subjects(SH.targetClass, c) if s != c), key=str
            )
            merged: dict[URIRef, dict] = {}
            for node in shapes:
                if g.value(node, SH.severity) in (SH.Info, SH.Warning):
                    severity = g.qname(g.value(node, SH.severity))
                    self.report.append(
                        f"left out, advice of severity {severity} on {owner}"
                    )
                    continue
                for predicate in sorted(set(g.predicates(node)) - NODE_KEYS, key=str):
                    if c in self.classes and predicate in (OWL.equivalentClass,):
                        continue
                    self.report.append(
                        f"left out, the {g.qname(predicate)} constraint of {owner}"
                    )
                for shape in g.objects(node, SH.property):
                    read = self._read_shape(owner, shape)
                    if read:
                        merged[read[0]] = self._merge(
                            merged.get(read[0], {}), read[1], owner
                        )
            self.own[c] = merged
        # A CO property is a slot of its CO domain; a property no class shape
        # names joins its rdfs:domain's class.
        for p in sorted(self.properties, key=str):
            if self.ns_of(p) == CO and self.local(p) in CO_DOMAINS:
                cls = URIRef(CO_NS + CO_DOMAINS[self.local(p)])
                if p not in self.own[cls]:
                    self.own[cls][p] = {}
                    self.report.append(
                        f"{self.curie(p)} is a slot of {self.class_name[cls]}, CO's domain for it"
                    )
        used = {p for fields in self.own.values() for p in fields}
        for p in sorted(self.properties - used, key=str):
            domain = self._domain(p)
            if domain is not None:
                self.own[domain][p] = {}
                self.report.append(
                    f"{self.curie(p)} is a slot of {self.class_name[domain]}, its rdfs:domain"
                )
            else:
                self.report.append(
                    f"{self.curie(p)} is a slot no class lists: no class shape names it"
                )

    def _domain(self, p) -> URIRef | None:
        while p is not None:
            domain = self.g.value(p, RDFS.domain)
            if domain in self.classes:
                return domain
            p = self.g.value(p, RDFS.subPropertyOf)
        return None

    def _merge(self, a: dict, b: dict, where: str) -> dict:
        out = dict(a)
        for key, value in b.items():
            if key == "min":
                out[key] = max(out.get(key, 0), value)
            elif key == "max":
                out[key] = min(out[key], value) if key in out else value
            elif key in out and out[key] != value:
                self.report.append(
                    f"two shapes on {where} disagree on {key}; the first is kept"
                )
            else:
                out.setdefault(key, value)
        return out

    # -- ranges ---------------------------------------------------------------------

    def _datatype(self, dt, module: str) -> tuple[tuple[str, ...], tuple]:
        """A datatype IRI as a LinkML range and any bounds it adds."""
        if dt in BUILTIN:
            return (BUILTIN[dt],), ()
        if dt in CO_BOUNDS and not self.visible(module, CORE):
            return ("integer",), (("minimum_value", CO_BOUNDS[dt]),)
        if dt in XSD_TYPES:
            return (XSD_TYPES[dt][0],), ()
        if dt in self.enums:
            return (self.enum_name[dt],), ()
        if dt in self.datatypes:
            return (self.type_name[dt],), ()
        if dt in self.classes:
            # pattern:patternExpression is a literal whose sh:datatype names
            # the class pattern:PatternExpression, which has no properties.
            if dt not in self.literal_classes:
                self.literal_classes.add(dt)
                self.report.append(
                    f"{self.curie(dt)} is a class that a shape names as a datatype; "
                    "the literal it types is a string"
                )
            return ("string",), ()
        raise SystemExit(f"no LinkML range for the datatype {dt}")

    def _enum_for(self, values: list[str], where: str) -> str:
        wanted = set(values)
        found = [e for e, members in self.enums.items() if set(members) == wanted]
        if len(found) != 1:
            raise SystemExit(f"no one vocabulary has the values sh:in lists on {where}")
        return self.enum_name[found[0]]

    def _raw_range(
        self, raw: dict, module: str, where: str
    ) -> tuple[tuple[str, ...] | None, tuple]:
        if "class" in raw:
            if raw["class"] not in self.classes:
                raise SystemExit(f"no class {raw['class']} for {where}")
            return (self.class_name[raw["class"]],), ()
        if "in" in raw:
            return (self._enum_for(raw["in"], where),), ()
        if "datatype" in raw:
            return self._datatype(raw["datatype"], module)
        if "or" in raw:
            names: list[str] = []
            bounds: tuple = ()
            for dt in raw["or"]:
                rng, b = self._datatype(dt, module)
                names += [n for n in rng if n not in names]
                bounds += b
            return tuple(names), bounds
        return None, ()

    def _declared_range(self, p, module: str) -> tuple[tuple[str, ...] | None, tuple]:
        """The property's rdfs:range as a LinkML range and bounds."""
        g = self.g
        r = g.value(p, RDFS.range)
        if r is None:
            return None, ()
        if isinstance(r, URIRef):
            if r in self.classes:
                return (self.class_name[r],), ()
            return self._datatype(r, module)
        union = g.value(r, OWL.unionOf)
        if union is not None:
            names: list[str] = []
            for member in Collection(g, union):
                rng, _ = self._datatype(member, module)
                names += [n for n in rng if n not in names]
            enums = [n for n in names if n in self.enum_name.values()]
            return tuple(enums + [n for n in names if n not in enums]), ()
        base = g.value(r, OWL.onDatatype)
        if base is not None:
            rng, bounds = self._datatype(base, module)
            for restriction in Collection(g, g.value(r, OWL.withRestrictions)):
                for facet, key in FACETS.items():
                    value = g.value(restriction, facet)
                    if value is not None:
                        bounds += ((key, int(value)),)
            return rng, bounds
        self.report.append(
            f"left out, the rdfs:range of {self.curie(p)}: a class expression"
        )
        return None, ()

    def constraint(self, p, raw: dict, module: str, where: str) -> Constraint:
        rng, bounds = self._raw_range(raw, module, where)
        has_value = raw.get("has_value")
        if has_value is not None and not isinstance(has_value, Literal):
            self.report.append(
                f"left out, an sh:hasValue that is not a literal on {where}"
            )
            has_value = None
        return Constraint(
            range=rng,
            min=raw.get("min", 0),
            max=raw.get("max"),
            has_value=str(has_value) if has_value is not None else None,
            bounds=bounds,
            absent=raw.get("absent", False),
        )

    # -- the conjunction of a class's shapes and its parents' -------------------

    def class_ancestors_names(self, name: str) -> set[str]:
        c = self.class_by_name[name]
        return {self.class_name[a] for a in self.ancestors(c)}

    def _under(self, x: str, y: str) -> bool:
        if x == y:
            return True
        return (
            x in self.class_by_name
            and y in self.class_by_name
            and y in self.class_ancestors_names(x)
        )

    def conj(self, a: Constraint, b: Constraint, where: str) -> Constraint:
        """Both constraints at once, as SHACL applies a class's shapes and its
        parents' to one node."""
        if a.range is None or b.range is None:
            rng = a.range if b.range is None else b.range
        else:
            rng = tuple(
                dict.fromkeys(
                    [x for x in a.range if any(self._under(x, y) for y in b.range)]
                    + [y for y in b.range if any(self._under(y, x) for x in a.range)]
                )
            )
            if not rng:
                self.report.append(
                    f"{where}: its range {a.range} and its parent's {b.range} do not meet; its own is kept"
                )
                rng = a.range
        maxes = [m for m in (a.max, b.max) if m is not None]
        bounds = dict(b.bounds)
        for key, value in a.bounds:
            if key in bounds:
                value = (
                    max(value, bounds[key])
                    if key == "minimum_value"
                    else min(value, bounds[key])
                )
            bounds[key] = value
        return Constraint(
            range=rng,
            min=max(a.min, b.min),
            max=min(maxes) if maxes else None,
            has_value=a.has_value or b.has_value,
            bounds=tuple(sorted(bounds.items())),
            absent=a.absent or b.absent,
        )

    def _effective(self) -> None:
        self.class_by_name = {name: c for c, name in self.class_name.items()}
        self.base: dict[URIRef, Constraint] = {}
        for p in self.properties:
            module = self.ns_of(p)
            self.base[p] = self.constraint(
                p, self.wide.get(p, {}), module, f"the subjects of {self.curie(p)}"
            )
        self.eff: dict[URIRef, dict[URIRef, Constraint]] = {}
        self.class_order: list[URIRef] = []
        self._declared: dict = {}
        remaining = sorted(self.classes, key=str)
        while remaining:
            for c in list(remaining):
                parents = [q for q in [self.is_a[c], *self.mixins[c]] if q is not None]
                if any(q in remaining for q in parents):
                    continue
                own = {
                    p: self.conj(
                        self.constraint(
                            p,
                            raw,
                            self.ns_of(c),
                            f"{self.class_name[c]}.{self.local(p)}",
                        ),
                        self.base[p],
                        f"{self.class_name[c]}.{self.slot_name[p]}",
                    )
                    for p, raw in self.own[c].items()
                }
                result: dict[URIRef, Constraint] = {}
                for q in parents:
                    for p, k in self.eff[q].items():
                        result[p] = (
                            self.conj(
                                result[p],
                                k,
                                f"{self.class_name[c]}.{self.slot_name[p]}",
                            )
                            if p in result
                            else k
                        )
                for p, k in own.items():
                    result[p] = (
                        self.conj(
                            k, result[p], f"{self.class_name[c]}.{self.slot_name[p]}"
                        )
                        if p in result
                        else k
                    )
                self.eff[c] = result
                self.class_order.append(c)
                remaining.remove(c)

    # -- rendering ----------------------------------------------------------------

    def description(self, iri, kind: str) -> str:
        if self.ns_of(iri) == CO:
            return CO_DESCRIPTIONS[self.local(iri)]
        if iri in self.undeclared:
            return f"UCO {self.version} names the property {self.curie(iri)} in a shape without declaring it."
        comment = self.g.value(iri, RDFS.comment)
        if comment is not None and text(comment):
            return text(comment)
        return f"UCO {self.version} declares the {kind} {self.curie(iri)} without a definition."

    def title(self, iri, name: str) -> dict:
        label = self.g.value(iri, RDFS.label)
        if label is not None and text(label) != name and text(label) != self.local(iri):
            return {"title": text(label)}
        return {}

    def see_also(self, iri) -> dict:
        refs = sorted(
            self.curie(r) if self.ns_of(r) else str(r)
            for r in self.g.objects(iri, RDFS.seeAlso)
            if isinstance(r, URIRef)
        )
        return {"see_also": refs} if refs else {}

    def declared(self, p) -> tuple[tuple[str, ...] | None, tuple]:
        """The property's rdfs:range, read once."""
        if p not in self._declared:
            self._declared[p] = self._declared_range(p, self.ns_of(p))
        return self._declared[p]

    def field(self, p, k: Constraint, where: str) -> dict:
        """A constraint as the LinkML keys a slot or slot_usage carries, with
        required, multivalued and inlined stated even when false."""
        declared_range, declared_bounds = self.declared(p)
        rng = k.range if k.range is not None else declared_range
        bounds = dict(k.bounds)
        if rng is not None and rng == declared_range:
            for key, value in declared_bounds:
                bounds.setdefault(key, value)
        f: dict = {}
        if rng is not None:
            if len(rng) == 1:
                f["range"] = rng[0]
            else:
                f["any_of"] = [{"range": r} for r in rng]
        f["required"] = k.min >= 1
        multivalued = k.max is None or k.max > 1
        f["multivalued"] = multivalued
        if k.min > 1:
            f["minimum_cardinality"] = k.min
        if k.max is not None and k.max > 1:
            f["maximum_cardinality"] = k.max
        if rng is not None and len(rng) == 1 and rng[0] in self.class_by_name:
            inlined = not self.has_id(self.class_by_name[rng[0]])
            f["inlined"] = inlined
            if inlined and multivalued:
                f["inlined_as_list"] = True
        elif rng is not None and any(r in self.class_by_name for r in rng):
            raise SystemExit(f"{where}: a union of classes")
        if k.has_value is not None:
            if multivalued:
                f["has_member"] = {"equals_string": k.has_value}
            else:
                f["equals_string"] = k.has_value
        for key, value in sorted(bounds.items()):
            f[key] = value
        return f

    def _home(self, name: str) -> str | None:
        kind = self._kind_of(name)[0]
        return self.home.get((kind, name))

    def _sees(self, module: str, rng) -> bool:
        """Whether a module sees every class, enum or type a range names."""
        names = [rng] if isinstance(rng, str) else [alt["range"] for alt in rng]
        for name in names:
            home = self._home(name)
            if home is not None and not self.visible(module, home):
                return False
        return True

    def _default(self, key: str):
        return DEFAULTS.get(key)

    def _agreed(self, p, uses: dict) -> dict:
        """The keys every class that has the slot agrees on, a missing key
        counting as its default. A slot no class lists states no boolean:
        LinkML would pass a true one to every slot under it, and no slot can
        turn one off again."""
        if not uses:
            f = self.field(p, self.base[p], self.curie(p))
            return {
                k: v
                for k, v in f.items()
                if k not in ("required", "multivalued", "inlined", "inlined_as_list")
            }
        keys = list(dict.fromkeys(k for f in uses.values() for k in f))
        first = next(iter(uses.values()))
        common = {
            k: first.get(k, self._default(k))
            for k in keys
            if len({repr(f.get(k, self._default(k))) for f in uses.values()}) == 1
        }
        common = {k: v for k, v in common.items() if v is not None}
        # The slot's own module must see its range; where it does not, each
        # class's slot_usage carries the range instead.
        for key in ("range", "any_of"):
            if key in common and not self._sees(
                self.home[("slot", self.slot_name[p])], common[key]
            ):
                del common[key]
                common.pop("inlined", None)
                common.pop("inlined_as_list", None)
        if "range" not in common and "any_of" not in common:
            rng, _ = self.declared(p)
            if (
                rng is not None
                and len(rng) == 1
                and self._sees(self.home[("slot", self.slot_name[p])], rng[0])
            ):
                common["range"] = rng[0]
                if rng[0] in self.class_by_name:
                    common["inlined"] = not self.has_id(self.class_by_name[rng[0]])
        return common

    def _induced_def(self, p) -> dict:
        """What LinkML reads as the slot's own value of each key: its written
        definition over its parent slot's, where a boolean true anywhere in
        the chain stands, since SchemaView reads a false as unset."""
        parent = self.g.value(p, RDFS.subPropertyOf)
        base = self._induced_def(parent) if parent in self.properties else {}
        out = {**base, **self.written[p]}
        for key in ("required", "multivalued", "inlined", "inlined_as_list"):
            if base.get(key) is True:
                out[key] = True
        return out

    def _elements(self) -> dict[tuple[str, str], Element]:
        """Every element of every module, placed by self.home."""
        elements: dict[tuple[str, str], Element] = {}

        def add(kind: str, name: str, iri, data: dict) -> None:
            elements[(kind, name)] = Element(
                kind, name, self.home[(kind, name)], iri, data
            )

        for e, values in sorted(self.enums.items(), key=lambda kv: str(kv[0])):
            add(
                "enum",
                self.enum_name[e],
                e,
                {
                    "enum_uri": self.curie(e),
                    **self.title(e, self.enum_name[e]),
                    "description": self.description(e, "vocabulary"),
                    "permissible_values": {v: {} for v in values},
                },
            )
        for t in sorted(self.datatypes, key=str):
            add(
                "type",
                self.type_name[t],
                t,
                {
                    "typeof": "string",
                    "base": "str",
                    "uri": self.curie(t),
                    "description": self.description(t, "datatype"),
                },
            )
        for dt in sorted(self.used_xsd, key=str):
            name, data = XSD_TYPES[dt]
            add(
                "type",
                name,
                dt,
                {
                    "typeof": data["typeof"],
                    "base": data["base"],
                    "uri": "xsd:" + self.local_xsd(dt),
                    **{k: v for k, v in data.items() if k not in ("typeof", "base")},
                },
            )

        # Slots: each carries what every class that has it agrees on.
        self.fields: dict[URIRef, dict[URIRef, dict]] = defaultdict(dict)
        for c in self.class_order:
            for p, k in self.eff[c].items():
                self.fields[p][c] = self.field(
                    p, k, f"{self.class_name[c]}.{self.slot_name[p]}"
                )
        self.written: dict[URIRef, dict] = {}
        for p in self.slot_order():
            agreed = self._agreed(p, self.fields.get(p, {}))
            parent = self.g.value(p, RDFS.subPropertyOf)
            inherited = self._induced_def(parent) if parent in self.properties else {}
            self.written[p] = {
                k: v
                for k, v in agreed.items()
                if not (k in DEFAULTS and v == DEFAULTS[k])
                and not (v is False and inherited.get(k) is True)
            }
            # A slot multivalued through its parent slot holds an inlined
            # range as a list, as every other inlined list here does.
            if (
                inherited.get("multivalued") is True
                and self.written[p].get("inlined") is True
            ):
                self.written[p]["inlined_as_list"] = True
        for p in sorted(self.properties, key=str):
            data = {
                **self.title(p, self.slot_name[p]),
                "description": self.description(p, "property"),
                "slot_uri": self.curie(p),
            }
            parent = self.g.value(p, RDFS.subPropertyOf)
            if parent is not None and parent in self.properties:
                data["is_a"] = self.slot_name[parent]
            domain = self._domain(p)
            if domain is not None:
                data["domain"] = self.class_name[domain]
            inverse = self.g.value(p, OWL.inverseOf)
            if inverse is not None and inverse in self.properties:
                data["inverse"] = self.slot_name[inverse]
            if (p, RDF.type, OWL.TransitiveProperty) in self.g:
                data["transitive"] = True
            data.update(self.see_also(p))
            data.update(ordered(self.written[p]))
            add("slot", self.slot_name[p], p, data)

        # Classes, parents first, each with a slot_usage where LinkML's
        # inheritance would give it another value than its own conjunction.
        emitted: dict[URIRef, dict[URIRef, dict]] = defaultdict(dict)
        for c in self.class_order:
            for p in sorted(self.eff[c], key=lambda p: self.slot_name[p]):
                usage = self._usage(c, p, emitted)
                if usage:
                    emitted[c][p] = usage
        for c in sorted(self.classes, key=str):
            name = self.class_name[c]
            data: dict = {}
            if self.is_a[c] is not None:
                data["is_a"] = self.class_name[self.is_a[c]]
            if self.mixins[c]:
                data["mixins"] = [self.class_name[m] for m in self.mixins[c]]
            data["class_uri"] = self.curie(c)
            data.update(self.title(c, name))
            data["description"] = self.description(c, "class")
            data.update(self.see_also(c))
            if self.disjoint.get(c):
                data["disjoint_with"] = sorted(self.disjoint[c])
            # sh:maxCount 0 forbids a property. One condition per slot: LinkML
            # 1.12.1's JSON Schema joins several value_presence: ABSENT into
            # one "not all of them" rule.
            absent = sorted(
                self.slot_name[p] for p, k in self.eff[c].items() if k.absent
            )
            if absent:
                data["none_of"] = [
                    {"slot_conditions": {name: {"value_presence": "PRESENT"}}}
                    for name in absent
                ]
            slots = []
            if c in self.id_classes:
                slots.append(ID_SLOT)
            if c in self.type_classes:
                slots.append(TYPE_SLOT)
            slots += sorted(self.slot_name[p] for p in self.own[c])
            if slots:
                data["slots"] = slots
            if emitted[c]:
                data["slot_usage"] = {
                    self.slot_name[p]: ordered(u)
                    for p, u in sorted(
                        emitted[c].items(), key=lambda kv: self.slot_name[kv[0]]
                    )
                }
            add("class", name, c, data)
        return elements

    def _usage(self, c, p, emitted) -> dict:
        """The keys class c must state for slot p: those where its own
        conjunction differs from a value it would inherit, from an ancestor's
        slot_usage or else from the slot's definition."""
        mine = self.fields[p][c]
        induced = self._induced_def(p)
        keys = list(dict.fromkeys([*mine, *induced]))
        for a in self.ancestors(c):
            keys += [k for k in emitted.get(a, {}).get(p, {}) if k not in keys]
        usage = {}
        for k in keys:
            want = mine.get(k, self._default(k))
            sources = [
                emitted[a][p][k]
                for a in self.ancestors(c)
                if k in emitted.get(a, {}).get(p, {})
            ]
            if not sources:
                if k == "range":
                    sources = [
                        induced.get(k, None if "any_of" in induced else "string")
                    ]
                else:
                    sources = [induced.get(k, self._default(k))]
            if all(s == want for s in sources):
                continue
            if (
                want is False
                and k in DEFAULTS | {"inlined": None, "inlined_as_list": None}
                and any(sources)
            ):
                # SchemaView reads a false here as unset, so an inherited true
                # stands. A slot that holds one value here keeps its list
                # form and holds at most one item.
                if k == "multivalued":
                    usage["maximum_cardinality"] = 1
                    if mine.get("inlined") is True and not any(
                        s is True
                        for s in self._inherited(
                            c, p, "inlined_as_list", emitted, induced
                        )
                    ):
                        usage["inlined_as_list"] = True
                    self.narrowed.append(f"{self.class_name[c]}.{self.slot_name[p]}")
                    continue
                raise SystemExit(
                    f"{self.class_name[c]}.{self.slot_name[p]} cannot turn off the {k} it inherits"
                )
            if want is None:
                if k == "range" and "any_of" in mine:
                    continue
                self.report.append(
                    f"{self.class_name[c]}.{self.slot_name[p]} cannot unset the inherited {k}"
                )
                continue
            usage[k] = want
        return usage

    def _inherited(self, c, p, k, emitted, induced) -> list:
        """The values of key k that class c would inherit for slot p."""
        sources = [
            emitted[a][p][k]
            for a in self.ancestors(c)
            if k in emitted.get(a, {}).get(p, {})
        ]
        return sources or [induced.get(k, self._default(k))]

    def slot_order(self) -> list[URIRef]:
        """The properties, each after its super-property."""
        deps = {}
        for p in self.properties:
            parent = self.g.value(p, RDFS.subPropertyOf)
            deps[str(p)] = {str(parent)} if parent in self.properties else set()
        return [URIRef(p) for p in toposort(deps)]

    def local_xsd(self, dt) -> str:
        return str(dt)[len(str(XSD)) :]

    def _disjointness(self) -> dict[URIRef, set[str]]:
        g = self.g
        pairs = [
            (a, b)
            for a, b in g.subject_objects(OWL.disjointWith)
            if a in self.classes and b in self.classes
        ]
        for group in g.subjects(RDF.type, OWL.AllDisjointClasses):
            members = list(Collection(g, g.value(group, OWL.members)))
            pairs += [(a, b) for a in members for b in members if a != b]
        out: dict[URIRef, set[str]] = defaultdict(set)
        for a, b in sorted(pairs, key=str):
            if self.visible(self.ns_of(a), self.ns_of(b)):
                out[a].add(self.class_name[b])
            elif self.visible(self.ns_of(b), self.ns_of(a)):
                out[b].add(self.class_name[a])
                self.report.append(
                    f"{self.class_name[a]} is disjoint with {self.class_name[b]}; "
                    f"the schema states it on {self.class_name[b]}, whose module sees both"
                )
            else:
                self.report.append(
                    f"left out, the disjointness of {self.class_name[a]} and {self.class_name[b]}"
                )
        return out

    def build(self) -> dict[str, dict]:
        """Every schema file by name: the umbrella and one module per namespace."""
        self.home: dict[tuple[str, str], str] = {}
        for e in self.enums:
            self.home[("enum", self.enum_name[e])] = self.ns_of(e)
        for t in self.datatypes:
            self.home[("type", self.type_name[t])] = self.ns_of(t)
        self.used_xsd = {
            dt
            for p in self.properties
            for dt in self._datatypes_named(p)
            if dt in XSD_TYPES and not (dt in CO_BOUNDS and self.ns_of(p) == CO)
        }
        for dt in self.used_xsd:
            self.home[("type", XSD_TYPES[dt][0])] = CORE
        for p in self.properties:
            self.home[("slot", self.slot_name[p])] = self.ns_of(p)
        for c in self.classes:
            self.home[("class", self.class_name[c])] = self.ns_of(c)
        self.disjoint = self._disjointness()
        self.hoisted: list[str] = []
        self.narrowed: list[str] = []
        while True:
            self.narrowed = []
            elements = self._elements()
            if not self._hoist(elements):
                break
        for name in self.narrowed:
            self.report.append(
                f"{name} holds a list of at most one: its parent's slot is multivalued"
            )
        return self._files(elements)

    def _datatypes_named(self, p) -> set:
        out = set()
        for raw in [
            self.wide.get(p, {}),
            *(fields[p] for fields in self.own.values() if p in fields),
        ]:
            if "datatype" in raw:
                out.add(raw["datatype"])
            out |= set(raw.get("or", []))
        r = self.g.value(p, RDFS.range)
        if isinstance(r, URIRef):
            out.add(r)
        elif r is not None:
            if self.g.value(r, OWL.onDatatype) is not None:
                out.add(self.g.value(r, OWL.onDatatype))
            union = self.g.value(r, OWL.unionOf)
            if union is not None:
                out |= set(Collection(self.g, union))
        return out

    # -- modules ----------------------------------------------------------------------

    def _references(self, el: Element) -> list[tuple[str, str]]:
        """The (kind, name) of each element an element names."""
        out: list[tuple[str, str]] = []
        d = el.data

        def ranges(f: dict) -> None:
            if "range" in f:
                out.append(self._kind_of(f["range"]))
            for alt in f.get("any_of", []):
                out.append(self._kind_of(alt["range"]))

        if el.kind == "class":
            for parent in [d.get("is_a"), *d.get("mixins", [])]:
                if parent:
                    out.append(("class", parent))
            out += [("slot", s) for s in d.get("slots", [])]
            for s, f in d.get("slot_usage", {}).items():
                out.append(("slot", s))
                ranges(f)
        elif el.kind == "slot":
            ranges(d)
            for key in ("is_a", "inverse"):
                if key in d:
                    out.append(("slot", d[key]))
            if "domain" in d:
                out.append(("class", d["domain"]))
        return [
            r for r in out if r[1] not in (ID_SLOT, TYPE_SLOT) and r[0] != "builtin"
        ]

    def _kind_of(self, name: str) -> tuple[str, str]:
        if name in self.class_by_name:
            return ("class", name)
        if name in self.enum_name.values():
            return ("enum", name)
        if name in self.type_name.values() or name in {
            n for n, _ in XSD_TYPES.values()
        }:
            return ("type", name)
        return ("builtin", name)

    def _hoist(self, elements: dict[tuple[str, str], Element]) -> bool:
        """Declare in a module each element it needs from a module it does not
        import, keeping the element's IRI. Returns whether anything moved."""
        moved = False
        for el in sorted(elements.values(), key=lambda e: (e.module, e.kind, e.name)):
            for ref in self._references(el):
                target = elements.get(ref)
                if target is None:
                    raise SystemExit(
                        f"{el.kind} {el.name} names {ref}, which is not declared"
                    )
                home = self.home[ref]
                if self.visible(el.module, home):
                    continue
                if any(h.startswith(f"{target.name} (") for h in self.hoisted):
                    raise SystemExit(f"{ref} is needed in both {home} and {el.module}")
                self.report.append(
                    f"moved, the {target.kind} {target.name} from uco_{home} to uco_{el.module}, "
                    f"since {el.name} needs it and uco_{el.module} does not import uco_{home}"
                )
                self.hoisted.append(f"{target.name} ({self.curie(target.iri)})")
                self.home[ref] = el.module
                moved = True
        return moved

    def prefixes(self) -> dict:
        p = {OWN_PREFIX: OWN_NS}
        for ns in self.namespaces:
            p[f"uco-{ns}"] = f"{UCO_NS}{ns}/"
        p[CO_PREFIX] = CO_NS
        p.update(
            {"linkml": "https://w3id.org/linkml/", "rdf": str(RDF), "xsd": str(XSD)}
        )
        return p

    def header(
        self, name: str, title: str, description: str, imports: list[str], comments=None
    ) -> dict:
        ident = (
            SCHEMA_ID
            if name == UMBRELLA
            else f"{SCHEMA_ID}-{name.removeprefix('uco_')}"
        )
        h: dict = {
            "id": ident,
            "name": name,
            "title": title,
            "description": description,
            "version": self.version,
            "source": self.source,
            "license": LICENSE,
            "see_also": [
                SITE,
                f"https://unifiedcyberontology.org/releases/{self.version}/",
            ],
        }
        if comments:
            h["comments"] = comments
        h["prefixes"] = self.prefixes()
        h["default_prefix"] = OWN_PREFIX
        h["default_range"] = "string"
        h["imports"] = imports
        return h

    def _files(self, elements: dict[tuple[str, str], Element]) -> dict[str, dict]:
        module_names = {m: f"uco_{m}" for m in self.files}
        files: dict[str, dict] = {}
        for m in self.order:
            name = module_names[m]
            imports = ["linkml:types"] + [
                f"./{module_names[d]}" for d in self.order if d in self.imports[m]
            ]
            if m == CO:
                title = "Collections Ontology terms that UCO uses"
                description = (
                    "The classes and properties of the Collections Ontology (CO), http://purl.org/co/, "
                    f"that UCO {self.version}'s files use, with CO's IRIs and the constraints UCO's co.ttl adds."
                )
                comments = [
                    "CO states no licence, so the descriptions here are this project's own; none is CO's text.",
                    "CO's index and size are integers with CO's bounds, since this module imports no module "
                    "that declares UCO's XSD types.",
                ]
            else:
                onto = next(self.files[m].subjects(RDF.type, OWL.Ontology))
                comment = self.g.value(onto, RDFS.comment)
                title = f"UCO {m.capitalize()}"
                description = (
                    text(comment)
                    if comment is not None
                    else f"The classes, properties and vocabularies of UCO {self.version}'s {m} namespace, "
                    f"{UCO_NS}{m}/."
                )
                comments = None
            schema = self.header(name, title, description, imports, comments)
            mine = [e for e in elements.values() if e.module == m]
            if m == CORE:
                mine_slots = {e.name: e.data for e in mine if e.kind == "slot"}
                mine_slots[ID_SLOT] = {
                    "description": "The IRI of the thing, written as a CURIE or in full. A reference to it "
                    "from any slot is this IRI.",
                    "identifier": True,
                    "range": "uriorcurie",
                    "comments": [
                        "UCO's JSON-LD writes the IRI as @id; UCO has no property for it, so the key lives "
                        "in this schema's own namespace."
                    ],
                }
                mine_slots[TYPE_SLOT] = {
                    "description": "The class the thing is an instance of, as the class's CURIE, such as "
                    "uco-observable:File.",
                    "slot_uri": "rdf:type",
                    "designates_type": True,
                    "range": "uriorcurie",
                    "comments": [
                        "UCO's JSON-LD writes the same key as @type. The value names one class; a class's "
                        "ancestors follow from the schema."
                    ],
                }
            else:
                mine_slots = {e.name: e.data for e in mine if e.kind == "slot"}
            for kind, key in (("type", "types"), ("enum", "enums")):
                found = {e.name: e.data for e in mine if e.kind == kind}
                if found:
                    schema[key] = dict(sorted(found.items()))
            if mine_slots:
                schema["slots"] = dict(sorted(mine_slots.items()))
            found = {e.name: e.data for e in mine if e.kind == "class"}
            if found:
                schema["classes"] = dict(sorted(found.items()))
            files[name] = schema

        renamed = ", ".join(sorted(self.renamed_slots))
        umbrella = self.header(
            UMBRELLA,
            "Unified Cyber Ontology (UCO)",
            f"A LinkML rendering of the Unified Cyber Ontology (UCO) {self.version}: one module per UCO "
            "namespace and one for the Collections Ontology terms UCO uses, with every class, property and "
            "vocabulary keeping its UCO IRI.",
            ["linkml:types"] + [f"./{module_names[m]}" for m in self.order],
            comments=[
                "scripts/uco_to_linkml.py writes every YAML file in this folder from UCO's files in upstream/. "
                "Change the script or the copy, never the files.",
                "Each module imports the modules its UCO file imports, and this file imports them in that "
                "order, so an importer can import one module alone.",
                "The descriptions are UCO's rdfs:comment texts, which the UCO Community publishes under the "
                "Apache License 2.0.",
                "Where UCO defines one local name in more than one namespace, the namespace that comes first "
                "in this file's imports keeps it, and each other takes its namespace as a prefix: "
                f"{renamed}.",
                "Declared in uco_core although their IRIs are in UCO's types namespace, since Event's "
                "eventAttribute ranges over them and uco-core imports no other UCO namespace: "
                + ", ".join(self.hoisted)
                + ".",
                "Left out: SHACL advice (severity sh:Info or sh:Warning), SPARQL constraints, sh:not, sh:xone, "
                "paths of more than one property, and UCO's rule that a UcoThing is never a blank node, "
                "which a facet inlined here is when written as RDF.",
            ],
        )
        umbrella["slots"] = {
            GRAPH_SLOT: {
                "description": "The things the document holds: UCO objects, with their facets inlined, "
                "threads and their items.",
                "range": "UcoThing",
                "multivalued": True,
                "inlined": True,
                "inlined_as_list": True,
                "comments": ["UCO's JSON-LD holds the same list under @graph."],
            }
        }
        umbrella["classes"] = {
            DOCUMENT: {
                "class_uri": f"{OWN_PREFIX}:{DOCUMENT}",
                "description": "A document of UCO data, as a JSON-LD file of UCO holds one graph.",
                "tree_root": True,
                "slots": [GRAPH_SLOT],
            }
        }
        return {UMBRELLA: umbrella, **files}


# -- writing YAML ---------------------------------------------------------------


class _Dumper(yaml.SafeDumper):
    def increase_indent(
        self, flow=False, indentless=False
    ):  # lists sit indented under their key
        return super().increase_indent(flow, False)


def _represent_str(dumper, data):
    if len(data) > 80 and " " in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=">")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_Dumper.add_representer(str, _represent_str)

_SECTION_KEYS = {
    "prefixes",
    "default_prefix",
    "imports",
    "types",
    "enums",
    "slots",
    "classes",
}
_ELEMENT_SECTIONS = {"types", "enums", "slots", "classes"}


def dump(schema: dict) -> str:
    raw = yaml.dump(
        schema,
        Dumper=_Dumper,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=100,
    )
    out: list[str] = []
    in_elements = False
    for line in raw.split("\n"):
        indent = len(line) - len(line.lstrip())
        if line.strip() and indent == 0 and ":" in line:
            key = line.split(":", 1)[0]
            if key in _SECTION_KEYS and out and out[-1] != "":
                out.append("")
            in_elements = key in _ELEMENT_SECTIONS
        elif (
            line.strip()
            and indent == 2
            and in_elements
            and not line.lstrip().startswith("-")
        ):
            if out and out[-1] != "":
                out.append("")
        out.append(line)
    text_out = "\n".join(out).rstrip("\n") + "\n"
    return "---\n" + text_out


def write_all(files: dict[str, dict], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, schema in files.items():
        (out_dir / f"{name}.yaml").write_text(dump(schema), encoding="utf-8")


def check(files: dict[str, dict], out_dir: Path) -> int:
    """Compare a fresh rendering with the files in out_dir; 0 when they agree."""
    with tempfile.TemporaryDirectory() as tmp:
        fresh = Path(tmp)
        write_all(files, fresh)
        status = 0
        expected = {f"{name}.yaml" for name in files}
        present = {p.name for p in out_dir.glob("*.yaml")}
        for name in sorted(present - expected):
            print(f"not written by the converter: {out_dir / name}")
            status = 1
        for name in sorted(expected):
            new = (fresh / name).read_text(encoding="utf-8")
            old_path = out_dir / name
            old = old_path.read_text(encoding="utf-8") if old_path.exists() else ""
            if new != old:
                status = 1
                diff = difflib.unified_diff(
                    old.splitlines(),
                    new.splitlines(),
                    str(old_path),
                    "regenerated",
                    lineterm="",
                    n=1,
                )
                print("\n".join(list(diff)[:40]))
        return status


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--upstream",
        type=Path,
        default=DEFAULT_UPSTREAM,
        help="the copy of UCO's files",
    )
    parser.add_argument(
        "-d",
        "--output-dir",
        type=Path,
        default=DEFAULT_OUT,
        help="where the modules go",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="compare with the output folder instead of writing",
    )
    args = parser.parse_args(argv)
    converter = Converter(args.upstream)
    files = converter.build()
    for line in converter.report:
        print(f"note: {line}", file=sys.stderr)
    if args.check:
        return check(files, args.output_dir)
    write_all(files, args.output_dir)
    count = {
        key: sum(len(s.get(key, {})) for s in files.values())
        for key in ("classes", "slots", "enums", "types")
    }
    print(
        f"UCO {converter.version}: {len(files) - 1} modules, {count['classes']} classes, "
        f"{count['slots']} slots, {count['enums']} enums, {count['types']} types, written to {args.output_dir}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
