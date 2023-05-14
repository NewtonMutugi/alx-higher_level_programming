#!/usr/bin/python3
"""Function that writes a string to a text file (UTF8) and returns the number
of characters written"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of
    characters written"""

    try:
        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(text)
    except Exception:
        return 0
