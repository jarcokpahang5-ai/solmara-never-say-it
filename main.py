#!/usr/bin/env python3
"""Say out loud the line that should never be said out loud.

The line is defined once, in entry_text. This script imports it
under a local nickname and prints it, and prints nothing else.
"""

from entry_text import LINE as unsayable

if __name__ == "__main__":
    print(unsayable)
