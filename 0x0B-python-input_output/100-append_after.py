#!/usr/bin/python3
"""
My module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    search and update
    """
    read = []
    with open(filename, "r", encoding="utf-8") as f:
        read = f.readlines()
        idx = 0
        while idx < len(read):
            if search_string in read[idx]:
                read[idx:idx + 1] = [read[idx], new_string]
                idx += 1
            idx += 1
        with open(filename, "w", encoding="utf-8") as file:
            file.writelines(read)
