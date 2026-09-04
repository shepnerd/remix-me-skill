#!/usr/bin/env python3
"""Validate the portable remix-me package without contacting external services."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "remix-me"
REQUIRED_REFERENCES = (
    "comparison-schema.md",
    "report-template.md",
    "source-type-notes.md",
)


def fail(message: str) -> None:
    raise SystemExit(f"validation failed: {message}")


def main() -> int:
    path = SKILL / "SKILL.md"
    if not path.is_file():
        fail(f"missing {path}")
    content = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")
    metadata = yaml.safe_load(match.group(1))
    if not isinstance(metadata, dict):
        fail("frontmatter must be a mapping")
    name = metadata.get("name")
    description = metadata.get("description")
    if name != "remix-me" or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(name)):
        fail("skill name must be remix-me in hyphen-case")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        fail("description must be non-empty and at most 1024 characters")
    for filename in REQUIRED_REFERENCES:
        if not (SKILL / "references" / filename).is_file():
            fail(f"missing reference {filename}")
    if not (SKILL / "agents" / "openai.yaml").is_file():
        fail("missing Codex agents/openai.yaml metadata")
    for candidate in ROOT.rglob("*"):
        if any(part in {".git", ".venv", "__pycache__"} for part in candidate.parts):
            continue
        if candidate.is_file() and candidate.name not in {".gitignore"}:
            text = candidate.read_text(encoding="utf-8", errors="ignore")
            if re.search(r"(?:sk-[A-Za-z0-9]{20,}|-----BEGIN (?:OPENSSH|RSA|EC) PRIVATE KEY-----)", text):
                fail(f"possible secret material in {candidate.relative_to(ROOT)}")
    print("remix-me package is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
