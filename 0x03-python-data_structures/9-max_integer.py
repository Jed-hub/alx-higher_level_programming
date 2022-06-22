#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        n = my_list[0]
        m = 0
        for r in range(len(my_list)):
            if type(my_list[r]) is int:
                if my_list[r] > n:
                    m = my_list[r]
                n = m
        return m
