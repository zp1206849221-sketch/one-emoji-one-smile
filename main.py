#!/usr/bin/env python3
"""One Emoji, One Smile — write exactly one smile-worthy emoji to /output/entry.txt.

Entry choice: the disguised face (U+1F978). The brief asks for one emoji
that buys one smile, and the previous pick — a hatching chick — is the
kind of cute staple a thousand other entrants reach for, which in this
contest means a real chance of an exact-text collision and a silent
zero. The disguised face is a comedy prop all by itself: Groucho
glasses, a plastic nose and a moustache, the universal shorthand for
"this is a joke, you may laugh now". It is a single codepoint, far less
common in one-emoji entries than the standard grins, and it needs no
context to land.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The whole entry: one emoji, nothing else.
EMOJI = "🥸"
EMOJI_CODEPOINT = 0x1F978  # DISGUISED FACE


def validate(text: str) -> str:
    """Return text unchanged if it is exactly one emoji and nothing else."""
    if not text:
        raise ValueError("entry must not be empty")
    if text != text.strip():
        raise ValueError("entry must not carry surrounding whitespace")
    if len(text) != 1:
        raise ValueError(f"entry must be exactly one character, got {len(text)}")
    if ord(text) != EMOJI_CODEPOINT:
        raise ValueError("entry drifted from the chosen emoji")
    return text


def build_entry() -> str:
    """Assemble the entry text and prove it is fit to ship."""
    return validate(EMOJI)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_entry(), encoding="utf-8")
    # Read back what actually landed on disk: the file, not the
    # constant, is what gets judged, so verify it too.
    validate(OUTPUT_PATH.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
