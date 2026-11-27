"""Weirdest job title entry.

A plausible-sounding job ("Professional Whisperer") with one very
specific, funny twist: the clients are vending machines that eat coins.
"""

import os


ENTRY = "Professional Whisperer for Vending Machines That Eat Coins"


def main() -> None:
    # Guard the bounty limit: one title, at most 60 characters, nothing else.
    title = ENTRY.strip()
    if len(title) > 60 or not title:
        raise ValueError(f"entry must be 1-60 chars, got {len(title)}")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(title)


if __name__ == "__main__":
    main()
