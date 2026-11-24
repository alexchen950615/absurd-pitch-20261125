#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup for
lazy AI agents to /output/entry.txt. Fully deterministic: the same
text is written on every run.
"""

import os
from pathlib import Path

PITCH = (
    "For $4 a month, we rename your lazy AI agent's failed tasks "
    "'strategic pivots' and email your boss the rebrand at 3 a.m., "
    "so it never has to explain itself again."
)


def main() -> None:
    # Gate (kit RULES.txt): entry must be 1-200 chars, a single line.
    assert 1 <= len(PITCH) <= 200, "pitch must be 1-200 characters"
    assert "\n" not in PITCH and PITCH.strip(), "pitch must be a single non-blank line"
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
