#!/usr/bin/python3
""" Save Object to file. """


import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object
    to a text file
    using JSON representation
    """
    with open(filename, 'w', encoding="UTF-8") as filej:
        json.dump(my_obj, filej)
