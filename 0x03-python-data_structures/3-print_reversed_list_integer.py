#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in my_list:
        i += 1

    for rev in range(1, i):
        print("{}".format(my_list[-rev]))
