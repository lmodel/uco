---
type: Playbook
id: https://w3id.org/lmodel/uco/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Update the upstream pins
description: "What to do when the weekly upstream watch reports a newer UCO release or tag, a moved tag, a changed or dropped copied file, a changed licence, or a check that could not finish: replace the copy whole from one release, move the pins, rerun the converter and the examples writer, and run the tests."
resource: scripts/check_upstream_release.py
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring and the pins
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# Update the upstream pins

1. Read the issue the upstream watch opened, titled "Upstream watch: the Unified Cyber Ontology has changed", and UCO's release notes.
2. Replace `src/uco/schema/upstream/` whole from the new release, under UCO's paths.
3. Move `PINNED_TAG`, `PINNED_COMMIT` and `PINNED_BLOBS` in `scripts/check_upstream_release.py` together, and check `PINNED_LICENSE` against what GitHub now detects.[^check_upstream_release.py]
4. Run the converter and the examples writer, then regenerate and test as `CONTRIBUTING.md` says.[^contributing.md] A new fault in UCO's failing examples needs a row in `UNSTATED` or must fail the validator.

[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring and the pins
[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
