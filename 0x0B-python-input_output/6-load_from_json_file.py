#!/usr/bin/python3
""" Create onject from JSon file. """


import json


def load_from_json_file(filename):
    """ Function that creates an object from JSON file. """
    with open(filename, encoding="UTF-8") as load_f:
        return json.load(load_f)
