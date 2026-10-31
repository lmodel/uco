---
type: Tool
id: https://w3id.org/lmodel/uco/knowledge/tools/check-upstream-release
genre: reference
title: The upstream watch script (check_upstream_release.py)
description: "`scripts/check_upstream_release.py`, the standard-library script the upstream watch runs: it asks the GitHub API about ucoProject/UCO and reports a newer release or tag, a moved tag, a changed or dropped copied file, a changed licence and a check that could not finish."
resource: scripts/check_upstream_release.py
references:
  - https://w3id.org/lmodel/uco/knowledge/datasets/uco-copy
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring, the pins and the checks
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:14:11Z"
status: draft
---

# The upstream watch script

`scripts/check_upstream_release.py` pins the release `1.5.0`, the commit its tag names, the licence `Apache-2.0` and the git object hash of each of the 79 copied files. It asks the GitHub API for UCO's latest release and its tags, the licence GitHub detects, the commit the pinned tag names, and the file trees, and compares each copied file with its blob by hash.[^check_upstream_release.py]

It prints a Markdown report, writes it to `--report` when given, and exits 1 when anything needs attention. A file UCO adds in a watched folder is reported for information only. It sends `GITHUB_TOKEN` to api.github.com alone, in an unredirected header.

[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring, the pins and the checks
