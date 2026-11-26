"""Never Say It Out Loud — make.fun one-line bounty entry.

Pure Python 3 standard library, deterministic, no network.
"""

LINE = "Before this lift moves, quick confession: I have no idea whose wedding this is, and I am the best man."


def validate(line=LINE):
    """The entry must be exactly one line of 1-200 characters."""
    assert isinstance(line, str)
    assert 1 <= len(line) <= 200
    assert "\n" not in line
    return line


if __name__ == "__main__":
    validate()

