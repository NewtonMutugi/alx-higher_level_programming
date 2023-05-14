#!/usr/bin/python3
"""Module that inserts a line of text to a file, after each line
containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line
    containing a specific string"""
    with open(filename, mode="r+", encoding="utf-8") as myFile:
        lines = myFile.readlines()
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
        myFile.seek(0)
        myFile.writelines(new_lines)
