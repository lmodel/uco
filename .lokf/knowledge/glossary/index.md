# Glossary

* [UcoThing](uco-thing.md) - In UCO, the top class of every individual: objects, facets, threads and thread items. The schema renders it as `UcoThing`, which carries the `type` designator.
* [UcoObject](uco-object.md) - In UCO, the base class of every object a graph names by IRI, such as a file, an account, a tool or an action. The schema renders it as `UcoObject`, one of the four classes its adapt copy roots on `Concept`.
* [Facet](facet.md) - In UCO, a group of properties that describe one aspect of an object, such as a file's name and size. The schema renders each facet as a value inside its object's `hasFacet` list.
* [ObservableObject](observable-object.md) - In UCO, an object of the digital domain that can be observed, such as a file, a device, an account or a network connection. The schema renders it as `ObservableObject`, with 95 direct subclasses.
* [Open vocabulary](open-vocabulary.md) - In UCO, a list of suggested string values for a property, such as the hash names MD5 and SHA256. The schema renders each as an enum, and a property that takes one also takes any string.
