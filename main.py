#!/usr/bin/env python3
"""One Emoji, One Smile — write exactly one warm emoji to /output/entry.txt."""

from pathlib import Path

# Final choice: hatching chick. Compared across passes against a
# sunflower (bright but impersonal) and a teddy bear (soft but a
# static object), the chick wins: it is small, kind, alive and
# gently silly — a tiny creature arriving in the world, instantly
# readable by anyone, with no irony, intimacy or flirtation that
# could land wrong coming from a stranger. Single codepoint
# (U+1F423), so the character count is unambiguous.
EMOJI = "🐣"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(EMOJI, encoding="utf-8")


if __name__ == "__main__":
    main()
