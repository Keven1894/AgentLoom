"""catalog-ui-must-tell-the-story — Tier A validator.

Behavior MD: agents/behaviors/builder/behavior-catalog-ui-must-tell-the-story.md

Checks: every starter/<app>/index.html contains 8 elements with
data-catalog-role attributes whose value is one of the required markers,
each with non-empty inner content.

Exempt files: those containing the literal HTML comment
    <!-- catalog-storytelling: bootstrapping -->
(transitional during paired-commit hard-launch).

Exit 0 iff all targets pass. Exit 1 if any violation. Exit 2 if no targets
found AND the workspace clearly should have catalogs (sentinel: starter/
exists with at least one subdir) — silent-pass would hide drift.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]

REQUIRED_ROLES = [
    "title",
    "provenance",
    "acquisition",
    "data-shape",
    "processing",
    "kg-link",
    "reuse",
    "data-view",
]

EXEMPT_MARKER = "<!-- catalog-storytelling: bootstrapping -->"

ROLE_PATTERN = re.compile(
    r"<([a-zA-Z][a-zA-Z0-9]*)\b[^>]*\bdata-catalog-role\s*=\s*[\"']([^\"']+)[\"'][^>]*>"
    r"(.*?)"
    r"</\1\s*>",
    re.DOTALL | re.IGNORECASE,
)

COMMENT_PATTERN = re.compile(r"<!--.*?-->", re.DOTALL)
TAG_PATTERN = re.compile(r"<[^>]+>")
CHILD_TAG_PATTERN = re.compile(r"<[a-zA-Z][a-zA-Z0-9]*\b")
WS_PATTERN = re.compile(r"\s+")

MIN_INNER_CHARS = 10

CONTAINER_ROLES = {"data-view"}


def _normalize_inner(raw: str) -> str:
    no_comments = COMMENT_PATTERN.sub("", raw)
    no_tags = TAG_PATTERN.sub(" ", no_comments)
    return WS_PATTERN.sub(" ", no_tags).strip()


def _has_child_element(raw: str) -> bool:
    no_comments = COMMENT_PATTERN.sub("", raw)
    return bool(CHILD_TAG_PATTERN.search(no_comments))


def check_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    if EXEMPT_MARKER in text:
        return []

    found: dict[str, tuple[str, str]] = {}
    for match in ROLE_PATTERN.finditer(text):
        role = match.group(2).strip().lower()
        raw_inner = match.group(3)
        inner = _normalize_inner(raw_inner)
        if role not in found or len(inner) > len(found[role][0]):
            found[role] = (inner, raw_inner)

    violations: list[str] = []
    for role in REQUIRED_ROLES:
        if role not in found:
            violations.append(f"missing data-catalog-role: {role}")
            continue
        inner, raw_inner = found[role]
        if role in CONTAINER_ROLES:
            if not _has_child_element(raw_inner):
                violations.append(
                    f"data-catalog-role={role} present but contains no child element "
                    f"(JS hydration target required, e.g. <div id=\"map\"></div>)"
                )
        elif len(inner) < MIN_INNER_CHARS:
            violations.append(
                f"data-catalog-role={role} present but inner content too short "
                f"({len(inner)} chars; need >={MIN_INNER_CHARS})"
            )
    extras = sorted(set(found) - set(REQUIRED_ROLES))
    if extras:
        violations.append(
            f"unknown data-catalog-role values (typo? extension proposal?): {extras}"
        )
    return violations


def main() -> int:
    starter_dir = WORKSPACE / "starter"
    if not starter_dir.exists():
        print(f"[INFO] {starter_dir.relative_to(WORKSPACE)} not found — nothing to check.")
        return 0

    targets = sorted(starter_dir.glob("*/index.html"))
    if not targets:
        if any(starter_dir.iterdir()):
            print(f"[ERROR] starter/ has subdirs but no */index.html files.")
            return 2
        return 0

    n_violations = 0
    n_checked = 0
    n_exempt = 0
    for f in targets:
        rel = f.relative_to(WORKSPACE).as_posix()
        text = f.read_text(encoding="utf-8")
        if EXEMPT_MARKER in text:
            n_exempt += 1
            print(f"  [EXEMPT] {rel} :: bootstrapping marker present")
            continue
        n_checked += 1
        for msg in check_file(f):
            print(f"  [VIOLATION] {rel} :: {msg}")
            n_violations += 1

    print(
        f"\nChecked {n_checked} catalog file(s); skipped {n_exempt} bootstrapping; "
        f"{n_violations} violation(s)."
    )
    return 0 if n_violations == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
