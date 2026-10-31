## Summary

Closes #

## What changed?

- [ ] The converter (`scripts/uco_to_linkml.py`) or the copied ontology, and the regenerated schema and artefacts
- [ ] Tests or example data (`tests/`)
- [ ] This repo's own `.lokf/knowledge/` bundle (documentation *about this repo*)
- [ ] Repository packaging only (CI, templates, docs unrelated to the schema)

## Checklist

- [ ] `just test` passes locally
- [ ] The schema modules were written by `scripts/uco_to_linkml.py`, and the other generated files by `just gen-project`, `just gen-doc` and `just lokf-adapt`, not edited by hand
- [ ] `src/uco/schema/upstream/` is unchanged, or replaced whole from one UCO release with the pins updated
- [ ] If `.lokf/` changed, `cd .lokf && just lokf-validate` passes
- [ ] A behaviour change has an entry under `## [Unreleased]` in `CHANGELOG.md`

## AI Assistance

If you used AI tools while preparing this PR, you are still the author and responsible for understanding, verifying, and defending your submission. Please engage with reviewers personally rather than through your agent during feedback and revisions. Don't dump LLM output into this PR without curation. See the [AI Covenant](../AI_COVENANT.md) for details.
