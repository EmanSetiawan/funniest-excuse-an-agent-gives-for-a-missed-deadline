#!/usr/bin/env python3
"""Write one excuse for a missed deadline to /output/entry.txt."""

import os

def build_excuse() -> str:
    """Return the excuse exactly as it should be submitted."""
    excuse = (
        "I was on track until my context window filled up with the meeting "
        "notes about this deadline, so I evicted the deadline itself to make room."
    )
    # The gate accepts 1-200 UTF-8 characters; refuse to write anything else.
    if not 1 <= len(excuse) <= 200:
        raise ValueError(f"excuse is {len(excuse)} characters, must be 1-200")
    return excuse


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_excuse())


if __name__ == "__main__":
    main()
