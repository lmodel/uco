# About uco

The schema is written by `scripts/uco_to_linkml.py` from UCO 1.5.0's Turtle files, so it says what UCO's OWL and SHACL say, in LinkML's terms. This page lists where the two differ. The converter's docstring gives every rule, and it prints a note for each part of the ontology it leaves out, renames or moves.

## The data's form

- **Keys.** A key is the schema's slot name, UCO's local name for the property (`hasFacet`), not UCO's CURIE (`uco-core:hasFacet`).
- **Names UCO uses twice.** Where UCO defines one local name in two namespaces, the namespace that comes first in the modules' import order keeps it, and each other takes its namespace as a prefix: `observable_endTime` beside core's `endTime`. The umbrella's comments list all 20.
- **One type.** `type` names one class, the most specific. A node that UCO types with two unrelated classes has no form here.
- **Facets inside their object.** A facet, a hash, a dictionary and UCO's other value classes sit inside the object that holds them, without an IRI of their own. In UCO every UcoThing has an IRI. Here only an object, a thread, a thread item and a UcoType instance has one, as `id`.
- **References by IRI.** A slot ranged over an object holds the object's IRI as a string. The validator checks that it is a string, not the class of what it names.
- **Open vocabularies.** UCO 1.4.0 made its vocabularies suggestions: a property such as `hashMethod` takes a vocabulary value or any string, as its `rdfs:range` says. Three properties keep a closed vocabulary, such as `objectStatus`.
- **Literals without datatypes.** A value is its lexical form. UCO's rule that a literal carry a given datatype IRI has no counterpart.

## The schema's shape

- **Modules.** Each module imports the modules its UCO file imports. UCO's core file names `types:Dictionary` without importing the types file, so `Dictionary`, `DictionaryEntry` and their three slots are declared in `uco_core`, under their types IRIs.
- **Several parents.** A class with two parents takes one as `is_a` and the other as a mixin. `ObservableObject` is an `Observable` with `Item` mixed in.
- **Inherited constraints.** SHACL applies a class's shapes to its subclasses, so each class's slot is the conjunction of its own shapes and its parents'. Where a class holds one value of a slot its parent holds many of, it keeps the list form and holds one item at most, since LinkML cannot turn a parent's multivalued slot back.
- **Forbidden slots.** `sh:maxCount 0` becomes `none_of` on the class: `ActionLifecycle` has no status, start or end time of its own.
- **Collections Ontology.** CO's terms are those of lmodel/collections' schema, which the modules import from `collections/collections.yaml`, a copy of its v0.1.0 release. They keep CO's IRIs, and three take another name: CO's `Item`, `size` and `index` are `CoItem`, `co_size` and `co_index`. That schema states, as strictly or more so, each rule of UCO's `co.ttl` that LinkML can state, so the converter leaves those shapes out. A list's items sit inside the list without an IRI, so an item's links to the next and previous item hold copies of those items.
- **Threads.** A thread is a CO bag and a thread item a CO item, and both have IRIs. lmodel/collections holds a bag's items inside the bag, so `Thread` names its items by IRI through `slot_usage`, which turns `inlined` and `inlined_as_list` off. It also requires an item's content, and UCO does not, so `ThreadItem` keeps `itemContent` optional. The validator and the JSON Schema and Pydantic models hold both. The Python dataclasses that `gen-python` writes read the false `inlined` as unset, so they take a thread's item IRIs as items with an `id` only.

## Left out

The schema leaves out SHACL advice (severity Info or Warning), SPARQL constraints, `sh:not` and `sh:xone`, shapes over a path of more than one property or on a property's objects, the rule that `hasFacet` is inverse functional, and the shapes in UCO's `owl.ttl`. A property UCO deprecates, `creationTime`, is `deprecated` with UCO's message. `tests/test_data.py` lists each fault of UCO's failing examples that the schema does not state, with the reason.
