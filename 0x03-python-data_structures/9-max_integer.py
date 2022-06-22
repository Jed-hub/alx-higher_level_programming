#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        n = 0
        for r in range(len(my_list)):
            if my_list[r] > n:
                m = my_list[r]
            n = m
        return m
