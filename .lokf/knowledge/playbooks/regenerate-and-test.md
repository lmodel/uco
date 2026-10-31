---
type: Playbook
id: https://w3id.org/lmodel/uco/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test after a change
description: "How to change the schema and check it: `uv sync --group dev`, change the converter or the copy, run the converter and the examples writer, then `just gen-project`, `just gen-doc`, `just lokf-adapt`, `just lint` and `just test`, and the pre-commit hooks before a pull request."
resource: CONTRIBUTING.md
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Development setup and Before opening a pull request
  - id: justfile
    resource: justfile
    title: the lint, gen-project, gen-doc and test recipes
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# Regenerate and test after a change

1. Install the tools with `uv sync --group dev`.[^contributing.md]
2. Change `scripts/uco_to_linkml.py`, or replace the copy under `src/uco/schema/upstream/` whole from one UCO release. Never edit a module by hand.
3. Run `uv run python scripts/uco_to_linkml.py`, then `uv run python scripts/uco_examples.py`.
4. Run `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit what they write.
5. Run `just lint`, where a warning fails, and `just test`, which generates the project into `tmp/`, runs pytest and validates the examples.[^justfile]
6. Run the pre-commit hooks on what you staged.

[^contributing.md]: CONTRIBUTING.md, Development setup and Before opening a pull request
[^justfile]: justfile, the lint, gen-project, gen-doc and test recipes
