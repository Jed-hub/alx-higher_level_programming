#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for n in range(x):
            print("{}".format(my_list[n]), end="")
        print("")
        return x

    except (IndexError):
        print("")
        return n
