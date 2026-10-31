#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check the copy of UCO's files against ucoProject/UCO's releases.

Four things can go wrong with ``src/uco/schema/upstream/`` without any change
in this repository:

- the UCO Community releases or tags a newer version of the Unified Cyber
  Ontology (UCO), so the schema falls behind;
- the pinned tag is moved to another commit;
- the copied files drift from the files they were taken from;
- UCO's licence changes, which decides what this repository may copy.

The release, the commit its tag names and each copied file's git object hash
are pinned below. The script asks the GitHub API for ucoProject/UCO's latest
release, its tags, the licence GitHub detects, the commit the pinned tag
names, and the repository's file tree at the pinned commit and at a newer
release, one listing each. It compares every copied file with its blob by
git object hash, so nothing is downloaded but listings.

It prints a Markdown report, and exits 1 when:

- a newer release or tag is out;
- a pinned file changed or is gone at a newer release;
- a copied file differs from its pin, or the copy holds an unpinned file;
- the pinned tag moved;
- the licence is no longer Apache-2.0, or GitHub detects none;
- a check could not finish, such as a refused, failed or cut-off request,
  or an answer larger than the script reads.

A file the UCO Community adds beside the copied ones, in the folders the
copy is taken from, is reported for information only.

Text the API chose, such as a tag name or an error message, is quoted as
code in the report, so the issue the workflow opens from it cannot mention
anyone. Set ``GITHUB_TOKEN`` to raise the API rate limit. The token goes to
api.github.com alone, never on to a redirect. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import os
import re
import sys
import urllib.error
import urllib.request
from urllib.parse import quote
from functools import cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY = ROOT / "src" / "uco" / "schema" / "upstream"
API = "https://api.github.com/repos/ucoProject/UCO"
USER_AGENT = "lmodel-uco-upstream-check"

# The most the script reads of one answer. The largest, the file tree at
# the pinned commit, is about 54 kB.
MAX_BYTES = 5_000_000

# The release and the commit its tag names. Move them together when the copy
# is replaced from a newer release, with PINNED_BLOBS, the schema header
# (scripts/uco_to_linkml.py writes it) and the regenerated schema.
PINNED_TAG = "1.5.0"
PINNED_COMMIT = "7ebb3957e9e9a2e1bb9c66cd1ede8c912a726344"

# The licence GitHub detects for ucoProject/UCO, which allows the copy.
PINNED_LICENSE = "Apache-2.0"

# The address of the pinned release, which is the schema header's `source`;
# tests/test_upstream.py holds the two equal.
PINNED_SOURCE = f"https://github.com/ucoProject/UCO/releases/tag/{PINNED_TAG}"

# Each copied file, by its path in ucoProject/UCO and in the copy, and its
# git object hash at PINNED_COMMIT. tests/test_upstream.py checks the hashes
# offline.
PINNED_BLOBS = {
    "LICENSE": "261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64",
    "ontology/co/co.ttl": "02ca1dea3654e08c9f5f0f363fbfa6ff3d294f02",
    "ontology/uco/action/action.ttl": "408bc73a0c85cb81e5df9a8d64859df2cb989b01",
    "ontology/uco/analysis/analysis.ttl": "16f6a702dbed6985ef4ab2206c8fde1718497cc7",
    "ontology/uco/configuration/configuration.ttl": "bdb1e7ea6e1b1053ca4290ae6951ac1e011eb751",
    "ontology/uco/core/core.ttl": "22ce16f1395f8dbf617a8dd1122b25912b060da4",
    "ontology/uco/identity/identity.ttl": "0f0ba6eaa29aaa337bb769c1eed6ab40b8e59234",
    "ontology/uco/location/location.ttl": "2e1cb15a9bfc5ec06ea3caba4c670074079bd829",
    "ontology/uco/marking/marking.ttl": "741c4ed6ad9e48b23331cad8284fa6c47eea77d9",
    "ontology/uco/master/uco.ttl": "c297ad3e817261779cf9a9649abdabbec93a5a8c",
    "ontology/uco/observable/observable.ttl": "1b81df70b09d3f849c7e75684a551c428579015a",
    "ontology/uco/pattern/pattern.ttl": "cb972e32b036559cc0b3672773bd3f24ee1b8316",
    "ontology/uco/role/role.ttl": "1465b15917ea0ef70947499426fd966c95ef0193",
    "ontology/uco/time/time.ttl": "3993a505ef577882b7d655bb180eaf22a1359592",
    "ontology/uco/tool/tool.ttl": "16c61a4a46a3f705cdd80410d9d6cb5f47e6c96c",
    "ontology/uco/types/types.ttl": "5a0401292d226afcf742130a8836c6f38a00aa2d",
    "ontology/uco/victim/victim.ttl": "d7e637fa5f9dd57d647a08e102444b3b603a9ff2",
    "ontology/uco/vocabulary/vocabulary.ttl": "4862b4bab32a69e4fe3c6a0ad1de00272f5cfa8b",
    "tests/examples/action_inheritance_PASS.json": "4312558dd5876928b9e8716190dd818b4966be45",
    "tests/examples/action_inheritance_XFAIL.json": "2b9d09c3ea452d91031c2b2558de34d3af53b3ec",
    "tests/examples/action_inheritance_XFAIL_validation.ttl": "8d239b77d777beffdd0ddd9422c626da6925c4f2",
    "tests/examples/action_result_PASS.json": "3831b31127c4ccd2aa25eee620e857f7fcebcb6a",
    "tests/examples/alternate_data_stream_PASS.json": "e6abd5bba0f09a628fb5ab3a778da96eaf85349a",
    "tests/examples/configuration_setting_PASS.json": "44a893ad775758ff370859a373cc0bae5f238bba",
    "tests/examples/configuration_setting_XFAIL.json": "8bf5ff38d2caa823407085bddb9d7420747fe4aa",
    "tests/examples/configuration_setting_XFAIL_validation.ttl": "866e84aebedd823c7fc94fc1d72ebd7e1a10fa4e",
    "tests/examples/co_PASS.json": "430e20936d8638e467ec4d7f958ee7fb29b96c21",
    "tests/examples/co_XFAIL.json": "4a383609d4d113ca15fecfec2d65ad87cf494798",
    "tests/examples/co_XFAIL_validation.ttl": "9888889d52331c746e42f45f2ac97318686f152f",
    "tests/examples/database_records_PASS.json": "0a5897370f5b6789e202423bb3e586e6b586e966",
    "tests/examples/database_records_XFAIL.json": "3071e7202c8a232cb072e05927b2b4705722ccb6",
    "tests/examples/database_records_XFAIL_validation.ttl": "30d9ec99fc21de313470019a8c1cb9571666345d",
    "tests/examples/dictionary_PASS.json": "31e1aab8dedcfa360d5d3a8a4edda92a85f769e6",
    "tests/examples/dictionary_XFAIL.json": "dd2a45676b0c797495bf0f393ee5101dcceaaae1",
    "tests/examples/dictionary_XFAIL_validation.ttl": "f15a758098a93ddc09768dd4def3310fa440afc2",
    "tests/examples/disjointedness_PASS.json": "227775a6c3080aef4c8f809599cc361efbe56756",
    "tests/examples/event_XFAIL.json": "9f2a59d95aabe9035bb39cedc6859c24c12d0f52",
    "tests/examples/event_XFAIL_validation.ttl": "be6dbd961d00c86cfb2f9424b372844877c1418b",
    "tests/examples/file_url_PASS.json": "58d2abb3a7c5d08ace7dff5b567f8a0806d00350",
    "tests/examples/has_facet_inverse_functional_PASS.json": "f9f67af563a0fc229674bdd04d2c11ca6cf4aaa2",
    "tests/examples/has_facet_inverse_functional_XFAIL.json": "e2e3f75ae535fae320acefce2b8b10bb69328270",
    "tests/examples/has_facet_inverse_functional_XFAIL_validation.ttl": "de5e2aa078519d93a690b2fba86695d1cd0665a9",
    "tests/examples/hash_PASS.json": "228d3355c5098c0f95961146b9344484728f3aab",
    "tests/examples/hash_XFAIL.json": "d00974083a40a81d7d5b78cc9bacbc356420838b",
    "tests/examples/hash_XFAIL_validation.ttl": "48cc07e1bac2fbf9515a6e5c14f4ef48b8ac59d0",
    "tests/examples/location_PASS.json": "660cd15d1108addf86630fbfec5ae49b3a6a493e",
    "tests/examples/location_XFAIL.json": "4418955947e94e6d901d7bf65ba75cb9b59ef613",
    "tests/examples/location_XFAIL_validation.ttl": "d38323c9e2fc954a3faebb678fe2b12e8e8ac29d",
    "tests/examples/message_thread_PASS.json": "a7834d6cf91fea610b896041fc6bfe2c8710d14e",
    "tests/examples/message_thread_XFAIL.json": "a35746e2eb2136acb4ae1eb640c36568191fe1f4",
    "tests/examples/message_thread_XFAIL_validation.ttl": "e9365720c1ae9e0d249f397f744b8d18ad2ff6d0",
    "tests/examples/object_status_PASS.json": "3f4d116599b31de860ef323ed05f2950d0d8fdb8",
    "tests/examples/object_status_XFAIL.json": "b827c238ef2038f7acb1e85ee2ce2f6d82be23bb",
    "tests/examples/object_status_XFAIL_validation.ttl": "57a35e5fd386380f7df04d9a1125211433143f87",
    "tests/examples/observable_creation_time_PASS.json": "cde684fa393658771dd98e039fbf0e3bfef12f78",
    "tests/examples/operating_system_PASS.json": "c97ff495a4ce529205ebdfa3657734bc95b44600",
    "tests/examples/owl_axiom_PASS.json": "7d57e8fd036982394642a9ab508c7ba473319555",
    "tests/examples/owl_axiom_XFAIL.json": "de369bd67b40d2b4fb63b1795a419985e7a913a6",
    "tests/examples/owl_axiom_XFAIL_validation.ttl": "c450be7258604dfd2afed25b5988555ec82e55e3",
    "tests/examples/owl_properties_PASS.json": "2224ece633f6bf74e78a2f98d139f4131a772a13",
    "tests/examples/owl_properties_XFAIL.json": "b39d9c5ed8c582be8a1d0117e2a70e7eea2e347b",
    "tests/examples/owl_properties_XFAIL_validation.ttl": "cf07d5c39aa2da764497c8ce087387e83a24238e",
    "tests/examples/rdf_list_PASS.json": "7462e256236843a6be80e0f55d53a60f257562e3",
    "tests/examples/rdf_list_XFAIL.json": "9e188cfec1495ba0029ac0cb198e960dc46d6358",
    "tests/examples/rdf_list_XFAIL_validation.ttl": "d8646eda0e9122f6b154ee4ec9e3218e3ac15f6c",
    "tests/examples/relationship_PASS.json": "4abedfbb7d72580b194b0eda3ccb1d80e897f15c",
    "tests/examples/relationship_XFAIL.json": "da1579545e9339522527b08ee098bfc77dae932f",
    "tests/examples/relationship_XFAIL_validation.ttl": "c4f912e1f22000cbc4d47087f8aaa2901c1fd673",
    "tests/examples/technique/technique_data_PASS.json": "a6bf76706ab1758d2025ff3d8b6426e201cece4f",
    "tests/examples/technique/technique_data_XFAIL.json": "d288d406cb60c167b8179a26183b758acd2aa1f9",
    "tests/examples/technique/technique_data_XFAIL_validation.ttl": "32c3a5dce3ba2f4ed84b85094039738b05f8f6bd",
    "tests/examples/thread_PASS.json": "1dd1350ba952e002fb2700c56708d8838ce8a256",
    "tests/examples/thread_XFAIL.json": "6d213367ce5a2c984532c626ffbdf7f9b45f3297",
    "tests/examples/thread_XFAIL_validation.ttl": "7e86377fc2cd1ca5cbf9a34c22760fecfd9ebeaa",
    "tests/examples/uco_thing_XFAIL.json": "fedcf22983acd3ad9809d187854d642c926fdeb8",
    "tests/examples/uco_thing_XFAIL_validation.ttl": "ab5f60130b11a5ea1c03433e5e4e567b2d04678e",
    "tests/examples/uco_type_PASS.json": "a6970b72a64f620abbdec53424294ca926e72d28",
    "tests/examples/uco_type_XFAIL.json": "eb16563dcb64a64b221cf660291406fb064c16e5",
    "tests/examples/uco_type_XFAIL_validation.ttl": "02ff95b6dd47ed85b55a81ed4fc464a238585170",
}

# The folders whose new files are worth a reader's look: the ontology and
# UCO's example data.
WATCHED = ("ontology/", "tests/examples/")

# Files in WATCHED that the copy leaves out on purpose, so that only a file
# the UCO Community adds is reported. owl.ttl holds SHACL shapes over OWL
# itself, which the schema does not render. The Makefiles, the catalogs,
# the READMEs and the test runner are build files. The SHACL reports on the
# examples that pass hold no fault the tests read, and the technique
# folder's Turtle files are ontology fragments for its tests, not data.
LEFT_OUT = re.compile(
    r"^("
    r"ontology/owl/.*"
    r"|ontology/(.*/)?Makefile"
    r"|ontology/(.*/)?catalog-v001\.xml"
    r"|tests/examples/(technique/)?(Makefile|README\.md|\.gitignore)"
    r"|tests/examples/(technique/)?[^/]+_PASS_validation\.ttl"
    r"|tests/examples/technique/technique_(ontology|shapes)_[^/]+\.ttl"
    r"|tests/examples/test_validation\.py"
    r")$"
)


def _get(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API):
        # urllib copies ordinary headers onto a redirect, so the token goes in
        # an unredirected one and reaches api.github.com alone.
        req.add_unredirected_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = resp.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError(f"the answer from {url} is larger than {MAX_BYTES} bytes")
    return body


def _code(text: object) -> str:
    """Text the API chose, such as a tag name, as a code span, so it cannot
    mention a person or add a link in the issue."""
    return "`" + str(text).replace("`", "'") + "`"


def _version_key(tag: str) -> tuple[int, ...]:
    """Numeric parts of a tag, padded so that 1.5 and 1.5.0 order alike."""
    parts = [int(x) for x in re.findall(r"\d+", tag)]
    return tuple(parts + [0] * (4 - len(parts)))


def _blob_sha(path: Path) -> str:
    """The git object hash of a file, as the trees API reports it."""
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


@cache
def _tree(ref: str) -> dict[str, str]:
    """Every file of the repository at a ref, by path, with its object hash.
    A ref the repository does not hold gives an empty mapping. Each tree is
    asked for once, and no caller changes what it returns."""
    try:
        # A tag name is the API's text: quoted, it names one ref and no other path.
        body = json.loads(_get(f"{API}/git/trees/{quote(ref, safe='')}?recursive=1"))
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return {}
        raise
    if body.get("truncated"):
        raise OSError(f"the tree at {ref} is too large for one listing")
    return {e["path"]: e["sha"] for e in body.get("tree", []) if e["type"] == "blob"}


def _tag_commit(tag: str) -> str | None:
    """The commit a tag names, read through the tag object when the tag is an
    annotated one, or None when the repository has no such tag."""
    try:
        target = json.loads(_get(f"{API}/git/ref/tags/{tag}"))["object"]
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise
    while target["type"] == "tag":
        target = json.loads(_get(f"{API}/git/tags/{target['sha']}"))["object"]
    return target["sha"]


@cache
def _latest() -> str:
    """The newest version ucoProject/UCO has released or tagged, asked once.
    UCO publishes each release as a GitHub release of the same tag, but a
    tag can come first, so the tags count too."""
    tags = [json.loads(_get(f"{API}/releases/latest"))["tag_name"]]
    tags += [t["name"] for t in json.loads(_get(f"{API}/tags?per_page=100"))]
    return max(tags, key=_version_key)


def _newer(tag: str) -> bool:
    return _version_key(tag) > _version_key(PINNED_TAG)


def _added(tree: dict[str, str]) -> list[str]:
    """The files of the watched folders that are neither copied nor left out
    on purpose."""
    return sorted(
        path
        for path in tree
        if path.startswith(WATCHED)
        and path not in PINNED_BLOBS
        and not LEFT_OUT.match(path)
    )


def check_release() -> tuple[list[str], bool]:
    """Report whether ucoProject/UCO has a newer release or tag than the pin."""
    latest = _latest()
    if _newer(latest):
        return [
            f"- **UCO {_code(latest)} is out; the schema renders {PINNED_TAG}.** Read its "
            "release notes, replace the copy from that release, move the pins "
            "here, and run `scripts/uco_to_linkml.py` and `just test`."
        ], True
    return [f"- Latest release: UCO {_code(latest)}, the pinned one."], False


def check_licence() -> tuple[list[str], bool]:
    """Report whether GitHub still detects the pinned licence. GitHub
    answers 404, or names no licence, when it detects none."""
    try:
        found = (json.loads(_get(f"{API}/license")).get("license") or {}).get("spdx_id")
    except urllib.error.HTTPError as err:
        if err.code != 404:
            raise
        found = None
    if found != PINNED_LICENSE:
        shown = _code(found) if found else "no licence GitHub detects"
        return [
            f"- **ucoProject/UCO's licence now reads as {shown}, not {PINNED_LICENSE}.** "
            "Check what it allows before the copy or the descriptions taken from it "
            "move to a newer release, and update NOTICE."
        ], True
    return [f"- Licence: {PINNED_LICENSE}, as pinned."], False


def check_copy() -> tuple[list[str], bool]:
    """Report whether the pinned tag still names the pinned commit, whether
    the copy is the files pinned there, and whether a newer release changes
    or drops any of them."""
    report = [
        f"- Pinned release: UCO {PINNED_TAG}, commit `{PINNED_COMMIT[:12]}`, "
        "copied to `src/uco/schema/upstream/`.",
    ]
    attention = False

    commit = _tag_commit(PINNED_TAG)
    if commit != PINNED_COMMIT:
        attention = True
        named = f"commit {_code(commit[:12])}" if commit else "nothing"
        report.append(
            f"- **The tag {PINNED_TAG} now names {named}, not the pinned commit "
            f"`{PINNED_COMMIT[:12]}`.** Find out why it moved before trusting either."
        )

    pinned_tree = _tree(PINNED_COMMIT)
    matching, differing = 0, []
    for name, pinned_sha in sorted(PINNED_BLOBS.items()):
        path = COPY / name
        if not path.is_file():
            differing.append(f"`{name}` is missing from the copy")
        elif pinned_tree.get(name) != pinned_sha:
            differing.append(
                f"`{name}` at commit `{PINNED_COMMIT[:12]}` is not the pinned blob"
            )
        elif _blob_sha(path) != pinned_sha:
            differing.append(f"`{name}` differs from its file at {PINNED_TAG}")
        else:
            matching += 1
    extra = sorted(
        p.relative_to(COPY).as_posix()
        for p in COPY.rglob("*")
        if p.is_file() and p.relative_to(COPY).as_posix() not in PINNED_BLOBS
    )
    differing += [f"`{name}` is in the copy but not pinned" for name in extra]
    report.append(
        f"- {matching} of {len(PINNED_BLOBS)} copied files match the pinned commit byte for byte."
    )
    if differing:
        attention = True
        report.append(f"- **{len(differing)} problem(s) with the copy:**")
        report += [f"  - {d}" for d in differing]
    added = {PINNED_TAG: _added(pinned_tree)}

    latest = _latest()
    if _newer(latest):
        latest_tree = _tree(latest)
        dropped = sorted(n for n in PINNED_BLOBS if n not in latest_tree)
        changed = sorted(
            n
            for n, sha in PINNED_BLOBS.items()
            if n in latest_tree and latest_tree[n] != sha
        )
        for name in dropped:
            attention = True
            report.append(
                f"- **UCO {_code(latest)} no longer holds `{name}`.** Find where the UCO "
                "Community now publishes it, and move the pins."
            )
        for name in changed:
            attention = True
            report.append(
                f"- **UCO {_code(latest)} changes `{name}`.** Replace "
                f"`src/uco/schema/upstream/{name}` with the file at that tag, move the "
                "pins here, and regenerate the schema."
            )
        if not dropped and not changed:
            report.append(
                f"- Latest release: UCO {_code(latest)}, which holds the pinned files unchanged."
            )
        added[latest] = _added(latest_tree)

    for ref, names in added.items():
        if names:
            report.append(
                f"- For information, ucoProject/UCO at {_code(ref)} also holds "
                + ", ".join(_code(n) for n in names)
                + ", which the copy neither holds nor leaves out on purpose."
            )
    return report, attention


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("release", check_release),
    ("licence", check_licence),
    ("copy", check_copy),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines, attention = [], False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed request and a timeout,
        # HTTPException and EOFError a connection cut off mid-answer,
        # ValueError an answer that is not JSON or is too large, and
        # LookupError, TypeError and AttributeError JSON of another shape.
        except (
            OSError,
            http.client.HTTPException,
            EOFError,
            ValueError,
            LookupError,
            TypeError,
            AttributeError,
        ) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
