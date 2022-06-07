#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in my_list:
        i += 1
    if idx < 0:
        return my_list
    elif idx >= i - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
