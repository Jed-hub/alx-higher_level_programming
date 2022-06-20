#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for rev in range(1, len(my_list)):
        print("{:d}".format(my_list[-rev]))
