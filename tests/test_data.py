"""Checks the example data, and UCO's own failing examples, against the schema.

The valid examples under tests/data/valid/ are written by
scripts/uco_examples.py: from UCO's own examples where they hold the class,
and from the schema where not. The counter-examples under tests/data/invalid/
are written by hand, one per kind of constraint the schema states, and each
first line names where the validator must report it.

UCO's XFAIL examples are read with the same reader. Each fault that UCO's
SHACL report on them names either fails here at the slot it names, or is
listed in UNSTATED with the reason LinkML does not state it.

The validator reads a merged copy of the schema: it reads a schema's imports
again for every instance it checks, which takes seconds with sixteen modules.
"""

import functools
import importlib.util
import json
import re
import sys
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView
from rdflib import BNode, Graph, URIRef
from rdflib.namespace import RDF, SH

import uco.datamodel.uco

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "uco" / "schema" / "uco.yaml"
GENERATED_JSON_SCHEMA = ROOT / "project" / "jsonschema" / "uco.schema.json"
DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"
VALID_EXAMPLE_FILES = sorted(DATA_DIR_VALID.glob("*.yaml"))
INVALID_EXAMPLE_FILES = sorted(DATA_DIR_INVALID.glob("*.yaml"))


def _examples_module():
    spec = importlib.util.spec_from_file_location(
        "uco_examples", ROOT / "scripts" / "uco_examples.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


EXAMPLES = _examples_module()


@functools.cache
def _validator() -> Validator:
    view = SchemaView(str(SCHEMA))
    view.merge_imports()
    return Validator(
        view.schema, validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )


@functools.cache
def _reader():
    return EXAMPLES.Reader()


def _messages(instance: dict, target: str) -> list[str]:
    return [r.message for r in _validator().validate(instance, target).results]


def _target(path: Path) -> str:
    return path.stem.split("-")[0]


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES, ids=lambda p: p.name)
def test_valid_data_files(filepath):
    """Each valid example loads into the generated dataclasses."""
    obj = yaml_loader.load(
        str(filepath), target_class=getattr(uco.datamodel.uco, _target(filepath))
    )
    assert obj


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES, ids=lambda p: p.name)
def test_valid_data_files_validate(filepath):
    """Each valid example passes the validator, the one check that applies
    every constraint the schema states."""
    messages = _messages(yaml.safe_load(filepath.read_text()), _target(filepath))
    assert not messages, messages


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES, ids=lambda p: p.name)
def test_invalid_data_files_fail(filepath):
    """Each counter-example fails at the place its first line names, as
    `# Fails at: <JSON pointer>`, so a file that starts failing for another
    reason fails this test."""
    text = filepath.read_text()
    first = text.splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{filepath.name}: the first line names where it fails"
    )
    pointer = first.removeprefix("# Fails at: ").strip()
    messages = _messages(yaml.safe_load(text), _target(filepath))
    assert any(m.endswith(f" in {pointer}") for m in messages), messages


@functools.cache
def _generated() -> dict:
    return json.loads(GENERATED_JSON_SCHEMA.read_text())


def _generated_failures(instance, target: str | None = None) -> list[tuple[str, str]]:
    """Each error from the committed project/jsonschema file itself, against
    the class's definition there or against its root, a UcoDocument, as the
    JSON pointer to where it is and its message."""
    schema = _generated()
    if target is not None:
        schema = {
            "$schema": schema["$schema"],
            "$defs": schema["$defs"],
            "$ref": f"#/$defs/{target}",
        }
    cls = jsonschema.validators.validator_for(schema)
    return [
        ("/" + "/".join(str(p) for p in e.absolute_path), e.message)
        for e in cls(schema, format_checker=cls.FORMAT_CHECKER).iter_errors(instance)
    ]


def _generated_errors(instance, target: str | None = None) -> list[str]:
    return [message for _, message in _generated_failures(instance, target)]


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES, ids=lambda p: p.name)
def test_valid_data_files_pass_the_generated_json_schema(filepath):
    """Each valid example passes the JSON Schema gen-project writes, which a
    user validates against without LinkML."""
    errors = _generated_errors(yaml.safe_load(filepath.read_text()), _target(filepath))
    assert not errors, errors


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES, ids=lambda p: p.name)
def test_invalid_data_files_fail_the_generated_json_schema(filepath):
    """Each counter-example fails the generated JSON Schema too, at the place
    its first line names."""
    text = filepath.read_text()
    pointer = text.splitlines()[0].removeprefix("# Fails at: ").strip()
    failures = _generated_failures(yaml.safe_load(text), _target(filepath))
    assert any(where == pointer for where, _ in failures), failures


def test_a_document_of_the_examples_passes_the_generated_json_schema():
    """The valid examples of UcoThing's classes, in one UcoDocument's graph,
    pass the generated JSON Schema at its root."""
    things = [
        yaml.safe_load(f.read_text())
        for f in VALID_EXAMPLE_FILES
        if "UcoThing" in _reader().ancestors(_target(f))
    ]
    assert things
    errors = _generated_errors({"graph": things})
    assert not errors, errors[:5]


def test_every_concept_type_has_an_example():
    """Each class a concept may name as its type has a valid example."""
    examples = {_target(f) for f in VALID_EXAMPLE_FILES}
    missing = sorted(set(_reader().concept_types()) - examples)
    assert not missing, missing


# Each kind of constraint the schema states, the key that states it, and the
# counter-example that breaks it.
KINDS = {
    "required": ("required", "Relationship-missing-target.yaml"),
    "single value": ("multivalued", "UcoObject-two-names.yaml"),
    "datatype": ("range", "Relationship-directional-not-boolean.yaml"),
    "inlined class": ("inlined", "UcoObject-facet-of-another-class.yaml"),
    "reference by IRI": ("inlined", "UcoObject-creator-inline.yaml"),
    "closed vocabulary": ("enum", "UcoObject-unknown-status.yaml"),
    "pattern": ("pattern", "Hash-value-not-hex.yaml"),
    "slot bound": ("maximum_value", "ConfidenceFacet-over-100.yaml"),
    "lower bound": ("minimum_value", "ConfidenceFacet-below-0.yaml"),
    "union of datatypes": ("any_of", "TableFieldFacet-row-id-a-boolean.yaml"),
    "type bound": (
        "maximum_value",
        "WindowsPEOptionalHeader-version-over-unsigned-short.yaml",
    ),
    "fixed value": ("equals_string", "Observation-not-observe.yaml"),
    "fixed member": ("has_member", "LicenseMarking-other-definition-type.yaml"),
    "forbidden slot": ("none_of", "ActionLifecycle-with-status.yaml"),
    "at most one item": ("maximum_cardinality", "ActionLifecycle-two-phases.yaml"),
    "at most four items": (
        "maximum_cardinality",
        "WindowsVolumeFacet-five-attributes.yaml",
    ),
    "designator": ("designates_type", "UcoObject-unknown-class.yaml"),
    "closed class": ("slots", "UcoObject-unknown-key.yaml"),
    "identifier": ("identifier", "UcoObject-missing-id.yaml"),
}


def _keys(node, out: set) -> set:
    if isinstance(node, dict):
        out |= set(node)
        for value in node.values():
            _keys(value, out)
    elif isinstance(node, list):
        for value in node:
            _keys(value, out)
    return out


def test_each_kind_of_constraint_has_a_counter_example():
    """Every key the modules use to constrain data has a counter-example,
    and every counter-example is one of the kinds."""
    used = set()
    for module in SCHEMA.parent.glob("uco*.yaml"):
        used |= _keys(yaml.safe_load(module.read_text()), set())
    view = SchemaView(str(SCHEMA))
    if view.all_enums():
        used.add("enum")
    for kind, (key, name) in KINDS.items():
        assert key in used, f"{kind}: the schema no longer uses {key}"
        assert (DATA_DIR_INVALID / name).is_file(), f"{kind}: {name} is missing"
    constraint_keys = {
        "pattern",
        "equals_string",
        "has_member",
        "none_of",
        "minimum_value",
        "maximum_value",
        "maximum_cardinality",
        "any_of",
    }
    assert constraint_keys <= {key for key, _ in KINDS.values()}
    assert {f.name for f in INVALID_EXAMPLE_FILES} == {
        name for _, name in KINDS.values()
    }


# -- UCO's XFAIL examples ------------------------------------------------------

REF_CLASS = "the class of an object a slot names by IRI: the validator checks the IRI, not what it names"
NODE_KIND = "a literal where UCO wants an IRI: the schema holds a reference as a string either way"
LITERAL_TYPE = (
    "a literal's datatype IRI: data in the schema's form holds the value alone"
)
TWO_TYPES = (
    "a node of two classes, which a LinkML instance cannot be: its type names one"
)
XONE = "sh:xone, which the converter leaves out"
SPARQL = "a SPARQL constraint, which the converter leaves out"
NOT = "an sh:not, which the converter leaves out"
PATH = "a shape over a path of more than one property, which the converter leaves out"
BLANK = "a UcoThing that is a blank node: a facet here is a value without an IRI, so the rule is left out"
PREFIX = "a type whose prefix the example's context leaves undeclared, so it names no UCO class"
OWL = "OWL and RDF list structure, not UCO data"
OWN_ONTOLOGY = "classes and shapes the example's own ontology defines, which the schema cannot know"
METACLASS = "a class as an instance of UcoType, which data in the schema's form does not describe"
ITEM_LINK = (
    "a list item's link to the next or previous item: lmodel/collections holds the"
    " linked item as a copy inside the item, and the example's items link back to"
    " each other, which no finite copy holds"
)

# Each fault UCO reports that this schema does not state, as (example,
# focus node, path, constraint component), with the reason.
UNSTATED = {
    (
        "action_inheritance_XFAIL.json",
        "array-of-action-6f91380f-703f-471e-9be6-cf7499bf44f2",
        "action:action",
        "ClassConstraintComponent",
    ): REF_CLASS,
    (
        "action_inheritance_XFAIL.json",
        "array-of-action-6f91380f-703f-471e-9be6-cf7499bf44f2",
        "action:action",
        "NodeKindConstraintComponent",
    ): NODE_KIND,
    (
        "co_XFAIL.json",
        "list-d6039e14-1426-4f92-9d9f-db9d94f87da7",
        "path",
        "MaxCountConstraintComponent",
    ): PATH,
    (
        "co_XFAIL.json",
        "list-02de67a8-bfb9-4e00-a305-bae3daf6384b",
        "co:size",
        "DatatypeConstraintComponent",
    ): LITERAL_TYPE,
    (
        "co_XFAIL.json",
        "list-item-4361eb9c-a1c2-40e7-ba83-92802554392a",
        "-",
        "NotConstraintComponent",
    ): NOT,
    ("co_XFAIL.json", "*", "co:nextItem", "MaxCountConstraintComponent"): ITEM_LINK,
    ("co_XFAIL.json", "*", "co:previousItem", "MaxCountConstraintComponent"): ITEM_LINK,
    (
        "configuration_setting_XFAIL.json",
        "configuration-entry-5f0fc3ea-e763-4b6d-997a-be0d1ceffc8c",
        "-",
        "XoneConstraintComponent",
    ): XONE,
    (
        "configuration_setting_XFAIL.json",
        "configured-object-7156bff0-b805-4190-83ee-230fae31e33a",
        "configuration:isConfigurationOf",
        "ClassConstraintComponent",
    ): REF_CLASS,
    ("database_records_XFAIL.json", "*", "-", "XoneConstraintComponent"): XONE,
    (
        "dictionary_XFAIL.json",
        "Dictionary-5bc55661-4808-48e6-9e02-80a153eee5d3",
        "-",
        "NotConstraintComponent",
    ): TWO_TYPES,
    ("dictionary_XFAIL.json", "*", "-", "SPARQLConstraintComponent"): SPARQL,
    (
        "event_XFAIL.json",
        "Action-0-03ee1fe6-12cf-4a35-b7dd-06d4e69369b5",
        "-",
        "NotConstraintComponent",
    ): TWO_TYPES,
    (
        "has_facet_inverse_functional_XFAIL.json",
        "facet-b94b9cce-f11a-49f2-b5d4-9efff5e8ab2d",
        "core:hasFacet",
        "SPARQLConstraintComponent",
    ): SPARQL,
    (
        "hash_XFAIL.json",
        "hash-66954988-aa9a-4f0d-8ad1-380700c830fc",
        "types:hashValue",
        "DatatypeConstraintComponent",
    ): LITERAL_TYPE,
    (
        "message_thread_XFAIL.json",
        "message-thread-facet-5be8604b-49ad-4432-a560-d529f998807b",
        "path",
        "ClassConstraintComponent",
    ): PATH,
    (
        "object_status_XFAIL.json",
        "ArchiveFileFacet-5884ca1c-2f5e-4e66-bdc6-7d48606f9fbc",
        "-",
        "ClassConstraintComponent",
    ): PREFIX,
    ("owl_axiom_XFAIL.json", "*", "*", "*"): OWL,
    ("owl_properties_XFAIL.json", "*", "*", "*"): OWL,
    ("rdf_list_XFAIL.json", "*", "*", "*"): OWL,
    (
        "relationship_XFAIL.json",
        "*",
        "core:kindOfRelationship",
        "DatatypeConstraintComponent",
    ): LITERAL_TYPE,
    (
        "technique_data_XFAIL.json",
        "*",
        "*",
        "QualifiedMinCountConstraintComponent",
    ): OWN_ONTOLOGY,
    (
        "thread_XFAIL.json",
        "thread-1c73bebd-798e-4ea2-a1be-553db145e7b5",
        "*",
        "ClassConstraintComponent",
    ): REF_CLASS,
    (
        "thread_XFAIL.json",
        "thread-item-2bd09467-d413-4a03-af5d-f0e428f7d987",
        "-",
        "NotConstraintComponent",
    ): NOT,
    (
        "thread_XFAIL.json",
        "thread-item-2bd09467-d413-4a03-af5d-f0e428f7d987",
        "co:itemContent",
        "ClassConstraintComponent",
    ): REF_CLASS,
    ("uco_thing_XFAIL.json", "_:blank", "-", "SPARQLConstraintComponent"): BLANK,
    ("uco_type_XFAIL.json", "*", "*", "*"): METACLASS,
}


def _short(report: Graph, path) -> str:
    if path is None:
        return "-"
    if isinstance(path, URIRef):
        return report.namespace_manager.normalizeUri(path)
    return "path"


@functools.cache
def _faults() -> dict[tuple, tuple]:
    """Each Violation UCO's reports name, by (example, focus node, path,
    constraint component), with what the check needs to read it."""
    out = {}
    folder = EXAMPLES.EXAMPLES
    for data in sorted(folder.glob("*_XFAIL.json")) + sorted(
        folder.glob("technique/*_XFAIL.json")
    ):
        report = Graph().parse(
            data.with_name(data.name.replace(".json", "_validation.ttl"))
        )
        for result in report.objects(None, SH.result):
            if report.value(result, SH.resultSeverity) != SH.Violation:
                continue
            focus = report.value(result, SH.focusNode)
            path = report.value(result, SH.resultPath)
            component = str(report.value(result, SH.sourceConstraintComponent)).rsplit(
                "#", 1
            )[-1]
            name = (
                "_:blank" if isinstance(focus, BNode) else str(focus).rsplit("/", 1)[-1]
            )
            out[(data.name, name, _short(report, path), component)] = (
                data,
                focus,
                path,
            )
    return out


def _reason(key: tuple) -> str | None:
    for (example, node, path, component), reason in UNSTATED.items():
        if all(
            want in ("*", got)
            for want, got in zip((example, node, path, component), key, strict=True)
        ):
            return reason
    return None


def test_unstated_faults_are_faults_uco_reports():
    """Every entry of UNSTATED matches a fault in UCO's reports, so the list
    shrinks when UCO or the converter changes."""
    keys = list(_faults())
    for pattern in UNSTATED:
        assert any(
            all(want in ("*", got) for want, got in zip(pattern, key, strict=True))
            for key in keys
        ), pattern


@pytest.mark.parametrize(
    "key",
    sorted(k for k in _faults() if _reason(k) is None),
    ids=lambda k: f"{k[0]}:{k[1][:24]}:{k[2]}",
)
def test_uco_xfail_fault_fails_here(key):
    """A fault UCO's report names, and UNSTATED does not, fails the
    validator on the same node, at the slot UCO's report names. That slot is
    one the node's class has, so the failure is the constraint UCO names and
    not a key the class lacks."""
    data, focus, path = _faults()[key]
    reader = _reader()
    graph = EXAMPLES.read(data)
    target = reader.type_of(graph, focus)
    messages = _messages(reader.instance(graph, focus, strict=False), target)
    assert messages, f"{key} validates"
    if path is not None and isinstance(path, URIRef):
        slot = reader.slot_by_iri[str(path)]
        assert slot in reader.induced(target), f"{target} has no slot {slot}"
        assert any(f" in /{slot}" in m or f"'{slot}'" in m for m in messages), messages


# The one place where UCO's co_PASS.json lists, in the schema's form, fail
# the schema: each list's first item has the index 0, written as an
# xsd:positiveInteger. pySHACL does not check that (UCO's co_XFAIL.json says
# so), but the schema's minimum of 1 does. lmodel/collections names CO's
# index co_index.
CO_PASS_DIFFERENCES = (
    r"0 is less than the minimum of 1 in /(firstItem|item/\d+)/co_index",
)


def test_ucos_lists_differ_only_where_known():
    """UCO's two co_PASS lists, each a bag with a size and elements as CO
    has it, fail the validator only where CO_PASS_DIFFERENCES says."""
    reader = _reader()
    graph = EXAMPLES.read(EXAMPLES.EXAMPLES / "co_PASS.json")
    lists = sorted(graph.subjects(RDF.type, URIRef("http://purl.org/co/List")))
    assert len(lists) == 2
    for node in lists:
        instance = reader.instance(graph, node, strict=False)
        assert {"co_size", "element", "item"} <= set(instance), node
        messages = _messages(instance, "List")
        unexplained = [
            m
            for m in messages
            if not any(re.fullmatch(d, m) for d in CO_PASS_DIFFERENCES)
        ]
        assert not unexplained, unexplained
