#!/usr/bin/python3
def no_c(my_string):
    for c in my_string:
        if c == "c" or c == "C":
            c == ""
        else:
            print("{}".format(c), end="")

    return c
