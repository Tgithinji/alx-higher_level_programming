#!/usr/bin/python3
"""
This modelue defines append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line
    containing a specific string
    """
    lines = []
    with open(filename, 'r', encoding='utf-8') as a_file:
        for line in a_file:
            lines.append(line)

    for i, line in enumerate(lines):
        if search_string in line:
            lines.insert(i+1, new_string)

    with open(filename, 'w', encoding='utf-8') as file:
        lines = "".join(lines)
        file.write(lines)
