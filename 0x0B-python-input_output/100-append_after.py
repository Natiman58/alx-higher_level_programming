#!/usr/bin/python3
"""
    A module containing the 'append_after' fun.
"""
def append_after(filename="", search_string="", new_string=""):
    """
        Inserts a new line of text to a file\
        after each line containing a specific string.
     """
    with open(filename, 'r+', encoding="utf-8") as f:
        all_lines = f.readlines()

    count = 0
    with open(filename, 'w', encoding="utf-8") as j:
        for line in all_lines:
            count += 1
            if search_string in line:
                all_lines.insert(count, new_string)
        for line in all_lines:
            j.write(line)
