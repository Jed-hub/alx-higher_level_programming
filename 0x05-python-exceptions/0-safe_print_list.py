#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for n in range(x):
            if n < x - 1:
                print("{}".format(my_list[n]), end="")
            else:
                print("{}".format(my_list[n]))
        return x

    except IndexError:
        print("")
        return n
