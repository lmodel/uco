---
type: Playbook
id: https://w3id.org/lmodel/uco/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose."
resource: .
sources:
  - resource: README.md
  - resource: docs/index.md
  - resource: docs/about.md
  - resource: src/uco/schema
  - resource: src/uco/schema/upstream
  - resource: scripts/uco_to_linkml.py
  - resource: scripts/uco_examples.py
  - resource: scripts/check_upstream_release.py
  - resource: src/uco/datamodel
  - resource: project.justfile
  - resource: .lokf/uco.yaml
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
  - resource: NOTICE
  - resource: LICENSE
  - resource: .github/scripts
  - resource: .github/workflows
  - resource: .github/dependabot.yml
  - resource: .github/release
  - resource: justfile
  - resource: .linkml/generators.yaml
  - resource: .linkmllint.yaml
  - resource: .pre-commit-config.yaml
  - resource: project
  - resource: docs/schema
  - resource: tests
  - resource: CONTRIBUTING.md
  - resource: .releaserc.json
  - resource: CHANGELOG.md
  - resource: website
  - resource: SECURITY.md
  - resource: AI_COVENANT.md
exclusions:
  - resource: .github/ISSUE_TEMPLATE
    reason: Issue forms, which are governance text and state nothing about the schema.
  - resource: .github/pull_request_template.md
    reason: The pull request checklist, which repeats CONTRIBUTING.md.
  - resource: CODE_OF_CONDUCT.md
    reason: The Contributor Covenant, governance text with nothing about the schema.
  - resource: uv.lock
    reason: The package's lock file, tooling that pins versions.
  - resource: pyproject.toml
    reason: Package metadata and spell checkers' settings; the changelog states the Python project's name.
  - resource: .gitignore
    reason: "Tooling: the files git ignores."
  - resource: .editorconfig
    reason: "Tooling: editor settings."
  - resource: .yamllint.yaml
    reason: "Tooling: the YAML linter's settings."
  - resource: .markdownlint-cli2.jsonc
    reason: "Tooling: the Markdown linter's settings."
  - resource: lychee.toml
    reason: "Tooling: the link checker's settings."
  - resource: config.public.mk
    reason: "Tooling: the variables the justfile loads."
  - resource: .copier-answers.yml
    reason: The copier template's answers, which `just update` reads.
  - resource: src/README.md
    reason: Text from the project template.
  - resource: src/uco/schema/README.md
    reason: Text from the project template.
  - resource: docs/templates-linkml
    reason: The template's placeholders for gen-doc, not pages.
  - resource: docs/elements
    reason: The folder for gen-doc's element pages, which git ignores; only its placeholder is tracked.
  - resource: examples/README.md
    reason: Text from the project template about generated example output.
  - resource: src/uco/__init__.py
    reason: Package plumbing.
  - resource: src/uco/_version.py
    reason: Package plumbing.
  - resource: tests/__init__.py
    reason: Test plumbing.
  - resource: llms.txt
    reason: The pointer that sends agents to this bundle.
  - resource: knowledge_bundle
    reason: The sidecar's link to the bundle.
  - resource: .github/PULL_REQUEST_TEMPLATE
    reason: The sidecar sync's pull request template.
  - resource: .lokf/lokf.yaml
    reason: LOKF's schema, pinned by the sidecar.
  - resource: .lokf/scripts
    reason: The sidecar's scripts, which the weekly sync replaces.
  - resource: .lokf/m365
    reason: The sidecar's Copilot skill builder and its instructions.
  - resource: .lokf/README.md
    reason: The sidecar's own README.
  - resource: .lokf/queries.http
    reason: The sidecar's sample queries.
  - resource: .lokf/ingest.yaml.sample
    reason: The sidecar's example ingest manifest, which this host does not use.
  - resource: .lokf/uv.lock
    reason: The sidecar's lock file.
  - resource: .lokf/.gitignore
    reason: The sidecar's git settings.
  - resource: .lokf/.gitattributes
    reason: The sidecar's git settings.
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# Knowledge sources

Each refresh run after the first re-verifies these sources instead of discovering them again. Update this map whenever the layout of the repository's sources changes. Each concept names the file or folder it derives from by its path from the repository root, in `resource` and in `sources`, and `knowledge-report.sh worklist` lists the concepts whose source moved since their stamp.

| Source | Yields | Re-check by |
| --- | --- | --- |
| `src/uco/schema/uco*.yaml`, `scripts/uco_to_linkml.py` | `datasets/uco-linkml-schema`, `tools/uco-to-linkml`, the `glossary/` terms | rerun the converter with `--check`; re-read the umbrella's comments and the counts it prints |
| `project.justfile`, `.lokf/uco.yaml`, `.lokf/justfile`, `.lokf/pyproject.toml`, the README's Knowledge Trust Ladder (KTL) section | the domain-schema section of `datasets/uco-linkml-schema`, `explanations/element-names` | re-read the `--root` list, the copy's notes, the `schema :=` line and the `[tool.lokf]` table |
| `src/uco/schema/upstream/`, the UCO section of `NOTICE` | `datasets/uco-copy`, `references/unified-cyber-ontology`, `references/collections-ontology` | the upstream watch compares the blobs weekly; re-read the pins |
| `scripts/check_upstream_release.py`, `.github/scripts/` | `tools/check-upstream-release`, `playbooks/update-upstream-pins`, `workflows/upstream-watch` | re-read the pins, the docstring and the left-out pattern |
| `scripts/uco_examples.py`, `tests/` | `tools/uco-examples`, `datasets/test-data` | rerun the script with `--check`; re-count `valid/` and `invalid/`; re-read `UNSTATED` in `tests/test_data.py` |
| `README.md`, `docs/about.md`, `docs/index.md`, `.linkmllint.yaml`, `CHANGELOG.md` | `explanations/scope-and-influences`, `explanations/data-form`, `playbooks/validate-data` | re-read each section and the lint comment |
| `justfile`, `.linkml/generators.yaml`, `project/`, `src/uco/datamodel/`, `docs/schema/`, `.pre-commit-config.yaml` | `datasets/generated-artefacts`, `playbooks/regenerate-and-test` | re-read the recipes and the generators' settings; re-list `project/*/` |
| `CONTRIBUTING.md` | `playbooks/regenerate-and-test` | confirm the setup and the checklist |
| `.releaserc.json`, `.github/release/`, `CHANGELOG.md` | `playbooks/release`, `workflows/semantic-release` | re-read the release rules and the baseline paragraph |
| the nine files in `.github/workflows/` | the nine `workflows/` concepts | re-read each file's `on` keys, its jobs' permissions and environments, and the variables and secrets it reads |
| `website/` | `services/documentation-site` | re-read `site.config.mjs` and `website/README.md` |
| `NOTICE`, `LICENSE`, the License section of `README.md` | `policies/license-and-attribution` | re-read each third-party entry |
| `SECURITY.md`, `.github/dependabot.yml` | `policies/security-policy` | re-read the table of surfaces and the settings not yet in force |
| `AI_COVENANT.md` | `policies/ai-covenant` | re-read the project note |

The paths under `exclusions` were looked at and left out, each for the reason it gives: governance text, tooling settings, template text, package plumbing, the pointer for agents, and the sidecar's files. Of the sidecar's files, the domain schema, the justfile's `schema :=` line and the `[tool.lokf]` table are sources.
