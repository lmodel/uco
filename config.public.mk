# config.public.mk

# This file is public in git. No sensitive info allowed.

###### schema definition variables, used by justfile

# Note:
# - just works fine with quoted variables of dot-env files like this one
LINKML_SCHEMA_NAME="uco"
LINKML_SCHEMA_AUTHOR="Noel McLoughlin <noel.mcloughlin@gmail.com>"
LINKML_SCHEMA_DESCRIPTION="Unified Cyber Ontology (UCO): LinkML Schema"
LINKML_SCHEMA_SOURCE_DIR="src/uco/schema"

###### linkml generator variables, used by justfile

## gen-project configuration file
LINKML_GENERATORS_CONFIG_YAML=.linkml/generators.yaml

## pass args if gendoc ignores config.yaml (i.e. --no-mergeimports)
LINKML_GENERATORS_DOC_ARGS=

## pass args to workaround genowl rdfs config bug (linkml#1453)
##   (i.e. --no-type-objects --no-metaclasses --metadata-profile=rdfs)
# LINKML_GENERATORS_OWL_ARGS="--no-type-objects --no-metaclasses --metadata-profile=rdfs"
## The generator's announced future defaults, set now, as lmodel/spdx does, so
## that the OWL stays the same when they become the defaults. They leave out
## the vacuous axioms, which makes the OWL a fifth smaller.
LINKML_GENERATORS_OWL_ARGS="--skip-vacuous-min-zero-cardinality-axioms --skip-vacuous-local-range-axioms --consolidate-cardinality-axioms"

## pass args to pydantic generator which isn't supported by gen-project
## https://github.com/linkml/linkml/issues/2537
LINKML_GENERATORS_PYDANTIC_ARGS=
