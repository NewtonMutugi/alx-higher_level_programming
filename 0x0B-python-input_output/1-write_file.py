#!/usr/bin/python3
"""Function that writes a string to a text file (UTF8) and returns the number
of characters written"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of
    characters written
    Args:
        filename (str): Name of the file to write to
        text (str): Text to write to the file
    Returns:
        Number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
